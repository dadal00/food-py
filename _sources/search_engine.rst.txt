Search Engine
=============

Every request for foods is a proxied request to the search engine.

*Also handles sorting, filtering and top n.*

1. Request goes to the backend.
2. Backend forwards request to the search engine.
3. Search engine processes request.
4. Search engine sends a response to the backend.
5. Backend forwards the respones back the user.

Notes
-----
Why the extra round trip?

The normal model is to expose the search engine to the public. We
choose to route the user traffic to our backend first then to the
search engine and back.

Given these assumptions:

- We are running the search engine on the same machine as the backend, giving microsecond latency round trip.
- We are using Protobuf.
- We are further optimizing the payload using the bitmap scheme.

The extra round trip latency would be in microseconds. The 
bottleneck would be the network round trip to and from the user, the
reverse proxy, or the processing time in the search engine. But,
this would be the same if we were to expose the search engine.

As a result, there are only benefits provided our assumptions
hold true.

Benefits:

- Smaller payload to send.
- Faster decoding using Protobuf + custom scheme.
- Bottlnecks are the same even if we were to just expose the search engine.


Attributes
----------
Location: string, today's location

Votes: integer, vote count 


