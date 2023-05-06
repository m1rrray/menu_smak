from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    page = Post.objects.all()
    return render(request, 'index.html', {'page': page})


# def dish_modal(request, dish_id):
#     dish = Post.objects.get(id=dish_id)
#     context = {'dish': dish}
#     return render(request, 'dish_modal.html', context)