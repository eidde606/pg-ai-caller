from datetime import datetime


def save_transcript(scenario, response):
    filename = datetime.now().strftime("transcripts/%Y%m%d_%H%M%S.txt")

    with open(filename, "w") as file:
        file.write("Scenario:\n")
        file.write(scenario)
        file.write("\n\nAI Patient Response:\n")
        file.write(response)

    print(f"Transcript saved: {filename}")
