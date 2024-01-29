from django.db import models

# Create your models here.


class Approval(models.Model):
    committe_type = models.CharField(max_length=255)
    hospital_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.committe_type


class Person(models.Model):
    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    approval_type = models.CharField(max_length=255)
    diagnosis = models.TextField()
    approval = models.ForeignKey(Approval, on_delete=models.CASCADE, null=True)
    approval_date = models.DateField()
    additional_note = models.TextField()
