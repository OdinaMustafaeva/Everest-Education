from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User, AbstractUser


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
    image = models.ImageField(default="img.png")
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class subjects(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class course(models.Model):
    level = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media", default="4317_Y7xt2pm.jpg")
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


class ielts(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name="teacher_stu_ielts")
    ielts = models.FloatField(max_length=9.0)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.name} - {self.ielts}"
    # class Post(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.ForeignKey(subjects, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     participants = models.ManyToManyField(
#         User, related_name='participants', blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-updated', '-created']
#
#     def __str__(self):
#         return self.name
#
#
# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-updated', '-created']
#
#     def __str__(self):
#         return self.body[0:50]
