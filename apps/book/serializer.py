from rest_framework import serializers
from apps.book.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'title', 'author', 'price', 'rating', 'updated_at', 'created_at')




