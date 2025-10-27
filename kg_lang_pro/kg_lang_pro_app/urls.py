from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('lessons/',lessons, name='lessons'),
    path('lessons/alphabet/',letters_list, name='alphabet'),
    path('lessons/numbers/',numbers_list, name='numbers'),
    path('grammar/', lessons_list, name='grammar'),
    path('materials/', materials_list, name='materials'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)