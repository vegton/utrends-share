from django import forms
from .models import Story, StoryPart, PredictionQuestion, PredictionComment

# ---------------- Story Forms ----------------
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Story title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class StoryPartForm(forms.ModelForm):
    class Meta:
        model = StoryPart
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Continue the story...',
                'rows': 3,
                'maxlength': 200
            }),
        }


# ---------------- Prediction Forms ----------------
class PredictionQuestionForm(forms.ModelForm):
    class Meta:
        model = PredictionQuestion
        fields = ['question', 'category']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class PredictionCommentForm(forms.ModelForm):
    class Meta:
        model = PredictionComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your prediction...',
                'rows': 3,
                'maxlength': 200
            }),
        }
