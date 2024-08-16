# Standard Library
from typing import Callable

# Third Party
from pydantic import Field

# First Party
from .configuration_ import ExtraConfiguration
from notion_api.data.properties import Property


class PropertiesStructure(ExtraConfiguration):
    properties: list = Field(exclude=True, default=[])


def parse_properties(
    v: dict, deserialization_func: Callable[[dict], Property]
) -> PropertiesStructure:
    properties = []
    for key, value in v.items():
        value["name"] = key
        _class = deserialization_func(value)
        properties.append(_class)
        v[key] = _class

    v["properties"] = properties
    return v
