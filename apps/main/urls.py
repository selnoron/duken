from django.urls import path

# Local
from .views import MainView, CreateView


urlpatterns = [
    path('', MainView.as_view()),
    path('create/', CreateView.as_view())
]