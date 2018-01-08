from django.urls import path
from .views import IndexView, PrivateView, LoginView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('private/', PrivateView.as_view(), name='private'),
    path('login/', LoginView.as_view(), name='login'),
]

