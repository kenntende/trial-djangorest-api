from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='testy@mymail.co', password='passy787'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'main@manser.com'
        password = 'yiuuihj234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of a new user is normalized"""
        email = 'test@MANSERVER.COM'
        user = get_user_model().objects.create_user(email, 'testse223234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Testing creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12334dff')

    def test_create_new_super_user(self):
        """Creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@appextreme.org',
            '23e2dfr3f'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag str representation"""
        tag = models.Tag.objects().create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)