from rest_framework import serializers
from .models import Story, StoryPart, PredictionQuestion, PredictionComment

class StoryPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryPart
        fields = ['id', 'story', 'author', 'text', 'created_at', 'likes_count']

class StorySerializer(serializers.ModelSerializer):
    parts = StoryPartSerializer(many=True, read_only=True)
    class Meta:
        model = Story
        fields = ['id', 'title', 'category', 'created_by', 'created_at', 'parts']

class PredictionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionComment
        fields = ['id', 'question', 'author', 'text', 'created_at', 'likes_count']

class PredictionQuestionSerializer(serializers.ModelSerializer):
    comments = PredictionCommentSerializer(many=True, read_only=True)
    class Meta:
        model = PredictionQuestion
        fields = ['id', 'question', 'category', 'created_by', 'created_at', 'comments']
