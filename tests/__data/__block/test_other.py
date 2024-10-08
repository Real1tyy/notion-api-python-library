# Third Party
import pytest

# First Party
from notion_apilib.data.blocks import Block, Breadcrumb, ColumnList, Divider, Unsupported
from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__block.helper import extract_create_assert_serialization, extract_create_assert_structure

# No specific data required as these blocks are empty
EMPTY_DATA = {}


@pytest.fixture
def empty_block(block_data):
    def create_empty_data(block_type) -> dict:
        return block_data(block_type, EMPTY_DATA)

    return create_empty_data


def assert_empty_block_data_is_correct(data: Block, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)


@pytest.mark.parametrize("block_class", [Divider, ColumnList, Breadcrumb, Unsupported])
def test_empty_block_structure(empty_block, block_class):
    extract_create_assert_structure(empty_block, block_class, assert_empty_block_data_is_correct)


@pytest.mark.parametrize("block_class", [Divider, ColumnList, Breadcrumb, Unsupported])
def test_empty_block_serialization(empty_block, block_class):
    extract_create_assert_serialization(empty_block, block_class)
