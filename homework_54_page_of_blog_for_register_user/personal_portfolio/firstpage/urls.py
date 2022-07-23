from django.urls import path

from .views import *

urlpatterns = [
    path('blog/', BlogHome.as_view(), name="blog"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
]
