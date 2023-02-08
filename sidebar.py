import streamlit as st


def sidebar():
    st.set_page_config(layout="wide", page_title="Assignment Automation")

    with st.sidebar:
        st.markdown("""
                    See my Github Profile!
                    
                    [![GitHub followers](https://img.shields.io/github/followers/caesariodito?style=social)](https://github.com/caesariodito)
                    
                    Star this repo!
                    
                    [![GitHub Repo stars](https://img.shields.io/github/stars/caesariodito/mp-assignment-automation?style=social)](https://github.com/caesariodito/mp-assignment-automation)
                    
                    Connect with me!
                    
                    [![Linkedin](https://img.shields.io/badge/linked-in-369?style=flat-square&logo=linkedin&logoColor=white&color=blue)](https://www.linkedin.com/in/caesariodito)
                    """)
