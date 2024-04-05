# tournaments/forms.py

from django import forms
from .models import Tournament, Match, Participant

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'sport', 'start_date','time','end_date']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['tournament', 'home_team', 'away_team', 'date','home_score', 'away_score']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['tournament','first_name', 'last_name', 'age']
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['home_score', 'away_score']
