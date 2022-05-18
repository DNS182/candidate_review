from candidate.models import Candidate
from rest_framework import serializers

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['Name','Contact' , 'Email', 'Country','Degree' , 'Position' , 'Experience' , 'Applied_for' , 'Skills']