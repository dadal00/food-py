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
