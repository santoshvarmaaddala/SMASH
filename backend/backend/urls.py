from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import MyModelViewSet, index

router = routers.DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # This routes API requests to your viewsets
    path('', index),  # This handles the root URL
]
