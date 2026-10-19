# -*- coding: utf-8 -*-
"""
First AI agent to test LangChain capabilities
"""
from langchain.agents import create_agent
from langchain.messages import HumanMessage


class BlackSmith:
    def __init__(self):
        self.agent = create_agent(
            model="ollama:qwen3:8b",
            system_prompt="You are a helpful coding assistant. Respond only with the coding lines."
        )

    def run(self, message: str):
        print("Blacksmith is working on his tasks")
        response = self.agent.invoke(
            {"messages": [
                HumanMessage(content=message)
            ]}
        )
        return response