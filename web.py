import streamlit as st

import input
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
keywords = None

if genre == 'PDF':
    # pdf input section
    pdf = st.file_uploader(label="Upload your assignment PDF here.", type=['pdf'])

    if pdf != None:
        # function read pdf
        text = input.read_pdf(pdf)
        
        st.write(text)
        
        res, keywords = solve(text[0])
    
elif genre == 'Image':
    st.write('I\'m sorry, this feature is still on development.')
    
    img = st.file_uploader(label="Upload your assignment image here.", type=['jpeg, jpg, png'])

    if img != None:
        pass

else:
    # text input section    
    text_input = st.text_area("Copy and paste your assignment's question here.")
    
    if text_input != '':
        res, keywords = solve(text_input)

# insight section
if res != '' and keywords != None:
    st.markdown('### Insights 🌟')
    st.write(res)
    
    st.markdown('#### Generated Keywords')
    st.write(str(keywords))