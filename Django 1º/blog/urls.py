from blog import views
from django.urls import path

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]