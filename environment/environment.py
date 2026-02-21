import random

class DisasterEnvironment:
    def __init__(self):
        self.events = ["Fire", "Flood", "Earthquake", "Landslide"]

    def generate_event(self):
        event = random.choice(self.events)
        severity = random.randint(1, 10)
        return {"event": event, "severity": severity}