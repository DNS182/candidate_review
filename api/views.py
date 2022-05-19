from rest_framework import viewsets
from .serializers import CandidateSerializer
from candidate.models import Candidate
from rest_framework import filters


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter , filters.OrderingFilter]
    search_fields = ['Name','Position'] 
    ordering_fields = '__all__'