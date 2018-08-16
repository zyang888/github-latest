from django.urls import path
from .views import stub_view, list_view

urlpatterns = [
    path(r'^posts/<int:post_id>/',
    	stub_view,
    	name="blog_detail"),
    path('',
        list_view,
        name="blog_index"),
]