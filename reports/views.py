import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from reports.models import Category, Report, Region, Tag
from reports.serializer import CategoryModelSerializer, ReportModelSerializer, RegionModelSerializer, TagModelSerializer


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


class ReportModelViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportModelSerializer
    parser_classes = (MultiPartParser, )
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'region']


class RegionAPIView(GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', )

    def get(self, request):
        region = Region.objects.all()
        serializer = self.serializer_class(region, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class TagAPIVTag(GenericAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    Tagilter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', )

    def get(self, request):
        region = Tag.objects.all()
        serializer = self.serializer_class(region, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

