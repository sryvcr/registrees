from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from registrees.apps.relationtp.mixins import DefaultViewSetMixin, ModelViewSetMixin
from registrees.apps.relationtp.models import Tree, Park
from registrees.apps.relationtp.serializers import TreeSerializer, ParkSerializer, CurrentUserSerializer



# ViewSet de arboles
class TreeViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    filter_fields = ('nombre', 'altura', )
    ordering_fields = ('nombre', 'altura', )


# ViewSet de parques
class ParkViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    filter_fields = ('nombre', )
    ordering_fields = ('nombre', )


# ViewSet del login
class AuthLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        if username is not None and password is not None:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    serializer = CurrentUserSerializer(user)
                    response = {
                        'status': 'Ok',
                        'user': serializer.data,
                    }
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid username/password'}, 
                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)