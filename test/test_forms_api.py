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
from pycherwell.api.forms_api import FormsApi  # noqa: E501
from pycherwell.rest import ApiException


class TestFormsApi(unittest.TestCase):
    """FormsApi unit test stubs"""

    def setUp(self):
        self.api = pycherwell.api.forms_api.FormsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1(self):
        """Test case for forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1

        Get mobile form by BusObId and Public ID  # noqa: E501
        """
        pass

    def test_forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1(self):
        """Test case for forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1

        Get mobile form by Business Object ID and Business Object Record ID.  # noqa: E501
        """
        pass

    def test_forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1(self):
        """Test case for forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1

        Get mobile form by Business Object name and Public ID  # noqa: E501
        """
        pass

    def test_forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1(self):
        """Test case for forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1

        Get mobile form by Business Object name and record ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
