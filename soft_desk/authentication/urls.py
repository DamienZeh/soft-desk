from django.urls import include, path
from .views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("signup/", RegisterView.as_view(), name="auth_register"),
]
