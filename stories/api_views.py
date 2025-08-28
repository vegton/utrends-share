from rest_framework import generics
from .models import Story, StoryPart, PredictionQuestion, PredictionComment
from .serializers import StorySerializer, StoryPartSerializer, PredictionQuestionSerializer, PredictionCommentSerializer

# Stories
class StoryListAPI(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class StoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class StoryPartAPI(generics.ListCreateAPIView):
    queryset = StoryPart.objects.all()
    serializer_class = StoryPartSerializer

# Predictions
class PredictionQuestionListAPI(generics.ListCreateAPIView):
    queryset = PredictionQuestion.objects.all()
    serializer_class = PredictionQuestionSerializer

class PredictionQuestionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = PredictionQuestion.objects.all()
    serializer_class = PredictionQuestionSerializer

class PredictionCommentAPI(generics.ListCreateAPIView):
    queryset = PredictionComment.objects.all()
    serializer_class = PredictionCommentSerializer
