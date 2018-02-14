from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class DjappView(View):
    def get(self, request, *args, **kwargs):
        t1 = kwargs.get('thing1')
        t2 = kwargs.get('thing2')

        if t1 is None:
            response_part_1 = 't1 is none'
        else:
        	response_part_1 = 't1 is ' + str(t1) + ' of type: ' + type(t1).__name__

        if t2 is None:
            response_part_2 = 't2 is none'
        else:
        	response_part_2 = 't2 is ' + str(t2) + ' of type: ' + type(t2).__name__

        response_string = response_part_1 + '<br>' + response_part_2
        return HttpResponse(response_string)