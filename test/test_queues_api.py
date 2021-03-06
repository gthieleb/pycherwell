# coding: utf-8

"""
    Cherwell REST API

    Unofficial Python Cherwell REST API library.  # noqa: E501

    The version of the OpenAPI document: 9.3.2
    Contact: See AUTHORS.
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pycherwell
from pycherwell.api.queues_api import QueuesApi  # noqa: E501
from pycherwell.rest import ApiException


class TestQueuesApi(unittest.TestCase):
    """QueuesApi unit test stubs"""

    def setUp(self):
        self.api = pycherwell.api.queues_api.QueuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_queues_add_item_to_queue_v1(self):
        """Test case for queues_add_item_to_queue_v1

        Add a Business Object to a queue  # noqa: E501
        """
        pass

    def test_queues_check_in_queue_item_v1(self):
        """Test case for queues_check_in_queue_item_v1

        Check a Business Object in to a queue  # noqa: E501
        """
        pass

    def test_queues_check_out_queue_item_v1(self):
        """Test case for queues_check_out_queue_item_v1

        Check a Business Object out of a queue  # noqa: E501
        """
        pass

    def test_queues_get_queues_folder_v1(self):
        """Test case for queues_get_queues_folder_v1

        Get available queues.  # noqa: E501
        """
        pass

    def test_queues_get_queues_scope_owner_v1(self):
        """Test case for queues_get_queues_scope_owner_v1

        Get available queues.  # noqa: E501
        """
        pass

    def test_queues_get_queues_scope_v1(self):
        """Test case for queues_get_queues_scope_v1

        Get available queues.  # noqa: E501
        """
        pass

    def test_queues_get_queues_v1(self):
        """Test case for queues_get_queues_v1

        Get available queues.  # noqa: E501
        """
        pass

    def test_queues_remove_item_from_queue_v1(self):
        """Test case for queues_remove_item_from_queue_v1

        Remove an item from a queue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
