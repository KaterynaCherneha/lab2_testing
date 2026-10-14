import unittest
from unittest.mock import patch, mock_open
from salon_manager import SalonManager

class TestSalonManager(unittest.TestCase):

    def setUp(self):
        self.manager = SalonManager()
        self.manager.book_appointment("10:00", "Олена")
        self.manager.book_appointment("12:00", "Марія")

    def test_cancel_appointment_success(self):
        cancelled_client = self.manager.cancel_appointment("10:00")
        self.assertEqual(cancelled_client, "Олена")
        self.assertNotIn("10:00", self.manager.get_all_appointments())

    def test_book_appointment_duplicate_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.book_appointment("12:00", "Ірина")

    def test_cancel_missing_appointment_raises_error(self):
        with self.assertRaises(KeyError):
            self.manager.cancel_appointment("15:00")

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file(self, mock_file):
        filename = "test_appointments.json"
        result = self.manager.save_to_file(filename)
        self.assertTrue(result)
        mock_file.assert_called_once_with(filename, 'w', encoding='utf-8')
        self.assertTrue(mock_file().write.called)

if __name__ == '__main__':
    unittest.main()