from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import *
from rest_framework.response import Response


class AdminMatchCreateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)
    
    def post(self, request):
        serializer = MatchCreateSerializer(data = request.data)
        if serializer.is_valid(raise_exception=False):
            match = serializer.save()
            payload = {
                "message":"Match created successfully",
                "match_id": match.id
            }
            return Response(payload)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MatchDetailView(APIView):
    def get(self, request, match_id):
        match = Match.objects.get(id=match_id)
        serializer = MatchListOrDetailSerializer(match, context = {'is_detail':"True"})
        return Response(serializer.data)
    
class MatchListView(APIView):
    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchListOrDetailSerializer(matches, many=True)
        payload = {
            'matches': serializer.data
        }
        return Response(payload)
    
class AdminPlayerCreateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)
    
    def post(self, request, team_id):
        serializer = PlayerCreateSerializer(data = request.data)
        request.data['team'] = team_id
        print(request.data)
        if serializer.is_valid(raise_exception=False):
            player = serializer.save()
            payload = {
                "message":"Player added to squad successfully",
                "player_id": player.id
            }
            return Response(payload)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PlayerDetailView(APIView):
    def get(self, request, player_id):
        player = Player.objects.get(id=player_id)
        serializer = PlayerDetailSerializer(player)
        return Response(serializer.data)