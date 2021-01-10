from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    # Documentation: Maybe I need to change it with slug somehow https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/ 
    path(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
    path('post/new', views.CreatePostView.as_view(),name='post_new'),
    path(r'post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(),name='post_edit'),
    path(r'post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(),name='post_remove'),
    url('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
]