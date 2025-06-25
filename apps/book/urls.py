from django.urls import path
from apps.book.views import BookRetrieveUpdateDestroyView, BookListCreateView


urlpatterns = [
    path('', BookListCreateView.as_view()),
    path('<int:pk>', BookRetrieveUpdateDestroyView.as_view()),
]