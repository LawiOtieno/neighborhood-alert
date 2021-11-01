from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import NeighborHood,Profile,Business,Post

from django.forms import fields


#


# class SignUpForm(UserCreationForm):
#   first_name = forms.CharField(max_length=100, help_text='Last Name')
#   last_name = forms.CharField(max_length=100, help_text='Last Name')
#   email = forms.EmailField(max_length=150, help_text='Email')

#   class Meta:
#     model = User
#     fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# Profile/User
class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name','last_name','bio','profile_picture','location']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']


# NeighborHood
class CreateNeighborHoodForm(forms.ModelForm):
  class Meta:
    model = NeighborHood
    fields = ['name','location','description','population','police_contact','hospital_contact','image']

class UpdateNeighborhoodForm(forms.ModelForm):
  class Meta:
    model = NeighborHood
    fields = ['name','location','description','population','police_contact','hospital_contact','image']


# BusinessForm
class CreateBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ('name','description','image','email')


class UpdateBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ['name','description','image','email']


# PostForm
class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','post','image')

class UpdatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','post','image']
