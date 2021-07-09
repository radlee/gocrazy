from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about"),
    path('services/', views.services, name="blog-services"),
    path('recruitment/', views.recruitment, name="blog-recruitment"),
    path('exclusivehub/', views.exclusivehub, name="blog-exclusivehub"),
    path('contact/', views.contact, name="blog-contact"),
    path('brandpromo/', views.brandpromo, name="blog-brandpromo"),
    path('showcase/', views.showcase, name="blog-showcase"),
    path('tickets/', views.tickets, name="blog-tickets"),
    path('events/', views.events, name="blog-events"),
    path('rentals/', views.rentals, name="blog-rentals"),
    path('bookings/', views.bookings, name="blog-bookings"),
    path('team/', views.team, name="blog-team"),
]
