from django.contrib import admin
from .models import Story, StoryPart, PredictionQuestion, PredictionComment

# ---------------- Story & Parts ----------------
class StoryPartInline(admin.TabularInline):
    model = StoryPart
    extra = 1
    readonly_fields = ('author', 'created_at', 'likes_count')
    show_change_link = True

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'created_by__username')
    inlines = [StoryPartInline]
    ordering = ('-created_at',)


@admin.register(StoryPart)
class StoryPartAdmin(admin.ModelAdmin):
    list_display = ('story', 'author_name', 'text_short', 'likes_count', 'created_at')
    list_filter = ('story',)
    search_fields = ('text',)
    ordering = ('-created_at',)

    def author_name(self, obj):
        return obj.author.username if obj.author else "Anonymous"
    author_name.short_description = 'Author'

    def text_short(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    text_short.short_description = 'Text'


# ---------------- Prediction Questions & Comments ----------------
class PredictionCommentInline(admin.TabularInline):
    model = PredictionComment
    extra = 1
    readonly_fields = ('author', 'created_at', 'likes_count')
    show_change_link = True

@admin.register(PredictionQuestion)
class PredictionQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('question', 'created_by__username')
    inlines = [PredictionCommentInline]
    ordering = ('-created_at',)


@admin.register(PredictionComment)
class PredictionCommentAdmin(admin.ModelAdmin):
    list_display = ('question', 'author_name', 'text_short', 'likes_count', 'created_at')
    list_filter = ('question',)
    search_fields = ('text',)
    ordering = ('-created_at',)

    def author_name(self, obj):
        return obj.author.username if obj.author else "Anonymous"
    author_name.short_description = 'Author'

    def text_short(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    text_short.short_description = 'Text'
