from structures import Parent
from block import Block, _create_block
from _blocks.data import ChildDatabase, ChildAttributes, ChildPage
from _blocks.type import BlockType


def create_child_database(
        parent: Parent,
        title: str,
        children: list[Block] = None
) -> ChildDatabase:
    """
    Factory method to create ChildDatabase object
    :param parent: parent object
    :param title: title of the child database
    :param children: optional list of child _blocks
    :return: newly created ChildDatabase Object
    """
    return _create_block(
        ChildDatabase,
        parent=parent,
        block_type=BlockType.CHILD_DATABASE,
        children=children,
        child_database=ChildAttributes(title=title)
    )


def create_child_page(
        parent: Parent,
        title: str,
        children: list[Block] = None
) -> ChildPage:
    """
    Factory method to create ChildPage object
    :param parent: parent object
    :param title: title of the child page
    :param children: optional list of child _blocks
    :return: newly created ChildPage Object
    """
    return _create_block(
        ChildPage,
        parent=parent,
        block_type=BlockType.CHILD_PAGE,
        children=children,
        child_page=ChildAttributes(title=title)
    )
