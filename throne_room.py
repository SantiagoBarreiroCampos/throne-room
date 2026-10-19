# -*- coding: utf-8 -*-
"""
Main file to comunicate with the agents.
"""
from king import King

if __name__ == '__main__':
    # This is how you will talk to the king to ask for a request
    request = input("User: ")  # Example: "Hello my king. I want to make a simple loop in python to count from 1 to 10"
    king_in_the_throne = King()
    response = king_in_the_throne.run(request)

    print(response["messages"][-1].content)