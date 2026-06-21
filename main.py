from dotenv import load_dotenv
from app.caller import make_call


def main():
    load_dotenv()

    print("Starting call...")

    call_sid = make_call()

    print(f"Call created: {call_sid}")


if __name__ == "__main__":
    main()
