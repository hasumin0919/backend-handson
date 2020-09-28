from django.shortcuts import render
# from rest_framework import generics

# from .models import Handson
# from .serializers import HandsonSerializer

# Create your views here.
# APIのエンドポイントを生成する。APIサーバ的にはAPIエンドポイントこそがViewなのだ。
# モデルの整形などもここで行う
# class HandsonList(generics.ListCreateAPIView):
#     queryset = Handson.objects.all()
#     serializer_class = HandsonSerializer

# class HandsonDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Handson.objects.all()
#     serializer_class = HandsonSerializer

# viewsetsは複数に分けていたViewの機能を統合させる効能を持つ
# 下のclassは上二つのclassで行ってくれてたことを全部やってくれる
# class HandsonViewSet(viewsets.ModelViewSet):

#     queryset = Handson.objects.all()
#     serializer_class = HandsonSerializer