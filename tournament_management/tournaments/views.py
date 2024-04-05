from django.shortcuts import get_object_or_404, render, redirect
from .models import Tournament, Match, Participant, TournamentResult
from .forms import ScoreForm, TournamentForm, MatchForm, ParticipantForm

def tournament_registration(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tournament_list')  
    else:
        form = TournamentForm()
    return render(request, 'tournaments/tournament_registration.html', {'form': form})


def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournament_list.html', {'tournaments': tournaments})


def participant_management(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_management') 
    else:
        form = ParticipantForm()
    return render(request, 'tournaments/participant_management.html', {'form': form})

def statistics(request):
    total_matches = Match.objects.count()
    context = {
        'total_matches': total_matches,
    }
    return render(request, 'tournaments/statistics.html', context)

def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_management')
    else:
        form = ParticipantForm()
    return render(request, 'tournaments/create_participant.html', {'form': form})

def match_list(request):
    matches = Match.objects.all()
    print(matches)
    return render(request, 'tournaments/match_list.html', {'matches': matches})

def match_detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    print('Template dirs:', request.resolver_match.func.__globals__['__file__'])
    return render(request, 'tournaments/match_detail.html', {'match': match})

def update_match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    print('Template dirs:', request.resolver_match.func.__globals__['__file__'])
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_detail', match_id=match_id)
    else:
        form = MatchForm(instance=match)
    return render(request, 'tournaments/update_match.html', {'form': form})
def record_scores(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_detail', match_id=match_id)
    else:
        form = ScoreForm(instance=match)
    return render(request, 'tournaments/record_scores.html', {'form': form})

def determine_winner(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if match.home_score > match.away_score:
        winner = match.home_team
    elif match.away_score > match.home_score:
        winner = match.away_team
    else:
        winner = None  
    return render(request, 'tournaments/determine_winner.html', {'match': match, 'winner': winner})
def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')  
    else:
        form = MatchForm()
    return render(request, 'tournaments/match_form.html', {'form': form})

