from django.test import TestCase
from .forms import CommentForm
from .forms import CollaborateForm

# Create your tests here.
class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg = 'Form is not valid')

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            'name': 'Test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )