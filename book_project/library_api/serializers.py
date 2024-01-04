from rest_framework import serializers
from library.models import Book, UserLibrary


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=150)
#     author = serializers.CharField(max_length=100)
#     year_of_publishing = serializers.IntegerField()
#     isbn = serializers.CharField(max_length=17)
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.author = validated_data.get('author', instance.author)
#         instance.year_of_publishing = validated_data.get('year_of_publishing', instance.year_of_publishing)
#         instance.isbn = validated_data.get('isbn', instance.isbn)
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'year_of_publishing', 'isbn']


class UserLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = ['name', 'email', 'date_registered']
