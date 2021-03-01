from django.db import models


class Subject(models.Model):
    SUBJECT_NAME_CHOICES = [
        ('russian-lang', "Russian language"),
        ('social-sci', "Social science"),
        ('math', "Mathematics"),
    ]
    name = models.CharField(max_length=100, choices=SUBJECT_NAME_CHOICES, unique=True)


# class Message(models.Model):
#     text = models.CharField(max_length=100)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
