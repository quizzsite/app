from django.db import models
from django.contrib.auth import get_user_model
import os

def videodir(instance, filename): return os.path.join('lessons', 'video', instance.user.username, '%Y-%m-%d', filename)
def icondir(instance, filename): return os.path.join('courses', 'subject', instance.name, filename)

class Message(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=99999999)

class Material(models.Model):
    name = models.CharField(default="Без названия", max_length=99999999)
    text = models.CharField(max_length=99999999)

class Choice(models.Model):
    text = models.CharField(max_length=99999999)
    correct = models.BooleanField(default=False)

class Question(models.Model):
    text = models.CharField(max_length=99999999)
    choices = models.ManyToManyField(Choice)
    accuracy = models.IntegerField(default=0)

class Task(models.Model):
    questions = models.ManyToManyField(Choice)
    accuracy = models.IntegerField(default=0)

class Lesson(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default="-", max_length=99999999)
    # course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, blank=True, on_delete=models.DO_NOTHING)
    video = models.FileField(upload_to="", blank=True)
    chat = models.ManyToManyField(Message, blank=True)
    tasks = models.ManyToManyField(Task, blank=True)

class Subject(models.Model):
    name = models.CharField(default="-", max_length=99999999)
    iconpath = models.ImageField(upload_to=icondir)

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(default="Безымянный", max_length=99999999)
    price = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    lessons = models.ManyToManyField(Lesson)
    # progress = models.IntegerField()