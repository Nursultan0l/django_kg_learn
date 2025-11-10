from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, DocumentsViewSet, LetterViewSet, NumbersViewSet
router = DefaultRouter()
router.register('lessons', LessonViewSet)
router.register('documents', DocumentsViewSet)
router.register('letters', LetterViewSet)
router.register('numbers', NumbersViewSet)
urlpatterns = router.urls