import streamlit as st

from read_pdf_pypdf import read
from process import solve

st.title('Assignment Insight')


# intro section
st.markdown('## Introduction')
st.write('this is introduction section')


# upload section
st.markdown('## Upload Section')

genre = st.radio(
    "Choose your assignment file type",
    ('PDF', 'Image', 'Text'))

res = ''

if genre == 'PDF':
    # pdf input section
    pdf = st.file_uploader(label="Upload your assignment PDF here.", type=['pdf'])

    if pdf is not None:
        # function read pdf
        text = read(pdf)
        res = solve(text[0])
    
elif genre == 'Image':
    st.write('I\'m sorry, this feature is still on development.')
    

else:
    # text input section    
    text_input = st.text_area("Copy and paste your assignment's question here.")
    
    if text_input is not '':
        res = solve(text_input)

if res != '':
    st.markdown('### Insights 🌟')
    st.write(res)