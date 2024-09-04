from django.shortcuts import render
from quiz.models import Topic, Question
from django.db.models import Q
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    questions = Question.objects.all()
    topics = Topic.objects.all()
    active_topic = request.GET.get("topic", "")

    if active_topic:
        questions = questions.filter(topic__name=active_topic)

    search = request.GET.get("search", "")
    if search:
        questions = questions.filter(
            Q(header__icontains=search) | Q(description__icontains=search)
        )
    context = {
        "questions": questions,
        "topics": topics,
        "active_topic": active_topic,
    }

    return render(
        request=request,
        template_name="core/homepage.html",
        context=context,
    )
