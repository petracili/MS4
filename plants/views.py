from django.shortcuts import render
from .models import Plants
# Create your views here.


def all_plants(request):
    """ A view to show all books, including sorting and searches """

    plants = Plants.objects.all()
    
    context = {
        'plants': plants,
    }

    return render(request, 'plants/index.html', context)