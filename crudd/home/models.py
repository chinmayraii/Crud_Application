from django.db import models

class student(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    cname=models.CharField(max_length=20)
    email=models.EmailField()
    pnumber=models.IntegerField()
    def __str__(self) -> str:
        return self.fname
