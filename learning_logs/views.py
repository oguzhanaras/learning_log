from django.shortcuts import render
from .models import Topic, Entry
# Create your views here.


def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ show all topics """
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
