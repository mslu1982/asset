"""asset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from hnf import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^search', views.search, name='search'),

    url(r'^admin/', admin.site.urls),
    # url(r'^user/list/$', views.user_list),
    # url(r'^user/add/$', views.user_add),
    # url(r'^user/edit/(?P<cid>\d+)/$', views.user_edit),
    # url(r'^user/del/(?P<cid>\d+)/$', views.user_del),
    # url(r'^user/import/$', views.user_import),
    # url(r'^user/tpl/$', views.user_tpl),

    url(r'^asset/list/$', views.asset_list, name='asset_list'),
    url(r'^asset/add/$', views.asset_add),
    url(r'^asset/edit/(?P<cid>\d+)/$', views.asset_edit),
    url(r'^asset/del/(?P<cid>\d+)/$', views.asset_del),
    url(r'^asset/import/$', views.asset_import),
    url(r'^asset/tpl/$', views.asset_tpl),
    # url(r'^',include('hnf.urls')),
]
