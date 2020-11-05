from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('new/', views.new, name="new"),
]

