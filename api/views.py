from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework import mixins

from api.models import Article
from api.serializers import ArticleSerializer, ArticleModelSerializer

@csrf_exempt
def article_list(request, *a, **kw):
    if request.method == 'GET':
        articles = Article.objects.all()
        # serializer = ArticleSerializer(articles, many=True)
        serializer = ArticleModelSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # serializer = ArticleSerializer(data=data)
        serializer = ArticleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse('{}', status=200)

@csrf_exempt
def article_detail(request, *a, **kw):
    try:
        article = Article.objects.get(pk=kw['id'])
    except Article.DoesNotExist:
        return JsonResponse('{"errors":["not exists"]}')
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        serializer = ArticleModelSerializer(article)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        # serializer = ArticleModelSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=204)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse('{"status": "ok"}', status=204)

@api_view(['GET', 'POST'])
def getPostArticles(request, *a, **kw):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    serializer = ArticleModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#############
#############
#############

class ClassAPIView(APIView):
    def get(self, request, *a, **kw):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *a, **kw):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassAPIViewDetail(APIView):
    def getArticle(self, kw):
        try:
            return Article.objects.get(id=kw['id'])
        except Article.DoesNotExist:
            raise Http404("hello")

    def get(self, request, *a, **kw):
        article = self.getArticle(kw)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def put(self, request, *a, **kw):
        article = self.getArticle(kw)
        serializer = ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *a, **kw):
        article = self.getArticle(kw)
        article.delete()
        return Response('{"status": "ok"}', status=status.HTTP_204_NO_CONTENT)


#############
#############
#############

class ClassGenericAPIView(generics.GenericAPIView,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          ):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClassGenericAPIViewDetail(generics.GenericAPIView,
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                ):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#############
#############
#############

class GenericShortAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class GenericShortAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

#############
#############
#############

class ViewSet(viewsets.ViewSet):
    def list(self, request, *a, **kw):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request, *a, **kw):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, *a, **kw):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=kw['pk'])
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def update(self, request, *a, **kw):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=kw['pk'])
        serializer = ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, *a, **kw):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=kw['pk'])
        article.delete()
        return Response({"status": "ok"})


#############
#############
#############


class GenericViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = ArticleModelSerializer
    queryset = Article.objects.all()


#############
#############
#############


class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleModelSerializer
    queryset = Article.objects.all()
