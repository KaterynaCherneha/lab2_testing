from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Сервіс запису в салон краси")
fake_db = {}

class Appointment(BaseModel):
    time: str
    client_name: str

@app.post("/appointments/")
def create_appointment(appointment: Appointment):
    if appointment.time in fake_db:
        raise HTTPException(status_code=400, detail="Цей час вже зайнятий")
    fake_db[appointment.time] = appointment.client_name
    return {"message": "Запис створено", "data": appointment}

@app.get("/appointments/")
def get_appointments():
    return fake_db

@app.delete("/appointments/{time}")
def delete_appointment(time: str):
    if time not in fake_db:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    client = fake_db.pop(time)
    return {"message": "Запис скасовано", "client": client}