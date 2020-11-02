from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html', {
        'posts' : [
            {
            'id':'1',
            'author': 'zeus',
            'content': '오늘은 즐거운 하루였다.',
            'created_at': '1월 1일',
            },
            {
            'id':'2',
            'author': 'zeus',
            'content': '벌써 한달이 가다니ㅜㅜ',
            'created_at': '2월 1일',
            },
        ],
    })

def detail(request, post_id):
    if post_id == 1:
        context = {
        'post' : 
            {
            'id':'1',
            'author': 'zeus',
            'content': '오늘은 즐거운 하루였다.',
            'created_at': '1월 1일',
            },
        }

    if post_id == 2 :
        context = {
        'post' : 
            {
            'id':'2',
            'author': 'zeus',
            'content': '벌써 한달이 가다니ㅜㅜ',
            'created_at': '2월 1일',
            }
        }
    return render(request, 'posts/detail.html', context)
    
