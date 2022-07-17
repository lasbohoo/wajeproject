from django.conf.urls import url
from . import views


urlpatterns = [
   
   url(r'^book$',views.bookApi),
   # url(r'book/<int:pk>/',views.book_detail),
   url(r'^book/([0-9]+)$',views.book_detail),
   
   url(r'^author$',views.authorApi),
   # url(r'^author/<int:pk>/',views.author_detail),
   url(r'^author/([0-9]+)$',views.author_detail),
  
]