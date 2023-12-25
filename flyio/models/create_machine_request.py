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


class CreateMachineRequest(object):
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
        'config': 'CreateMachineRequestConfig',
        'lease_ttl': 'int',
        'lsvd': 'bool',
        'name': 'str',
        'region': 'str',
        'skip_launch': 'bool',
        'skip_service_registration': 'bool'
    }

    attribute_map = {
        'config': 'config',
        'lease_ttl': 'lease_ttl',
        'lsvd': 'lsvd',
        'name': 'name',
        'region': 'region',
        'skip_launch': 'skip_launch',
        'skip_service_registration': 'skip_service_registration'
    }

    def __init__(self, config=None, lease_ttl=None, lsvd=None, name=None, region=None, skip_launch=None, skip_service_registration=None, _configuration=None):  # noqa: E501
        """CreateMachineRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config = None
        self._lease_ttl = None
        self._lsvd = None
        self._name = None
        self._region = None
        self._skip_launch = None
        self._skip_service_registration = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if lease_ttl is not None:
            self.lease_ttl = lease_ttl
        if lsvd is not None:
            self.lsvd = lsvd
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if skip_launch is not None:
            self.skip_launch = skip_launch
        if skip_service_registration is not None:
            self.skip_service_registration = skip_service_registration

    @property
    def config(self):
        """Gets the config of this CreateMachineRequest.  # noqa: E501


        :return: The config of this CreateMachineRequest.  # noqa: E501
        :rtype: CreateMachineRequestConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CreateMachineRequest.


        :param config: The config of this CreateMachineRequest.  # noqa: E501
        :type: CreateMachineRequestConfig
        """

        self._config = config

    @property
    def lease_ttl(self):
        """Gets the lease_ttl of this CreateMachineRequest.  # noqa: E501


        :return: The lease_ttl of this CreateMachineRequest.  # noqa: E501
        :rtype: int
        """
        return self._lease_ttl

    @lease_ttl.setter
    def lease_ttl(self, lease_ttl):
        """Sets the lease_ttl of this CreateMachineRequest.


        :param lease_ttl: The lease_ttl of this CreateMachineRequest.  # noqa: E501
        :type: int
        """

        self._lease_ttl = lease_ttl

    @property
    def lsvd(self):
        """Gets the lsvd of this CreateMachineRequest.  # noqa: E501


        :return: The lsvd of this CreateMachineRequest.  # noqa: E501
        :rtype: bool
        """
        return self._lsvd

    @lsvd.setter
    def lsvd(self, lsvd):
        """Sets the lsvd of this CreateMachineRequest.


        :param lsvd: The lsvd of this CreateMachineRequest.  # noqa: E501
        :type: bool
        """

        self._lsvd = lsvd

    @property
    def name(self):
        """Gets the name of this CreateMachineRequest.  # noqa: E501

        Unique name for this Machine. If omitted, one is generated for you  # noqa: E501

        :return: The name of this CreateMachineRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMachineRequest.

        Unique name for this Machine. If omitted, one is generated for you  # noqa: E501

        :param name: The name of this CreateMachineRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this CreateMachineRequest.  # noqa: E501

        The target region. Omitting this param launches in the same region as your WireGuard peer connection (somewhere near you).  # noqa: E501

        :return: The region of this CreateMachineRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateMachineRequest.

        The target region. Omitting this param launches in the same region as your WireGuard peer connection (somewhere near you).  # noqa: E501

        :param region: The region of this CreateMachineRequest.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def skip_launch(self):
        """Gets the skip_launch of this CreateMachineRequest.  # noqa: E501


        :return: The skip_launch of this CreateMachineRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_launch

    @skip_launch.setter
    def skip_launch(self, skip_launch):
        """Sets the skip_launch of this CreateMachineRequest.


        :param skip_launch: The skip_launch of this CreateMachineRequest.  # noqa: E501
        :type: bool
        """

        self._skip_launch = skip_launch

    @property
    def skip_service_registration(self):
        """Gets the skip_service_registration of this CreateMachineRequest.  # noqa: E501


        :return: The skip_service_registration of this CreateMachineRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_service_registration

    @skip_service_registration.setter
    def skip_service_registration(self, skip_service_registration):
        """Sets the skip_service_registration of this CreateMachineRequest.


        :param skip_service_registration: The skip_service_registration of this CreateMachineRequest.  # noqa: E501
        :type: bool
        """

        self._skip_service_registration = skip_service_registration

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
        if issubclass(CreateMachineRequest, dict):
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
        if not isinstance(other, CreateMachineRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateMachineRequest):
            return True

        return self.to_dict() != other.to_dict()
