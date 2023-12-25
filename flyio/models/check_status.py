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


class CheckStatus(object):
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
        'name': 'str',
        'output': 'str',
        'status': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'output': 'output',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, name=None, output=None, status=None, updated_at=None, _configuration=None):  # noqa: E501
        """CheckStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._output = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if output is not None:
            self.output = output
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this CheckStatus.  # noqa: E501


        :return: The name of this CheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckStatus.


        :param name: The name of this CheckStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def output(self):
        """Gets the output of this CheckStatus.  # noqa: E501


        :return: The output of this CheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CheckStatus.


        :param output: The output of this CheckStatus.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def status(self):
        """Gets the status of this CheckStatus.  # noqa: E501


        :return: The status of this CheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckStatus.


        :param status: The status of this CheckStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this CheckStatus.  # noqa: E501


        :return: The updated_at of this CheckStatus.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CheckStatus.


        :param updated_at: The updated_at of this CheckStatus.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(CheckStatus, dict):
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
        if not isinstance(other, CheckStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckStatus):
            return True

        return self.to_dict() != other.to_dict()