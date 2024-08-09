from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),


    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile, name='profile'),

    path('add/', views.add_view, name='add'),
    path('my/articles/', views.my_articles, name='my_articles'),
    path('article/<int:id>/like', views.inc_like, name='inc_like'),
    path('article/<int:id>/edit', views.edit_view, name='edit'),
    path('article/<int:id>/delete', views.delete_view, name='delete'),
    path('article/<int:id>/detail', views.detail_view, name='detail'),
]





