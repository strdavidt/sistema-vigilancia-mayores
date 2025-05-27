import time
from datetime import datetime

class EventDetector:
    def __init__(self):
        self.last_positions = {}
        self.fall_timers = {}
        self.disappear_timers = {}

    def detect_events(self, results):
        events = []
        current_ids = []

        for i, (person, conf) in enumerate(zip(results[0].boxes.xyxy, results[0].boxes.conf)):
            if conf < 0.5:
                continue

            x1, y1, x2, y2 = person[:4]
            w = x2 - x1
            h = y2 - y1
            aspect_ratio = w / h

            person_id = f"p{i}"
            center_y = (y1 + y2) / 2
            current_ids.append(person_id)  

            # Detectar caída si está horizontal (aspect ratio alto)
            if aspect_ratio > 1.3:
                start_time = self.fall_timers.get(person_id, time.time())
                elapsed = time.time() - start_time

                if elapsed > 2:
                    events.append({
                        "type": "fall",
                        "id": person_id,
                        "center_y": center_y
                    })

                self.fall_timers[person_id] = start_time
            else:
                self.fall_timers.pop(person_id, None)

            # Guardar posición (aunque por ahora no lo uses)
            self.last_positions[person_id] = (x1, y1, x2, y2)
        #obtener la hora actual
        now = datetime.now()
        hour = now.hour

        # Detectar personas que ya no están
        for person_id in list(self.last_positions.keys()):
            if person_id not in current_ids:
                if 7 <= hour < 21:  # Horario de día
                    if person_id not in self.disappear_timers:
                        self.disappear_timers[person_id] = time.time()
                    else:
                        elapsed = time.time() - self.disappear_timers[person_id]
                        if elapsed > 1200:  # 20 minutos fuera de vista
                            events.append({
                                "type": "exit",
                                "id": person_id
                            })
                            # Limpiar memoria
                            self.last_positions.pop(person_id, None)
                            self.disappear_timers.pop(person_id, None)
                            self.fall_timers.pop(person_id, None)
                else:  # Horario nocturno
                    self.disappear_timers.pop(person_id, None)
            else:
                self.disappear_timers.pop(person_id, None)
        return events
