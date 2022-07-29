from django.urls import path

from .views import *

urlpatterns = [
    path('blog/', BlogHome.as_view(), name="blog"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    # path('register/', RegisterUser.as_view(), name='register'),

]
