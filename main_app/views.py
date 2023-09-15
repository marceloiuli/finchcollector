from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Snack
from .forms import PlayingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.snacks.all().values_list('id')
    snacks_finch_doesnt_have = Snack.objects.exclude(id__in=id_list)
    playing_form = PlayingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'playing_form': playing_form,
        'snacks': snacks_finch_doesnt_have
    })

def add_playing(request, finch_id):
    form = PlayingForm(request.POST)
    if form.is_valid():
        new_playing = form.save(commit=False)
        new_playing.finch_id = finch_id
        new_playing.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class SnackList(ListView):
    model = Snack

class SnackDetail(DetailView):
    model = Snack

class SnackCreate(CreateView):
    model = Snack
    fields = '__all__'

class SnackUpdate(UpdateView):
    model = Snack
    fields = ['name', 'color']

class SnackDelete(DeleteView):
    model = Snack
    success_url = '/snacks'

def assoc_snack(request, finch_id, snack_id):
    Finch.objects.get(id=finch_id).snacks.add(snack_id)
    return redirect('detail', finch_id=finch_id)



