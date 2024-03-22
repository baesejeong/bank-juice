from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

# from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST',])
@permission_classes([AllowAny])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({ 'message': '게시글 생성 완료 !!' })


@api_view(['GET', 'PUT', 'DELETE',])
@permission_classes([AllowAny])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({ 'message': '게시글 수정 완료 !!' })

    elif request.method == 'DELETE':
        article.delete()
        return Response({ 'message': '게시글 삭제 완료 !!' })


@api_view(['GET', 'POST',])
def comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response({ 'message' : '댓글 생성 완료 !!'})
    

@api_view(['GET', 'PUT', 'DELETE',])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({ 'message': '댓글 수정 완료 !!' })
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'message': '댓글 삭제 완료 !!' })


@api_view(['GET', ])
def article_search(request, keyword):
    # keyword가 글에 포함된 경우
    articles = Article.objects.filter(title__contains=keyword) | Article.objects.filter(content__contains=keyword) 
    # keyword가 댓글에 포함된 경우
    comments = Comment.objects.filter(content__contains=keyword)

    data = set()
    for comment in comments :
        data.add(comment.article)

    for article in articles:
        data.add(article)

    article_serializer = ArticleSerializer(list(data), many=True)
    return Response(article_serializer.data)