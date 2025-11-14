Foods
=========

Initialization
--------------

- External file for mapping food string to **index** number
- **index** refers to index in user's bitmap for votes
- Load in file as set at runtime, maintain same state

Beginning of Day
----------------

- Cron job daily pull foods for that day
- Check if gibberish and if already mapped in in-memory set
- If not mapped, append to external file, in-memory set, and to search engine
- If not gibberish, add it to todays food and its respective dining court

End of Day
----------

- Clear dining courts
