
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet
from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)


app_name = "polls"
urlpatterns = [
    path('api/', include(router.urls)),
    # ('api-auth/', include('rest_framework.urls')),
    path('api/users/', views.register_user, name='register_user'),
    path('api/userslogin/', views.login_user, name='login_user'),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:pk>/vote/", views.vote, name="vote"),

]
