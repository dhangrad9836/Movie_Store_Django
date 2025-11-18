from django.shortcuts import render

# Create your views here.

# home view
def index(request):
    template_data = {} # empty dictionary
    template_data['title'] = 'Movie Store'  # create key called title and store it in the template_data dictionary
    return render(request, 'home/index.html', {
        'template_data' : template_data     # third arg to pass in the template_data variable this will show when it's extended
    })


# about view
def about(request):
    return render(request, 'home/about.html')