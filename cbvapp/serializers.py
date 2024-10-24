from rest_framework import serializers  # import serializers

from .models import Student  # import Student model


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "score"]
