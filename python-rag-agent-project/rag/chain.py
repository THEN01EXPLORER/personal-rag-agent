from langchain_core.prompts import PromptTemplate

class RAGChain:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
        self.prompt_template = PromptTemplate(
            input_variables=["input"],
            template="You are a helpful assistant. Answer the following question: {input}"
        )

    def run(self, input_text: str):
        prompt = self.prompt_template.format(input=input_text)
        result = self.llm.invoke(prompt)
        return getattr(result, "content", str(result))

    def execute_agent(self, user_input: str):
        # Minimal passthrough to LLM; tool wiring would be added here if needed
        return self.run(user_input)