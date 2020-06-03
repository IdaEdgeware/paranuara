from app import APP
import pytest
import unittest


class FlaskTestCase(unittest.TestCase):
    def test_positive_route_company(self):
        tester = APP.test_client(self)
        response = tester.get(
            "/paranuara/company/COWTOWN", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_negative_route_company(self):
        tester = APP.test_client(self)
        response = tester.get(
            "/paranuara/companIES/COWTOWN", content_type="application/json"
        )
        self.assertNotEqual(response.status_code, 200)

    def test_positive_route_person(self):
        tester = APP.test_client(self)
        response = tester.get(
            "/paranuara/person/Decker%20Mckenzie", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_negative_route_people(self):
        tester = APP.test_client(self)
        response = tester.get(
            "paranuara/persON/Decker%20Mckenzie", content_type="application/json"
        )
        self.assertNotEqual(response.status_code, 200)

    def test_positive_route_people(self):
        tester = APP.test_client(self)
        response = tester.get(
            "/paranuara/people/?person1=Decker%20Mckenzie&person2=Rosemary%20Hayes",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_negative_route_person(self):
        tester = APP.test_client(self)
        response = tester.get(
            "paranuara//peOPle/person1=Decker%20Mckenzie&person2=Rosemary%20Hayes",
            content_type="application/json",
        )
        self.assertNotEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
