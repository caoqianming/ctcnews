"""ctcnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from news import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.newslist),
    url(r'^index/',views.index, name = 'index'),
    url(r'^newslist/',views.newslist, name = 'newslist'),
    url(r'^mp4list/',views.mp4list, name = 'mp4list'),
    url(r'^calzan/', views.calzan),
    url(r'^mp4play/(?P<pk>[0-9]+)/$', views.mp4play,name='mp4play'),    
    url(r'^main/',views.main, name = 'main'),  
    url(r'^wechat/',views.wechat, name = 'wechat'),
    url(r'^videos/',views.videos, name = 'videos'),
    url(r'^appdown/',views.appdown),
    url(r'^aqyjfull/',views.apk_down_full),
    url(r'^aqyjsimple/',views.apk_down_simple),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
