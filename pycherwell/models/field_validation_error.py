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


class FieldValidationError(object):
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
        'error': 'str',
        'error_code': 'str',
        'field_id': 'str'
    }

    attribute_map = {
        'error': 'error',
        'error_code': 'errorCode',
        'field_id': 'fieldId'
    }

    def __init__(self, error=None, error_code=None, field_id=None):  # noqa: E501
        """FieldValidationError - a model defined in OpenAPI"""  # noqa: E501

        self._error = None
        self._error_code = None
        self._field_id = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        if field_id is not None:
            self.field_id = field_id

    @property
    def error(self):
        """Gets the error of this FieldValidationError.  # noqa: E501


        :return: The error of this FieldValidationError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this FieldValidationError.


        :param error: The error of this FieldValidationError.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_code(self):
        """Gets the error_code of this FieldValidationError.  # noqa: E501


        :return: The error_code of this FieldValidationError.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this FieldValidationError.


        :param error_code: The error_code of this FieldValidationError.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def field_id(self):
        """Gets the field_id of this FieldValidationError.  # noqa: E501


        :return: The field_id of this FieldValidationError.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this FieldValidationError.


        :param field_id: The field_id of this FieldValidationError.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

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
        if not isinstance(other, FieldValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
