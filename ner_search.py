import re

# ==========================================================
# CITIES
# ==========================================================

CITIES = [

    "Kanpur",
    "Noida",
    "Allahabad",
    "Lucknow",
    "Patna",
    "Ghaziabad",
    "Mathura",
    "Meerut",
    "Moradabad",
    "Saharanpur",
    "Delhi",
    "Bhopal",
    "Gorakhpur",
    "Varanasi",
    "Bareilly",
    "Jaipur",
    "Agra",
    "Aligarh",
    "Nagpur",
    "Indore",
    "Mumbai",
    "Chennai",
    "Pune",
    "Ahmedabad",
    "Chandigarh",
    "Kolkata",
    "Hyderabad",
    "Bengaluru"

]

# ==========================================================
# ISSUE KEYWORDS
# ==========================================================

ISSUES = {

    "Electricity": [

        "electricity",
        "bijli",
        "power",
        "power cut",
        "current",
        "voltage",
        "transformer",
        "meter",
        "wire",
        "cable",
        "khamba",
        "pole",
        "light",
        "blackout",
        "load shedding",
        "spark",
        "fuse",
        "electric shock",
        "street light",
        "electricity bill",
        "bill",
        "connection"

    ],

    "Water": [

        "water",
        "paani",
        "jal",
        "tap",
        "nal",
        "pipeline",
        "pipe",
        "water supply",
        "drinking water",
        "tank",
        "motor",
        "pump",
        "borewell",
        "leakage",
        "water connection",
        "water bill",
        "low pressure"

    ],

    "Roads": [

        "road",
        "roads",
        "street",
        "gadda",
        "pothole",
        "footpath",
        "bridge",
        "divider",
        "traffic",
        "speed breaker",
        "construction",
        "cement road",
        "lane",
        "crossing"

    ],

    "Sanitation": [

        "garbage",
        "kachra",
        "waste",
        "dustbin",
        "cleaning",
        "drain",
        "naali",
        "drainage",
        "sewer",
        "overflow",
        "blocked drain",
        "dirty water",
        "waterlogging",
        "ganda paani",
        "paani bhar gaya",
        "paani jama",
        "mosquito",
        "smell",
        "filth",
        "septic"

    ],

    "Health": [

        "hospital",
        "doctor",
        "medicine",
        "patient",
        "ambulance",
        "clinic",
        "vaccination",
        "fever",
        "covid",
        "malaria",
        "dengue",
        "treatment",
        "blood",
        "operation",
        "health"

    ],

    "Police": [

        "police",
        "crime",
        "theft",
        "stolen",
        "robbery",
        "snatching",
        "fight",
        "violence",
        "harassment",
        "fraud",
        "cyber crime",
        "missing",
        "kidnap",
        "assault",
        "traffic police",
        "fir"

    ],

    "Education": [

        "school",
        "college",
        "teacher",
        "student",
        "exam",
        "principal",
        "library",
        "fees",
        "admission",
        "hostel",
        "scholarship",
        "certificate",
        "attendance",
        "education"

    ],

    "Transport": [

        "bus",
        "train",
        "metro",
        "transport",
        "auto",
        "taxi",
        "rickshaw",
        "driver",
        "vehicle",
        "parking",
        "station",
        "ticket",
        "platform",
        "airport",
        "flight"

    ]

}

# ==========================================================
# DEPARTMENT MAPPING
# ==========================================================

DEPARTMENT_MAP = {

    "Electricity": "Electricity Department",

    "Water": "Water Supply Department",

    "Roads": "Public Works Department",

    "Sanitation": "Municipal Corporation",

    "Health": "Health Department",

    "Police": "Police Department",

    "Education": "Education Department",

    "Transport": "Transport Department"

}

# ==========================================================
# DURATION PATTERNS
# ==========================================================

DURATION_PATTERNS = [

    r'\d+\s*days?',
    r'\d+\s*weeks?',
    r'\d+\s*months?',
    r'\d+\s*hours?',

    r'ek din',
    r'do din',
    r'teen din',
    r'char din',
    r'paanch din',

    r'ek hafta',
    r'do hafte',
    r'teen hafte',

    r'ek mahina',
    r'do mahine',

    r'kal se',
    r'aaj se',
    r'raat se',
    r'subah se',
    r'pichle hafte',
    r'pichle mahine'

]

# ==========================================================
# URGENCY KEYWORDS
# ==========================================================

HIGH_WORDS = [

    "urgent",
    "immediately",
    "emergency",
    "critical",
    "danger",
    "accident",
    "fire",
    "blood",
    "hospital",
    "death",
    "injured",
    "shock",
    "blast"

]

MEDIUM_WORDS = [

    "problem",
    "issue",
    "please",
    "repair",
    "broken",
    "overflow",
    "blocked",
    "leakage",
    "pending",
    "delay"

]


# ==========================================================
# ENTITY EXTRACTION
# ==========================================================

def extract_entities(text):

    text_lower = text.lower()

    # -----------------------------
    # Location
    # -----------------------------

    location = "Not Found"

    for city in CITIES:

        if city.lower() in text_lower:

            location = city

            break

    # -----------------------------
    # Duration
    # -----------------------------

    duration = "Not Specified"

    for pattern in DURATION_PATTERNS:

        match = re.search(pattern, text_lower)

        if match:

            duration = match.group()

            break

    # -----------------------------
    # Category
    # -----------------------------

    category = "Unknown"

    issue_keywords = []

    for cat, words in ISSUES.items():

        for word in words:

            if word.lower() in text_lower:

                issue_keywords.append(word)

                category = cat

        if category != "Unknown":
            break

    # -----------------------------
    # Department
    # -----------------------------

    department = DEPARTMENT_MAP.get(category, "Unknown")

    # -----------------------------
    # Urgency
    # -----------------------------

    urgency = "Low"

    for word in HIGH_WORDS:

        if word in text_lower:

            urgency = "High"

            break

    if urgency == "Low":

        for word in MEDIUM_WORDS:

            if word in text_lower:

                urgency = "Medium"

                break

    # -----------------------------
    # Return
    # -----------------------------

    return {

        "Location": location,

        "Duration": duration,

        "Category": category,

        "Department": department,

        "Urgency": urgency,

        "Matched Keywords": issue_keywords

    }


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    while True:

        complaint = input("\nEnter Complaint (type exit to quit): ")

        if complaint.lower() == "exit":
            break

        result = extract_entities(complaint)

        print("\n========== Extracted Information ==========\n")

        for key, value in result.items():

            print(f"{key} : {value}")

        print("\n===========================================")