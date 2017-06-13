import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def choices(request):
    return render(request, 'changeActions/choices.html')

def shortActions(request):
    allShortActions = ChangeAction.objects.filter(category__name="Short Actions")
    randAction = allShortActions[random.randint(0, len(allShortActions) - 1)]
    return redirect('detail', randAction.id)

def mediumActions(request):
    allMediumActions = ChangeAction.objects.filter(category__name="Medium Actions")
    randAction = allMediumActions[random.randint(0, len(allMediumActions) - 1)]
    return redirect('detail', randAction.id)

def longActions(request):
    allLongActions = ChangeAction.objects.filter(category__name="Long Actions")
    randAction = allLongActions[random.randint(0, len(allLongActions) - 1)]
    return redirect('detail', randAction.id)

def detail(request, action_id):
    action = get_object_or_404(ChangeAction, pk=action_id)
    return render(request, 'changeActions/detail.html', {'action': action})

def index(request):
    allCategories = Category.objects.all()
    pass

