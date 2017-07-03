import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def choices(request):
    return render(request, 'changeActions/choices.html')

def choiceActions(request, timespan):
    # picking one of the different categories of actions
    actions = ChangeAction.objects.filter(category__name=timespan)
    randAction = actions[random.randint(0, len(actions) - 1)]
    return redirect('detail', randAction.id)

def detail(request, action_id):
    # details page of a changeAction
    action = get_object_or_404(ChangeAction, pk=action_id)
    category = Category.objects.get(changeaction__id__contains=action.pk)
    return render(request, 'changeActions/detail.html', {'action': action, 'category': category})

def index(request):
    allCategories = Category.objects.all()
    pass

