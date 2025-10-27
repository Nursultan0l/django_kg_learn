from django.shortcuts import render, redirect
from .models import Lesson, Documents, Letter, Numbers


def home(request):
    return render(request, 'home.html')

def lessons(request):
    return render(request, 'lessons.html')

def alphabet(request):
    return render(request, 'lessons/alphabet.html')

def numbers(request):
    return render(request, 'lessons/number.html')

def grammar(request):
    return render(request, 'grammar.html')

def materials(request):
    return render(request, 'materials.html')

def lessons_list(request):
    lessons_ls = Lesson.objects.all()
    return render(request, 'grammar.html', {'lessons_ls': lessons_ls})

def materials_list(request):
    materials_ls = Documents.objects.all()
    return render(request, 'materials.html', {'materials_ls': materials_ls})

def letters_list(request):
    letters_ls = Letter.objects.all()
    return render(request, 'lessons/alphabet.html', {'letters_ls': letters_ls})


def numbers_list(request):
    numbers_ls = Numbers.objects.all()

    nums_0_9 = [n for n in numbers_ls if n.title.isdigit() and int(n.title) < 10]
    nums_10_90 = [n for n in numbers_ls if n.title.isdigit() and 10 <= int(n.title) <= 90]
    nums_100_1000000000 = [n for n in numbers_ls if n.title.isdigit() and 100 <= int(n.title) <= 1000000000]

    context = {
        'nums_0_9': nums_0_9,
        'nums_10_90': nums_10_90,
        'nums_100_1000000000': nums_100_1000000000,
    }
    return render(request, 'lessons/number.html', context)
