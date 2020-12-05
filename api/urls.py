"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from api.views import ClassAPIView, ClassAPIViewDetail, article_list, article_detail, \
    getPostArticles, ViewSet, GenericViewSet, ModelViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ViewSet, basename='my-viewset')

#alternative to above
viewset_alternative_list = ViewSet.as_view({
        'get': 'list',
        'post': 'create',
})

viewset_alternative_detail = ViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
})

##############
routerGeneric = DefaultRouter()
routerGeneric.register('', GenericViewSet, basename='generic-viewset')

##############
routerModel = DefaultRouter()
routerModel.register('', GenericViewSet, basename='model-viewset')

app_name = 'api'
urlpatterns = [
    # path('articles/', article_list, name='articles'),
    path('articles', article_list),
    path('articles/<int:id>/', article_detail, name='article-detail'),
    path('articles/<int:id>', article_detail),

    path('articles/', getPostArticles, name='articles'),
    path('articles', getPostArticles),

    path('class/', ClassAPIView.as_view(), name='class-articles'),
    path('class', ClassAPIView.as_view()),

    path('class/<int:id>/', ClassAPIViewDetail.as_view(), name='class-detail'),
    path('class/<int:id>', ClassAPIViewDetail.as_view()),

    path('generic/', ClassAPIView.as_view(), name='class-generic'),
    path('generic', ClassAPIView.as_view()),

    path('generic/<int:id>/', ClassAPIViewDetail.as_view(), name='class-generic-detail'),
    path('generic/<int:id>', ClassAPIViewDetail.as_view()),

    path('genericshort/', ClassAPIView.as_view(), name='class-generic-short'),
    path('genericshort', ClassAPIView.as_view()),

    path('genericshort/<int:id>/', ClassAPIViewDetail.as_view(), name='class-generic-detail-short'),
    path('genericshort/<int:id>', ClassAPIViewDetail.as_view()),

    path('viewset/', include(router.urls)),
    # path('viewset', include(router.urls)), # because of this -> nameclash with viewset-alt

    # path('viewset/<int:pk>/', include(router.urls)),
    # path('viewset/<int:pk>', include(router.urls)),  # cn redirect if only prefix is empty

    path('viewset-alt/', viewset_alternative_list),
    path('viewset-alt', viewset_alternative_list),

    path('viewset-alt/<int:pk>/', viewset_alternative_detail),
    path('viewset-alt/<int:pk>', viewset_alternative_detail),

    path('generic-viewset/', include(routerGeneric.urls)),

    path('model-viewset/', include(routerModel.urls)),
]
