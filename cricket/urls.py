from django.urls import path
from .views import *

# BASE URL = api/cricket/

urlpatterns = [
        path('admin/matches', AdminMatchCreateView.as_view(), name="admin-match-create"),
        path('admin/teams/<int:team_id>/squad', AdminPlayerCreateView.as_view(), name="admin-player-create"),
        path('matches', MatchListView.as_view(), name="match-list"),
        path('matches/<int:match_id>', MatchDetailView.as_view(), name="match-detail"),
        path('players/<int:player_id>/stats', PlayerDetailView.as_view(), name="player-detail"),
]