.. Food documentation master file

Food documentation
==================

Purdue dining court voting platform.

User Flow
---------

- Only once user tries first vote
- Requires verified Purdue email
- Requests 6-digit numeric code
- Once verified, user gets a long-lasting cookie
- If cookie exists, no need to check for or request email again

User Voting
-----------

- Search engine provides voting options
- Debounce search input by 200-500 ms to prevent overload
- Semantic search
- Thumbs-up or not
- Delay pushing user inputs until page refresh **or** max thumbs reached
- Daily cron job fetches that day's meal items

Database
--------

Requirements
~~~~~~~~~~~~

- Fast lookups
- Decently small dataset
- Max 255 food-int pairs
- Max 50,000 usernames (max 100 chars), 255 option pairs

Choice
~~~~~~~~~~~~

- **Redis**, in-memory database
- Use a **Redis hash** with 1 big key, then store key-values inside
- For users: string + 255-bit bitmap
- For foods: 8-bit int + 32-bit int
- Supports **atomic operations**
- Estimated memory usage:

   .. math::

      (32\text{ bytes (bitmap)} + 20\text{ bytes (key overhead)}) \times 50{,}000 = \text{roughly } 2.6\text{ MB}

Contents
--------

.. toctree::
   :maxdepth: 2

   docs
