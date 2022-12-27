from rest_framework import serializers
from djangotestapp.models import user

class UserSerailizer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ['email','username']
