import streamlit as st

# Set background color for the entire page
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container for the title and image in the same row
title_container = st.container()
with title_container:

    # Apply background color, border, and left alignment to the title container
    title_container.markdown(
        """
        <style>
            div.stContainer {
                background-color: #3498db; /* Specify your desired background color */
                border: 2px solid #2c3e50; /* Specify your desired border color and thickness */
                border-radius: 10px; /* Specify your desired border radius */
                padding: 10px; /* Specify your desired padding */
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: flex-start;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("test-ops-no-arrow.png", width=100)
    with col2:
        st.markdown(
            "<h1 style='text-align: left; color: #ecf0f1; margin-top: 0;'>TestOps Dashboard</h1>", unsafe_allow_html=True)

# Create a sidebar with options
selected_option = st.sidebar.radio(
    "", ['Process Mining', 'Test AI', 'PACT'])

# Display content based on the selected option
if selected_option == 'Process Mining':
    st.write("Welcome to Process Mining section. This is where you can analyze and optimize your processes.")

elif selected_option == 'Test AI':
    st.write(
        "Explore the Test AI section for advanced testing capabilities powered by AI.")

elif selected_option == 'PACT':
    st.write("PACT section provides insights into Pact testing for ensuring contract-driven API development.")

# Q1: What specific functionalities or information would you like to include in each section (Process Mining, Test AI, PACT)?
# Q2: Do you have any specific data sources or APIs you want to integrate into the dashboard for real-time information?
# Q3: Are there any specific design or layout preferences you have for the dashboard?
