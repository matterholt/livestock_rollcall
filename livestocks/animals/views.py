from django.shortcuts import render
from .models import Specific, History, Specie, Genealogy, Record


# Create your views here.
def index(request):
    """Vie function for hom page of site."""
    amount_animals = Specific.objects.all().count()
    amount_histories = History.objects.all().count()

    context = {"num_animals": amount_animals, "num_history": amount_histories}

    return render(request, "index.html", context=context)
