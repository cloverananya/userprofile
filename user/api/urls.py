from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
]






#
# urlpatterns = [
#     path('register/', views.UserRegistrationView.as_view()),
#     path('users/<int:pk>/', views.UserDetailView.as_view()),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
