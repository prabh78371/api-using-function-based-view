from rest_framework import serializers
from .models import student

class studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rollno = serializers.IntegerField()
    designation = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return student.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.rollno = validate_data.get('rollno',instance.rollno)
        instance.designation = validate_data.get('designation',instance.designation)
        instance.save()
        return instance
