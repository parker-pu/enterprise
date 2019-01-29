# Create your views here.
from rest_framework import serializers

from scrapyd_manage.models import ScrapydHostModel


class ScrapydHostSerializer(serializers.HyperlinkedModelSerializer):
    """用户的配置信息
    """

    class Meta:
        model = ScrapydHostModel
        fields = "__all__"
