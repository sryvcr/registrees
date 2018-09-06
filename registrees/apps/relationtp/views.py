from registrees.apps.relationtp.mixins import DefaultViewSetMixin, ModelViewSetMixin
from registrees.apps.relationtp.models import Tree, Park
from registrees.apps.relationtp.serializers import TreeSerializer, ParkSerializer



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

