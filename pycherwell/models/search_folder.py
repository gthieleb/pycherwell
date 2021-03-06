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


class SearchFolder(object):
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
        'child_folders': 'list[SearchFolder]',
        'child_items': 'list[SearchItem]',
        'folder_id': 'str',
        'folder_name': 'str',
        'links': 'list[Link]',
        'localized_scope_name': 'str',
        'parent_folder_id': 'str',
        'scope': 'str',
        'scope_owner': 'str'
    }

    attribute_map = {
        'association': 'association',
        'child_folders': 'childFolders',
        'child_items': 'childItems',
        'folder_id': 'folderId',
        'folder_name': 'folderName',
        'links': 'links',
        'localized_scope_name': 'localizedScopeName',
        'parent_folder_id': 'parentFolderId',
        'scope': 'scope',
        'scope_owner': 'scopeOwner'
    }

    def __init__(self, association=None, child_folders=None, child_items=None, folder_id=None, folder_name=None, links=None, localized_scope_name=None, parent_folder_id=None, scope=None, scope_owner=None, local_vars_configuration=None):  # noqa: E501
        """SearchFolder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._association = None
        self._child_folders = None
        self._child_items = None
        self._folder_id = None
        self._folder_name = None
        self._links = None
        self._localized_scope_name = None
        self._parent_folder_id = None
        self._scope = None
        self._scope_owner = None
        self.discriminator = None

        if association is not None:
            self.association = association
        if child_folders is not None:
            self.child_folders = child_folders
        if child_items is not None:
            self.child_items = child_items
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_name is not None:
            self.folder_name = folder_name
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

    @property
    def association(self):
        """Gets the association of this SearchFolder.  # noqa: E501


        :return: The association of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this SearchFolder.


        :param association: The association of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._association = association

    @property
    def child_folders(self):
        """Gets the child_folders of this SearchFolder.  # noqa: E501


        :return: The child_folders of this SearchFolder.  # noqa: E501
        :rtype: list[SearchFolder]
        """
        return self._child_folders

    @child_folders.setter
    def child_folders(self, child_folders):
        """Sets the child_folders of this SearchFolder.


        :param child_folders: The child_folders of this SearchFolder.  # noqa: E501
        :type: list[SearchFolder]
        """

        self._child_folders = child_folders

    @property
    def child_items(self):
        """Gets the child_items of this SearchFolder.  # noqa: E501


        :return: The child_items of this SearchFolder.  # noqa: E501
        :rtype: list[SearchItem]
        """
        return self._child_items

    @child_items.setter
    def child_items(self, child_items):
        """Sets the child_items of this SearchFolder.


        :param child_items: The child_items of this SearchFolder.  # noqa: E501
        :type: list[SearchItem]
        """

        self._child_items = child_items

    @property
    def folder_id(self):
        """Gets the folder_id of this SearchFolder.  # noqa: E501


        :return: The folder_id of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this SearchFolder.


        :param folder_id: The folder_id of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_name(self):
        """Gets the folder_name of this SearchFolder.  # noqa: E501


        :return: The folder_name of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this SearchFolder.


        :param folder_name: The folder_name of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def links(self):
        """Gets the links of this SearchFolder.  # noqa: E501


        :return: The links of this SearchFolder.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SearchFolder.


        :param links: The links of this SearchFolder.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def localized_scope_name(self):
        """Gets the localized_scope_name of this SearchFolder.  # noqa: E501


        :return: The localized_scope_name of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._localized_scope_name

    @localized_scope_name.setter
    def localized_scope_name(self, localized_scope_name):
        """Sets the localized_scope_name of this SearchFolder.


        :param localized_scope_name: The localized_scope_name of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._localized_scope_name = localized_scope_name

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this SearchFolder.  # noqa: E501


        :return: The parent_folder_id of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this SearchFolder.


        :param parent_folder_id: The parent_folder_id of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def scope(self):
        """Gets the scope of this SearchFolder.  # noqa: E501


        :return: The scope of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SearchFolder.


        :param scope: The scope of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def scope_owner(self):
        """Gets the scope_owner of this SearchFolder.  # noqa: E501


        :return: The scope_owner of this SearchFolder.  # noqa: E501
        :rtype: str
        """
        return self._scope_owner

    @scope_owner.setter
    def scope_owner(self, scope_owner):
        """Sets the scope_owner of this SearchFolder.


        :param scope_owner: The scope_owner of this SearchFolder.  # noqa: E501
        :type: str
        """

        self._scope_owner = scope_owner

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
        if not isinstance(other, SearchFolder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchFolder):
            return True

        return self.to_dict() != other.to_dict()
