import pytest

from __block.assertions import assert_block_data_is_correct, create_block_object, assert_serialization_to_json, \
    extract_block_data
from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from notion_api.data.blocks import ChildPage, ChildDatabase

TITLE = "BEST TITLE"
CHILD_DATA = {
    "title": TITLE,
}


@pytest.fixture
def child_block(block_data):
    def create_child_data(block_type) -> dict:
        return block_data(block_type, CHILD_DATA)

    return create_child_data


@pytest.mark.parametrize("child_class", [ChildPage, ChildDatabase])
def test_child_structure(child_block, child_class):
    extract_create_assert_structure(child_block, child_class, assert_child_data_is_correct)


@pytest.mark.parametrize("child_class", [ChildPage, ChildDatabase])
def test_child_serialization(child_block, child_class):
    extract_create_assert_serialization(child_block, child_class)


def assert_child_data_is_correct(data, expected_data):
    assert_block_data_is_correct(data, expected_data)
    block_type = data.__class__.get_associated_block_type()
    child_data = getattr(data, f"{block_type.value}")
    assert child_data.title == expected_data[block_type.value]["title"]
