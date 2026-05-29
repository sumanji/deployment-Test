from fastapi import FastAPI
from model import  message_
from chatbot_deploy import ChatBot
app = FastAPI()

cb = ChatBot()


@app.get("/")
def test_hello():
    return  {'Status':'ok'}

@app.post("/chat")
def chat(msg:message_):
    return cb.get_output(isfastAPI=True,msg=msg)