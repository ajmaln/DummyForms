from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import IndexForm


class IndexView(View):
    form_class = IndexForm(None)
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        return HttpResponse("Success")
