from rest_framework import status, permissions
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import  login as auth_login
from api.serializers import RegisterSerializer

from .forms import LoginForm


class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self,request):
#         try:
#             refresh_token = request.data['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import LoginForm, RegistrationForm, ProfileUpdateForm
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = getattr(form, 'user_cache', None)
            if user:
                auth_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Исправлено!

            # JWT токены (если нужно)
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            response = redirect('home')  # Исправлено!
            response.set_cookie('access', str(access), httponly=True)
            response.set_cookie('refresh', str(refresh), httponly=True)
            return response
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    return redirect('home')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

