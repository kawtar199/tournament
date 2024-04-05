from datetime import date
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name
class Participant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="John")  # Default value set to "John"
    last_name = models.CharField(max_length=100,default="doe")
    age = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TournamentResult(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.participant.user.username} - {self.tournament.name} (Rank: {self.rank})"



class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Participant, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Participant, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.tournament}"

