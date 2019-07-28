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


class AddUserToTeamRequest(object):
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
        'team_id': 'str',
        'user_is_team_manager': 'bool',
        'user_record_id': 'str'
    }

    attribute_map = {
        'team_id': 'teamId',
        'user_is_team_manager': 'userIsTeamManager',
        'user_record_id': 'userRecordId'
    }

    def __init__(self, team_id=None, user_is_team_manager=None, user_record_id=None):  # noqa: E501
        """AddUserToTeamRequest - a model defined in OpenAPI"""  # noqa: E501

        self._team_id = None
        self._user_is_team_manager = None
        self._user_record_id = None
        self.discriminator = None

        if team_id is not None:
            self.team_id = team_id
        if user_is_team_manager is not None:
            self.user_is_team_manager = user_is_team_manager
        if user_record_id is not None:
            self.user_record_id = user_record_id

    @property
    def team_id(self):
        """Gets the team_id of this AddUserToTeamRequest.  # noqa: E501


        :return: The team_id of this AddUserToTeamRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this AddUserToTeamRequest.


        :param team_id: The team_id of this AddUserToTeamRequest.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def user_is_team_manager(self):
        """Gets the user_is_team_manager of this AddUserToTeamRequest.  # noqa: E501


        :return: The user_is_team_manager of this AddUserToTeamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._user_is_team_manager

    @user_is_team_manager.setter
    def user_is_team_manager(self, user_is_team_manager):
        """Sets the user_is_team_manager of this AddUserToTeamRequest.


        :param user_is_team_manager: The user_is_team_manager of this AddUserToTeamRequest.  # noqa: E501
        :type: bool
        """

        self._user_is_team_manager = user_is_team_manager

    @property
    def user_record_id(self):
        """Gets the user_record_id of this AddUserToTeamRequest.  # noqa: E501


        :return: The user_record_id of this AddUserToTeamRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_record_id

    @user_record_id.setter
    def user_record_id(self, user_record_id):
        """Sets the user_record_id of this AddUserToTeamRequest.


        :param user_record_id: The user_record_id of this AddUserToTeamRequest.  # noqa: E501
        :type: str
        """

        self._user_record_id = user_record_id

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
        if not isinstance(other, AddUserToTeamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
