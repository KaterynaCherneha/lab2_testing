import unittest
from fastapi.testclient import TestClient
from main import app, fake_db

class TestSalonMicroservice(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        fake_db.clear()
        fake_db["10:00"] = "Олена"

    def test_create_appointment_success(self):
        response = self.client.post(
            "/appointments/",
            json={"time": "14:00", "client_name": "Ірина"}
        )
        self.assertEqual(response.status_code, 200)

    def test_create_appointment_conflict(self):
        response = self.client.post(
            "/appointments/",
            json={"time": "10:00", "client_name": "Марія"}
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_appointment_not_found(self):
        response = self.client.delete("/appointments/18:00")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()