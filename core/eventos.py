import time

class EventDetector:
    def __init__(self):
        self.last_positions = {}
        self.fall_timers = {}

    def detect_events(self, results):
        events = []

        for i, person in enumerate(results[0].boxes.xyxy):
            x1, y1, x2, y2 = person[:4]
            w = x2 - x1
            h = y2 - y1
            aspect_ratio = w / h

            person_id = f"p{i}"
            center_y = (y1 + y2) / 2

            # Detectar caída si está horizontal (aspect ratio alto)
            if aspect_ratio > 1.3:
                start_time = self.fall_timers.get(person_id, time.time())
                elapsed = time.time() - start_time

                if elapsed > 2:  # si lleva 2 segundos caído
                    events.append({
                        "type": "fall",
                        "id": person_id,
                        "center_y": center_y
                    })

                self.fall_timers[person_id] = start_time
            else:
                self.fall_timers.pop(person_id, None)

        return events
