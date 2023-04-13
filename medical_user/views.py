from django.shortcuts import render, redirect

from medical_user.forms import CustomUserForm
from medical_user.models import CustomUser
from django.db import transaction
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as logout_new


def logout(request, **kwargs):
    logout_new(request)

    return redirect('/')


def login(request, **kwargs):
    if request.POST:
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(email=email, user_type=user_type, password=password).first()
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            # User authentication failed, handle the error
            # You can display an error message to the user or take any other appropriate action
            error = 'This user is not available'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


def signup(request, **kwargs):
    if request.POST:
        form = CustomUserForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    # Perform database operations here, such as saving form data
                    form.save()
                    return redirect('login')
                    # Other database operations...
                # If all operations within the transaction are successful, commit the changes
                # to the database
            except Exception as e:
                # If any error occurs during the transaction, rollback the changes
                # to the database and handle the error
                transaction.rollback()
                return render(request, 'signup.html', {'form': form})



        else:
            return render(request, 'signup.html', {'form': form})

            # user = CustomUser()
            # user.user_type = user_type
            # user.first_name = first_name
            # user.last_name = last_name
            # user.email = email
            # user.password = password
            # user.save()

    else:
        form = CustomUserForm()

    return render(request, 'signup.html', {'form': form})
