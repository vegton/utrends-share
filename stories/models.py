from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
User = get_user_model()

# ---------------- Stories ----------------
class Story(models.Model):
    CATEGORY_CHOICES = [
        ('adventure', 'Adventure'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
    ]
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='adventure')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Story.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class StoryPart(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="parts")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="story_parts")
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)  # Anyone can react

    def __str__(self):
        return f"{self.author.username if self.author else 'Anonymous'}: {self.text[:30]}..."


# ---------------- Predictions ----------------
class PredictionQuestion(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('politics', 'Politics'),
        ('technology', 'Technology'),
        ('entertainment', 'Entertainment'),
        ('finance', 'Finance'),
        ('health', 'Health'),
    ]

    question = models.CharField(max_length=255)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sports')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.question)
            slug = base_slug
            counter = 1
            while PredictionQuestion.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question


class PredictionComment(models.Model):
    question = models.ForeignKey(PredictionQuestion, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="predictions")
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)  # Anyone can react

    def __str__(self):
        return f"{self.author.username if self.author else 'Anonymous'}: {self.text[:30]}..."
