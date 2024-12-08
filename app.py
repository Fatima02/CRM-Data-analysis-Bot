# import streamlit as st
# #from dotenv import load_dotenv
# import pandas as pd
# import os

# # Load environment variables from the .env file
# #load_dotenv()

# # Get API key from the environment variables
# openai_api_key = st.secrets["OPENAI_API_KEY"]  # Assuming the key is securely stored in Streamlit secrets

# # Initialize session state if it doesn't already exist
# if 'history' not in st.session_state:
#     st.session_state.history = []  # Store conversation history as a list

# def chat_with_csv(df, prompt):
#     # Importing PandasAI and related classes inside the function to avoid circular import issues
#     from pandasai.smart_dataframe import SmartDataframe
#     from pandasai.llm.openai import OpenAI
    
#     # Initialize the LLM (Language Learning Model) with the API key
#     llm = OpenAI(api_token=openai_api_key)
    
#     # Initialize PandasAI with the LLM
#     # Convert the DataFrame to a SmartDataframe with LLM
#     smart_df = SmartDataframe(df, config={"llm": llm})
    
#     # Run the LLM on the dataframe with the given prompt using the chat() method
#     result = smart_df.chat(prompt)  # Use chat() directly as shown in the example
    
#     return result


# st.set_page_config(layout='wide')

# st.title("CRM Chatbot")
# st.write("You can ask anything about your data in our Company")

# # File uploader to upload the CSV
# input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

# if input_csv is not None:
#     # Split into two columns for UI
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         st.info("CSV Uploaded Successfully")
#         data = pd.read_csv(input_csv)
#         with st.expander("🔎 Dataframe Preview"):
#             st.write(data.tail(3))

#     with col2:
#         st.info("Chat Below")
        
#         # Text area for user to input their query
#         input_text = st.text_area("Enter your query")
#         with st.spinner(text="Loading the reply – hang tight! This should take 1-2 minutes."):
#             if input_text:
#                 if st.button("Chat with CSV"):
#                     # Display user query in the conversation history
#                     st.session_state.history.append(f"You: {input_text}")
                    
#                     # Get response from the model
#                     result = chat_with_csv(data, input_text)
                    
#                     # Append the response to the conversation history
#                     st.session_state.history.append(f"Bot: {result}")
                    
#                     # Display the conversation history
#                     for message in st.session_state.history:
#                         st.write(message)
# ....................................................................................................
# import streamlit as st
# import pandas as pd

# # Load environment variables from Streamlit secrets
# openai_api_key = st.secrets["OPENAI_API_KEY"]

# # Initialize session state for conversation history and data
# if 'history' not in st.session_state:
#     st.session_state.history = []  # Store conversation history
# if 'data' not in st.session_state:
#     st.session_state.data = None  # Store uploaded data

# def chat_with_csv(df, prompt):
#     from pandasai.smart_dataframe import SmartDataframe
#     from pandasai.llm.openai import OpenAI
    
#     llm = OpenAI(api_token=openai_api_key)
#     smart_df = SmartDataframe(df, config={"llm": llm})
#     result = smart_df.chat(prompt)
#     return result

# # Page configuration
# st.set_page_config(page_title="CRM Chatbot", layout="wide")

# # Sidebar for file upload
# st.sidebar.title("Upload Your CSV")
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# # Load the data if a file is uploaded
# if uploaded_file is not None:
#     st.session_state.data = pd.read_csv(uploaded_file)
#     st.sidebar.success("File uploaded successfully!")
#     with st.sidebar.expander("🔎 Data Preview"):
#         st.write(st.session_state.data.head(3))

# # Main chat interface
# st.title("CRM Chatbot")
# st.write("Upload your CSV file and start asking questions about your data.")

# if st.session_state.data is not None:
#     # Display chat history in a container
#     chat_container = st.container()

#     # Display conversation history
#     with chat_container:
#         for message in st.session_state.history:
#             if message.startswith("You:"):
#                 st.markdown(f"**{message}**")
#             else:
#                 st.markdown(f"_{message}_")

#     # Bottom text input area with send button
#     with st.container():
#         input_col1, input_col2 = st.columns([8, 1])
#         with st.form("chat_form", clear_on_submit=True):
#             user_input = input_col1.text_input("Enter your query", key="user_input", placeholder="Ask your question here...")
#             send_button = input_col2.form_submit_button("Send")

#         if send_button and user_input.strip():
#             # Append user query to the chat history
#             st.session_state.history.append(f"You: {user_input.strip()}")
            
#             # Generate response from the CSV
#             with st.spinner("Processing your query..."):
#                 try:
#                     response = chat_with_csv(st.session_state.data, user_input.strip())
#                     st.session_state.history.append(f"Bot: {response}")
#                 except Exception as e:
#                     st.session_state.history.append(f"Bot: Error - {str(e)}")
            
# else:
#     st.info("Please upload a CSV file to start chatting.")
# #######################################################################
# import streamlit as st
# import pandas as pd

# # Load environment variables from Streamlit secrets
# openai_api_key = st.secrets["OPENAI_API_KEY"]

