from django.urls import path
from .views import login, signup, logout_view, edit_profile

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', edit_profile, name='edit_profile'),

]