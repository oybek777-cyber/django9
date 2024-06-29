from .views import homeindex,contact,page_404
from django.urls import path


urlpatterns=[
    path('page_404/',page_404,name='page_404'),
    path('contact/',contact,name='contact'),
    path('',homeindex,name='homeindex'),
   
]