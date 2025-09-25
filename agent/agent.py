import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from agent.tools import web_search
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompts.system import system_prompt
from dotenv import load_dotenv
load_dotenv()

class PostlyAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
        self.tools = [web_search]
    def create_agent(self):
        agent = create_react_agent(
            model=self.llm,
            tools=self.tools,
            prompt=system_prompt
        )
        return agent
    def get_response(self, user_input: str) -> str:
        agent = self.create_agent()
        response = agent.invoke({"messages":[{"role":"user","content":user_input}]})
        return response
agent = PostlyAgent()

def generate_lp_json_output(topic:str):
    user_input = topic
    response = agent.get_response(user_input)
    final_response = response["messages"][-1]
    final_content = final_response.content
    clean_content = (
        final_content.strip()
        .removeprefix("```json")
        .removeprefix("```")
        .removesuffix("```")
        .strip()
    )
    data = json.loads(clean_content)
    return data


if __name__ == "__main__":
    agent = PostlyAgent()
    user_input = "Write a LinkedIn post about the latest advancements in AI technology."
    response = agent.get_response(user_input)
    final_response = response["messages"][-1]
    final_content = final_response.content
    print(final_content)
    print(type(final_content))
    clean_content = (
        final_content.strip()
        .removeprefix("```json")
        .removeprefix("```")
        .removesuffix("```")
        .strip()
    )

    with open("output.json", "w") as f:
        data = json.loads(clean_content)
        json.dump(data, f, indent=2)

