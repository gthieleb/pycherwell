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


class SearchItem(object):
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
        'association': 'str',
        'links': 'list[Link]',
        'localized_scope_name': 'str',
        'parent_folder_id': 'str',
        'scope': 'str',
        'scope_owner': 'str',
        'search_id': 'str',
        'search_name': 'str'
    }

    attribute_map = {
        'association': 'association',
        'links': 'links',
        'localized_scope_name': 'localizedScopeName',
        'parent_folder_id': 'parentFolderId',
        'scope': 'scope',
        'scope_owner': 'scopeOwner',
        'search_id': 'searchId',
        'search_name': 'searchName'
    }

    def __init__(self, association=None, links=None, localized_scope_name=None, parent_folder_id=None, scope=None, scope_owner=None, search_id=None, search_name=None, local_vars_configuration=None):  # noqa: E501
        """SearchItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._association = None
        self._links = None
        self._localized_scope_name = None
        self._parent_folder_id = None
        self._scope = None
        self._scope_owner = None
        self._search_id = None
        self._search_name = None
        self.discriminator = None

        if association is not None:
            self.association = association
        if links is not None:
            self.links = links
        if localized_scope_name is not None:
            self.localized_scope_name = localized_scope_name
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if scope is not None:
            self.scope = scope
        if scope_owner is not None:
            self.scope_owner = scope_owner
        if search_id is not None:
            self.search_id = search_id
        if search_name is not None:
            self.search_name = search_name

    @property
    def association(self):
        """Gets the association of this SearchItem.  # noqa: E501


        :return: The association of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this SearchItem.


        :param association: The association of this SearchItem.  # noqa: E501
        :type: str
        """

        self._association = association

    @property
    def links(self):
        """Gets the links of this SearchItem.  # noqa: E501


        :return: The links of this SearchItem.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SearchItem.


        :param links: The links of this SearchItem.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def localized_scope_name(self):
        """Gets the localized_scope_name of this SearchItem.  # noqa: E501


        :return: The localized_scope_name of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._localized_scope_name

    @localized_scope_name.setter
    def localized_scope_name(self, localized_scope_name):
        """Sets the localized_scope_name of this SearchItem.


        :param localized_scope_name: The localized_scope_name of this SearchItem.  # noqa: E501
        :type: str
        """

        self._localized_scope_name = localized_scope_name

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this SearchItem.  # noqa: E501


        :return: The parent_folder_id of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this SearchItem.


        :param parent_folder_id: The parent_folder_id of this SearchItem.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def scope(self):
        """Gets the scope of this SearchItem.  # noqa: E501


        :return: The scope of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SearchItem.


        :param scope: The scope of this SearchItem.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def scope_owner(self):
        """Gets the scope_owner of this SearchItem.  # noqa: E501


        :return: The scope_owner of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._scope_owner

    @scope_owner.setter
    def scope_owner(self, scope_owner):
        """Sets the scope_owner of this SearchItem.


        :param scope_owner: The scope_owner of this SearchItem.  # noqa: E501
        :type: str
        """

        self._scope_owner = scope_owner

    @property
    def search_id(self):
        """Gets the search_id of this SearchItem.  # noqa: E501


        :return: The search_id of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this SearchItem.


        :param search_id: The search_id of this SearchItem.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

    @property
    def search_name(self):
        """Gets the search_name of this SearchItem.  # noqa: E501


        :return: The search_name of this SearchItem.  # noqa: E501
        :rtype: str
        """
        return self._search_name

    @search_name.setter
    def search_name(self, search_name):
        """Sets the search_name of this SearchItem.


        :param search_name: The search_name of this SearchItem.  # noqa: E501
        :type: str
        """

        self._search_name = search_name

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
        if not isinstance(other, SearchItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchItem):
            return True

        return self.to_dict() != other.to_dict()
