import re

NORMALIZATION = {

    "bijlee":"bijli",
    "pani":"paani",
    "sadak":"road",
    "nali":"naali",
    "nal":"tap",
    "bijlii":"bijli",
    "current":"electricity",
    "light":"electricity",
    "khamba":"pole"

}
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

ISSUES = {

    "Electricity": [
"electricity",
"electric",
"power",
"power cut",
"powercut",
"current",
"voltage",
"transformer",
"meter",
"electric meter",
"wire",
"cable",
"pole",
"electric pole",
"street light",
"streetlight",
"blackout",
"load shedding",
"spark",
"fuse",
"connection",
"bill",
"electricity bill",

"bijli",
"bijlee",
"light",
"light gayi",
"light chali gayi",
"light nahi",
"light nahi aa rahi",
"current nahi",
"current nahi aa raha",
"bijli nahi",
"bijli nahi aa rahi",
"khamba",
"tar",
"meter kharab",
"fuse udd gaya"
],

    "Water": [

"water",
"water supply",
"drinking water",
"tap",
"pipeline",
"pipe",
"tank",
"motor",
"pump",
"borewell",
"water leakage",
"water bill",
"water connection",

"pani",
"paani",
"jal",
"nal",
"nal ka pani",
"pipe phat gaya",
"pipe leak",
"pipeline leak",
"motor kharab",
"tanki",
"paani nahi aa raha",
"paani nahi",
"jal supply",
"water problem",
"leakage",
"low pressure",
"paani kam aa raha"
],

    "Roads": [

"road",
"roads",
"street",
"pothole",
"bridge",
"footpath",
"divider",
"construction",
"lane",
"crossing",
"speed breaker",

"gadda",
"gadde",
"road kharab",
"sadak",
"sadak kharab",
"sadak toot gayi",
"road damage",
"road toot gayi",
"bridge damage",
"footpath toot gaya"
 
    ],

    "Sanitation": [

"garbage",
"waste",
"dustbin",
"drain",
"drainage",
"sewer",
"sewage",
"overflow",
"dirty water",
"waterlogging",
"mosquito",
"filth",
"smell",

"kachra",
"kachra pada hai",
"naali",
"nali",
"naala",
"nala",
"jam",
"blocked drain",
"drain block",
"ganda pani",
"ganda paani",
"paani bhar gaya",
"paani jama",
"badbu",
"machhar",
"sewer line",
"sewer overflow"


    ],

    "Health": [
"hospital",
"doctor",
"clinic",
"medicine",
"patient",
"ambulance",
"vaccination",
"health",
"treatment",
"blood",
"covid",
"dengue",
"malaria",

"aspatal",
"doctor nahi",
"medicine nahi",
"dawai",
"dawai nahi",
"bimar",
"bukhar",
"fever",
"ambulance nahi",
"patient"

    ],

    "Police": [

"police",
"crime",
"theft",
"stolen",
"robbery",
"fight",
"violence",
"harassment",
"fraud",
"cyber crime",
"missing",
"kidnap",
"assault",
"fir",

"chori",
"loot",
"maar peet",
"marpit",
"jhagda",
"fraud hua",
"cyber fraud",
"mobile chori",
"bike chori",
"gaadi chori",
"police complaint"

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

"vidyalaya",
"school fees",
"college fees",
"teacher absent",
"principal",
"exam problem",
"admission issue",
"hostel problem",
"student"

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
"airport",

"bus nahi",
"bus late",
"train late",
"metro late",
"auto wala",
"rickshaw wala",
"gaadi",
"vehicle",
"parking problem",
"driver issue" 
  ]
 
}

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

DURATION_PATTERNS = [

    r'\d+\s*day[s]?',
    r'\d+\s*week[s]?',
    r'\d+\s*month[s]?',
    r'\d+\s*hour[s]?',
    r'\d+\s*year[s]?',

    r'\d+\s*din',
    r'\d+\s*hafte',
    r'\d+\s*mahine',
    r'\d+\s*saal',


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
    r'pichle mahine',
    r'last week',
    r'last month',
    r'since yesterday',
    r'since last week',
    r'since last month'

]


def extract_entities(text):

    text_lower = text.lower()
    
    text_lower = re.sub(r"[^a-zA-Z0-9\u0900-\u097F ]", " ", text_lower)

    text_lower = re.sub(r"\s+", " ", text_lower)

    text_lower = text_lower.strip()

    for old, new in NORMALIZATION.items():
        text_lower = text_lower.replace(old, new)

    locations = []

    for city in CITIES:

        if city.lower() in text_lower:   
            locations.append(city)

    if len(locations)==0:
        locations=["Not Found"]

    
    duration = "Not Specified"

    for pattern in DURATION_PATTERNS:

        match = re.search(pattern, text_lower)

        if match:
            duration = match.group()
            break

    matched_keywords = []

    for words in ISSUES.values():

        for word in words:

            if word.lower() in text_lower:

                matched_keywords.append(word)

    matched_keywords = sorted(list(set(matched_keywords)))

    return {    

    "Location": locations,

    "Duration": duration,

    "Matched Keywords": matched_keywords

    }

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