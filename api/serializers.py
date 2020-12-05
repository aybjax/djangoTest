from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    title = serializers.CharField(max_length=30)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'title',
            'date',
        ]
        model = Article
