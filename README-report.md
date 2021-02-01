# Assessment report

## First thoughts:

After reading the instructions, I thought I would need to write two core components:

- A client to fetch data from twitter
- A service that consumes this client and does the aggregation of the words, and other business rules

Then, I would need to think about the boundaries of the system, mainly:

- Transport layer (API)
- The data access Layer (Persistence)

With those components in mind, here is my thoughts about them:

## Twitter client

I chose to build a twitter client that wraps the external library, instead of using the lib directly, for two reasons:

- Decouple the service from a specific external library
- Allow dependency injection, so I can test better and avoid patching

Then, I chose to use a lib that support the features that I needed

## Word Cloud Service

The service uses the client to fetch all tweets in the last 24h. Then, it aggregates the words in a dictionary and build a response with the timestamps

A good improvement would be to have a dictionary of pronouns, articles, prepositions and other unwanted word classes

To get the maximum allowed number of words, I've reverse ordered the aggregation of words by the number of appearences, and got the first n words. That way, the words that appear the most have the priority

## Transport Layer

For the API, I chose the FastAPI framework. I like it because it is very lightweight, performative and gives freedom to chose what software design to use.

To make the authentication, I chose a simple approach to just compare an API Key. For production code I would choose something more secure, but for the assessment, it's enough to reproduce the behavior of the API

## Persistence

Initially I was thinking in using MySQL to store user or API Keys. Since the description of the assessment tells to avoid much code and to build everything in no more than an afternoon, I chose to store a key in plain text and use it, so I removed all the database related stuff from the initial boilerplate.
