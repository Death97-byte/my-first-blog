from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Homepage(View):
    def get(self, request):
      context = {}
      return render(request,'homepage.html',context)
    
