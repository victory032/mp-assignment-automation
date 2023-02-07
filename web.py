import sidebar
import streamlit as st
import input
from process import solve

st.title('Assignment Automation')


# intro section
st.markdown('## Introduction')
st.write("""
Assignment Automation offers answers to complex questions, saving users time and effort. You just need to input your question in pdf, image, or texts format and it will provide you a brief insights about the question.

Note: **This project is for educational purposes only and the generated output may not be correct. Use at your own risk ⚠️.**
""")

st.write('---')

col1, col2 = st.columns(2, gap="medium")

with col1:

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

    clicked = False
    # Run Process
    if st.button('Solve Question!') and text_input != '':
        res, keywords = solve(text_input)
        clicked = True
        st.success('Done!')

with col2:
    st.markdown('## Result Section')

    if clicked != True:
        st.write(
            'Please input your question on the left side to generate the result!')

    st.write('---')

    # insight/output section
    if res != '' and keywords != None:
        st.markdown('### Insights 🌟')
        st.write(res)

        st.markdown('#### Generated Keywords')
        st.write(str(keywords))
