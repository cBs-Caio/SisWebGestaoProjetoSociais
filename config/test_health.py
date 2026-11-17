from unittest.mock import patch

from django.db import OperationalError
from django.test import TestCase


class HealthTests(TestCase):
    def test_returns_up_when_database_responds(self):
        response = self.client.get("/healthz/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "up"})
        self.assertIn("no-store", response.headers["Cache-Control"])

    def test_returns_down_when_database_unavailable(self):
        with patch("config.health.connection.cursor", side_effect=OperationalError):
            response = self.client.get("/healthz/")

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json(), {"status": "down"})
