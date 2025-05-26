from ultralytics import YOLO
import cv2
from core.eventos import EventDetector

class VideoAnalyzer:
    def __init__(self, source=0):
        self.model = YOLO("yolov8n.pt")
        self.source = source
        self.event_detector = EventDetector()

    def start_detection(self):
        cap = cv2.VideoCapture(self.source)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model(frame)
            boxes = results[0].boxes

            person_mask = boxes.cls == 0  # 0 es la clase de 'person' en COCO
            person_boxes = boxes[person_mask]
            # Reemplazar las detecciones originales con solo personas
            results[0].boxes = person_boxes

            # Dibujar solo las personas
            annotated_frame = results[0].plot()

            events = self.event_detector.detect_events([results[0]])

            for event in events:
                if event["type"] == "fall":
                    cv2.putText(annotated_frame, "CAIDA DETECTADA!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("Monitoreo", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
