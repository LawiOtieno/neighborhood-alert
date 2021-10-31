from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect

from django.contrib.auth import login, authenticate
from .forms import *
# from .forms import SignUpForm
from .models import NeighborHood,Profile,Post,Business
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.core.mail import EmailMessage



# Create your views here.
@login_required
def index(request):
    current_user = request.user
    neighborhoods = NeighborHood.objects.all().order_by('-created_at')
    return render(request, 'index.html',{'current_user':current_user, 'neighborhoods':neighborhoods})

def signup_view(request):
  if request.method  == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.refresh_from_db()
      user.profile.first_name = form.cleaned_data.get('first_name')
      user.profile.last_name = form.cleaned_data.get('last_name')
      user.profile.email = form.cleaned_data.get('email')
      # user can't login until link confirmed
      user.is_active = False
      user.save()
      current_site = get_current_site(request)
      subject = 'Please Activate Your Account'
      # load a template like get_template() 
      # and calls its render() method immediately.
      message = render_to_string('registration/activation_request.html', {
          'user': user,
          'domain': current_site.domain,
          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
          # method will generate a hash value with user related data
          'token': account_activation_token.make_token(user),
      })
      to_email = form.cleaned_data.get('email')
      email = EmailMessage(subject, message, to=[to_email])
      email.send()
      return redirect('activation_sent')
  else:
    form = SignUpForm()
  return render(request, 'registration/signup.html', {'form': form})
