from rest_framework import serializers
from projects.models import project, tag, Reviews
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many = False)
    Tags = TagSerializer(many = True)
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = project
        fields = '__all__'

    def get_reviews(self,obj):
        reviews = obj.reviews_set.all()
        serializer = ReviewSerializer(reviews,many = True)
        return serializer.data