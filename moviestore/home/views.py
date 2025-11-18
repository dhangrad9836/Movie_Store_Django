from django.shortcuts import render

# Create your views here.

# home view
def index(request):
    template_data = {} # empty dictionary
    template_data['title'] = 'Movies Store'  # create key called title and store the 'Movie Store' title valuein the template_data dictionary
    return render(request, 'home/index.html', {
        'template_data' : template_data })    # third arg to pass in the template_data variable this will show when it's extended
    


# about view
def about(request):
    template_data = {} # empty dictionary
    template_data['title'] = 'About'    # create a key called title and store the 'About' title value in the template_data dictonary
    return render(request, 'home/about.html', { 'template_data' : template_data })