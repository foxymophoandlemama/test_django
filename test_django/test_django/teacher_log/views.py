from django.shortcuts import render
from django.views import generic
from models import Scholar


def index(request):
    return render(request, 'index.html')

class ListScholarsView(generic.ListView):
    template_name = 'scholars.html'
    context_object_name = 'scholars'

    def get_queryset(self):
        return Scholar.objects.all()

class ScholarDetailView(generic.DetailView):
    model = Scholar
    template_name = 'scholar.html'
