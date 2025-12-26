from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfilesView.as_view())
] 
