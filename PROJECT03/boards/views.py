from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    boards = Board.objects.all()[::-1]
    return render(request, 'boards/index.html', {'boards':boards})
    
@login_required#로그인한 사람만이 페이지를 수정할수있도록 하게끔;;
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    return render(request, 'boards/detail.html', {'board':board})
@login_required    
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title') #.get method는 dic형태에서 사용가능
            # content = form.cleaned_data.get('content')
            # board = Board(title=title, content=content) # Board.objects.create(title, content=content)로 쓰면 save까지 같이 실행
            # board.save()
            
            board=form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
    else:
        form= BoardForm()
    return render(request, 'boards/form.html', {'form':form})
        
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     board = Board(title =title, content=content)
    #     board.save()
    #     return redirect('boards:detail', board.pk)
    # else:
    #     return render(request, 'boards/create.html')
    
def delete(request, board_pk):
    board = get_object_or_404(Board, pk = board_pk)
    if board.user ==request.user:
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:index')
        
@login_required   
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
            # board.title = form.cleaned_data.get('title')
            # board.content = form.cleaned_data.get('content')
            # board.save()
                board = form.save()
                return redirect('board:deatil', board.pk)
        else:
            form = BoardForm(initial=board.__dict__)
    else:
        return redirect('boards:index')
    return render(request, 'boards/form.html', {'form':form, 'board':board})
        

