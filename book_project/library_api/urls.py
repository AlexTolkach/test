from .views import BooksList, BookDetail, UserLibraryList
from django.urls import path

urlpatterns = [
    path('books/', BooksList.as_view()),
    path('books/<int:pk>', BookDetail.as_view()),
    path('user', UserLibraryList.as_view())
]
