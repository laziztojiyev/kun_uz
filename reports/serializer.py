from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from reports.models import Category, Region, Report, Tag


class CategoryModelSerializer(ModelSerializer):
    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError('this category is already token')
        return data

    class Meta:
        model = Category
        fields = ('name', 'id')


class RegionModelSerializer(ModelSerializer):
    def validate(self, data):
        if Region.objects.filter(name=data['name']).exists():
            raise ValidationError('this category is already token')
        return data

    class Meta:
        model = Region
        fields = ('name', 'id')


class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReportModelSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
