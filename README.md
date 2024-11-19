
# LaTeX Generator using ChatGPT

This is a simple, single-file application that generates beautiful LaTeX files based on the prompt you provide. The content and structure of the file will be created by ChatGPT. For example, you can ask ChatGPT to create a "How to Solve Double Integrals" file, and it will generate both the content and the LaTeX code. The LaTeX file is then converted into a PDF locally.

---

## Requirements

### Operating System
- Windows, macOS, or Linux

### Software
1. **Python 3.8 or later**
2. **LaTeX Distribution**: 
   - Windows: [MikTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)
   - macOS: [MacTeX](https://tug.org/mactex/)
   - Linux: `sudo apt install texlive-full`
3. **Python Packages**: `openai`, `pdflatex`, `pathlib`
   - Install with: `pip install openai pdflatex pathlib`

4. **OpenAI API Key**
   - Save your API key in a `config.json` file:
     ```json
     {
       "openai_api_key": "your-api-key-here"
     }
     ```

---

## How to Run

1. Clone or download this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python your_script_name.py`
4. Enter a topic when prompted, and the program will:
   - Generate a `.tex` file in the `latex_files/` directory.
   - Compile it into a PDF.

---

## Example

1. Input: `How to Solve Double Integrals`
2. Output:
   - `latex_files/how-to-solve-double-integrals/how-to-solve-double-integrals.tex`
   - `latex_files/how-to-solve-double-integrals/how-to-solve-double-integrals.pdf`

---

## Notes

- Ensure your LaTeX distribution is installed and in your system's PATH.
- Ensure internet access to interact with the OpenAI API.

---

## License

This project is licensed under the MIT License.