# # Initialize session state for conversation history and data
# if 'history' not in st.session_state:
#     st.session_state.history = []  # Store conversation history
# if 'data' not in st.session_state:
#     st.session_state.data = None  # Store uploaded data

# def chat_with_csv(df, prompt):
#     from pandasai.smart_dataframe import SmartDataframe
#     from pandasai.llm.openai import OpenAI
    
#     llm = OpenAI(api_token=openai_api_key)
#     smart_df = SmartDataframe(df, config={"llm": llm})
#     result = smart_df.chat(prompt)
#     return result

# # Page configuration
# st.set_page_config(page_title="CRM Chatbot", layout="wide")

# # Sidebar for file upload
# st.sidebar.title("Upload Your CSV")
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# # Load the data if a file is uploaded
# if uploaded_file is not None:
#     st.session_state.data = pd.read_csv(uploaded_file)
#     st.sidebar.success("File uploaded successfully!")
#     with st.sidebar.expander("🔎 Data Preview"):
#         st.write(st.session_state.data.head(3))

# # Main chat interface
# st.title("CRM Chatbot")
# st.write("Upload your CSV file and start asking questions about your data.")

# if st.session_state.data is not None:
#     # Display chat history in a container
#     chat_container = st.container()

#     # Display conversation history
#     with chat_container:
#         for message in st.session_state.history:
#             if message.startswith("You:"):
#                 st.markdown(f"**{message}**")
#             else:
#                 st.markdown(f"_{message}_")

#     # Bottom text input area with send button
    
#     with st.container():
#         # Create a single form that includes both the text input and the submit button
#         with st.form("chat_form", clear_on_submit=False):  # Unique form key for input
#             input_col1, input_col2 = st.columns([8, 1])

#             # Input text field inside the form
#             with input_col1:
#                 user_input = st.text_input("Enter your query", key="user_input", placeholder="Ask your question here...")

#             # Submit button inside the form
#             with input_col2:
#                 send_button = st.form_submit_button("Send")

#             # Form submission logic
#             if send_button and user_input.strip():
#                 # Append user query to the chat history
#                 st.session_state.history.append(f"You: {user_input.strip()}")
#             # Generate response from the CSV
#                 with st.spinner("Processing your query..."):
#                     try:
#                         response = chat_with_csv(st.session_state.data, user_input.strip())
#                         st.write(response)
#                         st.session_state.history.append(f"Bot: {response}")
                        
#                         # Clear the input field after displaying the response
#                         st.session_state.user_input = ""  # This will clear the input box

#                     except Exception as e:
#                         st.session_state.history.append(f"Bot: Error - {str(e)}")
            
# else:
#     st.info("Please upload a CSV file to start chatting.")
# ===========================================================================================
import streamlit as st
import pandas as pd

# Load environment variables from Streamlit secrets
openai_api_key = "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"

# Initialize session state for conversation history and data
if 'history' not in st.session_state:
    st.session_state.history = []  # Store conversation history
if 'data' not in st.session_state:
    st.session_state.data = None  # Store uploaded data

def chat_with_csv(df, prompt):
    from pandasai.smart_dataframe import SmartDataframe
    from pandasai.llm.openai import OpenAI
    
    llm = OpenAI(api_token=openai_api_key)
    smart_df = SmartDataframe(df, config={"llm": llm})
    result = smart_df.chat(prompt)
    return result

# Page configuration
st.set_page_config(page_title="CRM Chatbot", layout="wide")

# Sidebar for file upload
st.sidebar.title("Upload Your CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Load the data if a file is uploaded
if uploaded_file is not None:
    st.session_state.data = pd.read_csv(uploaded_file)
    st.sidebar.success("File uploaded successfully!")
    with st.sidebar.expander("🔎 Data Preview"):
        st.write(st.session_state.data.head(3))

# Main chat interface
st.title("CRM Chatbot")
st.write("Upload your CSV file and start asking questions about your data.")

if st.session_state.data is not None:
    # Use containers to create separate areas for rows
    with st.container():  # First container for the file upload and input area
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_input("Enter your query", key="user_input", placeholder="Ask your question here...")

            send_button = st.form_submit_button("Send")

            # Form submission logic
            if send_button and user_input.strip():
                # Append user query to the chat history
                st.session_state.history.append(f"You: {user_input.strip()}")

                # Generate response from the CSV
                with st.spinner("Processing your query..."):
                    try:
                        response = chat_with_csv(st.session_state.data, user_input.strip())
                        
                        # Append bot's response to the history
                        st.session_state.history.append(f"Bot: {response}")
                        
                    except Exception as e:
                        st.session_state.history.append(f"Bot: Error - {str(e)}")

    # Second container for displaying conversation history
    with st.container():
        for message in st.session_state.history:
            if message.startswith("You:"):
                st.markdown(f"**{message}**")  # Display user query
            else:
                st.markdown(f"_{message}_")  # Display bot response

else:
    st.info("Please upload a CSV file to start chatting.")
