from django.shortcuts import render, redirect
from .models import Board, Comment

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'boards' : boards})
    
    
def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        board = Board(title=title, content=content, image=image)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')

# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content') #db를 건드리는 행위를 실시할때는 GET이 아닌 POST(create,delete 등)
    
#     board = Board(title=title, content=content)
#     board.save()
    
#     return redirect('boards:detail', board.pk)
    
    
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    return render(request, 'boards/detail.html', {'board':board}, {'comments':comments})
    
    
    
def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
         board.delete()
         return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
    
    
def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk) #있던 값을 가져오는 것 !!
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board.image = request.FILES.get('image')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/edit.html', {'board':board})
    
    
# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.save()
    
#     return redirect('boards:detail', board.pk)


def comments_create(request, board_pk):
    board = Board.objects.get(pk =board_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.board = board
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)
        
def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)


