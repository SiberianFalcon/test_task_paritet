from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import TestTaskViewSet

router = routers.DefaultRouter()
router.register(r'test-task', TestTaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
