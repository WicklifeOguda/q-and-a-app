from django.contrib import admin
from quiz.models import Topic, Question


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    ordering = ("name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    ordering = ("topic__name",)
