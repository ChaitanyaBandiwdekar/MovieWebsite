from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'cap_login.html')

    else:
        u_name = request.POST['u_name']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=u_name, password=pass1)

        if user is not None:
            auth.login(request, user)
            print('User logged in')
            return redirect('/')

        else:
            print('error')
            messages.info(request, 'Invalid credentials! Please try again')
            return redirect('/accounts/login/')

def signup(request):

    if request.method == 'GET':
        return render(request, 'cap_signup_form.html')

    else:
        u_name = request.POST['u_name']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, 'Username already taken!', extra_tags='u_name')
                return redirect('/accounts/signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken!', extra_tags='email')
                return redirect('/accounts/signup')

            else:
                user = User(username=u_name, email=email, first_name=f_name, last_name=l_name)
                user.set_password(pass1)
                user.save()
                return redirect('/accounts/login')

        else:
            messages.info(request, 'Password not matching!', extra_tags='pass')
            return redirect('/accounts/signup')


def logout(request):
    auth.logout(request)
    return redirect('/')
