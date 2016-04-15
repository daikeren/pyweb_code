from django.shortcuts import render
import random
from excuse.models import Excuse

def home(request):
    excuse = random.choice(Excuse.objects.all())
    return render(request, "index.html", {'excuse': excuse})
