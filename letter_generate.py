from datetime import date


def generate_letter(
    complaint_text,
    category,
    urgency,
    department,
    entities
):

    letter = f"""
------------------------------------------------------------

                    GOVERNMENT COMPLAINT LETTER

------------------------------------------------------------

To,
The Concerned Officer,
{department["department_name"]}

Subject: Complaint Regarding {category}

Respected Sir/Madam,

I am writing to formally lodge a complaint regarding the following issue.

Complaint Description:
------------------------------------------------------------
{complaint_text}
------------------------------------------------------------

Complaint Details

Location           : {entities["Location"]}

Duration           : {entities["Duration"]}

Category           : {category}

Urgency Level      : {urgency}

Department         : {department["department_name"]}

Helpline Number    : {department["helpline"]}

Complaint Date     : {date.today()}

I kindly request your department to investigate this issue and take the necessary action at the earliest.

Your prompt attention to this matter will be highly appreciated.

Thank you.

Yours faithfully,

Citizen

------------------------------------------------------------
"""
    return letter
    

   