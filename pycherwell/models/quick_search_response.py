# coding: utf-8

"""
    Cherwell REST API

    Unofficial Python Cherwell REST API library.  # noqa: E501

    The version of the OpenAPI document: 9.3.2
    Contact: See AUTHORS.
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class QuickSearchResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'search_results_table': 'SearchResultsTableResponse',
        'simple_results_list': 'SimpleResultsList',
        'error_code': 'str',
        'error_message': 'str',
        'has_error': 'bool'
    }

    attribute_map = {
        'search_results_table': 'searchResultsTable',
        'simple_results_list': 'simpleResultsList',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'has_error': 'hasError'
    }

    def __init__(self, search_results_table=None, simple_results_list=None, error_code=None, error_message=None, has_error=None):  # noqa: E501
        """QuickSearchResponse - a model defined in OpenAPI"""  # noqa: E501

        self._search_results_table = None
        self._simple_results_list = None
        self._error_code = None
        self._error_message = None
        self._has_error = None
        self.discriminator = None

        if search_results_table is not None:
            self.search_results_table = search_results_table
        if simple_results_list is not None:
            self.simple_results_list = simple_results_list
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if has_error is not None:
            self.has_error = has_error

    @property
    def search_results_table(self):
        """Gets the search_results_table of this QuickSearchResponse.  # noqa: E501


        :return: The search_results_table of this QuickSearchResponse.  # noqa: E501
        :rtype: SearchResultsTableResponse
        """
        return self._search_results_table

    @search_results_table.setter
    def search_results_table(self, search_results_table):
        """Sets the search_results_table of this QuickSearchResponse.


        :param search_results_table: The search_results_table of this QuickSearchResponse.  # noqa: E501
        :type: SearchResultsTableResponse
        """

        self._search_results_table = search_results_table

    @property
    def simple_results_list(self):
        """Gets the simple_results_list of this QuickSearchResponse.  # noqa: E501


        :return: The simple_results_list of this QuickSearchResponse.  # noqa: E501
        :rtype: SimpleResultsList
        """
        return self._simple_results_list

    @simple_results_list.setter
    def simple_results_list(self, simple_results_list):
        """Sets the simple_results_list of this QuickSearchResponse.


        :param simple_results_list: The simple_results_list of this QuickSearchResponse.  # noqa: E501
        :type: SimpleResultsList
        """

        self._simple_results_list = simple_results_list

    @property
    def error_code(self):
        """Gets the error_code of this QuickSearchResponse.  # noqa: E501


        :return: The error_code of this QuickSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QuickSearchResponse.


        :param error_code: The error_code of this QuickSearchResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this QuickSearchResponse.  # noqa: E501


        :return: The error_message of this QuickSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this QuickSearchResponse.


        :param error_message: The error_message of this QuickSearchResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_error(self):
        """Gets the has_error of this QuickSearchResponse.  # noqa: E501


        :return: The has_error of this QuickSearchResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this QuickSearchResponse.


        :param has_error: The has_error of this QuickSearchResponse.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuickSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
