import os
from pathlib import Path
from pdflatex import PDFLaTeX

current_dir = Path(__file__).parent

subfolder = "latex_files"
file_name = "latex.tex"

file_path = current_dir / subfolder / file_name

output_dir = current_dir / subfolder
output_dir.mkdir(parents=True, exist_ok=True)

original_cwd = os.getcwd()
try:
    os.chdir(output_dir)
    pdfl = PDFLaTeX.from_texfile(file_path)
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
finally:
    os.chdir(original_cwd)

print(f"PDF created successfully in {output_dir}")
