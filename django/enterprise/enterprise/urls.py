"""enterprise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from scrapyd_manage.views import ScrapydHostViewSet
from user_token.views import AuthTokenView

# 自定义路由
router_v1 = routers.DefaultRouter()
router_v1.register(r'scrapyd-host', ScrapydHostViewSet)

# 规则匹配的路由
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', AuthTokenView.as_view()),  # token 认证
    path('api/v1/', include(router_v1.urls)),  # 相应的接口
]
