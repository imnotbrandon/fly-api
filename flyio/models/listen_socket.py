# coding: utf-8

"""
    Fly Machines API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyio.configuration import Configuration


class ListenSocket(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'proto': 'str'
    }

    attribute_map = {
        'address': 'address',
        'proto': 'proto'
    }

    def __init__(self, address=None, proto=None, _configuration=None):  # noqa: E501
        """ListenSocket - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._proto = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if proto is not None:
            self.proto = proto

    @property
    def address(self):
        """Gets the address of this ListenSocket.  # noqa: E501


        :return: The address of this ListenSocket.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListenSocket.


        :param address: The address of this ListenSocket.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def proto(self):
        """Gets the proto of this ListenSocket.  # noqa: E501


        :return: The proto of this ListenSocket.  # noqa: E501
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this ListenSocket.


        :param proto: The proto of this ListenSocket.  # noqa: E501
        :type: str
        """

        self._proto = proto

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ListenSocket, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListenSocket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListenSocket):
            return True

        return self.to_dict() != other.to_dict()
