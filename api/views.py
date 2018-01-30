from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
import tweepy
from textblob import TextBlob
import os
import json
# Create your views here.


def index(request):

    query = request.GET.urlencode()
    cleanedQuery = query[6:]

    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    public_tweets = api.search(cleanedQuery)

    listOfResponses = []

    #print("list of repsones: before")
    #print(listOfResponses)

    for tweet in public_tweets:
        print("in loop")
        print(tweet.user.name)
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        listOfResponses.append({"tweet": tweet.text, "analysis": analysis.sentiment, "created_at": tweet.created_at, "user": tweet.user.name, "screen_name": tweet.user.screen_name, "user_desc": tweet.user.description })

# API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
# Returns tweets that match a specified query.
#
# Parameters:
# q – the search query string
# lang – Restricts tweets to the given language, given by an ISO 639-1 code.
# locale – Specify the language of the query you are sending. This is intended for language-specific clients and the default should work in the majority of cases.
# rpp – The number of tweets to return per page, up to a max of 100.
# page – The page number (starting at 1) to return, up to a max of roughly 1500 results (based on rpp * page.
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
# geocode – Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by “latitide,longitude,radius”, where radius units must be specified as either “mi” (miles) or “km” (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly.
# show_user – When true, prepends “<user>:” to the beginning of the tweet. This is useful for readers that do not display Atom’s author field. The default is false.

    print('length of listOfResponses')
    print(len(listOfResponses))
    #testResponse = [ {"test": [{"test2": "test3"}]}, { "test2": [{"test4": "lksdjfls"}]}]

    #return JsonResponse(testResponse, safe=False)

    # print('response list start *******************************')
    # print('response list end *******************************')
    #newJson = json.dumps(listOfResponses)

    return JsonResponse(listOfResponses, safe=False)

    #GET TWEEPY RESULTS FOR QUERY
    #return HttpResponse(response)

    # return JsonResponse(
    #     listOfResponses,
    #     safe=False
    # )

# def buildResponseList(responses):
#     print(responses)
#     listOfResponses = []
#
#     for tweet in responses:
#         print(tweet.text)
#         analysis = TextBlob(tweet.text)
#         print(analysis.sentiment)
#         listOfResponses.append({"tweet": tweet, "analysis": analysis})
#
#     return listOfResponses
