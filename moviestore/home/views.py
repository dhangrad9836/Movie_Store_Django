from django.shortcuts import render

# Create your views here.

# home view
def index(request):
    template_data = {}
    template_data['title'] = 'Movie Store'
    return render(request, 'home/index.html', {
        'template_data' : template_data
    })


# about view
def about(request):
    return render(request, 'home/about.html')