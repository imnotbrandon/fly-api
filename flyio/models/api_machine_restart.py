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


class ApiMachineRestart(object):
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
        'max_retries': 'int',
        'policy': 'str'
    }

    attribute_map = {
        'max_retries': 'max_retries',
        'policy': 'policy'
    }

    def __init__(self, max_retries=None, policy=None, _configuration=None):  # noqa: E501
        """ApiMachineRestart - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_retries = None
        self._policy = None
        self.discriminator = None

        if max_retries is not None:
            self.max_retries = max_retries
        if policy is not None:
            self.policy = policy

    @property
    def max_retries(self):
        """Gets the max_retries of this ApiMachineRestart.  # noqa: E501

        When policy is on-failure, the maximum number of times to attempt to restart the Machine before letting it stop.  # noqa: E501

        :return: The max_retries of this ApiMachineRestart.  # noqa: E501
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this ApiMachineRestart.

        When policy is on-failure, the maximum number of times to attempt to restart the Machine before letting it stop.  # noqa: E501

        :param max_retries: The max_retries of this ApiMachineRestart.  # noqa: E501
        :type: int
        """

        self._max_retries = max_retries

    @property
    def policy(self):
        """Gets the policy of this ApiMachineRestart.  # noqa: E501

        * no - Never try to restart a Machine automatically when its main process exits, whether that’s on purpose or on a crash. * always - Always restart a Machine automatically and never let it enter a stopped state, even when the main process exits cleanly. * on-failure - Try up to MaxRetries times to automatically restart the Machine if it exits with a non-zero exit code. Default when no explicit policy is set, and for Machines with schedules.  # noqa: E501

        :return: The policy of this ApiMachineRestart.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ApiMachineRestart.

        * no - Never try to restart a Machine automatically when its main process exits, whether that’s on purpose or on a crash. * always - Always restart a Machine automatically and never let it enter a stopped state, even when the main process exits cleanly. * on-failure - Try up to MaxRetries times to automatically restart the Machine if it exits with a non-zero exit code. Default when no explicit policy is set, and for Machines with schedules.  # noqa: E501

        :param policy: The policy of this ApiMachineRestart.  # noqa: E501
        :type: str
        """
        allowed_values = ["no", "always", "on-failure"]  # noqa: E501
        if (self._configuration.client_side_validation and
                policy not in allowed_values):
            raise ValueError(
                "Invalid value for `policy` ({0}), must be one of {1}"  # noqa: E501
                .format(policy, allowed_values)
            )

        self._policy = policy

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
        if issubclass(ApiMachineRestart, dict):
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
        if not isinstance(other, ApiMachineRestart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiMachineRestart):
            return True

        return self.to_dict() != other.to_dict()
