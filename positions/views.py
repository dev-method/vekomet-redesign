from django.shortcuts import render
from positions.models import Metall

# Create your views here.
def position_detail(request,slug):
    position = Metall.objects.get(slug=slug)
    fotos = position.positionfoto_set.all()
    positions = Metall.objects.all()
    return render(request, 'positions/dev/position-detail.html', {'fotos':fotos, 'position': position, 'positions': positions})
