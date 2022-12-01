from rest_framework.serializers import ModelSerializer
from .models import Post
from reviews.serializers import CommentSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance: Post):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.username
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep