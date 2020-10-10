from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from vacasawebservice.answer_question import answer_question
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework.request import Request
#import requests

#@api_view(['GET'])
def question(request):
    return_value = ''
    query = request.GET.get('q')
    print(query)
    return_value = answer_question(query)
    return HttpResponse(return_value)
    