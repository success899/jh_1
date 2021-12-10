from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import NewModel


def hello_world(request):

    if request.method == 'POST':
        input_data = request.POST.get('input_data')

        new_model = NewModel()
        new_model.text = input_data
        new_model.save()

        new_model_list = NewModel.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

        # return render(request, 'accountapp/hello_world.html', context={'new_model': new_model,
        #                                                                'new_model_list': new_model_list})

    new_model_list = NewModel.objects.all()

    return render(request, 'accountapp/hello_world.html', context={'new_model_list': new_model_list})
