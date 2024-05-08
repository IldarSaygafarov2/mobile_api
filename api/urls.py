from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.PDFFileAPIView.as_view()),
    path('photos/', views.PhotoAPIView.as_view())
]