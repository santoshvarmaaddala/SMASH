from django.contrib import admin
from django.urls import path
from rest_framework import routers
from myapp.views import MyModelViewSet

router = routers.DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
