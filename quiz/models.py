from django.db import models
import uuid


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    header = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    answer = models.TextField()
    topic = models.ForeignKey(Topic, related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return self.header
