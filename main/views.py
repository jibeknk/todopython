from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Book




def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")


def third(request):
    return HttpResponse("This is page test3")


def test4(request):
    return render(request, "added.html")


def test5(request):
    return render(request, "changed.html")


def test6(request):
    return render(request, "deleted.html")
    

def books(request):
    book_date = Book.objects.all()
    return render(request, "books.html", {"book_date": book_date})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def add_book(request):
    form = request.POST
    title = form["book_title"]
    book = Book(title = title)
    book.save()
    return redirect(books)