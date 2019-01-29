# -*- coding: utf-8 -*-
# Create your views here.
from rest_framework import viewsets
from custom.permission import CustomPermission
from scrapyd_manage.models import ScrapydHostModel
from scrapyd_manage.serializers import ScrapydHostSerializer

"""
这个模块是用来操作 scrapyd 的，一些东西
"""


class ScrapydHostViewSet(viewsets.ModelViewSet):
    """ 处理用户
    """
    permission_classes = (CustomPermission,)  # 设置权限

    queryset = ScrapydHostModel.objects.all()
    serializer_class = ScrapydHostSerializer
