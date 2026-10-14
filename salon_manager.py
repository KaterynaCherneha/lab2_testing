import json

class SalonManager:
    def __init__(self):
        self.appointments = {}

    def book_appointment(self, time: str, client_name: str):
        if time in self.appointments:
            raise ValueError(f"Час {time} вже зайнятий!")
        self.appointments[time] = client_name
        return True

    def cancel_appointment(self, time: str):
        if time not in self.appointments:
            raise KeyError("Запису на цей час не знайдено.")
        return self.appointments.pop(time)

    def get_all_appointments(self):
        return self.appointments

    def save_to_file(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.appointments, f)
        return True