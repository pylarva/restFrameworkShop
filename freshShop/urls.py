"""freshShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.conf.urls import url, include
import xadmin

from freshShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
# token authentication 认证
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

# from goods.views import GoodsListView
from goods.views import GoodsListViewSet, CatagoryViewset
from apps.users.views import SmsCodeViewset

# 使用Routers功能能够自动将路由转换成下面类似的goods_list
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置category的url
router.register(r'categorys', CatagoryViewset, base_name='categorys')

# 短信注册
router.register(r'codes', SmsCodeViewset, base_name="codes")


# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 商品列表页
    # url(r'^goods/$', GoodsListView.as_view(), name="good-list"),
    # ViewSets & Routers 实现路由商品列表
    # url(r'^goods/$', goods_list, name="good-list"),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='freshShop')),

    # drf自带的认证
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt认证
    url(r'^login/', obtain_jwt_token),
]
