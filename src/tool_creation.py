from langchain.tools import tool


@tool
def sum_numbers(a:int,b:int) ->int:
    """add two numbers"""
    return a+b
