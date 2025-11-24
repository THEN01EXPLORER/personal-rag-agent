"""
Document processing agent using Groq LLM and LangChain tools.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from langchain_groq import ChatGroq
from tools.document_tool import ingest_document, query_document

# Initialize Groq LLM (updated model name; ChatGroq expects 'model')
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Setup tools
tools = [ingest_document, query_document]

# System prompt for the agent
system_prompt = (
    "You are a helpful assistant. You can use two tools: ingest_document (to load a PDF) and query_document (to answer questions about previously ingested PDFs). "
    "When needed, think step by step. If you need to call a tool, respond with:\n"
    "Action: <tool name>\nAction Input: <input for tool>\n"
    "Otherwise, just answer the user directly. After you receive an Observation you must produce a Final Answer."
)

tool_map = {t.name: t for t in tools}


def run_agent(user_input: str) -> str:
    """
    Run the agent with user input.
    
    Args:
        user_input: The user's question or command
        
    Returns:
        The agent's response
    """
    try:
        # First LLM call
        response = llm.invoke([
            ("system", system_prompt),
            ("user", user_input)
        ])
        content = getattr(response, "content", str(response))

        if "Action:" in content and "Action Input:" in content:
            # Parse tool invocation
            lines = content.splitlines()
            action_line = next((l for l in lines if l.startswith("Action:")), "")
            input_line = next((l for l in lines if l.startswith("Action Input:")), "")
            tool_name = action_line.replace("Action:", "").strip()
            action_input = input_line.replace("Action Input:", "").strip()

            if tool_name not in tool_map:
                return f"Model requested unknown tool '{tool_name}'. Available: {list(tool_map.keys())}"

            observation = tool_map[tool_name].invoke(action_input)

            # Second LLM call with observation asking for final answer
            followup = llm.invoke([
                ("system", system_prompt),
                ("user", user_input),
                ("assistant", content),
                ("user", f"Observation: {observation}\nPlease provide Final Answer.")
            ])
            return getattr(followup, "content", str(followup))
        else:
            return content
    except Exception as e:
        return f"Error running agent loop: {e}"


if __name__ == "__main__":
    # Example usage
    print("Document Processing Agent")
    print("=" * 50)
    
    # Check if GROQ_API_KEY is set
    if not os.getenv('GROQ_API_KEY'):
        print("Warning: GROQ_API_KEY environment variable is not set!")
        print("Please set it before running the agent.")
    else:
        print("Agent initialized successfully!")
        print("\nExample commands:")
        print("1. Ingest a document: 'Load the PDF file at /path/to/document.pdf'")
        print("2. Query a document: 'What is the main topic discussed in the document?'")
        print("\n" + "=" * 50)
        
        # Interactive loop
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
            if not user_input:
                continue
                
            response = run_agent(user_input)
            print(f"\nAgent: {response}")
