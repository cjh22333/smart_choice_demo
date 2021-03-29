from rest_framework import serializers
from stock_be.models import *
from django.contrib.auth.models import User



class user_serializer(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        model = User  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        depth = 1  # 深度为1

class cash_serializer(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        model = cash_account  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # fields = ['id', 'image',"new_price"]  # 这里选择只显示这3个
        # depth = 1  # 深度为1

class watch_list_serrializer(serializers.ModelSerializer):
    class Meta:
        model = watch_list  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # depth = 1  # 深度为1
class position_serrializer(serializers.ModelSerializer):
    class Meta:
        model = user_stock_pofolio  # #可以更换数据库,这是个接口
        fields = "__all__"  # 是否显示所有数据,也是个接口
        # depth = 1  # 深度为1
