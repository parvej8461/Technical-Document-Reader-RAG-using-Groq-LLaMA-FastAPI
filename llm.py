from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def ask_llm(context, question):
    prompt = f"""
    Use the context below to answer accurately.

    Context:
    {context}

    Question:
    {question}
    """

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return completion.choices[0].message.content
