# !/usr/bin/env python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import Goods, GoodsCategory

# 1) 使用笨办法序列化数据
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=108)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         接收前端数据生成数据库数据
#         """
#         return Goods.objects.create(**validated_data)


# 2）使用serializers序列化简化
# 循环嵌套三级商品菜单
class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # 在一级商品里面嵌套二级商品 many=True表示会有多个
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'code', 'linenos', 'language', 'style')
        fields = "__all__"




