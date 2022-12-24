import uuid

from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import DateTimeField, CharField, SlugField, TextField, ImageField, ForeignKey, CASCADE, SET_NULL, \
    UUIDField, Model, ManyToManyField, PROTECT
from django.utils.text import slugify


# Create your models here.
class BaseModel(models.Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regionlar'


class Tag(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'


class Category(BaseModel):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, null=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Report(BaseModel):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=255)
    text = RichTextField()
    image = ImageField(upload_to='media')
    category = ForeignKey('reports.Category', CASCADE, 'category')
    tags = ForeignKey('reports.Tag', PROTECT)
    region = ForeignKey('reports.Region', CASCADE, null=True, blank=True)
    author = ForeignKey('auth.User', CASCADE)
    slug = SlugField(max_length=255, unique=True, null=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug
        if force_update is True:
            self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'reports'
        ordering = ('-created_at', )


