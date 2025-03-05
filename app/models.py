from django.db import models



class Fan(models.Model):
    objects=None
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "FAN"
        verbose_name_plural = "FANLAR"
        ordering = ['-pk']


class Student(models.Model):
    objects=None
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "STUDENT"
        verbose_name_plural = "STUDENTS"
        ordering = ['-pk']
