from django.shortcuts import render
from positions.models import Metall
from vekomet_redesign import settings

# Create your views here.
def position_detail(request,slug):
    position = Metall.objects.get(slug=slug)
    first_foto = position.positionfoto_set.all()[0]
    second_foto = position.positionfoto_set.all()[1]
    third_foto = position.positionfoto_set.all()[2]
    try:
        fotos = position.positionfoto_set.all()[3:]
    except:
        fotos=[]
    positions = Metall.objects.all()
    return render(request, 'positions/{}/position-detail.html'.format(settings.TEMP_PREFIX), {'first_foto': first_foto, 'second_foto': second_foto, 'third_foto': third_foto, 'fotos':fotos, 'position': position, 'positions': positions})
