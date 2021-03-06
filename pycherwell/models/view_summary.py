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

from pycherwell.configuration import Configuration


class ViewSummary(object):
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
        'group_summaries': 'list[ViewSummary]',
        'image': 'str',
        'is_part_of_view': 'bool',
        'bus_ob_id': 'str',
        'display_name': 'str',
        'group': 'bool',
        'lookup': 'bool',
        'major': 'bool',
        'name': 'str',
        'supporting': 'bool'
    }

    attribute_map = {
        'group_summaries': 'groupSummaries',
        'image': 'image',
        'is_part_of_view': 'isPartOfView',
        'bus_ob_id': 'busObId',
        'display_name': 'displayName',
        'group': 'group',
        'lookup': 'lookup',
        'major': 'major',
        'name': 'name',
        'supporting': 'supporting'
    }

    def __init__(self, group_summaries=None, image=None, is_part_of_view=None, bus_ob_id=None, display_name=None, group=None, lookup=None, major=None, name=None, supporting=None, local_vars_configuration=None):  # noqa: E501
        """ViewSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_summaries = None
        self._image = None
        self._is_part_of_view = None
        self._bus_ob_id = None
        self._display_name = None
        self._group = None
        self._lookup = None
        self._major = None
        self._name = None
        self._supporting = None
        self.discriminator = None

        if group_summaries is not None:
            self.group_summaries = group_summaries
        if image is not None:
            self.image = image
        if is_part_of_view is not None:
            self.is_part_of_view = is_part_of_view
        if bus_ob_id is not None:
            self.bus_ob_id = bus_ob_id
        if display_name is not None:
            self.display_name = display_name
        if group is not None:
            self.group = group
        if lookup is not None:
            self.lookup = lookup
        if major is not None:
            self.major = major
        if name is not None:
            self.name = name
        if supporting is not None:
            self.supporting = supporting

    @property
    def group_summaries(self):
        """Gets the group_summaries of this ViewSummary.  # noqa: E501


        :return: The group_summaries of this ViewSummary.  # noqa: E501
        :rtype: list[ViewSummary]
        """
        return self._group_summaries

    @group_summaries.setter
    def group_summaries(self, group_summaries):
        """Sets the group_summaries of this ViewSummary.


        :param group_summaries: The group_summaries of this ViewSummary.  # noqa: E501
        :type: list[ViewSummary]
        """

        self._group_summaries = group_summaries

    @property
    def image(self):
        """Gets the image of this ViewSummary.  # noqa: E501


        :return: The image of this ViewSummary.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ViewSummary.


        :param image: The image of this ViewSummary.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def is_part_of_view(self):
        """Gets the is_part_of_view of this ViewSummary.  # noqa: E501


        :return: The is_part_of_view of this ViewSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_part_of_view

    @is_part_of_view.setter
    def is_part_of_view(self, is_part_of_view):
        """Sets the is_part_of_view of this ViewSummary.


        :param is_part_of_view: The is_part_of_view of this ViewSummary.  # noqa: E501
        :type: bool
        """

        self._is_part_of_view = is_part_of_view

    @property
    def bus_ob_id(self):
        """Gets the bus_ob_id of this ViewSummary.  # noqa: E501


        :return: The bus_ob_id of this ViewSummary.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_id

    @bus_ob_id.setter
    def bus_ob_id(self, bus_ob_id):
        """Sets the bus_ob_id of this ViewSummary.


        :param bus_ob_id: The bus_ob_id of this ViewSummary.  # noqa: E501
        :type: str
        """

        self._bus_ob_id = bus_ob_id

    @property
    def display_name(self):
        """Gets the display_name of this ViewSummary.  # noqa: E501


        :return: The display_name of this ViewSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ViewSummary.


        :param display_name: The display_name of this ViewSummary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def group(self):
        """Gets the group of this ViewSummary.  # noqa: E501


        :return: The group of this ViewSummary.  # noqa: E501
        :rtype: bool
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ViewSummary.


        :param group: The group of this ViewSummary.  # noqa: E501
        :type: bool
        """

        self._group = group

    @property
    def lookup(self):
        """Gets the lookup of this ViewSummary.  # noqa: E501


        :return: The lookup of this ViewSummary.  # noqa: E501
        :rtype: bool
        """
        return self._lookup

    @lookup.setter
    def lookup(self, lookup):
        """Sets the lookup of this ViewSummary.


        :param lookup: The lookup of this ViewSummary.  # noqa: E501
        :type: bool
        """

        self._lookup = lookup

    @property
    def major(self):
        """Gets the major of this ViewSummary.  # noqa: E501


        :return: The major of this ViewSummary.  # noqa: E501
        :rtype: bool
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this ViewSummary.


        :param major: The major of this ViewSummary.  # noqa: E501
        :type: bool
        """

        self._major = major

    @property
    def name(self):
        """Gets the name of this ViewSummary.  # noqa: E501


        :return: The name of this ViewSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ViewSummary.


        :param name: The name of this ViewSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def supporting(self):
        """Gets the supporting of this ViewSummary.  # noqa: E501


        :return: The supporting of this ViewSummary.  # noqa: E501
        :rtype: bool
        """
        return self._supporting

    @supporting.setter
    def supporting(self, supporting):
        """Sets the supporting of this ViewSummary.


        :param supporting: The supporting of this ViewSummary.  # noqa: E501
        :type: bool
        """

        self._supporting = supporting

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
        if not isinstance(other, ViewSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ViewSummary):
            return True

        return self.to_dict() != other.to_dict()
