from django.test import TestCase
from .models import Project


class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title='first project')
        Project.objects.create(description='a description here')

    def test_title_content(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEquals(expected_object_name, 'first project')

    def test_description_content(self):
        project = Project.objects.get(id=2)
        expected_object_name = f'{project.description}'
        self.assertEquals(expected_object_name, 'a description here')