class Appointment:
    def __init__(self, title, date, time, location, description):
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.description = description

    def get_details(self):
        return f"{self.title} on {self.date} at {self.time}, {self.location}: {self.description}"

class OnlineAppointment(Appointment):  # Inheritance
    def __init__(self, title, date, time, location, description, link):
        super().__init__(title, date, time, location, description)
        self.link = link

    def get_details(self):  # Polymorphism (method override)
        return super().get_details() + f" (Online link: {self.link})"

def create_appointments():
    # Object Instantiation
    appt1 = Appointment("Dentist Visit", "2025-05-21", "10:00", "Clinic", "Routine checkup")
    appt2 = OnlineAppointment("Team Meeting", "2025-05-22", "14:00", "Home", "Monthly sync", "https://meet.link")

    appointments = [appt1, appt2]
    for appt in appointments:
        try:  # Exception Handling
            print(appt.get_details())
        except Exception as e:
            print(f"Error displaying appointment: {e}")

if __name__ == "__main__":
    create_appointments()