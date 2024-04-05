from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tournament, Participant, Match

admin.site.register(Tournament)
admin.site.register(Participant)
admin.site.register(Match)