from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [
    # ---------- Stories ----------
    path('', views.home, name='home'),
    path('stories/', views.story_list, name='story_list'),          # List all stories
    path('stories/create/', views.create_story, name='create_story'), # Create a new story
    path('stories/<slug:slug>/', views.story_detail, name='story_detail'), # View story with parts
    path('stories/<slug:slug>/add/', views.add_story_part, name='add_story_part'), # Add part to story

    # ---------- Predictions ----------
    path('questions/', views.question_list, name='question_list'),  # List all questions
    path('questions/create/', views.create_question, name='create_question'), # Create new prediction question
    path('questions/<slug:slug>/', views.question_detail, name='question_detail'), # View question with comments
    path('questions/<slug:slug>/add/', views.add_prediction_comment, name='add_prediction_comment'), # Add prediction
]

from . import api_views
urlpatterns += [
    # Stories
    # path('api/stories/', api_views.StoryListAPI.as_view(), name='api_stories'),
    # path('api/stories/<int:pk>/', api_views.StoryDetailAPI.as_view(), name='api_story_detail'),
    # path('api/story-parts/', api_views.StoryPartAPI.as_view(), name='api_story_parts'),
    #
    # # Predictions
    # path('api/questions/', api_views.PredictionQuestionListAPI.as_view(), name='api_questions'),
    # path('api/questions/<int:pk>/', api_views.PredictionQuestionDetailAPI.as_view(), name='api_question_detail'),
    # path('api/comments/', api_views.PredictionCommentAPI.as_view(), name='api_comments'),
]