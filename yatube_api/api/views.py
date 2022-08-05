from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly, GetOnly


class PostViewSet(viewsets.ModelViewSet):
    """ Вьюсет для модели Post. """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        """ Установим имя автора для автоматического добавления. """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """ Вьюсет для модели Group. """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [GetOnly, IsAuthenticated]


class PostCommentsViewSet(viewsets.ModelViewSet):
    """ Вьюсет для получения комментариев к конкретному посту. """

    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        """ Возвращаем queryset комментариев запрошенного поста. """
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        return comments
