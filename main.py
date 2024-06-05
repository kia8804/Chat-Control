import mss
from openai import OpenAI
import base64
import key
import sim_keys


def take_screenshot():
    """Take a screenshot of the current screen and return it as an image file path."""
    with mss.mss() as sct:
        screenshot_path = "sct.png"
        sct.shot(
            mon=1, output=screenshot_path
        )  # Save screenshot as PNG using the index
        return screenshot_path


def encode_image_to_base64(image_path):
    """Encode an image file to a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def send_image_to_gpt4o(client, messages):
    """Send conversation messages to the OpenAI GPT-4o model and return the API response."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.0,
    )
    return response


def main():
    client = OpenAI(api_key=key.api())
    messages = [
        {
            "role": "system",
            "content": """Give me a list of key presses, one key per line to do this. 
            If you need to use 2 keys simultaneously/holding 2 down at the same time put them on the same line (like "ctrl a")
            Don't use the shift key. List all your key commands after a line with the text.""",
        }
    ]

    while True:
        image_path = take_screenshot()
        base64_image = encode_image_to_base64(image_path)
        question = input("Enter your question for the image (or type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"},
                    },
                ],
            }
        )

        response = send_image_to_gpt4o(client, messages)
        if response.choices:
            output = response.choices[-1].message.content
            print("API Response:", output)
            sim_keys.multi_key_press(output)


if __name__ == "__main__":
    main()
