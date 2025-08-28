from django.shortcuts import render, redirect, get_object_or_404
from .models import Story, StoryPart, PredictionQuestion, PredictionComment
from .forms import StoryForm, StoryPartForm, PredictionQuestionForm, PredictionCommentForm
from django.db.models import Count

# ---------------- Stories ----------------
def story_list(request):
    category = request.GET.get('category', None)
    stories = Story.objects.all().annotate(parts_count=Count('parts')).order_by('-created_at')
    if category:
        stories = stories.filter(category=category)

    # Add category choices to context
    category_choices = Story.CATEGORY_CHOICES
    return render(request, 'hub/story_list.html', {
        'stories': stories,
        'category': category,
        'category_choices': category_choices
    })

def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    parts = story.parts.all().order_by('created_at')
    return render(request, 'hub/story_detail.html', {'story': story, 'parts': parts})

def create_story(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()
            return redirect('stories:story_detail', slug=story.slug)
    else:
        form = StoryForm()
    return render(request, 'hub/create_story.html', {'form': form})

def add_story_part(request, slug):
    story = get_object_or_404(Story, slug=slug)
    if request.method == 'POST':
        form = StoryPartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.story = story
            if request.user.is_authenticated:
                part.author = request.user
            part.save()
            return redirect('stories:story_detail', slug=story.slug)
    else:
        form = StoryPartForm()
    return render(request, 'hub/add_story_part.html', {'form': form, 'story': story})

def react_story_part(request, slug):
    part = get_object_or_404(StoryPart, slug=slug)
    part.likes_count += 1
    part.save()
    return redirect('stories:story_detail', slug=part.story.slug)


# ---------------- Predictions ----------------
def question_list(request):
    category = request.GET.get('category', None)
    questions = PredictionQuestion.objects.all().annotate(comments_count=Count('comments')).order_by('-created_at')
    if category:
        questions = questions.filter(category=category)
    return render(request, 'hub/question_list.html', {'questions': questions, 'category': category})

def question_detail(request, slug):
    question = get_object_or_404(PredictionQuestion, slug=slug)
    comments = question.comments.all().order_by('created_at')
    return render(request, 'hub/question_detail.html', {'question': question, 'comments': comments})

def create_question(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    if request.method == 'POST':
        form = PredictionQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('stories:question_detail', slug=question.slug   )
    else:
        form = PredictionQuestionForm()
    return render(request, 'hub/create_question.html', {'form': form})

def add_prediction_comment(request, slug):
    question = get_object_or_404(PredictionQuestion, slug=slug)
    if request.method == 'POST':
        form = PredictionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            return redirect('stories:question_detail', slug=question.slug)
    else:
        form = PredictionCommentForm()
    return render(request, 'hub/add_comment.html', {'form': form, 'question': question})

def react_prediction_comment(request, slug):
    comment = get_object_or_404(PredictionComment, slug=slug)
    comment.likes_count += 1
    comment.save()
    return redirect('stories:question_detail', slug=comment.question.slug)


# Add to views.py
# def home(request):
#     # Get latest stories with parts count
#     latest_stories = Story.objects.all().annotate(
#         parts_count=Count('parts')
#     ).order_by('-created_at')[:6]
#
#     # Get trending stories (most likes on parts)
#     trending_stories = Story.objects.all().annotate(
#         total_likes=Sum('parts__likes_count'),
#         parts_count=Count('parts')
#     ).order_by('-total_likes')[:3]
#
#     # Get latest prediction questions with comments count
#     latest_questions = PredictionQuestion.objects.all().annotate(
#         comments_count=Count('comments')
#     ).order_by('-created_at')[:6]
#
#     # Get trending questions (most comments)
#     trending_questions = PredictionQuestion.objects.all().annotate(
#         comments_count=Count('comments')
#     ).order_by('-comments_count')[:3]
#
#     # Get some statistics
#     total_stories = Story.objects.count()
#     total_predictions = PredictionQuestion.objects.count()
#     total_contributions = StoryPart.objects.count() + PredictionComment.objects.count()
#
#     context = {
#         'latest_stories': latest_stories,
#         'trending_stories': trending_stories,
#         'latest_questions': latest_questions,
#         'trending_questions': trending_questions,
#         'total_stories': total_stories,
#         'total_predictions': total_predictions,
#         'total_contributions': total_contributions,
#     }
#
#     return render(request, 'hub/home.html', context)