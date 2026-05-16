# Scope and Decisions Prompts

Prompts for making, auditing, and validating scope and design decisions.

---

## Making a scope call

> What do we currently know about [topic] from the documents? What options have been considered? What constraints apply? What's still unknown? Frame this as: we need to choose between X and Y because...

---

## Checking for conflicts after a decision

> I just decided [decision]. Does this conflict with anything already documented? What specs or stories need updating? What downstream features does this affect?

---

## Auditing past decisions

> Compile every decision made across all sources. For each: what was decided, when, by whom, and whether it's confirmed or assumed. Flag any decisions that exist only in meeting notes.

---

## Identifying assumptions treated as facts

> What assumptions are being treated as facts? Find statements presented as given that haven't been explicitly validated. For each: the assumption, where it appears, and the risk if it's wrong.

---

## MVP vs R1 triage

> List every requirement or feature mentioned across all sources. Classify each as: MVP (must have for launch), R1 (next release), or Unclear. For Unclear items, explain what would help make the call.

---

## Scope creep detector

> Compare the original scope (PRD, brief, or earliest spec) against the latest versions and meeting notes. What's been added since the original scope was set? For each addition: what it is, when it appeared, who requested it, and whether it was explicitly approved.

---

## Descoping impact analysis

> If we remove [feature/story] from MVP, what breaks? Check: does anything else depend on it? Does it affect a success metric? Is it promised to a stakeholder? What's the minimum viable alternative?

---

## Decision debt inventory

> List every open question, unresolved discussion, or deferred decision across all sources. For each: what needs deciding, who should decide, what's blocking the decision, and the cost of leaving it open another sprint.
