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

    complaint_text = transcribe_audio(audio_path)

    category, urgency = predict_complaint(complaint_text)
    
    entities = extract_entities(complaint_text)
    
    department, similarity = find_department(complaint_text)
    
    similar = find_similar_complaints(complaint_text)

    letter = generate_letter(
        complaint_text,
        category,
        urgency,
        department,
        entities
    )

    return {

        "transcribed_text": complaint_text,

        "category": category,

        "urgency": urgency,

        "department": department,

        "similar_complaints": similar,

        "entities": entities,

        "letter": letter
    }