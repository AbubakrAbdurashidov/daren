from django.urls import path
from . views import  (
    contact
)

app_name = 'main'

urlpatterns = [
    path('contact/', contact, name='contact')
]