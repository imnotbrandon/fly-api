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


class ApiMachineConfig(object):
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
        'auto_destroy': 'bool',
        'checks': 'dict(str, ApiMachineCheck)',
        'disable_machine_autostart': 'bool',
        'dns': 'ApiDNSConfig',
        'env': 'dict(str, str)',
        'files': 'list[ApiFile]',
        'guest': 'ApiMachineGuest',
        'image': 'str',
        'init': 'ApiMachineInit',
        'metadata': 'dict(str, str)',
        'metrics': 'ApiMachineMetrics',
        'mounts': 'list[ApiMachineMount]',
        'processes': 'list[ApiMachineProcess]',
        'restart': 'ApiMachineRestart',
        'schedule': 'str',
        'services': 'list[ApiMachineService]',
        'size': 'str',
        'standbys': 'list[str]',
        'statics': 'list[ApiStatic]',
        'stop_config': 'ApiStopConfig'
    }

    attribute_map = {
        'auto_destroy': 'auto_destroy',
        'checks': 'checks',
        'disable_machine_autostart': 'disable_machine_autostart',
        'dns': 'dns',
        'env': 'env',
        'files': 'files',
        'guest': 'guest',
        'image': 'image',
        'init': 'init',
        'metadata': 'metadata',
        'metrics': 'metrics',
        'mounts': 'mounts',
        'processes': 'processes',
        'restart': 'restart',
        'schedule': 'schedule',
        'services': 'services',
        'size': 'size',
        'standbys': 'standbys',
        'statics': 'statics',
        'stop_config': 'stop_config'
    }

    def __init__(self, auto_destroy=None, checks=None, disable_machine_autostart=None, dns=None, env=None, files=None, guest=None, image=None, init=None, metadata=None, metrics=None, mounts=None, processes=None, restart=None, schedule=None, services=None, size=None, standbys=None, statics=None, stop_config=None, _configuration=None):  # noqa: E501
        """ApiMachineConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_destroy = None
        self._checks = None
        self._disable_machine_autostart = None
        self._dns = None
        self._env = None
        self._files = None
        self._guest = None
        self._image = None
        self._init = None
        self._metadata = None
        self._metrics = None
        self._mounts = None
        self._processes = None
        self._restart = None
        self._schedule = None
        self._services = None
        self._size = None
        self._standbys = None
        self._statics = None
        self._stop_config = None
        self.discriminator = None

        if auto_destroy is not None:
            self.auto_destroy = auto_destroy
        if checks is not None:
            self.checks = checks
        if disable_machine_autostart is not None:
            self.disable_machine_autostart = disable_machine_autostart
        if dns is not None:
            self.dns = dns
        if env is not None:
            self.env = env
        if files is not None:
            self.files = files
        if guest is not None:
            self.guest = guest
        if image is not None:
            self.image = image
        if init is not None:
            self.init = init
        if metadata is not None:
            self.metadata = metadata
        if metrics is not None:
            self.metrics = metrics
        if mounts is not None:
            self.mounts = mounts
        if processes is not None:
            self.processes = processes
        if restart is not None:
            self.restart = restart
        if schedule is not None:
            self.schedule = schedule
        if services is not None:
            self.services = services
        if size is not None:
            self.size = size
        if standbys is not None:
            self.standbys = standbys
        if statics is not None:
            self.statics = statics
        if stop_config is not None:
            self.stop_config = stop_config

    @property
    def auto_destroy(self):
        """Gets the auto_destroy of this ApiMachineConfig.  # noqa: E501

        Optional boolean telling the Machine to destroy itself once it’s complete (default false)  # noqa: E501

        :return: The auto_destroy of this ApiMachineConfig.  # noqa: E501
        :rtype: bool
        """
        return self._auto_destroy

    @auto_destroy.setter
    def auto_destroy(self, auto_destroy):
        """Sets the auto_destroy of this ApiMachineConfig.

        Optional boolean telling the Machine to destroy itself once it’s complete (default false)  # noqa: E501

        :param auto_destroy: The auto_destroy of this ApiMachineConfig.  # noqa: E501
        :type: bool
        """

        self._auto_destroy = auto_destroy

    @property
    def checks(self):
        """Gets the checks of this ApiMachineConfig.  # noqa: E501


        :return: The checks of this ApiMachineConfig.  # noqa: E501
        :rtype: dict(str, ApiMachineCheck)
        """
        return self._checks

    @checks.setter
    def checks(self, checks):
        """Sets the checks of this ApiMachineConfig.


        :param checks: The checks of this ApiMachineConfig.  # noqa: E501
        :type: dict(str, ApiMachineCheck)
        """

        self._checks = checks

    @property
    def disable_machine_autostart(self):
        """Gets the disable_machine_autostart of this ApiMachineConfig.  # noqa: E501

        Deprecated: use Service.Autostart instead  # noqa: E501

        :return: The disable_machine_autostart of this ApiMachineConfig.  # noqa: E501
        :rtype: bool
        """
        return self._disable_machine_autostart

    @disable_machine_autostart.setter
    def disable_machine_autostart(self, disable_machine_autostart):
        """Sets the disable_machine_autostart of this ApiMachineConfig.

        Deprecated: use Service.Autostart instead  # noqa: E501

        :param disable_machine_autostart: The disable_machine_autostart of this ApiMachineConfig.  # noqa: E501
        :type: bool
        """

        self._disable_machine_autostart = disable_machine_autostart

    @property
    def dns(self):
        """Gets the dns of this ApiMachineConfig.  # noqa: E501


        :return: The dns of this ApiMachineConfig.  # noqa: E501
        :rtype: ApiDNSConfig
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this ApiMachineConfig.


        :param dns: The dns of this ApiMachineConfig.  # noqa: E501
        :type: ApiDNSConfig
        """

        self._dns = dns

    @property
    def env(self):
        """Gets the env of this ApiMachineConfig.  # noqa: E501

        An object filled with key/value pairs to be set as environment variables  # noqa: E501

        :return: The env of this ApiMachineConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this ApiMachineConfig.

        An object filled with key/value pairs to be set as environment variables  # noqa: E501

        :param env: The env of this ApiMachineConfig.  # noqa: E501
        :type: dict(str, str)
        """

        self._env = env

    @property
    def files(self):
        """Gets the files of this ApiMachineConfig.  # noqa: E501


        :return: The files of this ApiMachineConfig.  # noqa: E501
        :rtype: list[ApiFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ApiMachineConfig.


        :param files: The files of this ApiMachineConfig.  # noqa: E501
        :type: list[ApiFile]
        """

        self._files = files

    @property
    def guest(self):
        """Gets the guest of this ApiMachineConfig.  # noqa: E501


        :return: The guest of this ApiMachineConfig.  # noqa: E501
        :rtype: ApiMachineGuest
        """
        return self._guest

    @guest.setter
    def guest(self, guest):
        """Sets the guest of this ApiMachineConfig.


        :param guest: The guest of this ApiMachineConfig.  # noqa: E501
        :type: ApiMachineGuest
        """

        self._guest = guest

    @property
    def image(self):
        """Gets the image of this ApiMachineConfig.  # noqa: E501

        The docker image to run  # noqa: E501

        :return: The image of this ApiMachineConfig.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ApiMachineConfig.

        The docker image to run  # noqa: E501

        :param image: The image of this ApiMachineConfig.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def init(self):
        """Gets the init of this ApiMachineConfig.  # noqa: E501


        :return: The init of this ApiMachineConfig.  # noqa: E501
        :rtype: ApiMachineInit
        """
        return self._init

    @init.setter
    def init(self, init):
        """Sets the init of this ApiMachineConfig.


        :param init: The init of this ApiMachineConfig.  # noqa: E501
        :type: ApiMachineInit
        """

        self._init = init

    @property
    def metadata(self):
        """Gets the metadata of this ApiMachineConfig.  # noqa: E501


        :return: The metadata of this ApiMachineConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ApiMachineConfig.


        :param metadata: The metadata of this ApiMachineConfig.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def metrics(self):
        """Gets the metrics of this ApiMachineConfig.  # noqa: E501


        :return: The metrics of this ApiMachineConfig.  # noqa: E501
        :rtype: ApiMachineMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ApiMachineConfig.


        :param metrics: The metrics of this ApiMachineConfig.  # noqa: E501
        :type: ApiMachineMetrics
        """

        self._metrics = metrics

    @property
    def mounts(self):
        """Gets the mounts of this ApiMachineConfig.  # noqa: E501


        :return: The mounts of this ApiMachineConfig.  # noqa: E501
        :rtype: list[ApiMachineMount]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this ApiMachineConfig.


        :param mounts: The mounts of this ApiMachineConfig.  # noqa: E501
        :type: list[ApiMachineMount]
        """

        self._mounts = mounts

    @property
    def processes(self):
        """Gets the processes of this ApiMachineConfig.  # noqa: E501


        :return: The processes of this ApiMachineConfig.  # noqa: E501
        :rtype: list[ApiMachineProcess]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        """Sets the processes of this ApiMachineConfig.


        :param processes: The processes of this ApiMachineConfig.  # noqa: E501
        :type: list[ApiMachineProcess]
        """

        self._processes = processes

    @property
    def restart(self):
        """Gets the restart of this ApiMachineConfig.  # noqa: E501


        :return: The restart of this ApiMachineConfig.  # noqa: E501
        :rtype: ApiMachineRestart
        """
        return self._restart

    @restart.setter
    def restart(self, restart):
        """Sets the restart of this ApiMachineConfig.


        :param restart: The restart of this ApiMachineConfig.  # noqa: E501
        :type: ApiMachineRestart
        """

        self._restart = restart

    @property
    def schedule(self):
        """Gets the schedule of this ApiMachineConfig.  # noqa: E501


        :return: The schedule of this ApiMachineConfig.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ApiMachineConfig.


        :param schedule: The schedule of this ApiMachineConfig.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def services(self):
        """Gets the services of this ApiMachineConfig.  # noqa: E501


        :return: The services of this ApiMachineConfig.  # noqa: E501
        :rtype: list[ApiMachineService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ApiMachineConfig.


        :param services: The services of this ApiMachineConfig.  # noqa: E501
        :type: list[ApiMachineService]
        """

        self._services = services

    @property
    def size(self):
        """Gets the size of this ApiMachineConfig.  # noqa: E501

        Deprecated: use Guest instead  # noqa: E501

        :return: The size of this ApiMachineConfig.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ApiMachineConfig.

        Deprecated: use Guest instead  # noqa: E501

        :param size: The size of this ApiMachineConfig.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def standbys(self):
        """Gets the standbys of this ApiMachineConfig.  # noqa: E501

        Standbys enable a machine to be a standby for another. In the event of a hardware failure, the standby machine will be started.  # noqa: E501

        :return: The standbys of this ApiMachineConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._standbys

    @standbys.setter
    def standbys(self, standbys):
        """Sets the standbys of this ApiMachineConfig.

        Standbys enable a machine to be a standby for another. In the event of a hardware failure, the standby machine will be started.  # noqa: E501

        :param standbys: The standbys of this ApiMachineConfig.  # noqa: E501
        :type: list[str]
        """

        self._standbys = standbys

    @property
    def statics(self):
        """Gets the statics of this ApiMachineConfig.  # noqa: E501


        :return: The statics of this ApiMachineConfig.  # noqa: E501
        :rtype: list[ApiStatic]
        """
        return self._statics

    @statics.setter
    def statics(self, statics):
        """Sets the statics of this ApiMachineConfig.


        :param statics: The statics of this ApiMachineConfig.  # noqa: E501
        :type: list[ApiStatic]
        """

        self._statics = statics

    @property
    def stop_config(self):
        """Gets the stop_config of this ApiMachineConfig.  # noqa: E501


        :return: The stop_config of this ApiMachineConfig.  # noqa: E501
        :rtype: ApiStopConfig
        """
        return self._stop_config

    @stop_config.setter
    def stop_config(self, stop_config):
        """Sets the stop_config of this ApiMachineConfig.


        :param stop_config: The stop_config of this ApiMachineConfig.  # noqa: E501
        :type: ApiStopConfig
        """

        self._stop_config = stop_config

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
        if issubclass(ApiMachineConfig, dict):
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
        if not isinstance(other, ApiMachineConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiMachineConfig):
            return True

        return self.to_dict() != other.to_dict()