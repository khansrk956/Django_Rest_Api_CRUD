from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    sr_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    # Create
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # update
    def update(self, instance, validata_data):
        print(instance.name)
        instance.name = validata_data.get('name',instance)
        print(instance.name)
        instance.city = validata_data.get('city', instance)
        instance.save()
        return instance
    

    # delete
    

