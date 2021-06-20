# API Rate Limiter

Design a service or tool that monitor the number of requests per a window time a service agrees to allow. If the number of request exceeds the rate limiter blocks all the excess calls.

Things to analyze and discuss:

- Limiting the number of requests an entity can send to an API within a time window, for example, twenty requests per second. 
- Rate limiting should work for a distributed setup, as the APIs are available through a group of servers.
- How to handle throttling (soft and hard throttling, etc.).

