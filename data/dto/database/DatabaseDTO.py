from typing import Annotated

from pydantic import BeforeValidator

from database.PropertyDTO import PropertyDTO
from general.MajorObjectDTO import MajorObjectDTO
from validators import attributes_validator, properties_validator


class DatabaseDTO(MajorObjectDTO):
    title: Annotated[str, BeforeValidator(attributes_validator)]
    description: Annotated[str, BeforeValidator(attributes_validator)]
    is_inline: bool
    properties: Annotated[list[PropertyDTO], BeforeValidator(properties_validator)] = []
