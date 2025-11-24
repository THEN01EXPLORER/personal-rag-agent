from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor

class RAGChain:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
        self.prompt_template = PromptTemplate(
            input_variables=["input"],
            template="You are a helpful assistant. Answer the following question: {input}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def run(self, input_text):
        response = self.chain.run(input_text)
        return response

    def execute_agent(self, user_input):
        agent_executor = AgentExecutor(agent=self.llm, tools=self.tools)
        result = agent_executor.run(user_input)
        return result