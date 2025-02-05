from rest_framework import serializers
from watchlist.models import Student, WatchList, StreamPlatform, Review


# model based serializer
class ReviewsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

    def create(self, validated_data):

        return Review.objects.create(**validated_data)


class WatchListSerializer(serializers.ModelSerializer):
    # readonly ensures we can only read reviews and not add them from this serializer
    reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # when returning a single item
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     # instance is the old data
#     # validated_data is the new data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 'Name and Description should be different')
#         else:
#             return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# using viewsets and routers for students model
