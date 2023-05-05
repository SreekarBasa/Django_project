from django.shortcuts import render
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        Name = request.POST["Name"]
        username = request.POST['username']
        email = request.POST['email']
        Mobile = request.POST['phone_number']
        password = request.POST['password']
        password_check = request.POST['confirm_password']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            error = 'Username already exists. Please choose a different username.'
            return render(request, 'signup.html', {'error': error})

        # Proceed with signup process
        user = User.objects.create_user(username, email, password, Name)
        user.save()

        # Render success page
        return render(request, 'index.html')

    # Render signup form
    return render(request, 'signup.html')


'''
MY code...
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if "sign_up" in request.POST:
            Name = request.POST["Name"]
            username = request.POST["username"]
            password = request.POST["password"]
            password_check = request.POST["password_check"]
            Mobile = request.POST["Mobile"]
            Email = request.POST["Email"]
            if password == password_check:
                if User.objects.filter(username=username).exists():
                    if User.objects.filter(Email=Email).exists():
                        user = User.objects.create_user(username=username, password=password, Email=Email,
                                                        Name=Name, Mobile=Mobile)
                        messages.info(request, 'You have been successfully registered!!')
                        user.save()

                    else:
                        messages.info(request, 'Try a unique Email this already exists')
                        return redirect('/')

                else:
                    messages.info(request, 'Try a unique username this already exists')
                    return redirect('/')
            else:
                messages.info(request, ' Error! recheck your password ')
                return redirect('/')

    return render(request, 'signup.html')

'''