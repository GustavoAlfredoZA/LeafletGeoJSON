from django.views.generic import View
from django.shortcuts import render
from mezzanine_flares.models import PlotXRay
from mezzanine_flares.forms import PlotXRay_Form
from django.http import HttpResponseRedirect

class map(View):
    """docstring for map."""

    def __init__(self, arg):
        super(map, self).__init__()
        self.arg = arg

class map_View(View):
    initial={'kay':'value'}
    #form_class=Paciente_Form
    template_name = 'templates/index.html'

    def get(self, request, *args, **kwargs):
        #var1 = self.kwargs['var1']
        return render(request, self.template_name)

    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyPlugin_View, self).dispatch(*args, **kwargs)
