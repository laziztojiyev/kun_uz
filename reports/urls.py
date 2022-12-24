from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reports.views import CategoryModelViewSet, ReportModelViewSet, RegionAPIView, TagAPIVTag

router = DefaultRouter()
router.register('category', CategoryModelViewSet, basename='category')
router.register('report', ReportModelViewSet, basename='report')
urlpatterns = [
    path('', include(router.urls)),
    path('regions/', RegionAPIView.as_view(), name='regions_list'),
    path('tag/', TagAPIVTag.as_view(), name='tag_list'),
    path('api-auth/', include('rest_framework.urls'), name='api'),
]