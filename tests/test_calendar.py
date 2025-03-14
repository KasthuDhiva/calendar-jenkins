import unittest
from calendar import calendar

class TestCalendarApp(unittest.TestCase):
    def test_calendar_output(self):
        year = 2025
        result = calendar(year)
        self.assertIn("2025", result)  # Check if the year is in the output

if __name__ == "__main__":
    unittest.main()
