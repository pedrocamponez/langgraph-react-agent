import operator
from typing import Annotated, TypedDict, Union

from langchain_core.agents import AgentAction, AgentFinish


class AgentState(TypedDict):
    input: str  # Users input
    agent_outcome: Union[AgentAction, AgentFinish, None]  # None because the first node has an empty state
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]










