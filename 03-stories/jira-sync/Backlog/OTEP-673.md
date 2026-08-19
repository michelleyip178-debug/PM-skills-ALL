# OTEP-673: Workaround solution to force cft to resolve otep's webhook hostname to private ip 

**Type:** Task
**Status:** Backlog
**Assignee:** Hao Eng
**Story Points:** N/A

---

## Description

Context:      Otep is currently integrated with CFT via the intranet route.      Seems like after the recent change to implement split horizon, currently cft’s intranet is resolving  dev.careercompass.gov.sg  to our public ip instead of internal alb’s ip in intranet compartment.    This is causing issues as cft’s intranet endpoint cannot reach our public endpoint and we do not want them to hit our webhook via the internet route as well.   based on their logs, it seems that their dns resolver queries our r53 public zone   one of the workarounds we can do to force them to go through intranet route is to add a alias record to our public r53 record to point to our internal alb  e.g  cft.dev.careercompass.gov.sg  --alias record → our internal alb in intranet then all we need to do is to update the cft portal with this new webhook domain and it should be able to resolve the domain to a private ip again and hit us via the intranet route.  However, this also means we need to update the alb listener to listen on this and route to the correct ecs task. e.g  cft.dev.careercompass.gov.sg/cft  → otep-web ssl certs are already configured so this is not an issue at the moment.    AC: create r53 alias record to point  cft.dev.careercompass.gov.sg  to internal alb in intranet vpc in our public r53 zone ! do nslookup for the record to ensure it resolve to private ip update cft portal with new domain test the webhook  Notes:  this seems like a workaround solution cause it involves us putting a private route in our public dns record. this can be confusing to some people especially if they do not have the context. so it would be worth asking the cft team how their dns resolvers resolve domains to private ips so that we can do away with this.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
