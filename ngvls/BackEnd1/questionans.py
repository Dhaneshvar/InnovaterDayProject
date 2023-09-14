import openai


api_key = "here"


def openAiModelAnswer(paragraph, question):
    openai.api_key = api_key
    
    # Combine the paragraph and question into a prompt
    prompt = f"Given the following paragraph:\n{paragraph}\n\nQuestion: {question}\nAnswer:"

    # Generate a response from GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use other engines too
        prompt=prompt,
        max_tokens=50,  # Adjust the number of tokens as needed
    )

    # Extract and return the answer from the response
    answer = response.choices[0].text.strip()
    
    return answer


paragraph = """
Musk attended Queen’s University in Kingston, Ontario, and in 1992 he transferred to the University of Pennsylvania, Philadelphia, where he received bachelor’s degrees in physics and economics in 1997. He enrolled in graduate school in physics at Stanford University in California, but he left after only two days because he felt that the Internet had much more potential to change society than work in physics. In 1995 he founded Zip2, a company that provided maps and business directories to online newspapers. In 1999 Zip2 was bought by the computer manufacturer Compaq for $307 million, and Musk then founded an online financial services company, X.com, which later became PayPal, which specialized in transferring money online. The online auction eBay bought PayPal in 2002 for $1.5 billion.

Witness the launch of the SpaceX Dragon capsule, May 25, 2012
Witness the launch of the SpaceX Dragon capsule, May 25, 2012See all videos for this article
Musk was long convinced that for life to survive, humanity has to become a multiplanet species. However, he was dissatisfied with the great expense of rocket launchers. In 2002 he founded Space Exploration Technologies (SpaceX) to make more affordable rockets. Its first two rockets were the Falcon 1 (first launched in 2006) and the larger Falcon 9 (first launched in 2010), which were designed to cost much less than competing rockets. A third rocket, the Falcon Heavy (first launched in 2018), was designed to carry 117,000 pounds (53,000 kg) to orbit, nearly twice as much as its largest competitor, the Boeing Company’s Delta IV Heavy, for one-third the cost.
"""

# print("Welcome to the QA bot. Ask your questions about AI:")
# while True:
#     user_question = input("You: ")
#     if user_question.lower() == 'exit':
#         break

#     answer = ask_gpt3(paragraph, user_question)
#     print("AI: ", answer)
