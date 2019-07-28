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


class SortInfo(object):
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
        'field_id': 'str',
        'sort_direction': 'int'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'sort_direction': 'sortDirection'
    }

    def __init__(self, field_id=None, sort_direction=None):  # noqa: E501
        """SortInfo - a model defined in OpenAPI"""  # noqa: E501

        self._field_id = None
        self._sort_direction = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if sort_direction is not None:
            self.sort_direction = sort_direction

    @property
    def field_id(self):
        """Gets the field_id of this SortInfo.  # noqa: E501


        :return: The field_id of this SortInfo.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this SortInfo.


        :param field_id: The field_id of this SortInfo.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def sort_direction(self):
        """Gets the sort_direction of this SortInfo.  # noqa: E501


        :return: The sort_direction of this SortInfo.  # noqa: E501
        :rtype: int
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this SortInfo.


        :param sort_direction: The sort_direction of this SortInfo.  # noqa: E501
        :type: int
        """

        self._sort_direction = sort_direction

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
        if not isinstance(other, SortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
