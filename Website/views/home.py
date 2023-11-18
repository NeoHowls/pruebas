from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import *

@login_required()
def home(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'Website/home.html', {'categories':categories})