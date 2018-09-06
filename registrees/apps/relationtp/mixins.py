from datetime import datetime
from django.db import models
from rest_framework import filters, viewsets, status
from rest_framework.response import Response

class ManagerMain(models.Manager):
    def get_queryset(self):
        return super(ManagerMain, self).get_queryset().filter(deleted_at__isnull=True)


class ManagerAllMain(models.Manager):
    def get_queryset(self):
        return super(ManagerAllMain, self).get_queryset()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = ManagerMain()
    objects_all = ManagerAllMain()

    class Meta:
        abstract = True


# Mixins para agrupar todos los filters en todos los ViewSet
class DefaultViewSetMixin(object):
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )
    paginate_by = 10 # por cuanto vamos a paginar
    paginate_by_param = 'page_size'
    max_paginate_by = 100 # maximo de paginacion


# Mixins para borrar lógicamente un registro en todos los ViewSet
# sobreescribe el método destroy permitiendo actualizar el campo deleted_at y no borrando registro
class ModelViewSetMixin(viewsets.ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object() # recuperamos la instancia
        instance.deleted_at = datetime.now() # guarda la fecha
        instance.save() # actualiza
        response = {
            "result": "Ok"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)