from positions.models import Metall
from rest_framework import serializers

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metall
        fields = ('title', 'price','description_amp','description_clear', 'group','photo_amp_1','photo_amp_2','photo_amp_3','slug')

