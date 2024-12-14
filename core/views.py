from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from core.models import tablename, info, alenereproduct
from django.urls import reverse_lazy
# Create your views here.

class indexview(ListView):
    model = tablename
    context_object_name = "models"
    template_name = 'core/index.html'

class createview(CreateView):
    model = tablename
    fields = ['name', 'job', 'fav_color']
    template_name = 'core/create.html'

class deleteview(DeleteView):
    model = tablename
    success_url = reverse_lazy('core_index')


# Practice     

class newcreate(CreateView):
    model = info
    fields = ['firstname','lastname', 'phone', 'company']
    template_name = 'personal_project/create.html'

class newindex(ListView):
    model = info
    context_object_name = "info"
    template_name = 'personal_project/index.html'

class newdelete(DeleteView):
    model = info
    template_name = 'personal_project/ConfirmDelete.html'  # This is the template where you can display confirmation or list
    success_url = reverse_lazy('newindex')  # Redirect to 'newindex' after successful deletion
 
class newupdate(UpdateView):
    model = info
    fields = ['firstname','lastname', 'phone', 'company']
    template_name = 'personal_project/update.html'

# Alenere

class alenereindex(ListView):
    model = alenereproduct
    context_object_name = 'alenere'
    template_name = 'alenere/index.html'

class alenerecreate(CreateView):
    model = alenereproduct
    fields = ['product','color','category','price']
    template_name = 'alenere/create.html'

class aleneredelete(DeleteView):
    model = alenereproduct
    success_url = reverse_lazy('alenereindex')

class alenereupdate(UpdateView):
    model = alenereproduct
    fields = ['product','color','category','price']
    template_name = 'alenere/update.html'

class aleneredetail(DetailView):
    model = alenereproduct
    context_object_name = 'alenere'
    template_name = 'alenere/detail.html'