from langchain.chat_models import ChatGroq
from langchain.agents import initialize_agent
from tools.document_tool import ingest_document, query_document

# Initialize ChatGroq model (updated model name; use 'model' parameter)
groq_model = ChatGroq(model="llama-3.3-70b-versatile")

# Load tools
tools = [ingest_document, query_document]

# Create ReAct agent
agent = initialize_agent(tools, groq_model, agent_type="react", prompt="hwchase17/react")

# Simple loop for user input
while True:
    user_input = input("You: ")
    response = agent(user_input)
    print(f"Agent: {response}")