from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('post_food/', views.post_food_page, name='post_food_page'),
    path('', views.home, name='home'),
    path('request_food/<int:post_id>/', views.request_food, name='request_food_page'),
    path('food_feed/', views.food_feed, name='food_feed'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


