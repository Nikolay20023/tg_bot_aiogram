from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class HasLinkFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        entities = message.entities or []

        for entitie in entities:
            if entitie.type == "url":
                return {"link": entitie.extract_from(message.text)}
            
        return False