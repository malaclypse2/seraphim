from django.shortcuts import render
from django.template import loader

from .models import Combat


# Create your views here.
def index(request):
    combat_list_in_progress = Combat.objects.filter(in_progress=True)
    combat_list_complete = Combat.objects.filter(in_progress=False)
    context = {
        'combat_list_in_progress': combat_list_in_progress, 
        'combat_list_complete': combat_list_complete,
    }
    return render(request, 'tracker/index.html', context)
