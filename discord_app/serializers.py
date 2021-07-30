from django.db.models import fields
from rest_framework import serializers
from django.db import models

from .models import Discord_Apps_List, NLP_Models

class Discord_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Discord_Apps_List
        fields = '__all__'


class Nlp_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NLP_Models
        fields = '__all__'