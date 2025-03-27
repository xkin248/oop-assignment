from visitor import Visitor
import datetime

class VisitorManagementSystem:
    def __init__(self):
        self.visitors = {}
        self.database = {}

    def add_visitor(self, name, passport_number, visit_date, duration_of_stay):
        visitor = Visitor(name, passport_number, visit_date, duration_of_stay)
        self.visitors[visitor.id] = visitor
        self.database[visitor.passport_number] = visitor
        print(f"Visitor {name} added successfully with ID {visitor.id}")

    def get_visitor(self, visitor_id):
        return self.visitors.get(visitor_id)

    def get_visitor_by_passport(self, passport_number):
        return self.database.get(passport_number)

    def list_all_visitors(self):
        return list(self.visitors.values())

    def update_visitor(self, visitor_id, name=None, passport_number=None, visit_date=None, duration_of_stay=None):
        visitor = self.get_visitor(visitor_id)
        if visitor:
            if name:
                visitor.name = name
            if passport_number:
                visitor.passport_number = passport_number
            if visit_date:
                visitor.visit_date = visit_date
            if duration_of_stay:
                visitor.duration_of_stay = duration_of_stay
            print(f"Visitor {visitor_id} updated successfully")
        else:
            print(f"Visitor {visitor_id} not found")

    def delete_visitor(self, visitor_id):
        visitor = self.visitors.pop(visitor_id, None)
        if visitor:
            self.database.pop(visitor.passport_number, None)
            print(f"Visitor {visitor_id} deleted successfully")
        else:
            print(f"Visitor {visitor_id} not found")

    def generate_report(self):
        report = {}
        for visitor in self.visitors.values():
            year = visitor.visit_date.year
            if year not in report:
                report[year] = 0
            report[year] += 1
        return report