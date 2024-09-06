from django.shortcuts import render, redirect
from quiz.models import Topic, Question
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, logout
from core.forms import SignUpForm


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


def signup(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("/")
    else:
        form = SignUpForm()

    return render(
        request=request,
        template_name="core/signup.html",
        context={"form": form},
    )


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")


def user_login(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="core/login.html",
    )
