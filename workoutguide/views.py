from django.shortcuts import render
from .models import Workout

def index(request):
    workouts = Workout.objects.all()
    return render(request, 'workoutguide/index.html', {'workouts': workouts})

def home(request):
    return render(request, 'workoutguide/index.html')

def why(request):
    return render(request, 'workoutguide/why.html')

def trainers(request):
    return render(request, 'workoutguide/trainer.html')

def workoutplan(request):
    workouts = Workout.objects.all()
    return render(request, 'workoutguide/workoutplan.html', {'workouts': workouts})
