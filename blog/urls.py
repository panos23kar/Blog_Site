from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    path(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail') #documentaion
]