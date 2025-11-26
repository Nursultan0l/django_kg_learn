from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from .views import *

urlpatterns = [
    path('v1/auth/login/', include('rest_framework.urls')),
    path('v1/auth/register/', RegisterView.as_view(), name='register'),

    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # jwt
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # jwt
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # jwt

    # Letters
    path('v1/letters/', LettersAPIList.as_view(), name='letters_api_list'),
    path('v1/letters-update/<int:pk>/', LettersAPIUpdate.as_view(), name='letters_api_update'),
    path('v1/letters-delete/<int:pk>/', LettersAPIDelete.as_view(), name='letters_api_delete'),

    # lessons
    path('v1/lessons/', LessonsAPIList.as_view(), name='lessons_api_list'),
    path('v1/lessons-update/<int:pk>/', LessonsAPIUpdate.as_view(), name='lessons_api_update'),
    path('v1/lessons-delete/<int:pk>/', LessonsAPIDestroy.as_view(), name='lessons_api_delete'),

    # Documents
    path('v1/documents/', DocumentsAPIList.as_view(), name='documents_api_list'),
    path('v1/documents-update/<int:pk>/', DocumentsAPIUpdate.as_view(), name='documents_api_update'),
    path('v1/documents-delete/<int:pk>/', DocumentsAPIDestroy.as_view(), name='documents_api_delete'),

    # Numbers
    path('v1/numbers/', NumbersAPIList.as_view(), name='numbers_api_list'),
    path('v1/numbers-update/<int:pk>/', NumbersAPIUpdate.as_view(), name='numbers_api_update'),
    path('v1/numbers-delete/<int:pk>/', NumbersAPIDestroy.as_view(), name='numbers_api_delete'),
]