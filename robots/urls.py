from django.urls import path
from .views import validate_request, download_excel

urlpatterns = [
    path('post_data/', validate_request, name='post_data'),
    path('download_excel/', download_excel, name='download_excel'),
]
