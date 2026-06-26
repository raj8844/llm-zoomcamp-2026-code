def main():
    print("Hello from llm-zoomcamp-2026-code!")


if __name__ == "__main__":
    main()

from google import genai


client = genai.Client(api_key="AQ.Ab8RN6KlIaYdcK89Y5mYaBkM-02iSuRhtQ3-hgMut_qsxxLwKA")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)