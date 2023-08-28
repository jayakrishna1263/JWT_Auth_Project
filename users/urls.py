from django.urls import path,include

from .views import ClientListViewSet, AdminListViewSet,MyObtainTokenView

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register(r'clients', ClientListViewSet)
router.register(r'admins', AdminListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-token/', MyObtainTokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]