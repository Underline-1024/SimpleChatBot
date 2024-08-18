from typing import List

from langchain_ollama import ChatOllama
#from typing_extensions import TypedDict

class ToolCall():
    def __init__(self,function,model="llama3-groq-tool-use",temperature=0):
        self.model=model
        self.temperature=temperature
        self.function=function
        self.llm = ChatOllama(
        model=self.model,
        temperature=temperature,
        ).bind_tools([self.function])
    def calling(self,input_):
        input_=input_.replace("##function\_calling","")
        self.result = self.llm.invoke(
            input_
        )
        return self.result.tool_calls