from dotenv import load_dotenv
load_dotenv('D:/capstone/.env')
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model='gemini-flash-latest', temperature=0)
resp = llm.invoke([('user','Say OK')])
print('OK:', getattr(resp,'content',str(resp))[:60])
