from django.urls import include, path
from .views import ProjectViewSet
from rest_framework_nested import routers
from .views import ProjectViewSet

router = routers.SimpleRouter()

router.register(r"projects", ProjectViewSet, basename="projects")

"""router.register(
    r"projects/<pk>", RetrieveProjectDetails, basename="projects_pk"
)"""


urlpatterns = [
    path(r"", include(router.urls)),
]
