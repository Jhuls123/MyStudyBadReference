from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        # exclud means that if thiers input that you don't want to be included just put inside the squere bracket so that it will not be included to the form.
        exclude = ['host', 'participants'] 

class UserFrom(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
