from django.shortcuts import render

# Create your views here.
def privacy_view(request):
    return render(request, "privacy.html")