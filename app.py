import streamlit as st

from agent.agent import policy_agent
from agent.dependencies import get_dependencies


st.set_page_config(
    page_title="Nimbus HR & IT Policy Assistant",
    page_icon="🤖",
)

st.title("🤖 Nimbus HR & IT Policy Assistant")
st.write(
    "Ask questions about company HR and IT policies."
)

# Initialize dependencies only once
if "deps" not in st.session_state:
    st.session_state.deps = get_dependencies()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask your question..."):

    # Display user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Generate response
    with st.spinner("Searching policy documents..."):

        result = policy_agent.run_sync(
            prompt,
            deps=st.session_state.deps,
        )

        response = result.output

    # Display assistant response
    st.chat_message("assistant").markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )