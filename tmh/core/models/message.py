import uuid

from django.core.exceptions import ValidationError
from django.db import models

from tmh.core.models.user import User
from tmh.core.models.project import Project

def validate_message_content(content):
    if content is None or content == "" or content.isspace():
        raise ValidationError(
            'Content is empty/invalid',
            code='invalid',
            params={'content': content},
        )


class ProjectMessage(models.Model):

    id = models.UUIDField(
        primary_key=True,
        null=False,
        default=uuid.uuid4,
        editable=False
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    content = models.TextField(validators=[validate_message_content])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        '''A string representation of the model.'''
        return self.project.client.username + "'s " + self.project.room + ": " + self.content
