from django.contrib.auth import get_user_model
from rest_framework import serializers
from candidate.models import Candidate


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        exclude = ('Resume', 'Applied_on' , 'Status' )
