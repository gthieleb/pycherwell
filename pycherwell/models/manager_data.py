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


class ManagerData(object):
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
        'root': 'ManagerFolder',
        'supported_associations': 'list[NameValuePair]',
        'error_code': 'str',
        'error_message': 'str',
        'has_error': 'bool'
    }

    attribute_map = {
        'root': 'root',
        'supported_associations': 'supportedAssociations',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'has_error': 'hasError'
    }

    def __init__(self, root=None, supported_associations=None, error_code=None, error_message=None, has_error=None):  # noqa: E501
        """ManagerData - a model defined in OpenAPI"""  # noqa: E501

        self._root = None
        self._supported_associations = None
        self._error_code = None
        self._error_message = None
        self._has_error = None
        self.discriminator = None

        if root is not None:
            self.root = root
        if supported_associations is not None:
            self.supported_associations = supported_associations
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if has_error is not None:
            self.has_error = has_error

    @property
    def root(self):
        """Gets the root of this ManagerData.  # noqa: E501


        :return: The root of this ManagerData.  # noqa: E501
        :rtype: ManagerFolder
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this ManagerData.


        :param root: The root of this ManagerData.  # noqa: E501
        :type: ManagerFolder
        """

        self._root = root

    @property
    def supported_associations(self):
        """Gets the supported_associations of this ManagerData.  # noqa: E501


        :return: The supported_associations of this ManagerData.  # noqa: E501
        :rtype: list[NameValuePair]
        """
        return self._supported_associations

    @supported_associations.setter
    def supported_associations(self, supported_associations):
        """Sets the supported_associations of this ManagerData.


        :param supported_associations: The supported_associations of this ManagerData.  # noqa: E501
        :type: list[NameValuePair]
        """

        self._supported_associations = supported_associations

    @property
    def error_code(self):
        """Gets the error_code of this ManagerData.  # noqa: E501


        :return: The error_code of this ManagerData.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ManagerData.


        :param error_code: The error_code of this ManagerData.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this ManagerData.  # noqa: E501


        :return: The error_message of this ManagerData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ManagerData.


        :param error_message: The error_message of this ManagerData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_error(self):
        """Gets the has_error of this ManagerData.  # noqa: E501


        :return: The has_error of this ManagerData.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this ManagerData.


        :param has_error: The has_error of this ManagerData.  # noqa: E501
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
        if not isinstance(other, ManagerData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other