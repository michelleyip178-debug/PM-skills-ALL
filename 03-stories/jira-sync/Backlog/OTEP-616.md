# OTEP-616: Remove bastion for ssm tunneling and move it into ecs cluster

**Type:** Task
**Status:** Backlog
**Assignee:** Fanxu Wang
**Story Points:** N/A

---

## Description

Right now in otep, there are ec2 instances which function purely as bastion hosts to allow devs to create ssm sessions to reach otep application from their local machine during development.    ec2 instances requires networking management as well like nacl, sg which adds overhead and since it is an instance, it requires some form of maintenance and deployment overhead.    packing it into an ecs task makes it easier to deploy and manage any image updates.  there is no actual routing to manage cause ssm tunneling is actually a public call to aws api which is publicly available.   since the ecs task is already in the ecs cluster, there is no additional routing to manage since it will have access to all the resources similar to the services already deployed in the cluster    References:  -  https://sgts.gitlab-dedicated.com/wog/psd/pdo/intelligence/intelligence-iac/-/tree/main/module/ssm-tunnel?ref_type=heads  -  https://sgts.gitlab-dedicated.com/wog/psd/pdo/intelligence/intelligence-iac/-/blob/main/live/dev/compute/services/ssm-tunnel/terragrunt.hcl?ref_type=heads  -  https://sgts.gitlab-dedicated.com/wog/psd/pdo/intelligence/intelligence-iac/-/blob/main/.gitlab-ci.yml?ref_type=heads#L257  (you don’t necessarily need to do it this way but just an example here)    AC: ssm ecs task in ecs cluster but deployed to private subnet like other tasks add proper iam roles to the ecs task. refer to reference try starting a ssm session into the task to hit the db since this is the use case for it

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
