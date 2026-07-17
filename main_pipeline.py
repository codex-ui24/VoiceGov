from test_sarvam import transcribe_audio
def process_voice_complaint(audio_path):
    complaint_text = transcribe_audio(audio_path)


from predict_model import predict_complaint

from ir_search import (
    find_department,
    find_similar_complaints
)

from ner_search import extract_entities

from letter_generate import generate_letter


def process_voice_complaint(audio_path):

    # --------------------------------------------------
    # Step 1 : Speech → Text
    # --------------------------------------------------

    complaint_text = transcribe_audio(audio_path)

    # --------------------------------------------------
    # Step 2 : Category + Urgency
    # --------------------------------------------------

    category, urgency = predict_complaint(complaint_text)

    # --------------------------------------------------
    # Step 3 : Entity Extraction
    # --------------------------------------------------

    entities = extract_entities(complaint_text)

    # --------------------------------------------------
    # Step 4 : Department Search
    # --------------------------------------------------

    department, similarity = find_department(complaint_text)

    # --------------------------------------------------
    # Step 5 : Similar Complaints
    # --------------------------------------------------

    similar = find_similar_complaints(complaint_text)

    # --------------------------------------------------
    # Step 6 : Letter Generation
    # --------------------------------------------------

    letter = generate_letter(
        complaint_text,
        category,
        urgency,
        department,
        entities
    )

    # --------------------------------------------------
    # Step 7 : Return Everything
    # --------------------------------------------------

    return {

        "transcribed_text": complaint_text,

        "category": category,

        "urgency": urgency,

        "department": department,

        "similar_complaints": similar,

        "entities": entities,

        "letter": letter
    }