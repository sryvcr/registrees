"""registrees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from registrees.apps.relationtp.views import TreeViewSet, ParkViewSet, AuthLoginView



# Declara primer enrutador
router = routers.DefaultRouter()
# Registra URLs de los modelos
router.register(r'trees', TreeViewSet)
router.register(r'parks', ParkViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # inicializa todas las URLs en un solo punto
    url(r'^', include(router.urls)),
    #agrega url para poder logear
    url(r'^devices/login', AuthLoginView.as_view(), name='devices_login'),
]
