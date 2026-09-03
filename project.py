import streamlit as st
import google.generativeai as genai

# Use your own Google Gemini API key as an environment variable
GOOGLE_API_KEY = st.secrets("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title='Ai Flash Card Generator',layout='wide')

st.header('AI Flash Card Generator')

st.subheader('Generative AI Project-Flash Card Generator')

notes = st.text_area('Enter the text here',height=100)

st.markdown(notes)

if st.button('Generate Flash Cards'):
    if notes.strip():
        try:
            with st.spinner('Generating Flash Cards...'):
                prompt = f"""as a prompt engineer generate only 5 flash cards for the following topic along with question and answer.
                Notes:
                {notes}
                Please format the output as following:
                Q1: [Question]\n
                new line
                A1: [Answer]
                ---
                """

            model = genai.GenerativeModel('gemini-3.6-flash')
            response = model.generate_content(prompt)

            for line in response.text.splitlines():
                line = line.strip()

                if line.startswith("Q"):
                    st.markdown(f"**{line}**")
                elif line.startswith("A"):
                    st.markdown(line)
        except Exception as e:
            st.error(f'Error Generating the Response:{str(e)}')
    else:
        st.warning('Enter the text')


