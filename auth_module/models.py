from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    USER=(
        (1,'ADMIN'),
        (2, 'CORDINATOR'),
        (3, 'STUDENT'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Coridinator(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name

class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    programme = models.CharField(max_length=100, null=True)
    academic_year = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name
