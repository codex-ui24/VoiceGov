import re

CATEGORY_KEYWORDS = {

    "Electricity": [
        "bijli",
        "electricity",
        "power",
        "power cut",
        "power outage",
        "transformer",
        "voltage",
        "meter",
        "electric pole",
        "khambha",
        "wire",
        "bill"
    ],

    "Water": [
        "water",
        "pani",
        "jal",
        "water supply",
        "pipeline",
        "pipe",
        "tap",
        "leak",
        "leakage",
        "drainage"
    ],

    "Roads": [
        "road",
        "sadak",
        "pothole",
        "gadda",
        "bridge",
        "traffic",
        "street",
        "footpath"
    ],

    "Sanitation": [
        "garbage",
        "kachra",
        "dustbin",
        "waste",
        "cleaning",
        "sewage",
        "drain",
        "naali",
        "toilet"
    ],

    "Health": [
        "hospital",
        "doctor",
        "ambulance",
        "medicine",
        "medical",
        "health",
        "clinic"
    ],

    "Police": [
        "police",
        "crime",
        "theft",
        "robbery",
        "fight",
        "violence",
        "harassment"
    ],

    "Education": [
        "school",
        "teacher",
        "college",
        "student",
        "class",
        "exam"
    ],

    "Transport": [
        "bus",
        "train",
        "metro",
        "transport",
        "auto",
        "traffic signal"
    ]

}


HIGH_WORDS = [
    "fire",
    "aag",
    "electrocution",
    "shock",
    "gas leak",
    "explosion",
    "hospital",
    "ambulance",
    "accident",
    "death",
    "collapsed",
    "gir gaya",
    "flood"
]

MEDIUM_WORDS = [
    "2 days",
    "3 days",
    "teen din",
    "do din",
    "urgent",
    "not working",
    "band",
    "problem",
    "issue"
]


def apply_rules(text, ml_prediction):

    complaint = text.lower()

    # High priority
    for word in HIGH_WORDS:
        if word in complaint:
            return "High"

    # Medium priority
    for word in MEDIUM_WORDS:
        if word in complaint:
            if ml_prediction == "Low":
                return "Medium"

    return ml_prediction