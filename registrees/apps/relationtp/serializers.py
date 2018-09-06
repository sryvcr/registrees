from django.contrib.auth.models import User
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


# serializer usuario
class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email', 'is_staff', 
                  'is_active', 'date_joined', 'last_login') 