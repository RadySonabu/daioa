from django.test import TestCase
from .models import Student


class ModelTesting(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="django",
            middle_name="django",
            last_name="django",
            age=25,
        )

    def test_model(self):
        student = self.student
        self.assertTrue(isinstance(student, Student))
        self.assertEqual(str(student), "django django")
