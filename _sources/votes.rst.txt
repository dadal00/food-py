Votes
======

Protocol
--------

- HTTPS + Protobuf, smaller payloads + faster decoding than JSON

To User
-------

- 255 bitmap, flip the bit if that entry is being sent
- Array or list of integers representing votes
- We determine which integer vote by the order in flipped bits 

From User
---------

- 255 bitmap so 32 bytes payload, flip the bit if voted for

Notes
-----

gRPC is an option but not like local productions. 

Specifically, it works very well because of smaller payloads, faster
decoding, and duplex streaming. But, we get the first two benefits
using protobuf. The duplex streaming is not realistic for over the
web. As a result, it is better to stick to HTTPS then use Protobuf
for the payloads. 

We maintain smaller payloads and faster decoding using Protobuf.
