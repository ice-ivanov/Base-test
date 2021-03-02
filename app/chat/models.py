from django.db import models


class Subject(models.Model):
    SUBJECT_NAME_CHOICES = [
        ('russian-lang', "Russian language"),
        ('social-sci', "Social science"),
        ('math', "Mathematics"),
    ]
    name = models.CharField(max_length=100, choices=SUBJECT_NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name
