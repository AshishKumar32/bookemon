from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('book/',views.book,name="book"),
    path('bookticket/',views.bookticket,name="bookticket"),
    path('test/',views.test,name="test"),
    path('search/',views.search,name="search"),
    path('userdash/',views.userdash,name="userdash"),    
]
