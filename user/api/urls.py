from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('profile/<int:pk>/', views.ProfileDetailList.as_view()),
    # path('profile/', views.UserProfileList.as_view()),
    # path('profile/<int:pk>', views.UserProfileList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
