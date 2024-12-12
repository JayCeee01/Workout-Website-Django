from django.shortcuts import render
from .models import Workout, Tip

def index(request):
    workouts = Workout.objects.all()
    tips = Tip.objects.all()
    return render(request, 'workoutguide/index.html', {'workouts': workouts, 'tips': tips})

def home(request):
    return render(request, 'workoutguide/index.html')

def why(request):
    return render(request, 'workoutguide/why.html')

def trainers(request):
    return render(request, 'workoutguide/trainer.html')

def contact(request):
    return render(request, 'workoutguide/contact.html')
