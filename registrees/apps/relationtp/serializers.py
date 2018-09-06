from rest_framework import serializers
from registrees.apps.relationtp.models import Tree, Park



# serializer parques
class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ('id', 'nombre', 'direccion', )


# serializer arboles
class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ('id', 'nombre', 'altura', 'edad_aproximada', 'parque')