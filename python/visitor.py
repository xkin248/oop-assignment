import uuid
import datetime

class Visitor:
    def __init__(self, name, passport_number, visit_date, duration_of_stay):
        self.id = uuid.uuid4()
        self.name = name
        self.passport_number = passport_number
        self.visit_date = visit_date
        self.duration_of_stay = duration_of_stay