from django.shortcuts import render, HttpResponse


def frontend(request):
    return render(request, "frontend.html")

def hakkimizda(request):
    return render(request, "hakkimizda.html")