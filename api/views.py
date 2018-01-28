from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

def index(request):
    print("testing this request")
    query = request.GET.urlencode()
    cleanedQuery = query[6:]
    # GET TWEEPY RESULTS FOR QUERY
    return JsonResponse({"name": 'test reponse ***2342343****', "queryTest": cleanedQuery}, safe=False)
