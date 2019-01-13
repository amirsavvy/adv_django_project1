from django.shortcuts import render
from django.views.generic import (View, ListView,
                                DetailView,TemplateView,
                                CreateView, UpdateView,
                                DeleteView)
from django.http import HttpResponse
from . import models
from website import views
from django.urls import reverse_lazy

# Class base views
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Mian Amir Savvy'
        return context


class SchoolListView(ListView):
    # context_object_name = 'schools'
    model = models.School
    # template_name = 'website/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'website/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("website:list")



# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Amir Savvy in CBV")



# Create your views here.
# def index(request):
#     return render(request, 'index.html')
