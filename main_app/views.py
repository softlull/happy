from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from .models import Happy, User
from .forms import HappyForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    happys = Happy.objects.order_by('-likes')
    form = HappyForm()
    return render(request, 'index.html', {'happys':happys, 'form':form})

def detail(request, happy_id):
    happy = Happy.objects.get(id=happy_id)
    return render(request, 'detail.html', {'happy': happy})

def post_happy(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HappyForm(data = request.POST, files = request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            treasure = form.save(commit = False)
            treasure.user = request.user
            treasure.likes = 0
            treasure.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/')
        
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    happys = Happy.objects.filter(user=user)
    return render(request, 'profile.html',
                  {'username': username,
                  'happys': happys})
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_happy(request):
    happy_id = request.POST.get('happy_id', None)
    
    likes = 0
    if(happy_id):
        happy = Happy.objects.get(id=int(happy_id))
        if happy is not None:
            likes = happy.likes + 1
            happy.likes = likes
            happy.save()
            
    return HttpResponse(likes)