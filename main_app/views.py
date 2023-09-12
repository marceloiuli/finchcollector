from django.shortcuts import render

finches = [
    {'name': 'Waynebow', 'breed': 'Gouldian Finch', 'description': 'rainbow colored buddy', 'age': 10},
    {'name': 'Finkachu', 'breed': 'American Goldfinch', 'description': 'bright yellow and very energetic', 'age': 6},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })