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
    book_list = Book.objects.all()
    return render(request, "books.html", {"book_list": book_list})


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


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)


def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite=True
    book.save()
    return redirect(books)


def unmark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite=False
    book.save()
    return redirect(books)


def BooksDetail(request, id):
    book = Book.objects.get(id=id)
    book.save()
    return redirect(books_detail)
