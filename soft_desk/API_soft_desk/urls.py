from django.urls import include, path
from .views import ProjectViewSet
from rest_framework_nested import routers
from .views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r"projects", ProjectViewSet, basename="projects")


project_router = routers.NestedSimpleRouter(
    router, r"projects", lookup="project"
)

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(project_router.urls)),
]
