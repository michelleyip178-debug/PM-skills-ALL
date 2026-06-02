import re

file_path = '/Users/michelleyip/Library/Mobile Documents/com~apple~CloudDocs/Documents/PM-skills-ALL-1/02-prd/prd-opportunities.md'
with open(file_path, 'r') as f:
    content = f.read()

# Fix lists
content = re.sub(r'^(\s*)-\s*\n\s*\n(.*)$', r'\1- \2', content, flags=re.MULTILINE)

# Fix quote blocks
content = re.sub(r'^>\s*\n\s*\n(.*)$', r'> \1', content, flags=re.MULTILINE)

# Fix bolding
content = content.replace('**Current State **', '**Current State**')

# Fix problem statement specific block
bad_problem_statement = """*Officers ***struggle to discover and apply for development opportunities **because they are **fragmented across multiple portals, **resulting in confusion on validity of job postings and friction for officers to have a single view of all short term and long term opportunities.

*Host agencies face the same problem in reverse: no operational visibility into applicants, manual sign-up tracking, and no feedback loop on whether opportunities actually filled. *"""

good_problem_statement = """*Officers **struggle to discover and apply for development opportunities** because they are **fragmented across multiple portals**, resulting in confusion on validity of job postings and friction for officers to have a single view of all short term and long term opportunities.*

> *Host agencies face the same problem in reverse: no operational visibility into applicants, manual sign-up tracking, and no feedback loop on whether opportunities actually filled.*"""

content = content.replace(bad_problem_statement, good_problem_statement)

# Fix table cells at the end
bad_row_1 = """| **US-09 - Apply for a STIP or Gig via FormSG link**    **Auto-Populated Fields:** The BO also noted that since the officer must log into OTEP before signing up, the system should capture their basic profile information on the backend so they do not have to manually fill it out again. These fields include:   -   Full Name   -   Designation   -   Division & Department   -   Ministry / Agency   -   Work Email |  |  |  |"""

good_row_1 = """| **US-09 - Apply for a STIP or Gig via FormSG link**<br><br>**Auto-Populated Fields:** The BO also noted that since the officer must log into OTEP before signing up, the system should capture their basic profile information on the backend so they do not have to manually fill it out again. These fields include:<br>- Full Name<br>- Designation<br>- Division & Department<br>- Ministry / Agency<br>- Work Email |  |  |  |"""

bad_row_2 = """| ## ** Proposed changes for Application fields (for MVP, we keep it as current ie no changes to the FormSG forms)    **Fields to Retain / Add:**   -   **Contact Number**.   -   **Reporting Officer’s Name and Email:** These are retained specifically to trigger an automated email notifying the supervisor of the application, helping keep the process transparent and combat dropout rates.   -   **Job Grade:** This replaces the legacy question asking if the officer is an individual contributor or team leader. It will be a dropdown list of MX grades with an "Others" option for non-MX tracks.   -   **Main reason for application**.   -   **Meet pre-requisites**.   -   **Declarations:** Retained, though the BO noted that different sets of declarations may be needed depending on whether the posting is a STIP or a Gig.   -   **Custom Questions:** The BO requested functionality allowing opportunity posters to add custom questions for their specific postings, similar to the FormSG form builder.      **Fields to Drop:**   -   **HR Officer’s Name and Email:** Dropped because this information was rarely utilized and often caused confusion for applicants.   -   **"Where did you find out about this opportunity?":** Dropped because all traffic will now route centrally through OTEP. |  |  |  |"""

good_row_2 = """| **Proposed changes for Application fields** (for MVP, we keep it as current ie no changes to the FormSG forms)<br><br>**Fields to Retain / Add:**<br>- **Contact Number**.<br>- **Reporting Officer’s Name and Email:** These are retained specifically to trigger an automated email notifying the supervisor of the application, helping keep the process transparent and combat dropout rates.<br>- **Job Grade:** This replaces the legacy question asking if the officer is an individual contributor or team leader. It will be a dropdown list of MX grades with an "Others" option for non-MX tracks.<br>- **Main reason for application**.<br>- **Meet pre-requisites**.<br>- **Declarations:** Retained, though the BO noted that different sets of declarations may be needed depending on whether the posting is a STIP or a Gig.<br>- **Custom Questions:** The BO requested functionality allowing opportunity posters to add custom questions for their specific postings, similar to the FormSG form builder.<br><br>**Fields to Drop:**<br>- **HR Officer’s Name and Email:** Dropped because this information was rarely utilized and often caused confusion for applicants.<br>- **"Where did you find out about this opportunity?":** Dropped because all traffic will now route centrally through OTEP. |  |  |  |"""

content = content.replace(bad_row_1, good_row_1)
content = content.replace(bad_row_2, good_row_2)

with open(file_path, 'w') as f:
    f.write(content)

print("Done")
