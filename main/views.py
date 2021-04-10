from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


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