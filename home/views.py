from django.shortcuts import render, redirect
from django.db import transaction

from home.forms import AppointmentForm
from home.models import Appointment
from medical_user.models import CustomUser
# Create your views here.

def index(request, **kwargs):
    if request.user:
        if hasattr(request.user, 'user_type'):
            if request.user.user_type == '1':
                return render(request, 'appointment.html')

    return render(request, 'index.html')


def login(request, **kwargs):

    return render(request, 'index.html')


def add_appointment(request, **kwargs):
    patients = CustomUser.objects.filter(user_type='1').all()

    if request.POST:
        patient = request.POST.get('patient')
        doctor_name = request.POST.get('doctor_name')
        data = request.POST.get('data')

        form = AppointmentForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    # Perform database operations here, such as saving form data
                    form.instance.patient_id = request.POST.get('patient')
                    form.save()
                    return redirect('/appointment')
                    # Other database operations...
                # If all operations within the transaction are successful, commit the changes
                # to the database
            except Exception as e:
                # If any error occurs during the transaction, rollback the changes
                # to the database and handle the error
                transaction.rollback()
                return render(request, 'add_appointment.html', {'form': form})

    else:
        form = AppointmentForm()

    return render(request, 'add_appointment.html', {'patients': patients, 'form': form})


def appintment(request, **kwargs):
    if request.user:
        if hasattr(request.user, 'user_type'):
            if request.user.user_type == '1':
                appintments = Appointment.objects.filter(patient__user_type='1').all()

            else:
                appintments = Appointment.objects.all()



    return render(request, 'appointment.html', {'appintment': appintments})