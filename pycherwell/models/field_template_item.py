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


class FieldTemplateItem(object):
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
        'dirty': 'bool',
        'display_name': 'str',
        'field_id': 'str',
        'html': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'dirty': 'dirty',
        'display_name': 'displayName',
        'field_id': 'fieldId',
        'html': 'html',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, dirty=None, display_name=None, field_id=None, html=None, name=None, value=None):  # noqa: E501
        """FieldTemplateItem - a model defined in OpenAPI"""  # noqa: E501

        self._dirty = None
        self._display_name = None
        self._field_id = None
        self._html = None
        self._name = None
        self._value = None
        self.discriminator = None

        if dirty is not None:
            self.dirty = dirty
        if display_name is not None:
            self.display_name = display_name
        if field_id is not None:
            self.field_id = field_id
        if html is not None:
            self.html = html
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def dirty(self):
        """Gets the dirty of this FieldTemplateItem.  # noqa: E501


        :return: The dirty of this FieldTemplateItem.  # noqa: E501
        :rtype: bool
        """
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        """Sets the dirty of this FieldTemplateItem.


        :param dirty: The dirty of this FieldTemplateItem.  # noqa: E501
        :type: bool
        """

        self._dirty = dirty

    @property
    def display_name(self):
        """Gets the display_name of this FieldTemplateItem.  # noqa: E501


        :return: The display_name of this FieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FieldTemplateItem.


        :param display_name: The display_name of this FieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def field_id(self):
        """Gets the field_id of this FieldTemplateItem.  # noqa: E501


        :return: The field_id of this FieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this FieldTemplateItem.


        :param field_id: The field_id of this FieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def html(self):
        """Gets the html of this FieldTemplateItem.  # noqa: E501


        :return: The html of this FieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this FieldTemplateItem.


        :param html: The html of this FieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def name(self):
        """Gets the name of this FieldTemplateItem.  # noqa: E501


        :return: The name of this FieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldTemplateItem.


        :param name: The name of this FieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this FieldTemplateItem.  # noqa: E501


        :return: The value of this FieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FieldTemplateItem.


        :param value: The value of this FieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, FieldTemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
