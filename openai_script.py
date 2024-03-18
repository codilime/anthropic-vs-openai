from openai import OpenAI

client = OpenAI()


def summarize_and_get_keywords(text):
    prompt = f"Please summarize the following text and provide the top 10 keywords:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4",
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )
    result = response.choices[0].message.content

    return result


# url = input("Enter the URL: ")
# print(summarize_and_get_keywords(url))
