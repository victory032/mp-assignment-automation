import sidebar
import streamlit as st
import input
from process import solve

sidebar.sidebar()

st.title('Assignment Automation')

# intro section
st.markdown('## Introduction')
st.write("""
Assignment Automation offers answers to complex questions, saving users time and effort. You just need to input your question in pdf, image, or texts format and it will provide you a brief insights about the question.

Note: **This project is for educational purposes only and the generated output may not be correct. Use at your own risk ⚠️.**
""")

st.write('---')

st.markdown('## Input your OpenAI API')
st.write("""
         1. Go to https://platform.openai.com/account/api-keys, register if you haven't
         2. Generate new secret key
         3. Save and paste it here
         """)
st.text('I will not store or even use your API Key.')

api_key = st.text_input('API SECRET KEY: ', type='password')

st.write('----')

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
    text = ''
    file = None
    clicked = False

    if genre == 'PDF':
        # pdf input section
        file = st.file_uploader(
            label="Upload your assignment PDF here.", type=['pdf'])

        if file != None:
            # function read pdf
            text_list = input.read_pdf(file)
            text = ''.join(str(e+'\n') for e in text_list)

    elif genre == 'Image':
        file = st.file_uploader(
            label="Upload your assignment image here.", type=['jpeg', 'jpg', 'png'])

        if file != None:
            img_val = file.getvalue()
            st.write('Your Image')
            st.image(image=img_val)
            text_list = input.read_image(img_val)
            text = ''.join(str(e+'\n') for e in text_list)

    # disabled the button
    st.session_state.disabled = True

    if file != None or genre == 'Text':
        text_input = st.text_area("Your Question", value=text, height=400)
        # Run Process
        if text_input != '' and api_key != '':
            st.session_state.disabled = False

    st.text("Please fill 'Your Question' and 'API SECRET KEY' to continue.")
    solve_button = st.button(
        'Solve Question!', key='but_solve', disabled=st.session_state.get('disabled'))

    if solve_button and text_input != '':
        res, keywords = solve(text_input, api_key)
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
