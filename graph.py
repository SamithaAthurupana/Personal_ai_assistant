from langgraph.constants import START, END
from langgraph.graph import StateGraph
from typing_extensions import TypedDict
from agents import news_agent, router_agent

from guardrails import input_guardrails


class AgentState(TypedDict):

    input : str
    route : str
    response : str
    blocked : bool

def input_decision(state):
    if state.get("blocked"):
        return "end"
    return "router"

def router_decision(state):
    if state["route"]=="news":
        return "news"

graph  = StateGraph(AgentState)

graph.add_node("input_guard", input_guardrails)
graph.add_node("news", news_agent)
graph.add_node("router_agent", router_agent)

#graph.add_edge(START,"input_guard")
graph.set_entry_point("input_guard")
graph.add_conditional_edges("input_guard"
                      ,input_decision,
                      {"router": "router_agent"
                       ,"end": END})

graph.add_conditional_edges("router_agent", router_decision,
                            {"news":"news_agent"})