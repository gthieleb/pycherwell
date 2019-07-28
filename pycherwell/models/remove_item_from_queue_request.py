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


class RemoveItemFromQueueRequest(object):
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
        'bus_ob_id': 'str',
        'bus_ob_rec_id': 'str',
        'history_notes': 'str',
        'queue_stand_in_key': 'str'
    }

    attribute_map = {
        'bus_ob_id': 'busObId',
        'bus_ob_rec_id': 'busObRecId',
        'history_notes': 'historyNotes',
        'queue_stand_in_key': 'queueStandInKey'
    }

    def __init__(self, bus_ob_id=None, bus_ob_rec_id=None, history_notes=None, queue_stand_in_key=None):  # noqa: E501
        """RemoveItemFromQueueRequest - a model defined in OpenAPI"""  # noqa: E501

        self._bus_ob_id = None
        self._bus_ob_rec_id = None
        self._history_notes = None
        self._queue_stand_in_key = None
        self.discriminator = None

        if bus_ob_id is not None:
            self.bus_ob_id = bus_ob_id
        if bus_ob_rec_id is not None:
            self.bus_ob_rec_id = bus_ob_rec_id
        if history_notes is not None:
            self.history_notes = history_notes
        if queue_stand_in_key is not None:
            self.queue_stand_in_key = queue_stand_in_key

    @property
    def bus_ob_id(self):
        """Gets the bus_ob_id of this RemoveItemFromQueueRequest.  # noqa: E501


        :return: The bus_ob_id of this RemoveItemFromQueueRequest.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_id

    @bus_ob_id.setter
    def bus_ob_id(self, bus_ob_id):
        """Sets the bus_ob_id of this RemoveItemFromQueueRequest.


        :param bus_ob_id: The bus_ob_id of this RemoveItemFromQueueRequest.  # noqa: E501
        :type: str
        """

        self._bus_ob_id = bus_ob_id

    @property
    def bus_ob_rec_id(self):
        """Gets the bus_ob_rec_id of this RemoveItemFromQueueRequest.  # noqa: E501


        :return: The bus_ob_rec_id of this RemoveItemFromQueueRequest.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_rec_id

    @bus_ob_rec_id.setter
    def bus_ob_rec_id(self, bus_ob_rec_id):
        """Sets the bus_ob_rec_id of this RemoveItemFromQueueRequest.


        :param bus_ob_rec_id: The bus_ob_rec_id of this RemoveItemFromQueueRequest.  # noqa: E501
        :type: str
        """

        self._bus_ob_rec_id = bus_ob_rec_id

    @property
    def history_notes(self):
        """Gets the history_notes of this RemoveItemFromQueueRequest.  # noqa: E501


        :return: The history_notes of this RemoveItemFromQueueRequest.  # noqa: E501
        :rtype: str
        """
        return self._history_notes

    @history_notes.setter
    def history_notes(self, history_notes):
        """Sets the history_notes of this RemoveItemFromQueueRequest.


        :param history_notes: The history_notes of this RemoveItemFromQueueRequest.  # noqa: E501
        :type: str
        """

        self._history_notes = history_notes

    @property
    def queue_stand_in_key(self):
        """Gets the queue_stand_in_key of this RemoveItemFromQueueRequest.  # noqa: E501


        :return: The queue_stand_in_key of this RemoveItemFromQueueRequest.  # noqa: E501
        :rtype: str
        """
        return self._queue_stand_in_key

    @queue_stand_in_key.setter
    def queue_stand_in_key(self, queue_stand_in_key):
        """Sets the queue_stand_in_key of this RemoveItemFromQueueRequest.


        :param queue_stand_in_key: The queue_stand_in_key of this RemoveItemFromQueueRequest.  # noqa: E501
        :type: str
        """

        self._queue_stand_in_key = queue_stand_in_key

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
        if not isinstance(other, RemoveItemFromQueueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
