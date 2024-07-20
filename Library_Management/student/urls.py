from django.urls import path
from student import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('author_create/',views.Author_Creation.as_view(),name='author_create'),
    path('book_create/',views.Book_Creation.as_view(),name='book_create'),
    path('book_update/<int:pk>/',views.Book_Update.as_view(),name='book_update'),
    path('book_detail/<int:pk>/',views.Book_Details.as_view(),name='book_detail'),
    path('book_list/',views.Book_List.as_view(),name='books'),
    path('book_delete/<int:pk>/',views.Book_Delete.as_view(),name='book_delete'),
]