from dotenv import load_dotenv
from app.caller import make_call
from app.patient import get_patient_response
from app.scenarios import SCENARIOS

load_dotenv()


def main():
    scenario = SCENARIOS[0]

    print("Scenario:")
    print(scenario)

    response = get_patient_response(scenario)

    print("\nAI Patient:")
    print(response)

    make_call()


if __name__ == "__main__":
    main()
