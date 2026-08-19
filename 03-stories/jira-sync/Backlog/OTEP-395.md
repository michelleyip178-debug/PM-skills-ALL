# OTEP-395: Inferring competencies for CV

**Type:** Story
**Status:** Backlog
**Assignee:** Benjamin Aw
**Story Points:** N/A

---

## Description

As an officer using the infer CV feature on OTEP, I should see a set of relevant inferred competencies suggested to me based on my CV so I can easily add them to my profile.  Acceptance Criteria Clicking “Review competencies” will call the CIE and return a list of minimum 5 to maximum 12 most relevant competencies, sorted by relevance. There will be no confidence score indicated. For each segmented chunk of text, a minimum of 5 competencies will be returned. Competencies are aggregated across the whole CV and deduplicated so that the same competency will not be proposed to the user Recommended competencies whose similarity score differs sufficiently should be removed from the competency listing every time. The number of returned competencies is dependent on the length of the document and what the CIE engine returns, capped at 12.  The competencies that are recommended are only functional competencies from the WOG FC bank and excludes core and agency-specific competencies Competencies linked to more recent job descriptions will be shown to the user first. Tech Specifics Chunking Mechanism:  Currently deterministic. Each retained section is split into roughly one statement per chunk via a two-stage split: first a bullet split (leading markers, numbered/lettered lists, inline glyph separators), then a statement split on  .!?;  followed by whitespace. Recency logic  To be implemented via a date-capturing mechanism that extracts job/role dates from the CV, so competencies linked to more recent positions are surfaced first.  Similarity threshold:  Cosine similarity is used to filter results. Threshold are relative/per-CV. Drop competencies sufficiently far from the top results, plus remove very low/negative scores.

---

## Subtasks

_No subtasks._

---

## Latest Comments

_No comments._
