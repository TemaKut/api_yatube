from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Post. """
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author',
                  'image', 'group', 'comments')


class GroupSerializer(serializers.ModelSerializer):
    """ Сераилизатор для модели Group. """

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Comment. """
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created', 'author', 'post')
