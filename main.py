from dotenv import load_dotenv
import random

load_dotenv()

from app.patient import get_patient_response
from app.scenarios import SCENARIOS
from app.caller import make_call
from app.transcript import save_transcript


def main():
    scenario = random.choice(SCENARIOS)

    print("Scenario:")
    print(scenario)

    response = get_patient_response(scenario)

    print("\nAI Patient:")
    print(response)

    save_transcript(scenario, response)

    print("\nStarting call...")
    call_sid = make_call(response)

    if call_sid:
        print(f"Call created: {call_sid}")
    else:
        print("Call failed.")


if __name__ == "__main__":
    main()
