import streamlit as st
import os
from Tool.llm_comp import llm_deploy_run
from Tool.utils import is_valid_openai_api_key
import openai

# Config
about = "JobScanGPT is an LLM-based application designed to help users streamline the process of analyzing job descriptions. \
By scanning the provided job description, the app extracts key information, saving time and enhancing efficiency. :hourglass_flowing_sand:"

st.set_page_config(
    page_title="JobScanGPT",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yuting1214/JobScanGPT',
        'Report a bug': "https://github.com/yuting1214/JobScanGPT/issues",
        'About': about
    }
)

# Layout 
container1 = st.container()
## Main page
container1.title("JobScanGPT")
container1.write("""
Simplify your job search by extracting the core requirements of any job description.
""")

container2 = st.container()
cols = container2.columns(2)
cols[0].subheader('Result:')
cols[1].subheader('Cost:')

## Sidebar
### API key setting
# Load API
openai_api_key = os.getenv("OPENAI_API_KEY")
api_key_provided = openai_api_key is not None

if not api_key_provided:
    openai_api_key = st.sidebar.text_input(
        """Enter your OpenAI API Key: 
        [(click here to get a new key if you do not have one)](https://platform.openai.com/account/api-keys)""",
        type="password",
    )
    if openai_api_key:
        spinner = st.sidebar.empty()
        with st.spinner('Key Verifying...'):
            if is_valid_openai_api_key(openai_api_key):
                openai.api_key = openai_api_key
                st.sidebar.success('API key is valid!')
                api_key_provided = True
            else:
                st.sidebar.error('Incorrect API key provided')
                openai_api_key = None

### User Input
st.sidebar.header('User Input: 👇')
model_name = st.sidebar.selectbox('How would you like the LLM?',('GPT-3.5',))
role_name = st.sidebar.selectbox('What role are you looking for?',('Data relevant', 'Software Engineer', 'General', ))
user_message = st.sidebar.text_area('Provide a job description', '')
if st.sidebar.button('Submit'):
    with st.spinner('Processing...'):
        response, info = llm_deploy_run(model_name, role_name, user_message)
        cost = round(response['cost'], 4)
        if info == None:
            del response['cost']
            cols[0].write(response)
            cols[0].markdown("""
                * Years of Experience Level is categorized into four groups:
                    * [New grad]: Under one year of experience.
                    * [Mid-level]: Professional with 1 to 3 years of experience.
                    * [Senior]: Professional with more than 3 years of experience.
                    * [not mentioned]: If this requirement is not specified in the job description.
                            """)
        elif info == 'flagged':
            cols[0].write('The input is not appropriate!')
        elif info == 'not_job':
            cols[0].write('The input is not a job description.')
        elif info == 'not_json':
            cols[0].write('Somthing wrong with LLM.')
        else:
            cols[0].write(info)
        cols[1].write(str(cost)+'💲')
else:
    cols[0].write('Wait for input.')

### Note
st.sidebar.markdown('''
* English language supported only.
* Refreshing the app requires re-submitting the API key for security.
* Input and output data are not stored; see Github for data storage options.
* Expect a 5-second delay for output due to network latency.
                    ''')
st.sidebar.markdown('''[GitHub Repo](https://github.com/yuting1214/JobScanGPT)''', unsafe_allow_html=True)