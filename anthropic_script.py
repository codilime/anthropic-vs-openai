import anthropic

client = anthropic.Client()


def summarize_and_get_keywords(url):
    prompt = f"Please summarize the following text and provide the top 10 keywords:\n\n{url}"

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )
    result = response.content[0].text

    return result


# url = input("Enter the URL: ")
# print(summarize_and_get_keywords(url))
