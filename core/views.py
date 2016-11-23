from django.shortcuts import render
from bakery.views import BuildableTemplateView

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