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
            annotated_frame = results[0].plot()

            events = self.event_detector.detect_events(results)

            for event in events:
                if event["type"] == "fall":
                    cv2.putText(annotated_frame, "CAIDA DETECTADA!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("Monitoreo", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
