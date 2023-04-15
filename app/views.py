from django.shortcuts import render

# Create your views here.
def chucknoris(request):
    return render(request,'chucknoris.html')