from django.shortcuts import render, redirect
from .models import Game_Model
from .forms import GameForm


def list_all(request):
    video_game_list = Game_Model.objects.all
    context = {'video_game_list': video_game_list}
    return render(request, 'VideoGame_App/index.html', context)


def post_new(request, ):
    form = GameForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        # post.title = request.user
        post.save()
        return redirect("list_all")
    else:
        form = GameForm()
    return render(request,'VideoGame_App/add.html', {'form': form})