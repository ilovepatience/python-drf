from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.book.models import BookModel
from apps.book.serializer import BookSerializer
from apps.book.filter import filter_book



class BookListCreateView(ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        request = self.request
        return filter_book(request.query_params)



class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer





