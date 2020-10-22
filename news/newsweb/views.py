from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/everything?q=apple&from=2020-10-20&to=2020-10-20&sortBy=popularity&apiKey=3f0c4d518cf840189a1a2ae5568e3284")
    
    api = json.loads(news_api_request.content)
    
    return render(request, 'home.html', {'api':api})
