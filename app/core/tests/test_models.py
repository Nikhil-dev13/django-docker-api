from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with email is succesfull"""

        email = 'test@email.com'
        password = 'Testpaas123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user id normalized"""
        email = "test@EMAIL.com"
        user = get_user_model().objects.create_user(
            email,
            'test1233'
        )

        self.assertEqual(user.email, email.lower())

    def new_user_invalid_email(self):
        """Test creating a new user no email raises an error"""
        with self.asertRaises(ValueError):
            get_user_model.objects.create_user(None, 'test1233')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
