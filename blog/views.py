from django.shortcuts import render
from django.views.generic import (TemplateView)#parenthesis to extend to multiple lines
# Create your views here.

class AboutView(TemplateView):
    #TODO na brw ti einai kai apo pou erxetai to template_name
    template_name = 'about.html'