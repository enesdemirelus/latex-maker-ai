import json
import openai

import openai

def latex_maker_ai(api_key, prompt):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You will receive a specific topic provided by the user. Based solely on this topic, your task is to generate a highly detailed and professional college-level summary or explanation. Your response must be crafted entirely as a well-structured and visually appealing LaTeX code, ensuring the output is optimized for professional presentation. The only thing you should return is the LaTeX code—no additional text, explanations, or comments."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


if "__main__" == __name__:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        
    openai_api_key = config["openai_api_key"]
    prompt_from_user = input("Please enter the topic in few words: ")
    latex_code = latex_maker_ai(openai_api_key, prompt_from_user)
    file = open("latex.txt", "w")
    file.write(latex_code)
    file.close()
    print("File succesfully created!")
    