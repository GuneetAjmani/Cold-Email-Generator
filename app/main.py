# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from datetime import datetime
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text
#
# def get_greeting():
#     """Get a greeting based on the time of day."""
#     current_hour = datetime.now().hour
#     if current_hour < 12:
#         return "Good morning"
#     elif 12 <= current_hour < 18:
#         return "Good afternoon"
#     else:
#         return "Good evening"
#
#
# def create_streamlit_app(llm, portfolio, clean_text):
#     """Main Streamlit app for Cold Email Generator."""
#     # Custom CSS for Styling
#     st.markdown("""
#         <style>
#             .header {
#                 font-size: 3em;
#                 color: #007ACC;
#                 text-align: center;
#                 font-family: 'Courier New', Courier, monospace;
#                 margin-bottom: 0.5em;
#             }
#             .subheader {
#                 text-align: center;
#                 font-family: 'Courier New', Courier, monospace;
#                 margin-bottom: 2em;
#             }
#             .greeting {
#                 text-align: center;
#                 font-size: 1.5em;
#                 margin-bottom: 2em;
#             }
#         </style>
#     """, unsafe_allow_html=True)
#
#     # Session state initialization
#     if 'username' not in st.session_state:
#         st.session_state['username'] = ''
#     if 'email_output' not in st.session_state:
#         st.session_state['email_output'] = ''
#
#     # Step 1: User enters their name
#     if not st.session_state['username']:
#         st.title("📧 Welcome to the Cold Email Generator")
#         st.session_state['username'] = st.text_input("Please enter your name:", key="username_input")
#         st.button("Submit", key="submit_name_button")
#     else:
#         # Step 2: Greeting and instructions
#         st.markdown('<div class="header">Cold Email Generator</div>', unsafe_allow_html=True)
#         greeting = get_greeting()
#         st.markdown(f'<div class="greeting">{greeting}, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
#         st.markdown('<div class="subheader">Enter a job URL to generate a personalized cold email.</div>', unsafe_allow_html=True)
#
#         # Step 3: URL Input and Email Generation
#         url_input = st.text_input("Enter a job URL:")
#         submit_button = st.button("Generate Email", key="submit_url_button")
#
#         if submit_button:
#             try:
#                 # Process the job URL and generate cold email
#                 loader = WebBaseLoader([url_input])
#                 data = clean_text(loader.load().pop().page_content)
#
#                 if not data:
#                     st.error("Failed to process the job description. Please check the URL.")
#                     return
#
#                 portfolio.load_portfolio()
#                 jobs = llm.extract_jobs(data)
#                 email_outputs = []
#
#                 for job in jobs:
#                     skills = job.get('skills', [])
#                     if not skills:
#                         st.warning("No skills were found for this job. Consider revising the URL.")
#                         continue
#
#                     links = portfolio.query_links(skills)
#                     email = llm.write_mail(job, links)
#                     email_outputs.append(email)
#
#                 if email_outputs:
#                     st.session_state['email_output'] = "\n\n---\n\n".join(email_outputs)
#                 else:
#                     st.warning("No emails could be generated. Please try another job URL.")
#
#             except Exception as e:
#                 st.error(f"An Error Occurred: {e}")
#
#         # Step 4: Display Generated Email
#         if st.session_state['email_output']:
#             st.subheader("Generated Cold Email")
#             st.code(st.session_state['email_output'], language='markdown')
#
#
# if __name__ == "__main__":
#     st.set_page_config(page_title="Cold Email Generator", layout="wide", page_icon="📧")
#     chain = Chain()
#     portfolio = Portfolio()
#     create_streamlit_app(chain, portfolio, clean_text)

# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from datetime import datetime
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text
#
#
# def get_greeting():
#     """Get a greeting based on the time of day."""
#     current_hour = datetime.now().hour
#     if current_hour < 12:
#         return "Good morning"
#     elif 12 <= current_hour < 18:
#         return "Good afternoon"
#     else:
#         return "Good evening"
#
#
# def create_streamlit_app(llm, portfolio, clean_text):
#     """Main Streamlit app for Cold Email Generator."""
#     # Custom CSS for Styling
#     st.markdown("""
#         <style>
#             .header {
#                 font-size: 3em;
#                 color: #007ACC;
#                 text-align: center;
#                 font-family: 'Courier New', Courier, monospace;
#                 margin-bottom: 0.5em;
#             }
#             .subheader {
#                 text-align: center;
#                 font-family: 'Courier New', Courier, monospace;
#                 margin-bottom: 2em;
#             }
#             .greeting {
#                 text-align: center;
#                 font-size: 1.5em;
#                 margin-bottom: 2em;
#             }
#             .success {
#                 background-color: #d4edda;
#                 color: #155724;
#                 padding: 10px;
#                 border-radius: 5px;
#                 text-align: center;
#                 font-size: 1em;
#             }
#         </style>
#     """, unsafe_allow_html=True)
#
#     # Sidebar content
#     with st.sidebar:
#         st.title("📧 Cold Email Generator")
#         st.write("Generate personalized cold emails for job applications.")
#         st.write("### How to Use:")
#         st.write("1. Enter your name.")
#         st.write("2. Paste a job URL.")
#         st.write("3. Click **Generate Email**.")
#         st.markdown("---")
#         st.write("### About the App:")
#         st.write("- **Purpose:** Create professional cold emails.")
#         st.write("- **Technologies:** LangChain, Streamlit.")
#         st.write("💡 Ensure the job URL contains a detailed description for best results.")
#
#     # Session state initialization
#     if 'username' not in st.session_state:
#         st.session_state['username'] = ''
#     if 'email_output' not in st.session_state:
#         st.session_state['email_output'] = ''
#
#     # Step 1: User enters their name
#     if not st.session_state['username']:
#         st.title("📧 Welcome to the Cold Email Generator")
#         st.session_state['username'] = st.text_input("Enter your name 👤:", key="username_input",
#                                                      placeholder="Your name")
#         st.button("Submit", key="submit_name_button")
#     else:
#         # Step 2: Greeting and instructions
#         st.markdown('<div class="header">Cold Email Generator</div>', unsafe_allow_html=True)
#         greeting = get_greeting()
#         st.markdown(f'<div class="greeting">{greeting}, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
#
#         col1, col2 = st.columns([2, 1])
#
#         with col1:
#             st.markdown('<div class="subheader">Paste a job URL to generate your email:</div>', unsafe_allow_html=True)
#             url_input = st.text_input("🔗 Job URL:", placeholder="https://example.com/job-posting")
#
#         with col2:
#             st.image("https://via.placeholder.com/150", caption="Your Branding", use_column_width=True)
#
#         submit_button = st.button("🚀 Generate Email", key="submit_url_button")
#
#         if submit_button:
#             try:
#                 with st.spinner("Analyzing job description and generating email..."):
#                     loader = WebBaseLoader([url_input])
#                     data = clean_text(loader.load().pop().page_content)
#
#                     if not data:
#                         st.error("Failed to process the job description. Please check the URL.")
#                         return
#
#                     portfolio.load_portfolio()
#                     jobs = llm.extract_jobs(data)
#                     email_outputs = []
#
#                     for job in jobs:
#                         skills = job.get('skills', [])
#                         if not skills:
#                             st.warning("No skills were found for this job. Consider revising the URL.")
#                             continue
#
#                         links = portfolio.query_links(skills)
#                         email = llm.write_mail(job, links)
#                         email_outputs.append(email)
#
#                     if email_outputs:
#                         st.session_state['email_output'] = "\n\n---\n\n".join(email_outputs)
#                         st.success("✅ Email generated successfully!")
#                     else:
#                         st.warning("No emails could be generated. Please try another job URL.")
#
#             except Exception as e:
#                 st.error(f"An Error Occurred: {e}")
#
#         # Step 4: Display Generated Email
#         if st.session_state['email_output']:
#             st.markdown('<div class="success">Here is your generated email:</div>', unsafe_allow_html=True)
#             st.code(st.session_state['email_output'], language='markdown')
#
#         st.markdown("---")
#         st.write("💡 Need help or have feedback? Contact us at [support@example.com](mailto:support@example.com).")
#
#
# if __name__ == "__main__":
#     st.set_page_config(page_title="Cold Email Generator", layout="wide", page_icon="📧")
#     chain = Chain()
#     portfolio = Portfolio()
#     create_streamlit_app(chain, portfolio, clean_text)

# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from datetime import datetime
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text
#
#
# def get_greeting():
#     """Get a greeting based on the time of day."""
#     current_hour = datetime.now().hour
#     if current_hour < 12:
#         return "Good morning"
#     elif 12 <= current_hour < 18:
#         return "Good afternoon"
#     else:
#         return "Good evening"
#
#
# def create_streamlit_app(llm, portfolio, clean_text):
#     """Main Streamlit app for Cold Email Generator."""
#     # Custom CSS for Styling
#     st.markdown("""
#         <style>
#             body {
#                 background: linear-gradient(120deg, #89f7fe, #66a6ff);
#                 font-family: 'Arial', sans-serif;
#             }
#             .header {
#                 font-size: 3em;
#                 color: #1f2937;
#                 text-align: center;
#                 margin-top: 0.5em;
#                 margin-bottom: 0.5em;
#                 font-weight: bold;
#             }
#             .subheader {
#                 font-size: 1.2em;
#                 color: #3b4d61;
#                 text-align: center;
#                 margin-bottom: 1.5em;
#             }
#             .greeting {
#                 font-size: 1.5em;
#                 color: #374151;
#                 text-align: center;
#                 margin-bottom: 2em;
#                 font-weight: bold;
#             }
#             .success-box {
#                 background-color: #d4edda;
#                 color: #155724;
#                 padding: 15px;
#                 border-radius: 8px;
#                 font-size: 1.1em;
#                 text-align: center;
#                 margin-top: 20px;
#             }
#             .error-box {
#                 background-color: #f8d7da;
#                 color: #721c24;
#                 padding: 15px;
#                 border-radius: 8px;
#                 font-size: 1.1em;
#                 text-align: center;
#                 margin-top: 20px;
#             }
#         </style>
#     """, unsafe_allow_html=True)
#
#     # Sidebar content
#     with st.sidebar:
#         st.image(
#             "https://via.placeholder.com/200",
#             caption="Your Branding",
#             use_column_width=True,
#         )
#         st.title("📧 Cold Email Generator")
#         st.write("Generate personalized cold emails for job applications.")
#         st.write("### Steps:")
#         st.write("1. Enter your name.")
#         st.write("2. Paste a job URL.")
#         st.write("3. Click **Generate Email**.")
#         st.markdown("---")
#         st.write("### Tips:")
#         st.write("- Ensure the URL contains a job description.")
#         st.write("- Use valid job links for accurate results.")
#
#     # Hero Section
#     st.markdown('<div class="header">Cold Email Generator</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subheader">Create professional emails effortlessly!</div>', unsafe_allow_html=True)
#
#     # Session state initialization
#     if 'username' not in st.session_state:
#         st.session_state['username'] = ''
#     if 'email_output' not in st.session_state:
#         st.session_state['email_output'] = ''
#
#     # Step 1: User enters their name
#     if not st.session_state['username']:
#         st.image(
#             "https://via.placeholder.com/600x200",
#             caption="Generate impactful cold emails for job applications!",
#         )
#         st.markdown('<div class="subheader">Please enter your name to get started.</div>', unsafe_allow_html=True)
#         st.session_state['username'] = st.text_input("Enter your name 👤:", placeholder="Your name")
#         st.button("Submit", key="submit_name_button")
#     else:
#         # Step 2: Greeting and instructions
#         greeting = get_greeting()
#         st.markdown(f'<div class="greeting">{greeting}, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
#
#         # Input section
#         col1, col2 = st.columns([2, 1])
#         with col1:
#             st.markdown('<div class="subheader">Paste a job URL to generate your email:</div>', unsafe_allow_html=True)
#             url_input = st.text_input("🔗 Job URL:", placeholder="https://example.com/job-posting")
#
#         with col2:
#             st.image(
#                 "https://via.placeholder.com/150",
#                 caption="Powered by AI",
#                 use_column_width=True,
#             )
#
#         # Generate Email Button
#         submit_button = st.button("🚀 Generate Email", key="submit_url_button")
#
#         # Process email generation
#         if submit_button:
#             try:
#                 with st.spinner("⏳ Generating your email..."):
#                     loader = WebBaseLoader([url_input])
#                     data = clean_text(loader.load().pop().page_content)
#
#                     if not data:
#                         st.markdown('<div class="error-box">❌ Failed to process the job description. Please check the URL.</div>', unsafe_allow_html=True)
#                         return
#
#                     portfolio.load_portfolio()
#                     jobs = llm.extract_jobs(data)
#                     email_outputs = []
#
#                     for job in jobs:
#                         skills = job.get('skills', [])
#                         if not skills:
#                             st.warning("No skills found for this job. Try another URL.")
#                             continue
#
#                         links = portfolio.query_links(skills)
#                         email = llm.write_mail(job, links)
#                         email_outputs.append(email)
#
#                     if email_outputs:
#                         st.session_state['email_output'] = "\n\n---\n\n".join(email_outputs)
#                         st.markdown('<div class="success-box">✅ Email generated successfully!</div>', unsafe_allow_html=True)
#                     else:
#                         st.warning("No emails generated. Please try another URL.")
#
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
#
#         # Step 4: Display Generated Email
#         if st.session_state['email_output']:
#             st.subheader("📩 Your Generated Email:")
#             st.code(st.session_state['email_output'], language='markdown')
#
#     # Footer
#     st.markdown("---")
#     st.write("💡 Need help or have feedback? Contact us at [support@example.com](mailto:support@example.com).")
#
#
# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Cold Email Generator",
#         layout="wide",
#         page_icon="📧",
#     )
#     chain = Chain()
#     portfolio = Portfolio()
#     create_streamlit_app(chain, portfolio, clean_text)

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from datetime import datetime
from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def get_greeting():
    """Get a greeting based on the time of day."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def create_streamlit_app(llm, portfolio, clean_text):
    """Main Streamlit app for Cold Email Generator."""
    # Custom CSS for Styling
    st.markdown("""
        <style>
            body {
                background: linear-gradient(to right, #f9f9f9, #e3f2fd);
                font-family: 'Arial', sans-serif;
            }
            .header {
                font-size: 2.8em;
                color: #0d47a1;
                text-align: center;
                margin-top: 0.5em;
                margin-bottom: 0.5em;
                font-weight: bold;
                text-shadow: 1px 1px 2px #b3e5fc;
            }
            .subheader {
                font-size: 1.2em;
                color: #1e88e5;
                text-align: center;
                margin-bottom: 1.5em;
            }
            .button {
                background-color: #1976d2;
                color: white;
                padding: 10px 20px;
                font-size: 1em;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            }
            .button:hover {
                background-color: #1565c0;
            }
            .input-box {
                border: 1px solid #bbdefb;
                border-radius: 8px;
                padding: 10px;
                margin-bottom: 1em;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            }
            .success-box {
                background-color: #d4edda;
                color: #155724;
                padding: 15px;
                border-radius: 8px;
                font-size: 1.1em;
                text-align: center;
                margin-top: 20px;
            }
            .error-box {
                background-color: #f8d7da;
                color: #721c24;
                padding: 15px;
                border-radius: 8px;
                font-size: 1.1em;
                text-align: center;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Content
    with st.sidebar:
        st.image(
            "https://via.placeholder.com/200",
            caption="Brand Logo",
            use_column_width=True,
        )
        st.title("📧 Cold Email Generator")
        st.markdown("""
            Generate personalized cold emails for job applications.
            ### Steps:
            1. Enter your name.
            2. Paste a job URL.
            3. Click **Generate Email**.
        """)
        st.markdown("---")
        st.markdown("""
            💡 Tips:
            - Ensure the URL contains a job description.
            - Use valid job links for accurate results.
        """)

    # Hero Section
    st.markdown('<div class="header">Cold Email Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Create professional emails effortlessly!</div>', unsafe_allow_html=True)

    # Initialize Session State
    if 'username' not in st.session_state:
        st.session_state['username'] = ''
    if 'email_output' not in st.session_state:
        st.session_state['email_output'] = ''

    # Step 1: User enters their name
    if not st.session_state['username']:
        st.markdown('<div class="subheader">Please enter your name to get started.</div>', unsafe_allow_html=True)
        st.session_state['username'] = st.text_input(
            "👤 Enter your name:",
            placeholder="John Doe",
            help="Your name will be used to personalize the email."
        )
        if st.button("Submit", key="submit_name_button", use_container_width=True):
            st.experimental_rerun()
    else:
        # Step 2: Greeting and Instructions
        greeting = get_greeting()
        st.markdown(f'<div class="greeting">{greeting}, {st.session_state["username"]}!</div>', unsafe_allow_html=True)

        # Input Section with Layout
        col1, col2 = st.columns([2, 1])
        with col1:
            st.text_input(
                "🔗 Job URL:",
                key="url_input",
                placeholder="Paste the job posting link here...",
                help="Enter a URL with a detailed job description.",
                label_visibility="visible",
                on_change=None
            )
        with col2:
            st.image(
                "https://via.placeholder.com/150",
                caption="Powered by AI",
                use_column_width=True,
            )

        if st.button("🚀 Generate Email", key="submit_url_button", use_container_width=True):
            try:
                with st.spinner("⏳ Analyzing job description and generating email..."):
                    loader = WebBaseLoader([st.session_state.get("url_input")])
                    data = clean_text(loader.load().pop().page_content)

                    if not data:
                        st.markdown('<div class="error-box">❌ Failed to process the job description. Please check the URL.</div>', unsafe_allow_html=True)
                        return

                    portfolio.load_portfolio()
                    jobs = llm.extract_jobs(data)
                    email_outputs = []

                    for job in jobs:
                        skills = job.get('skills', [])
                        if not skills:
                            st.warning("No skills found for this job. Try another URL.")
                            continue

                        links = portfolio.query_links(skills)
                        email = llm.write_mail(job, links)
                        email_outputs.append(email)

                    if email_outputs:
                        st.session_state['email_output'] = "\n\n---\n\n".join(email_outputs)
                        st.markdown('<div class="success-box">✅ Email generated successfully!</div>', unsafe_allow_html=True)
                    else:
                        st.warning("No emails generated. Please try another URL.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

        # Step 4: Display Generated Email
        if st.session_state['email_output']:
            st.subheader("📩 Your Generated Email:")
            st.code(st.session_state['email_output'], language='markdown')

    # Footer
    st.markdown("---")
    st.write("💡 Need help or have feedback? Contact us at [support@example.com](mailto:support@example.com).")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Cold Email Generator",
        layout="wide",
        page_icon="📧",
    )
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)



