from rest_framework import serializers
from . models import TrialClass

class TrialClassSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = TrialClass
        fields =('parents_name','child_name')