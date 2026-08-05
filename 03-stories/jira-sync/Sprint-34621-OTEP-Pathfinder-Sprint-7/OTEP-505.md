# OTEP-505: [FE] CFT integration - upload file and webhook

**Status:** QA
**Assignee:** Hao Eng
**Story Points:** N/A
**Sprint:** OTEP-Pathfinder Sprint 7 (34621)

---

## Description

The DNS name of the CFT API server.  https://api.cft.stack.gov.sg  (Internet)  https://api.in.cft.stack.gov.sg  (Intranet) ← we shld be using this based on  https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-docs/-/merge_requests/16#note_15522070 CFT references HTTPS authentication:    Uploading file: https://docs.developer.tech.gov.sg/docs/cft-rest-api-documentation/#tag/Files/operation/upload-files-key      Infra changes none cos the CFT is in intranet and the OTEP IP ranges should able to cover. Ingress and egress are all under intranet. https://docs.developer.tech.gov.sg/docs/cft-additional-docs/firewall-clearance?product=Cloud+File+Transfer+(CFT) Testing for webhook notification in local using ngrok setup:  https://dashboard.ngrok.com/get-started/setup/mac-os when run, will hit x509 cert error, change the cloudfare setting to DOH  testing webhook locally:     can forward to the sub-directory by putting  <ngrok public url>/api/cft/<domain> Decision Multiple web webhook endpoint vs single endpoint? choose single endpoint instead cos next time there will be an API GW that suppose to forward to respective service endpoint instead, and this will be temporarily solution (single  route.ts  easier to see all the logic) Web does the mapping to know which service endpoint to call  check the map of workflow id → service endpoint  one webhook url called  /api/cft  at web Environment variables https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/merge_requests/45 https://sgts.gitlab-dedicated.com/wog/psd/pdo/otep/otep-iac/-/merge_requests/49 CFT_WEB_CLIENT_ID, CFT_WEB_CLIENT_SECRET - used for cft   /auth  to form bearer token in request header when calling CFT upload file API CFT_SERVICE_CLIENT_ID, CFT_SERVICE_CLIENT_SECRET - used for cft  /auth  to form bearer token in request header when calling CFT download file API CFT_BASE_URL  - intranet CFT URL CFT_WORKFLOW_ID_OPPORTUNITY - to know which workflow ID to send to for the particular file type (in this case, opportunity OTG) CFT_WEBHOOK_SECRET -for verifying the signature of the event payload at web OTEP_SERVICE_API_KEY  - for service-to-service call authentication Out of scope Calling CFT to check for missing notification Retry processing for  cft_upload  db table  NEW  status populate the error data rows back to web from service (currently only consider happy path. if want to check for error, need to go DB check error message in  cft_upload  table) if service endpoint  /cft/upload  is not called by web, the  cft_upload db record wont be created (maybe service is down for a moment). When event notification comes in, will still proceed to download and ingest the file but this  CFT_FILE_ID  will be lost as there is no such upload db record. What shld be the behaviour for this?

---

## Subtasks

_No subtasks._

---

## Latest Comments

**boonsiangteh** (2026-07-21)
Hao Eng CHUA  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-service  on branch  main :   Refactor CFT client and simplify shared packages

---

**boonsiangteh** (2026-07-21)
Hao Eng CHUA  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-service  on branch  fix/otep-505-refactoring : fix:    fix the body close and shallow copy of httpclient

---

**boonsiangteh** (2026-07-21)
Hao Eng CHUA  mentioned this issue in  a commit  of  WOG / PSD / pdo / OTEP / otep-service  on branch  fix/otep-505-refactoring : chore:    fileprocessor as interface

---
*Synced from Jira: 2026-08-05*
