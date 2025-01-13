from rest_framework import serializers
from watchlist.models import Student
from watchlist.models import Movie


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')
    else:
        return value


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    # instance is the old data
    # validated_data is the new data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                'Name and Description should be different')
        else:
            return data


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    subject = serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.save()
        return instance
