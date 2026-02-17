# from langchain.tools import tool


# @tool
# def sum_numbers(a:int,b:int) ->int:
#     """add two numbers"""
#     return a+b


# # customised tool


# @tool("web_search")
# def search(query: str) -> str:
#     """you are searching the information"""

#     return f"serachung {query} on the web"

# print(search.name)




# @tool("dixitha")
# def dixitha_tool(query:str)-> str:
#     "you are very smart and honest person"

#     return f"you are searching {query} on the web"
# print(dixitha_tool.name)
# print(dixitha_tool.description)
# print(dixitha_tool.func)


from langchain.tools import tool,ToolRuntime
from langchain.messages import HumanMessage

@tool("user_info")
def user_info(runtime: ToolRuntime) -> str:
    "get the most recent message from user"
    messages=runtime.state["messages"]


# update stae: use cammnad to update state/ reducer
# 
from langchain.types import command    



# tool_node :  rebuild node that execute tool from langgraph. it handles parelel execution, error handing, state injection auttomatically



from langchain.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, MessagesState, START, END


@tool
def 


# route with tool_condition


from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph, MessagesState, START, END


builder=StateGraph(MessagesState)
builder.add_node(START)