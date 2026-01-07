from django.urls import path
from . import views

urlpatterns = [
    path('sample-recommendations/', views.sample_ai_view, name='sample_recommendations'),
]
