---
date: 2015-01-27 02:08:00
title: Twitter Markov Generator
featured-image: twitter-markov-generator-screenshot.png
---

I recently built a Markov Generator for Twitter in a few hours. The site will look at your last few hundred tweets and randomly try to find something that you might say. It uses probability from your previous tweets to find words that might go together.

I built this to take a break from applying for Software Engineer positions in SF.

The results can be quite funny and sometimes you might not be able to tell if it is real or not.

The frontend is a tiny angular app. There is a PHP backend that will connect to the Twitter API and get the most recent tweets from the supplied user and attempt to build a markov chain. You can get the [source code on GitHub](https://github.com/jamesduffy/twitter-markov-generator).

I want to revisit this and build proper Twitter Authentication and more robust error handling, but it works right now and is pretty fun.