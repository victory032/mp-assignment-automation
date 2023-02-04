import os
from pypdf import PdfReader

PATH = os.getcwd() + '/docs/data/example.pdf'

reader = PdfReader(PATH)

number_of_pages = len(reader.pages)

text = []

for i in range(number_of_pages):
    page = reader.pages[i]
    text.append(page.extract_text())

print(len(text))
print(text[0])

def read_pdf():
    return text[0]

# HOELIT FINAL EXAM 2022   1. Write an essay of 850-1500 words.  2. You need at least 4 (four) reliable sources. Write all your references in References section. Cite your sources properly.  3. In your essay, you need to discuss a writer (or more)/ a literary work (or more)/ a literary movement that we have discussed throughout this semester. You may discuss the characteristics, the contribution they have made, the values/ criticism they contain, etc. Below are some sample topics for your essay: a. Shakespeare and his contribution to English language and literature, b. Stream of consciousness as a literary breakthrough in twentieth century English literature, c. Social criticism in Charles Dicken’s works.  4. Provide a title and write your essay in paragraphs. Your essay must have the introduction, body (discussion), and the conclusion. 5. Use the provided template.  6. Submit your essay to the LMS no later than 24 December 2022 (early submission is always welcome).  7. If you want to discuss your plan for the essay, feel free to contact me.  8. Plagiarism might result in score reduction or test failure.