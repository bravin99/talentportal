from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from accounts.tokens import account_activation_token
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Profile
from accounts.forms import SignUpForm, UpdateUserForm, ProfileForm
import six
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Talent Portal Account'
            message = render_to_string('registration/emails/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect("account_activation_sent")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_encode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.confirmed_email = True
        user.save()
        login(request, user)
        return redirect("/")
    else:
        return render(request, 'registration/account_activation_invalid.html')


@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user.username)
    user_profile = get_object_or_404(Profile, user__username=user.username)

    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, request.FILES, instance=user)
        update_profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
    else:
        update_user_form = UpdateUserForm(instance=user)
        update_profile_form = ProfileForm(instance=user_profile)

    context = {
        'profile_form': update_profile_form,
        'user_form': update_user_form
        }
    return render(request, "accounts/profile.html", context)