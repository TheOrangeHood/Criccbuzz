from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class PlayerRole(models.TextChoices):
    BATSMAN = "batsman", "Batsman"
    BOWLER = "bowler", "Bowler"
    ALL_ROUNDER = "allrounder", "All Rounder"
    WICKET_KEEPER = "wicket_keeper", "Wicket Keeper"

class Player(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=PlayerRole.choices, default=PlayerRole.BATSMAN)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    matches_played = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    strike_rate = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name
    
class MatchStatus(models.TextChoices):
    UPCOMING = "upcoming", "Upcoming"
    COMPLETED = "completed", "Completed"

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2")
    date = models.DateField()
    status = models.CharField(max_length=200, choices=MatchStatus.choices, default=MatchStatus.UPCOMING)
    venue = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.team1} vs {self.team2} on {self.date}"

    
