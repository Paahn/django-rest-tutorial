from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# Create your views here

# The REST framework provides us a set of already mixed-in generic views that we can use to trim down
# our views code even more

# basically we don't even need to define methods for HTTP actions anymore, just pass the generic view into the class

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer