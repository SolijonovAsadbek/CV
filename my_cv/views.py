from django.shortcuts import render

# Create your views here.
from django.views import generic

from my_cv.models import Head


class HeadClass(generic.ListView):
    model = Head
    template_name = 'my_cv/index.html'
    context_object_name = 'heads'

    def get_queryset(self):
        return Head.objects.first()
