from armstrong.core.arm_sections.models import Section
from django.db import models
from model_utils.managers import InheritanceManager


class Common(models.Model):
    title = models.CharField(max_length=20)
    section = models.ForeignKey(Section)

    objects = InheritanceManager()


class Article(Common):
    summary = models.TextField(default="Default", blank=True)


class Photo(Common):
    url = models.URLField(default="http://localhost/", blank=True)


class SimpleCommon(models.Model):
    title = models.CharField(max_length=20)
    section = models.ForeignKey(Section)


class SimpleArticle(SimpleCommon):
    summary = models.TextField(default="Default", blank=True)


class SimplePhoto(SimpleCommon):
    url = models.URLField(default="http://localhost/", blank=True)


class NonStandardField(models.Model):
    title = models.CharField(max_length=20)
    sections_by_another_name = models.ForeignKey(Section)