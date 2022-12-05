from django.shortcuts import render

# Create your views here.


def skilles(request):
    context = {"skills": "active"}
    return render(request, "skills/skilles.html", context)
