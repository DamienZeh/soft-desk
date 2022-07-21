from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers


router = routers.SimpleRouter()
# router.register('category', CategoryViewset, basename='category')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("API_soft_desk.urls")),
    # path("api/", include(router.urls)),
]
