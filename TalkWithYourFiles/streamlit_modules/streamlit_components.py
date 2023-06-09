import streamlit as st
from .streamlit_helper_functions import *

def setup_page_configurations():
    ##### PAGE CONFIGURATIONS
    st.set_page_config(
                    page_title="Talk With Your Files",
                    page_icon="random",
                    layout="wide", # centered or wide
                    initial_sidebar_state="collapsed", #auto, expanded, collapsed
                    menu_items={
                        'Get Help': 'https://github.com/Safakan',
                        'Report a bug': "https://github.com/Safakan/TalkWithYourFiles-LLM-GUI",
                        'About': "# This is a header. This is an *extremely* cool app!"
                        }
                    )


def setup_header_area():
    ##### HEADER
    st.header("Talk With Your Files")


def setup_sidebar(flow_coordinator):
    ##### SIDEBAR
    st.sidebar.header("Talk With Your Files")
    st.sidebar.write("Hello and welcome! I hope this helps you! <3")
    
    ##### Authorization box for OpenAI API KEY
    create_authorization_box(flow_coordinator)




def tab1_qa_chain_files(param_controller, flow_coordinator):
    """
    Main function to run the Streamlit interface and execute the run function from file_processor.
    This file follows the dependency inversion principle, and separates UI from backend functionalities:
    Streamlit framework is used to render the GUI and manage file uploads.
    To use other approaches or frameworks: 
    1) Make sure to set up a GUI that allows users to upload files & enter text input for their questions.
    2) Import the run method from the flow_coordinator.py
    3) Get the response by running the run(files, user_question) method with the appropriate arguments. 
    
    """
 


    ##### FILE UPLOADS
    files = st.file_uploader("Upload files", 
                            type=["pdf", "docx", "txt","csv"], 
                            accept_multiple_files=True
                            )



    ##### ADVANCED PARAMETERS SECTION
    with st.expander("Show Advanced Parameters?"):
        advanced_parameters_section(param_controller)



    ##### USER QUESTION INPUT
    user_question = st.text_input("Please ask me about your uploaded files and I shall help you: ")


    ##### QA CHAIN RUN BUTTON
    run_button_clicked = st.button("Run",
                                   use_container_width=True                                   
                                   )

    ##### START QA CHAIN
    if user_question and files and run_button_clicked:       
        response = flow_coordinator.run(files, user_question)
        st.write(response)





def tab2_active_params(param_controller):
    ## for testing purposes - to see the params in the UI as I change them.
    st.write(param_controller.parameters)







