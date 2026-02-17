from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware,human_in_the_loop

agent=create_agent(
    middleware=[

        SummarizationMiddleware(...),
        human_in_the_loop(...)
    ]
)


## the agent loop

#core agent loop involve calling a model, letting it decide tool, teh finish
# but with middleware expose hooks before and after each step

# re -> before agent->before mode->