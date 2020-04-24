---
title: "Twitter Authentication in Django with Tweepy"
date: 2015-01-13 00:36:00
aliases:
    - /journal/2015/twitter-authentication-in-django-with-tweepy/
---

While working on a recent project during my internship I had to come up with a way to authenticate users in our Django application. We use an Angular front-end that makes calls to Django.

I am going to strip out all the angular magic, but seriously. You need to go check it out. It makes building front-end applications in the browser stupid easy with just a little of javascript know how.

First off go make sure you check out the [Tweepy documentation](http://tweepy.readthedocs.org/en/v2.3.0/). I found it extremely helpful.

I am assuming you can set up the Django `urls.py` file yourself. We have at least two routes we need to make.

1. Start Twitter Authentication
2. Callback from Twitter

In our first view we need to do a few things. We need to set up our twitter application’s consumer token, consumer secret and the callback url.

```python
auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret', 'callback_url')
```

This authenticates your application with twitter so you can later authenticate a user. To authenticate a user you need to redirect them to twitter’s website to accept logging into your application. Tweepy has an easy way to get this url using ``.get_authorization_url()``. You should wrap any calls to outside services in try/except because you can never be sure when they will fail because of no fault of your own and when it does you can show a nice error message rather than everything crashing to a halt.

```python
try:
    redirect_url = auth.get_authorization_url()
    except tweedy.TweepError:
        return HttpResponse('error', status=500)
```

Your finished view file should look something like this:

```python
import tweepy


def twitterAuthenticate(request):
    auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret', 'callback_url')

    try:
        redirect_url = auth.get_authorization_url()
     except tweepy.TweepError:
        return HttpResponse('error', status=500)

    request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)

    return HttpResponseRedirect(redirect_url)

def twitterAuthorizeCallback(request):
    verifier = request.GET.get('oauth_verifier')

    auth = tweepy.OAuthHandler('consumer_token', 'consumer_secret')

    token = request.session.get('request_token')
    request.session.delete('request_token')
    auth.set_request_token(token[0], token[1])

    try:
        token = auth.get_access_token(verifier)
    except tweepy.TweepError:
        return HttpResponse('error', status=500)

    response_data = {}
    response_data['key'] = auth.access_token.key
    response_data['secret'] = auth.access_token.secret

    response = 'you are now authenticated'

    return HttpResponse(response)
```
