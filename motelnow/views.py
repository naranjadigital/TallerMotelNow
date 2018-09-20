from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from motelnow.forms import HostalForm
from motelnow.models import Hostal


def index(request):
    context = {'hostales': Hostal.objects.all()}
    return render(request, 'frontend/index.html', context)

def detail(request, pk):
    hostal = get_object_or_404(Hostal, pk=pk)
    return render(request, 'frontend/detail.html', {'hostal':hostal})


def backoffice(request):
    return render(request, 'base_backoffice.html')


class HostalCreate(CreateView):
    model = Hostal
    form_class = HostalForm
    success_url = reverse_lazy('hostal-list')
    template_name = 'hostal/hostal_create.html'


class HostalList(ListView):
    model = Hostal
    template_name = 'hostal/hostal_list.html'


class HostalUpdate(UpdateView):
    model = Hostal
    form_class = HostalForm
    success_url = reverse_lazy('hostal-list')
    template_name = 'hostal/hostal_update.html'


class HostalDelete(DeleteView):
    model = Hostal
    template_name = 'hostal/hostal_delete.html'
    success_url = reverse_lazy('hostal-list')