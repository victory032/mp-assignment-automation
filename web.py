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
    ('PDF', 'Image', 'Text'), horizontal=True)

lang = st.radio(
    "Choose your language input",
    ('English', 'Indonesia'), horizontal=True)

if lang != '':
    if lang == 'English':
        lang = 'en'
    else:
        lang = 'in'

# topic = st.text_input('Add Topic', placeholder='')

# Select Input -> Parse Section
res = ''
keywords = None
text_input = ''

if genre == 'PDF':
    # pdf input section
    pdf = st.file_uploader(
        label="Upload your assignment PDF here.", type=['pdf'])

    if pdf != None:
        # function read pdf
        text_list = input.read_pdf(pdf)
        text = ''.join(str(e+'\n') for e in text_list)
        text_input = st.text_area("Your Question", value=text, height=400)

elif genre == 'Image':
    img = st.file_uploader(
        label="Upload your assignment image here.", type=['jpeg', 'jpg', 'png'])

    if img != None:
        img_val = img.getvalue()
        st.write('Your Image')
        st.image(image=img_val)
        text_list = input.read_image(img_val)
        text = ''.join(str(e+'\n') for e in text_list)
        text_input = st.text_area("Your Question", value=text, height=400)

else:
    # text input section
    text_input = st.text_area(
        "Copy and paste your assignment's question here.", height=400)

# Run Process
if st.button('Solve Question!') and text_input != '':
    with st.spinner('Processing...'):
        res, keywords = solve(text_input)
    st.success('Done!')

st.write('---')

# insight/output section
if res != '' and keywords != None:
    st.markdown('### Insights 🌟')
    st.write(res)

    st.markdown('#### Generated Keywords')
    st.write(str(keywords))
