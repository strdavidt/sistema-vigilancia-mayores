from ultralytics import YOLO
import cv2

class VideoAnalyzer:
    def __init__(self, source=0):
        self.model = YOLO("yolov8n.pt")  # Modelo pequeño, rápido
        self.source = source

    def start_detection(self):
        cap = cv2.VideoCapture(self.source)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model(frame)
            annotated_frame = results[0].plot()
            cv2.imshow("Deteccion de Personas", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
