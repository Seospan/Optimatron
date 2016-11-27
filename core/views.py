from django.shortcuts import render
from bakery.views import BuildableTemplateView, BuildableListView, BuildableDetailView
from .models import Snippet

# Create your views here.
from django.http import HttpResponse
from django.template import loader


class TestView(BuildableTemplateView):
    context = {
        'var1': "TOTO",
        'var2': "TOTO2",
    }
    build_path = 'test.html'

    def get_context_data(self, **kwargs):
        context = {
            'var1' : "TOTO",
            'var2' : "TOTO2",
        }
        return context

    template_name = "core/test.html"


class SnippetListView(BuildableListView):
    queryset = Snippet.objects.all().order_by("titre")
    build_path = 'snippets/index.html'

    def get_context_data(self, **kwargs):
        context = super(SnippetListView, self).get_context_data(**kwargs)
        return context

class SnippetDetailView(BuildableDetailView):
    model = Snippet

    def get_context_data(self, **kwargs):
        context = super(SnippetDetailView, self).get_context_data(**kwargs)
        return context


def testid(request,id):
    # template = loader.get_template('core/test.html')
    context = {
        'var1' : "TOTO",
        'var2' : "TOTO2",
        'id' : id,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'core/testid.html', context)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")