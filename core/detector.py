from ultralytics import YOLO
import cv2
import time
from core.eventos import EventDetector

class VideoAnalyzer:
    def __init__(self, source=0):
        self.model = YOLO("yolov8n.pt")
        self.source = source
        self.event_detector = EventDetector()
        self.active_events = []  # Lista de eventos visibles

    def start_detection(self):
        cap = cv2.VideoCapture(self.source)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model(frame)
            boxes = results[0].boxes

            person_mask = boxes.cls == 0  # Solo personas
            person_boxes = boxes[person_mask]
            results[0].boxes = person_boxes

            annotated_frame = results[0].plot()

            new_events = self.event_detector.detect_events([results[0]])
            current_time = time.time()

            # Agregar eventos nuevos solo si no están ya activos
            for event in new_events:
                if not any(e["type"] == event["type"] for e in self.active_events):
                    self.active_events.append({
                        "type": event["type"],
                        "timestamp": current_time
                    })

            # Limpiar eventos viejos
            self.active_events = [
                e for e in self.active_events if current_time - e["timestamp"] < 3
            ]

            # Mostrar eventos activos
            y_offset = 30
            for e in self.active_events:
                if e["type"] == "fall":
                    text = "CAIDA DETECTADA"
                    color = (0, 0, 255)
                elif e["type"] == "exit":
                    text = "LA PERSONA SALIO DE LA VISTA"
                    color = (0, 165, 255)
                else:
                    continue

                cv2.putText(annotated_frame, text, (10, y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                y_offset += 40

            cv2.imshow("Monitoreo", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
