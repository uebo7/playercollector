from django.forms import ModelForm
from .models import Win

class TourneyForm(ModelForm):
    class Meta:
        model = Win
        fields = ['tourney_wins', 'date']
