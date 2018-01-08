from rest_framework import serializers
from .models import Procesados, Tendencias

# Serializers define the API representation.
class ProcesadosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procesados
        fields = '__all__'

class TendenciasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tendencias
        fields = '__all__'