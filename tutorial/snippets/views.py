from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

# Create your views here

# The REST framework provides us a set of already mixed-in generic views that we can use to trim down
# our views code even more

# basically we don't even need to define methods for HTTP actions anymore, just pass the generic view into the class

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automagically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automagically provides `list`, `create`, `retrieve`, 
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request_user)
