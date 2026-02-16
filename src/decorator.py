# def decorator(func):
#     def wrapper():
#         print("before calling function")

#         func()
#         print("after calling function")

#     return wrapper

# @decorator
# def greet():
#     print("hello word")

# greet()    



# PII middleware

from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain.agents.middleware import HumanInTheLoopMiddleware
agnet=create_agent(

    model=model,
    tool=[customer_service_tool,email_tool]
    middleware=PIIMiddleware(email,
                             statergr="redact,"
                             )



    
    )


    agent=create_agent(
        model="",
        tool=[],
        middleware=[
            HumanInTheLoopMiddleware(
                
            )
        ]
    )
