from django.utils import timezone
from rest_framework import serializers
from books.models import Book ,Author, Publisher
from datetime import datetime, timedelta


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields ='__all__'
        
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields ='__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields ='__all__'

    
    def validate(self, attrs):
        title = attrs.get("title")
        description = attrs.get("description")
        published_date = attrs.get("published_date")
        price = attrs.get("price")

        if title and len(title) > 100:
            raise serializers.ValidationError("Title cannot exceed 100 characters")

        if description and len(description.split()) < 10:
            raise serializers.ValidationError("Description must have at least 10 words")

        if published_date:
            one_month_ago = datetime.now().date() - timedelta(days=30)
            if published_date > one_month_ago:
                raise serializers.ValidationError("Publication date must be at least one month old")

        if price is not None and (price < 100 or price > 10000):
            raise serializers.ValidationError("Price must be between 100 and 10000")

        return attrs


        
    def create(self, validated_data):
        author_data = validated_data.pop("author")
        publisher_data = validated_data.pop("publisher", None)
        
        author_serializer = AuthorSerializer(data=author_data)
        if author_serializer.is_valid():
            author_instance = author_serializer.save()
            validated_data["author"] = author_instance
        
        if publisher_data:
            publisher_serializer = PublisherSerializer(data=publisher_data)
            if publisher_serializer.is_valid():
                publisher_instance = publisher_serializer.save()
                validated_data["publisher"] = publisher_instance

        return super().create(validated_data)


        

    def update(self , instance, validated_date):
        validated_data["updated_at"] = timezone.now()
        
        author_data = validated_data.pop("author", None)
        publisher_data = validated_data.pop("publisher", None)

        if author_data:
            author_serializer = AuthorSerializer(instance.author, data=author_data)
            if author_serializer.is_valid():
                author_serializer.save()

        if publisher_data:
            publisher_serializer = PublisherSerializer(instance.publisher, data=publisher_data)
            if publisher_serializer.is_valid():
                publisher_serializer.save()

        return super().update(instance, validated_data)
        


