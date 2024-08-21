import streamlit as st

st.title("EchoBot")

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#react to user input
if prompt := st.chat_input("What is up? "):
    #Display user message in chat container
    st.chat_message("user").markdown(prompt)
    #Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    #Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


#DE ACÁ PARA ABAJO COPIÉ A MEDIAS EL AGENTE QUE ESTABA COMPARTIENDO:

tools = [TavilySearchResults(max_results=3)]


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

#Define the function that determines wether to continue the chat or not
def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    #If theere are no tool calls, then we finish the chat
    if not last_message.tool_calls:
        return "end"
    #Otherwise, we continue the chat
    else: 
        return "continue"








