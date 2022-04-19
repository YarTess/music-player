from django.urls import path
from django.views.generic import TemplateView
from . import views

# Add URLConf
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('', views.IndexView.as_view(), name='index')
]