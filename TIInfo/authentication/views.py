from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def SignIn(request):
    data = {'title' : 'Login to Travel India Info'
        
    }

    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('signin')

    return render(request, "authentication/SignIn.html", data)

def SignUp(request):
    data = {'title' : 'Sign Up to Travel India Info'
    }

    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")



        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other Username")
            return redirect("signup")
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect("signup")

        if len(username)>12:
            messages.error(request, "Username must be under 12 characters")
            return redirect("signup")
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect("signup")
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric! (use only alphabets and numbers.)")
            return redirect("signup")



        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request,"Your account is successfully created.")

        return redirect('/signin/')


    return render(request, "authentication/SignUp.html", data)


def SignOut(request):
    data = {'title' : 'Login'
        
    }

    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('signin')
