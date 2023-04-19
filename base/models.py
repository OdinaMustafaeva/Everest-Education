from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User


# Create your models here.

class location(models.Model):
    address = models.CharField(max_length=500)
    image = models.ImageField(null=True)
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class teacher(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Teachers")
    phone_number = models.CharField(max_length=50)
    work = models.ForeignKey(location, on_delete=models.CASCADE, null=True, related_name="work_address")
    age = models.IntegerField(null=True)
    victories = models.CharField(null=True)
    image = models.ImageField(null=True)
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class subjects(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class course(models.Model):
    level = models.CharField(max_length=100)
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE, related_name="course_subjects")
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name="teacher_course")
    daytime = models.CharField(max_length=150)
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} {self.level} -- {self.teacher.name}"


class students(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name="Students_in_course")

    def __str__(self):
        return self.name


class contact(models.Model):
    address = models.ForeignKey(location, on_delete=models.CASCADE, related_name="contact_adress")
    phone_number1 = models.CharField(max_length=100)
    phone_number2 = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=150, null=True)
    telegram = models.CharField(max_length=200, null=True)


class textbook(models.Model):
    user = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name="book_user")
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    file = models.FilePathField(null=True)
    since = models.DateTimeField(auto_now_add=True)
