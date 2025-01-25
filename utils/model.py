from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class ReplyModel:
    def __init__(self):
        self.template = """
            Answer the question below

            Here is conversation history : {context}

            Question = {question}


            Answer:
        """

        self.model = OllamaLLM(model="llama3:8b")
        self.prompt = ChatPromptTemplate.from_template(template=self.template)
        self.chain = self.prompt | self.model
        self.context = ""

    def reply(self, listened_text):
        input_data = {"context": self.context, "question": listened_text}
        result = self.chain.invoke(input=input_data)
        self.context += f"/nUser: {listened_text}/n AI:{result}"
        return result
