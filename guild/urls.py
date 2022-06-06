from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Edit Your Profile
    path('profile', views.profile, name='profile'),
    path('save_profile', views.save_profile, name='save_profile'),
    # Apply to the Guild
    path('apply', views.apply, name='apply'),
    path('submit_apply', views.submit_apply, name='submit_apply'),
    # Graphs are neat
    path('charts', views.charts, name='charts'),
]