from django.urls import include, path
from .views import ProjectViewSet
from rest_framework_nested import routers
from .views import ProjectViewSet, ContributorsViewSet, IssueViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'issues', IssueViewSet, basename='issues')
project_router.register(r'users', ContributorsViewSet, basename='users')

issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(project_router.urls)),
    path('', include(issue_router.urls))
]
