from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent import generate_lp_json_output
from mangum import Mangum

app = FastAPI()
class TopicRequest(BaseModel):
    topic:str

@app.post("/generate_post")
def generate_post(request: TopicRequest):
    topic = request.topic
    result = generate_lp_json_output(topic)
    return result
handler = Mangum(app)