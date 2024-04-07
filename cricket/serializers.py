from rest_framework import serializers
from .models import Match, Player, Team, MatchStatus

class MatchCreateSerializer(serializers.Serializer):
    team1 = serializers.CharField(max_length=200)
    team2 = serializers.CharField(max_length=200)
    date = serializers.DateField()
    venue = serializers.CharField(max_length=200)

    def validate(self, attrs):
        if attrs['team1'] == attrs['team2']:
            raise serializers.ValidationError("Teams cannot be same")
        
        try:
            team1 = Team.objects.get(name=attrs['team1'])
        except Team.DoesNotExist:
            raise serializers.ValidationError("Team1 does not exist")

        try:
            team2 = Team.objects.get(name=attrs['team2'])
        except Team.DoesNotExist:
            raise serializers.ValidationError("Team2 does not exist")
        
        attrs['team1'] = team1
        attrs['team2'] = team2

        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['status'] = MatchStatus.UPCOMING
        return Match.objects.create(**validated_data)
    
class MatchListOrDetailSerializer(serializers.ModelSerializer):
    match_id = serializers.SerializerMethodField()
    team1 = serializers.SerializerMethodField()
    team2 = serializers.SerializerMethodField()
    class Meta:
        model = Match
        fields = [
            "match_id", "team1", "team2", "date", "status", "venue"
        ]
    
    def get_match_id(self, obj):
        return obj.id
    
    def get_team1(self, obj):
        return obj.team1.name
    
    def get_team2(self, obj):
        return obj.team2.name
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('is_detail')=="True":
            team1_players = Player.objects.filter(team=instance.team1)
            team2_players = Player.objects.filter(team=instance.team2)
            representation['squad'] = {
                'team1': PlayerListSerializer(team1_players, many=True).data,
                'team2': PlayerListSerializer(team2_players, many=True).data
            }
        return representation
    

class PlayerListSerializer(serializers.ModelSerializer):
    player_id = serializers.SerializerMethodField()
    class Meta:
        model = Player
        fields = [
            "player_id", "name"
        ]

    def get_player_id(self, obj):
        return obj.id
    
class PlayerCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    role = serializers.CharField(max_length=200)
    team = serializers.CharField(max_length=200)
    matches_played = serializers.IntegerField(required=False)
    runs = serializers.IntegerField(required=False)
    average = serializers.FloatField(required=False)
    strike_rate = serializers.FloatField(required=False)

    def validate(self, attrs):
        try:
            team = Team.objects.get(id=attrs['team'])
        except Team.DoesNotExist:
            raise serializers.ValidationError("Team does not exist")
        
        attrs['team'] = team
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Player.objects.create(**validated_data)
    

class PlayerDetailSerializer(serializers.ModelSerializer):
    player_id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    class Meta:
        model = Player
        fields = [
            "player_id", "name", "role", "team", "matches_played", "runs", "average", "strike_rate"
        ]

    def get_player_id(self, obj):
        return obj.id

    def get_team(self, obj):
        return obj.team.name