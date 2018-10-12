from django import forms
from .models import Game_Model


class GameForm(forms.ModelForm):
    class Meta:
        model = Game_Model
        fields = {'title', 'genre', }