from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url('r^$',"blog_pages.views.post_list"),
    url('r^create/$',"blog_pages.views.post_create"),
    url('r^detail/$',"blog_pages.views.post_detail"),
    url('r^update/$',"blog_pages.views.post_update"),
    url('r^delete/$',"blog_pages.views.post_delete"),
]