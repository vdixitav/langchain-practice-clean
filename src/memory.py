# short term memry will remember the things within the sigle thread

# for short term memory to an agent need to add checkpointer while creating agent


# langgchai agents manages short term memory as a art of your agnet state



from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from src.llm import get_groq_llm
agent=create_agent(
    model=get_groq_llm(),
    tools=[],
    checkpointer=InMemorySaver()
)



# with short term memory , long conversation can also exceed llm contex : common solutions:trim messages(remove 1st to n messages), delete message: , summerized messages, costum statergy: filter


# long term memory: 


from dataclasses import dataclass

from langchain_core.runnables import RunnableConfig
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.store.memory import InMemoryStore


@dataclass
class Contex:
    user_id: str

store=InMemoryStore()
store.