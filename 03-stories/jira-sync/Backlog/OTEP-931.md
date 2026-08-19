# OTEP-931: Refactor interface_endpoint_extras from map(bool) to map(string) in networking module

**Type:** Task
**Status:** Backlog
**Assignee:** N/A
**Story Points:** N/A

---

## Description

Discovered while working on OTEP-801 (Pocdex connectivity). The  interface_endpoint_extras  variable in  module/networking  is typed as  map(bool) , forcing the module to derive the AWS service name from the Terraform key by replacing underscores with dots: service => "com.amazonaws.ap-southeast-1.${replace(service, "_", ".")}" This breaks for  execute-api  — the only valid Terraform key  execute_api  transforms to  execute.api , which does not exist in AWS. The workaround was to add  execute_api  to the hardcoded baseline map instead, but that grows module code every time a hyphenated service is needed. Fix: Change  interface_endpoint_extras  in  variables.tf  from  map(bool)  to  map(string)  where the value is the full AWS service name. Replace the transform in  main.tf  with a direct pass-through: # before
service => "com.amazonaws.ap-southeast-1.${replace(service, "_", ".")}"
# after
service => name Update all live configs using extras (qa, uat, prd) to pass explicit service name strings: interface_endpoint_extras = {
  ssmmessages = "com.amazonaws.ap-southeast-1.ssmmessages"
  ec2messages = "com.amazonaws.ap-southeast-1.ec2messages"
  sqs         = "com.amazonaws.ap-southeast-1.sqs"
} Run  terragrunt validate  and  terragrunt plan  across affected stacks — this is a pure refactor, no resource drift expected. As a side effect, this makes the hardcoded baseline map ( intranet_endpoint_service_names ) redundant long-term. Collapsing them is out of scope here.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
