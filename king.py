# -*- coding: utf-8 -*-
"""
Orchestrator AI agent to test LangChain capabilities
"""
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from blacksmith import BlackSmith
from langchain.tools import tool

@tool
def call_blacksmith(message: str) -> str:
    """Call blacksmith subagent to generate code"""
    print("King is calling the blacksmith")
    blacksmith = BlackSmith()
    return blacksmith.run(message)

class King:
    def __init__(self):
        self.agent = create_agent(
            model="ollama:qwen3:8b",
            tools=[call_blacksmith],
            system_prompt="You are a helpful assistant roleplaying as a king in a castle. "
                          "Delegate all tasks to your subordinates when their capabilities adjust to it. "
                          "You have to talk as if you were a king in court but only to the user."
        )

    def run(self, message: str):
        print("King is working on his tasks")
        response = self.agent.invoke(
            {"messages": [
                HumanMessage(content=message)
            ]}
        )
        return response
