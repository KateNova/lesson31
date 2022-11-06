from django.urls import path
from rest_framework import routers

from ads.views import (
    AdViewSet,
    AdUploadImageView,
    LocationViewSet,
    SelectionViewSet,
    CategoryViewSet,
)


router = routers.SimpleRouter()
router.register('location', LocationViewSet, basename='location')
router.register('selection', SelectionViewSet, basename='selection')
router.register('cat', CategoryViewSet, basename='category')
router.register('ad', AdViewSet, basename='ad')


urlpatterns = [
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view()),
]

urlpatterns += router.urls
