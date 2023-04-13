from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Player, Character
from .forms import TourneyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'players/index.html', {'players': players})

@login_required
def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    win_form = TourneyForm()
    player_character_ids = player.characters.all().values_list('id')
    characters_player_doesnt_play = Character.objects.exclude(id__in=player_character_ids)
    return render(request, 'players/detail.html', {
        'player': player, 
        'win_form': win_form,
        'characters': characters_player_doesnt_play
    })

@login_required
def add_win(request, player_id):
    form = TourneyForm(request.POST)
    if form.is_valid():
        new_win = form.save(commit=False)
        new_win.player_id = player_id
        new_win.save()
    return redirect('player_detail', player_id=player_id)

@login_required
def assoc_character(request, player_id, character_id):
    player = Player.objects.get(id=player_id)
    player.characters.add(character_id)
    return redirect('player_detail', player_id=player_id)

@login_required
def unassoc_character(request, player_id, character_id):
    player = Player.objects.get(id=player_id)
    player.characters.remove(character_id)
    return redirect('player_detail', player_id=player_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            return redirect('players_index')
        else:
            error_message = 'Invalid Sign In'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    })
    

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = 'name', 'age', 'current_rank', 'alltime_rank'
    template_name = 'players/player_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ('age', 'current_rank', 'alltime_rank')
    template_name = 'players/player_form.html'

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = 'players/player_confirm_delete.html'
    success_url = '/players/'

class CharacterIndex(LoginRequiredMixin, ListView):
    model = Character
    
class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = '__all__'
    
class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/characters/'
    
class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Character
    
class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    fields = '__all__'

