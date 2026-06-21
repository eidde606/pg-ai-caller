from openai import OpenAI
import os


def get_patient_response(scenario):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
    prompt = f"""
    You are a patient calling a doctor's office.
    Scenario:
    {scenario}
    
    Respond naturally in one sentence:
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a patient."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
