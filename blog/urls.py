from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    # Documentation: Maybe I need to change it with slug somehow https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/ 
    path(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail') #documentaion
]