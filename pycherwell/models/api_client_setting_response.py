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


class ApiClientSettingResponse(object):
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
        'name': 'str',
        'description': 'str',
        'culture': 'str',
        'client_key': 'str',
        'token_lifespan_minutes': 'int',
        'refresh_token_lifespan_minutes': 'int',
        'api_access_is_enabled': 'bool',
        'allow_anonymous_access': 'bool',
        'stand_in_key': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'has_error': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'culture': 'culture',
        'client_key': 'clientKey',
        'token_lifespan_minutes': 'tokenLifespanMinutes',
        'refresh_token_lifespan_minutes': 'refreshTokenLifespanMinutes',
        'api_access_is_enabled': 'apiAccessIsEnabled',
        'allow_anonymous_access': 'allowAnonymousAccess',
        'stand_in_key': 'standInKey',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'has_error': 'hasError'
    }

    def __init__(self, name=None, description=None, culture=None, client_key=None, token_lifespan_minutes=None, refresh_token_lifespan_minutes=None, api_access_is_enabled=None, allow_anonymous_access=None, stand_in_key=None, error_code=None, error_message=None, has_error=None, local_vars_configuration=None):  # noqa: E501
        """ApiClientSettingResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._culture = None
        self._client_key = None
        self._token_lifespan_minutes = None
        self._refresh_token_lifespan_minutes = None
        self._api_access_is_enabled = None
        self._allow_anonymous_access = None
        self._stand_in_key = None
        self._error_code = None
        self._error_message = None
        self._has_error = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if culture is not None:
            self.culture = culture
        if client_key is not None:
            self.client_key = client_key
        if token_lifespan_minutes is not None:
            self.token_lifespan_minutes = token_lifespan_minutes
        if refresh_token_lifespan_minutes is not None:
            self.refresh_token_lifespan_minutes = refresh_token_lifespan_minutes
        if api_access_is_enabled is not None:
            self.api_access_is_enabled = api_access_is_enabled
        if allow_anonymous_access is not None:
            self.allow_anonymous_access = allow_anonymous_access
        if stand_in_key is not None:
            self.stand_in_key = stand_in_key
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if has_error is not None:
            self.has_error = has_error

    @property
    def name(self):
        """Gets the name of this ApiClientSettingResponse.  # noqa: E501


        :return: The name of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiClientSettingResponse.


        :param name: The name of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiClientSettingResponse.  # noqa: E501


        :return: The description of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiClientSettingResponse.


        :param description: The description of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def culture(self):
        """Gets the culture of this ApiClientSettingResponse.  # noqa: E501


        :return: The culture of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this ApiClientSettingResponse.


        :param culture: The culture of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._culture = culture

    @property
    def client_key(self):
        """Gets the client_key of this ApiClientSettingResponse.  # noqa: E501


        :return: The client_key of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this ApiClientSettingResponse.


        :param client_key: The client_key of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._client_key = client_key

    @property
    def token_lifespan_minutes(self):
        """Gets the token_lifespan_minutes of this ApiClientSettingResponse.  # noqa: E501


        :return: The token_lifespan_minutes of this ApiClientSettingResponse.  # noqa: E501
        :rtype: int
        """
        return self._token_lifespan_minutes

    @token_lifespan_minutes.setter
    def token_lifespan_minutes(self, token_lifespan_minutes):
        """Sets the token_lifespan_minutes of this ApiClientSettingResponse.


        :param token_lifespan_minutes: The token_lifespan_minutes of this ApiClientSettingResponse.  # noqa: E501
        :type: int
        """

        self._token_lifespan_minutes = token_lifespan_minutes

    @property
    def refresh_token_lifespan_minutes(self):
        """Gets the refresh_token_lifespan_minutes of this ApiClientSettingResponse.  # noqa: E501


        :return: The refresh_token_lifespan_minutes of this ApiClientSettingResponse.  # noqa: E501
        :rtype: int
        """
        return self._refresh_token_lifespan_minutes

    @refresh_token_lifespan_minutes.setter
    def refresh_token_lifespan_minutes(self, refresh_token_lifespan_minutes):
        """Sets the refresh_token_lifespan_minutes of this ApiClientSettingResponse.


        :param refresh_token_lifespan_minutes: The refresh_token_lifespan_minutes of this ApiClientSettingResponse.  # noqa: E501
        :type: int
        """

        self._refresh_token_lifespan_minutes = refresh_token_lifespan_minutes

    @property
    def api_access_is_enabled(self):
        """Gets the api_access_is_enabled of this ApiClientSettingResponse.  # noqa: E501


        :return: The api_access_is_enabled of this ApiClientSettingResponse.  # noqa: E501
        :rtype: bool
        """
        return self._api_access_is_enabled

    @api_access_is_enabled.setter
    def api_access_is_enabled(self, api_access_is_enabled):
        """Sets the api_access_is_enabled of this ApiClientSettingResponse.


        :param api_access_is_enabled: The api_access_is_enabled of this ApiClientSettingResponse.  # noqa: E501
        :type: bool
        """

        self._api_access_is_enabled = api_access_is_enabled

    @property
    def allow_anonymous_access(self):
        """Gets the allow_anonymous_access of this ApiClientSettingResponse.  # noqa: E501


        :return: The allow_anonymous_access of this ApiClientSettingResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allow_anonymous_access

    @allow_anonymous_access.setter
    def allow_anonymous_access(self, allow_anonymous_access):
        """Sets the allow_anonymous_access of this ApiClientSettingResponse.


        :param allow_anonymous_access: The allow_anonymous_access of this ApiClientSettingResponse.  # noqa: E501
        :type: bool
        """

        self._allow_anonymous_access = allow_anonymous_access

    @property
    def stand_in_key(self):
        """Gets the stand_in_key of this ApiClientSettingResponse.  # noqa: E501


        :return: The stand_in_key of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._stand_in_key

    @stand_in_key.setter
    def stand_in_key(self, stand_in_key):
        """Sets the stand_in_key of this ApiClientSettingResponse.


        :param stand_in_key: The stand_in_key of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._stand_in_key = stand_in_key

    @property
    def error_code(self):
        """Gets the error_code of this ApiClientSettingResponse.  # noqa: E501


        :return: The error_code of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ApiClientSettingResponse.


        :param error_code: The error_code of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this ApiClientSettingResponse.  # noqa: E501


        :return: The error_message of this ApiClientSettingResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ApiClientSettingResponse.


        :param error_message: The error_message of this ApiClientSettingResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_error(self):
        """Gets the has_error of this ApiClientSettingResponse.  # noqa: E501


        :return: The has_error of this ApiClientSettingResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this ApiClientSettingResponse.


        :param has_error: The has_error of this ApiClientSettingResponse.  # noqa: E501
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
        if not isinstance(other, ApiClientSettingResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiClientSettingResponse):
            return True

        return self.to_dict() != other.to_dict()
