import json
import openai
import os
import subprocess
from pdflatex import PDFLaTeX
from pathlib import Path


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
    
    print("Code is successfully generated!")
    return response.choices[0].message.content


def file_saver(latex_code, prompt):
    parent_folder = "latex_files"
    folder_name = prompt.lower().replace(" ", "-")
    file_name = f"{folder_name}.tex"
    nested_folder = os.path.join(parent_folder, folder_name)
    
    if not os.path.exists(nested_folder):
        os.makedirs(nested_folder)
    else:
        nested_folder = os.path.join(parent_folder, f"{prompt}-2")
        os.makedirs(nested_folder)
        
        
    file_path = os.path.join(nested_folder, file_name)
    
    with open(file_path, "w") as file:
        file.write(latex_code)
        
    print("Code is successfully written into .tex file!")
    return folder_name


def verbatim_remover(folder_name):
    current_dir = Path(__file__).parent

    subfolder = "latex_files"
    file_name = f"{folder_name}.tex"
    file_path = current_dir / subfolder / folder_name / file_name

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if (r'\documentclass{article}' not in content):
        print()
        content = content.replace(r'\begin{verbatim}', r'\documentclass{article}')
    else:
        content = content.replace(r'\begin{verbatim}', '')
    
    content = content.replace(r'\end{verbatim}', '')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        file.close()
    
    print("All unnecessary code has been deleted from the .tex file")
    
    
    
    
def latex_compiler(folder_name):
    current_dir = Path(__file__).parent

    subfolder = "latex_files"
    folder_name = folder_name
    file_name = f"{folder_name}.tex"

    file_path = current_dir / subfolder / folder_name / file_name

    output_dir = current_dir / subfolder / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)

    original_cwd = os.getcwd()
    try:
        os.chdir(output_dir)
        pdfl = PDFLaTeX.from_texfile(file_path)
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
    finally:
        os.chdir(original_cwd)

    print(f"PDF created successfully in {output_dir}")

        

if "__main__" == __name__:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        
    openai_api_key = config["openai_api_key"]
    
    prompt_from_user = input("Please enter the topic in few words (Do not enter any custom ChatGPT prompt here!!): ")
    latex_code = latex_maker_ai(openai_api_key, prompt_from_user)

    folder_name = file_saver(latex_code, prompt_from_user)
    verbatim_remover(folder_name)
    
    latex_compiler(folder_name)
    
    
    