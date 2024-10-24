from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cities', CityViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'neighborhoods', NeighborhoodViewSet)  # Mahalle için
router.register(r'streets', StreetViewSet)
router.register(r'farmers', FarmerViewSet)
router.register(r'parners', PartnerViewSet)
router.register(r'lands', LandViewSet)
router.register(r'land-details', LandDetailViewSet)
router.register(r'todo-lists', TodoListViewSet)
router.register(r'weather-alerts', WeatherAlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lands/todo/<int:land_id>/', TodoListByLandView.as_view(), name='todo-list-by-land'),
    path('lands/todo/<int:land_id>/<int:todo_id>/', TodoDetailView.as_view(), name='todo-detail'),
]
