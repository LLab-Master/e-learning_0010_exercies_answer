from django.db import models

class Dept(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Emp(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

