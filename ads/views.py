from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ads.models import Category, Ad, Location, Selection
from ads.serializers import (
    AdSerializer,
    CategorySerializer,
    LocationSerializer,
    SelectionCreateSerializer,
    SelectionSerializer,
    SelectionDetailsSerializer,
)
from ads.permissions import AdUpdateDeletePermission, SelectionPermission


def index(request):
    return JsonResponse({'status': 'ok'}, status=200)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer


class AdViewSet(viewsets.ModelViewSet):
    permission_classes = [AdUpdateDeletePermission]
    serializer_class = AdSerializer

    def get_queryset(self):
        queryset = Ad.objects.all()
        if self.action == 'list':
            category_id = self.request.GET.get('cat', None)
            text = self.request.GET.get('text', None)
            location = self.request.GET.get('location', None)
            price_from = self.request.GET.get('price_from', None)
            price_to = self.request.GET.get('price_to', None)
            if category_id:
                queryset = queryset.filter(
                    category_id__exact=category_id
                )
            if text:
                queryset = queryset.filter(
                    name__icontains=text
                )
            if location:
                queryset = queryset.filter(
                    author__locations__name__icontains=location
                )
            if price_from and price_to:
                queryset = queryset.filter(
                    Q(price__gte=price_from) & Q(price__lte=price_to)
                )
        return queryset


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['image']
    object = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.FILES.get('image'):
            self.object.image = request.FILES['image']
            self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author.id,
            'price': self.object.price,
            'description': self.object.description,
            'category_id': self.object.category.id,
            'is_published': self.object.is_published,
            'image': self.object.image.url if self.object.image else None
        }, status=202)

    def patch(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()


class SelectionViewSet(viewsets.ModelViewSet):
    permission_classes = [SelectionPermission]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SelectionCreateSerializer
        if self.action == 'retrieve':
            return SelectionDetailsSerializer
        return SelectionSerializer

    def get_queryset(self):
        return Selection.objects.all()
