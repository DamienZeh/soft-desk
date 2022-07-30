from django.urls import include, path
from .views import ProjectViewSet
from rest_framework_nested import routers
from .views import ProjectViewSet, ContributorsViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'users', ContributorsViewSet, basename='user')


urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls)),
]
