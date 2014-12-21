from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response,render


def index(request):
    return render(request, "d3/tilford_tree.html")


def sunburst(request):
    return render(request, "d3/sunburst.html")