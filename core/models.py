from django.db import models


class Service(models.Model):
    name = models.CharField("Service Name",max_length=90)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    name = models.CharField("Name", max_length=90)
    description = models.TextField(blank=True, max_length=255)
    slug = models.SlugField(max_length=255)
    meta_title = models.CharField(max_length=90,blank=True)
    meta_description = models.TextField(max_length=255,blank=True)
    # image = models.ImageField()

    def __str__(self):
        return self.name
