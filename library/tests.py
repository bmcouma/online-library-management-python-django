from django.test import TestCase
from .models import Student, Book

class StudentModelTest(TestCase):
	def test_create_student(self):
		student = Student.objects.create(name='Test Student', email='test@student.com', branch='CSE', roll_no='123', phone='1234567890')
		self.assertEqual(student.name, 'Test Student')

class BookModelTest(TestCase):
	def test_create_book(self):
		book = Book.objects.create(name='Test Book', author='Author', isbn='1234567890')
		self.assertEqual(book.name, 'Test Book')
