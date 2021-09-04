from django.shortcuts import redirect, render
from .forms import UpdateDoctor
from .models import *

# Create your views here.


def home(request):
    return render(request, 'doct-home.html')


def createDoctor(request):
    form = UpdateDoctor()
    if request.method == 'POST':
        form = UpdateDoctor(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)

            instance.user = request.user
            instance.save()
            return redirect('doct_home')

    context = {'form': form}
    return render(request, 'doct-update.html', context)


def updateDoctor(request, id):

    doct = Doctor.objects.get(id=id)
    form = UpdateDoctor(instance=doct)
    if request.method == 'POST':
        form = UpdateDoctor(request.POST, request.FILES, instance=doct)
        if form.is_valid():
            form.save()
            return redirect('doct_home')

    context = {
        'form': form,
    }
    return render(request, 'doct-update.html', context)
