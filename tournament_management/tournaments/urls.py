from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
    path('register/', views.tournament_registration, name='tournament_registration'),
    path('matches/', views.match_list, name='match_list'),
    path('matches/<int:match_id>/', views.match_detail, name='match_detail'),
    path('matches/<int:match_id>/update/', views.update_match, name='update_match'),
    path('matches/<int:match_id>/record_scores/', views.record_scores, name='record_scores'),
    path('matches/<int:match_id>/determine_winner/', views.determine_winner, name='determine_winner'),   
    path('participants/', views.participant_management, name='participant_management'),
     path('participants/create/', views.create_participant, name='create_participant'),
    path('statistics/', views.statistics, name='statistics'),
    path('create-match/', views.create_match, name='create_match'),
        path('tournaments/', views.tournament_list, name='tournament_list'),

]
