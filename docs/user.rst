User
========

Flow
---------

- Only once user tries first vote
- Requires verified Purdue email
- Requests 6-digit numeric code
- Once verified, user gets a long-lasting cookie
- If cookie exists, no need to check for or request email again

Voting
-----------

- Search engine provides voting options
- Debounce search input by 200-500 ms to prevent overload
- Semantic search
- Thumbs-up or not
- Delay pushing user inputs until page refresh **or** max thumbs reached
- Daily cron job fetches that day's meal items
