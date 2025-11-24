import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.document_tool import ingest_document, query_document

# Initialize Google Gemini model (align with main app)
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Tools
TOOLS = {"ingest_document": ingest_document, "query_document": query_document}

SYSTEM_PROMPT = (
    "You are a helpful assistant. Use tools when necessary by replying with:\n"
    "Action: <tool name>\nAction Input: <input>\nOtherwise answer directly."
)


def run_agent(user_input: str) -> str:
    response = llm.invoke([("system", SYSTEM_PROMPT), ("user", user_input)])
    content = getattr(response, "content", str(response))
    if "Action:" in content and "Action Input:" in content:
        lines = content.splitlines()
        action_line = next((l for l in lines if l.startswith("Action:")), "")
        input_line = next((l for l in lines if l.startswith("Action Input:")), "")
        tool = action_line.replace("Action:", "").strip()
        arg = input_line.replace("Action Input:", "").strip()
        if tool not in TOOLS:
            return f"Unknown tool: {tool}. Available: {list(TOOLS)}"
        obs = TOOLS[tool].invoke(arg)
        followup = llm.invoke([
            ("system", SYSTEM_PROMPT),
            ("user", user_input),
            ("assistant", content),
            ("user", f"Observation: {obs}\nPlease provide Final Answer.")
        ])
        return getattr(followup, "content", str(followup))
    return content


if __name__ == "__main__":
    while True:
        msg = input("You: ").strip()
        if not msg:
            continue
        if msg.lower() in {"exit", "quit", "q"}:
            break
        print("Agent:", run_agent(msg))
