
from django.shortcuts import render
# Create your views here.

def front(request):
   return render(request, 'xj_front.html')

def test(request):
   return render(request, 'test.html')

def index(request):
   return render(request, 'index.html')

def paiban(request):
   return render(request, 'paiban.html')

def xunjian(request):
   return render(request, 'xunjian.html')

def shenji(request):
   return render(request, 'shenji.html')


