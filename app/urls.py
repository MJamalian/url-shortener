from django.urls import path
from app import views

urlpatterns = [
    path("", views.GetShortUrlView.as_view()),
    path("<str:short_url>/", views.GetLongUrlView.as_view())
]
