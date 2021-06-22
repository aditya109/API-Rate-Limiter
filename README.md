# API Rate Limiter

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2cbf2f5a98654e528ad35ba022b1b8f4)](https://www.codacy.com/gh/aditya109/API-Rate-Limiter/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=aditya109/API-Rate-Limiter&amp;utm_campaign=Badge_Grade)
[![BCH compliance](https://bettercodehub.com/edge/badge/aditya109/API-Rate-Limiter?branch=main)](https://bettercodehub.com/)

Design a service or tool that monitor the number of requests per a window time a service agrees to allow. If the number of request exceeds the rate limiter blocks all the excess calls.

Things to analyze and discuss:

- Limiting the number of requests an entity can send to an API within a time window, for example, twenty requests per second. 
- Rate limiting should work for a distributed setup, as the APIs are available through a group of servers.
- How to handle throttling (soft and hard throttling, etc.).

## Starting Server Manual

```powershell
docker run --name f-server -p 5001:5001 flask-server-app
```

