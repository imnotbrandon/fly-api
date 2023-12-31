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


class ApiMachineService(object):
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
        'autostart': 'bool',
        'autostop': 'bool',
        'checks': 'list[ApiMachineCheck]',
        'concurrency': 'ApiMachineServiceConcurrency',
        'force_instance_description': 'str',
        'force_instance_key': 'str',
        'internal_port': 'int',
        'min_machines_running': 'int',
        'ports': 'list[ApiMachinePort]',
        'protocol': 'str'
    }

    attribute_map = {
        'autostart': 'autostart',
        'autostop': 'autostop',
        'checks': 'checks',
        'concurrency': 'concurrency',
        'force_instance_description': 'force_instance_description',
        'force_instance_key': 'force_instance_key',
        'internal_port': 'internal_port',
        'min_machines_running': 'min_machines_running',
        'ports': 'ports',
        'protocol': 'protocol'
    }

    def __init__(self, autostart=None, autostop=None, checks=None, concurrency=None, force_instance_description=None, force_instance_key=None, internal_port=None, min_machines_running=None, ports=None, protocol=None, _configuration=None):  # noqa: E501
        """ApiMachineService - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._autostart = None
        self._autostop = None
        self._checks = None
        self._concurrency = None
        self._force_instance_description = None
        self._force_instance_key = None
        self._internal_port = None
        self._min_machines_running = None
        self._ports = None
        self._protocol = None
        self.discriminator = None

        if autostart is not None:
            self.autostart = autostart
        if autostop is not None:
            self.autostop = autostop
        if checks is not None:
            self.checks = checks
        if concurrency is not None:
            self.concurrency = concurrency
        if force_instance_description is not None:
            self.force_instance_description = force_instance_description
        if force_instance_key is not None:
            self.force_instance_key = force_instance_key
        if internal_port is not None:
            self.internal_port = internal_port
        if min_machines_running is not None:
            self.min_machines_running = min_machines_running
        if ports is not None:
            self.ports = ports
        if protocol is not None:
            self.protocol = protocol

    @property
    def autostart(self):
        """Gets the autostart of this ApiMachineService.  # noqa: E501


        :return: The autostart of this ApiMachineService.  # noqa: E501
        :rtype: bool
        """
        return self._autostart

    @autostart.setter
    def autostart(self, autostart):
        """Sets the autostart of this ApiMachineService.


        :param autostart: The autostart of this ApiMachineService.  # noqa: E501
        :type: bool
        """

        self._autostart = autostart

    @property
    def autostop(self):
        """Gets the autostop of this ApiMachineService.  # noqa: E501


        :return: The autostop of this ApiMachineService.  # noqa: E501
        :rtype: bool
        """
        return self._autostop

    @autostop.setter
    def autostop(self, autostop):
        """Sets the autostop of this ApiMachineService.


        :param autostop: The autostop of this ApiMachineService.  # noqa: E501
        :type: bool
        """

        self._autostop = autostop

    @property
    def checks(self):
        """Gets the checks of this ApiMachineService.  # noqa: E501


        :return: The checks of this ApiMachineService.  # noqa: E501
        :rtype: list[ApiMachineCheck]
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this ApiMachineService.


        :param checks: The checks of this ApiMachineService.  # noqa: E501
        :type: list[ApiMachineCheck]
        """

        self._checks = checks

    @property
    def concurrency(self):
        """Gets the concurrency of this ApiMachineService.  # noqa: E501


        :return: The concurrency of this ApiMachineService.  # noqa: E501
        :rtype: ApiMachineServiceConcurrency
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this ApiMachineService.


        :param concurrency: The concurrency of this ApiMachineService.  # noqa: E501
        :type: ApiMachineServiceConcurrency
        """

        self._concurrency = concurrency

    @property
    def force_instance_description(self):
        """Gets the force_instance_description of this ApiMachineService.  # noqa: E501


        :return: The force_instance_description of this ApiMachineService.  # noqa: E501
        :rtype: str
        """
        return self._force_instance_description

    @force_instance_description.setter
    def force_instance_description(self, force_instance_description):
        """Sets the force_instance_description of this ApiMachineService.


        :param force_instance_description: The force_instance_description of this ApiMachineService.  # noqa: E501
        :type: str
        """

        self._force_instance_description = force_instance_description

    @property
    def force_instance_key(self):
        """Gets the force_instance_key of this ApiMachineService.  # noqa: E501


        :return: The force_instance_key of this ApiMachineService.  # noqa: E501
        :rtype: str
        """
        return self._force_instance_key

    @force_instance_key.setter
    def force_instance_key(self, force_instance_key):
        """Sets the force_instance_key of this ApiMachineService.


        :param force_instance_key: The force_instance_key of this ApiMachineService.  # noqa: E501
        :type: str
        """

        self._force_instance_key = force_instance_key

    @property
    def internal_port(self):
        """Gets the internal_port of this ApiMachineService.  # noqa: E501


        :return: The internal_port of this ApiMachineService.  # noqa: E501
        :rtype: int
        """
        return self._internal_port

    @internal_port.setter
    def internal_port(self, internal_port):
        """Sets the internal_port of this ApiMachineService.


        :param internal_port: The internal_port of this ApiMachineService.  # noqa: E501
        :type: int
        """

        self._internal_port = internal_port

    @property
    def min_machines_running(self):
        """Gets the min_machines_running of this ApiMachineService.  # noqa: E501


        :return: The min_machines_running of this ApiMachineService.  # noqa: E501
        :rtype: int
        """
        return self._min_machines_running

    @min_machines_running.setter
    def min_machines_running(self, min_machines_running):
        """Sets the min_machines_running of this ApiMachineService.


        :param min_machines_running: The min_machines_running of this ApiMachineService.  # noqa: E501
        :type: int
        """

        self._min_machines_running = min_machines_running

    @property
    def ports(self):
        """Gets the ports of this ApiMachineService.  # noqa: E501


        :return: The ports of this ApiMachineService.  # noqa: E501
        :rtype: list[ApiMachinePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ApiMachineService.


        :param ports: The ports of this ApiMachineService.  # noqa: E501
        :type: list[ApiMachinePort]
        """

        self._ports = ports

    @property
    def protocol(self):
        """Gets the protocol of this ApiMachineService.  # noqa: E501


        :return: The protocol of this ApiMachineService.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ApiMachineService.


        :param protocol: The protocol of this ApiMachineService.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if issubclass(ApiMachineService, dict):
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
        if not isinstance(other, ApiMachineService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiMachineService):
            return True

        return self.to_dict() != other.to_dict()
