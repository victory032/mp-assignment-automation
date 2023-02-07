import os
import easyocr
import streamlit as st

from pypdf import PdfReader


def read_pdf(pdf: object) -> list:
    """This function is used to read pdf and parse the text

    Args:
        pdf (object): PDF file/path

    Returns:
        list: list of parsed text from the pdf input
    """
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    text_list = []
    for i in range(number_of_pages):
        page = reader.pages[i]
        text_list.append(page.extract_text())

    return text_list
# HOELIT FINAL EXAM 2022   1. Write an essay of 850-1500 words.  2. You need at least 4 (four) reliable sources. Write all your references in References section. Cite your sources properly.  3. In your essay, you need to discuss a writer (or more)/ a literary work (or more)/ a literary movement that we have discussed throughout this semester. You may discuss the characteristics, the contribution they have made, the values/ criticism they contain, etc. Below are some sample topics for your essay: a. Shakespeare and his contribution to English language and literature, b. Stream of consciousness as a literary breakthrough in twentieth century English literature, c. Social criticism in Charles Dicken’s works.  4. Provide a title and write your essay in paragraphs. Your essay must have the introduction, body (discussion), and the conclusion. 5. Use the provided template.  6. Submit your essay to the LMS no later than 24 December 2022 (early submission is always welcome).  7. If you want to discuss your plan for the essay, feel free to contact me.  8. Plagiarism might result in score reduction or test failure.


@st.cache
def read_image(imgpath: object, lang: list = ['id', 'en']) -> list:
    """This function is used to read image and parse the text

    Args:
        imgpath (object): img file | opencv | img path
        lang (list, optional): Language of the image input. Defaults to ['id', 'en'].

    Returns:
        list: list of parsed text from the image input
    """
    reader = easyocr.Reader(lang)
    text_list = reader.readtext(imgpath, detail=0, paragraph=True)
    return text_list
# 'Pertanyaan dan Tugas', "Jelaskan makna presisi dan akurasi dalam penarikan sampell Jelaskan yang dimaksud dengan populasi sasaran dan populasi target, kemudian berikan contoh! Sebutkan dua masalah yang dihadapi dalam teknik penarikan sampel! Kemukakan langkah-langkah dalam penarikan sampel! Tiga buah penelitian seperti di bawah ini dilakukan Tunjukanlah sampe can populasinya dalam masing-' masing penelitian. (a) Untuk mengetahui apakah seorang pasien menderita malaria atau tidak, seorang dokter mengambil darah pasien tersebut untuk diteliti atau diperiksa  Hasil penyelidikan (pemeriksaan) menunjukkan oanwa pasien tersebut menderita
# malaria_ (b) Seorang ibu telah membuat satu panci gulai kambing: Untuk mengetahui rasa gulai kambing hasil olahannya itu, setelah diaduk sampai rata satu sendok makan gulai tersebut dicicipi ternyata rasanya enak.
# (c) Seorang pedagang jeruk dipinggir jalan, selalu menawarkan sebuah jeruk untuk dicicipi pembelinya Sebuah populasi dibag menjadi beberapa grup, setiap grup mempunya variasi Yang besar tetapi antar grup mempunya varias kecil. Bila anda akan menarik sampe dari populasi tersebut, teknik sampling mana Yang akan anda gunakan? Buatlah suatu contoh kasus penarikan sampel, sehingga teknik Yang digunakan merupakan sampling Klaster
# Gunakan sebuah kalender; kemudian secara sistematik ambil sampel setiap delapan belas hari, dimulai pada tangga 4 Januari. Lakukan analisis terhadap (lima) buah skripsi/tesis disertasi, kemudian sebutkan: (a) populasi atau sampel penelitiannya, (b) jenis sampling apa Yang dipilih, (c) rumus dan perhitungan ukuran sampel Inya"
