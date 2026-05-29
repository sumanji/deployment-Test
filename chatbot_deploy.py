
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from model import  message_
from dotenv import load_dotenv

load_dotenv()
class ChatBot():
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o",temperature = 0 ,max_tokens=240)


    def get_prompt(self):
        prompt =(f"You are a helpful chat assistance . Your work is to answer question  in a polite manner and reply in below format"
                 )
        return prompt

    def get_output_(self):
        question = ""
        while question != "exit":
            question = input("Enter Your Question?")
            message = [SystemMessage(content=self.get_prompt()),
                       HumanMessage(content=question)
                       ]
            ai_message = self.llm.invoke(message)
            message.append(AIMessage(ai_message))

        return "Thank You"

    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

    def get_output(self,isfastAPI:bool=False,msg:message_={}):
        messages = [SystemMessage(content=self.get_prompt())]
        if isfastAPI:
            question = msg.question
            messages.append(HumanMessage(content=question))

            ai_message = self.llm.invoke(messages)
            msg.answer=ai_message.content
            return msg

        else:
            while True:
                question = input("Enter Your Question? ")

                if question.lower() == "exit":
                    break

                messages.append(HumanMessage(content=question))

                ai_message = self.llm.invoke(messages)
                print(ai_message.content)

                messages.append(ai_message)  # ✅ append directly

            return "Thank You"



