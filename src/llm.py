import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

def get_groq_llm(model_name: str="llama-3.1-8b-instant"):
    """
    Initialized and return a Groq Chat model
    
    """

    groq_api_key=os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    

    llm=ChatGroq(
        groq_api_key=groq_api_key,
        model=model_name,
        temperature=0.2,
        max_tokens=1000,
    )

    return llm


# test function

if __name__=="__main__":
    llm=get_groq_llm()
    # response=llm.invoke("explain langchain in 2 line.")
    # print("streaming response:")
    # for chunk in llm.stream("expian langchain in 2 lines"):
    #     full=chunk.content
    #     print(full)    
    # print(response.content)


    print("batch response:")

    responses=llm.batch([
        "explain langchain in 2 line.",
        "what is the capital of france?",
        "what is the capital of india?"
    ])

    for response in responses:
        print(response.content)