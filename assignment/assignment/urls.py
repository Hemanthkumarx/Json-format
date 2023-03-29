from django.urls import path
from .views import UploadAPIView, Top60Rows

urlpatterns = [
    path('upload/', UploadAPIView.as_view(), name='upload'),
    path('top60/', Top60Rows.as_view(), name='top60'),
]
