from typing import Literal, Type, TypedDict
from typing_extensions import NotRequired

from discord_typings.interactions.commands import ApplicationCommandOptionInteractionData, SubcommandGroupOptionInteractionData, SubcommandOptionInteractionData
from discord_typings.interactions.components import SelectMenuOptionData


class InteractionData(TypedDict):
    id: Snowflake
    application_id: Snowflake
    data: 


class ApplicationCommandInteractionData(TypedDict):
    id: Snowflake
    name: str
    type: Literal[1, 2, 3]
    resolved: NotRequired[ResolvedInteractionData]
    options: NotRequired[Union[SubcommandOptionInteractionData, SubcommandGroupOptionInteractionData, ApplicationCommandOptionInteractionData]]


class ButtonComponentInteractionData(TypedDict):
    custom_id: str
    component_type: Literal[2]


class SelectComponentInteractionData(TypedDict):
    custom_id: str
    component_type: Literal[3]
    values: List[SelectMenuOptionData]
