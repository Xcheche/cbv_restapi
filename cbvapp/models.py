from django.db import models


# Create your models here.
# The class `Student` defines a model with fields for student ID, name, and score.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """Return a string representation of the student,
        consisting of the student's name and score, e.g. 'John 99.99'."""

        return f"{self.name} {self.score}"
