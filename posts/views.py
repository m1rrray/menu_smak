from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    page = Post.objects.all()
    return render(request, 'index.html', {'page': page})