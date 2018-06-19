# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1LimitRangeItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'default': 'dict(str, str)',
        'default_request': 'dict(str, str)',
        'max': 'dict(str, str)',
        'max_limit_request_ratio': 'dict(str, str)',
        'min': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'default': 'default',
        'default_request': 'defaultRequest',
        'max': 'max',
        'max_limit_request_ratio': 'maxLimitRequestRatio',
        'min': 'min',
        'type': 'type'
    }

    def __init__(self, default=None, default_request=None, max=None, max_limit_request_ratio=None, min=None, type=None):
        """
        V1LimitRangeItem - a model defined in Swagger
        """

        self._default = None
        self._default_request = None
        self._max = None
        self._max_limit_request_ratio = None
        self._min = None
        self._type = None
        self.discriminator = None

        if default is not None:
          self.default = default
        if default_request is not None:
          self.default_request = default_request
        if max is not None:
          self.max = max
        if max_limit_request_ratio is not None:
          self.max_limit_request_ratio = max_limit_request_ratio
        if min is not None:
          self.min = min
        if type is not None:
          self.type = type

    @property
    def default(self):
        """
        Gets the default of this V1LimitRangeItem.
        Default resource requirement limit value by resource name if resource limit is omitted.

        :return: The default of this V1LimitRangeItem.
        :rtype: dict(str, str)
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this V1LimitRangeItem.
        Default resource requirement limit value by resource name if resource limit is omitted.

        :param default: The default of this V1LimitRangeItem.
        :type: dict(str, str)
        """

        self._default = default

    @property
    def default_request(self):
        """
        Gets the default_request of this V1LimitRangeItem.
        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.

        :return: The default_request of this V1LimitRangeItem.
        :rtype: dict(str, str)
        """
        return self._default_request

    @default_request.setter
    def default_request(self, default_request):
        """
        Sets the default_request of this V1LimitRangeItem.
        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.

        :param default_request: The default_request of this V1LimitRangeItem.
        :type: dict(str, str)
        """

        self._default_request = default_request

    @property
    def max(self):
        """
        Gets the max of this V1LimitRangeItem.
        Max usage constraints on this kind by resource name.

        :return: The max of this V1LimitRangeItem.
        :rtype: dict(str, str)
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this V1LimitRangeItem.
        Max usage constraints on this kind by resource name.

        :param max: The max of this V1LimitRangeItem.
        :type: dict(str, str)
        """

        self._max = max

    @property
    def max_limit_request_ratio(self):
        """
        Gets the max_limit_request_ratio of this V1LimitRangeItem.
        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.

        :return: The max_limit_request_ratio of this V1LimitRangeItem.
        :rtype: dict(str, str)
        """
        return self._max_limit_request_ratio

    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, max_limit_request_ratio):
        """
        Sets the max_limit_request_ratio of this V1LimitRangeItem.
        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.

        :param max_limit_request_ratio: The max_limit_request_ratio of this V1LimitRangeItem.
        :type: dict(str, str)
        """

        self._max_limit_request_ratio = max_limit_request_ratio

    @property
    def min(self):
        """
        Gets the min of this V1LimitRangeItem.
        Min usage constraints on this kind by resource name.

        :return: The min of this V1LimitRangeItem.
        :rtype: dict(str, str)
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this V1LimitRangeItem.
        Min usage constraints on this kind by resource name.

        :param min: The min of this V1LimitRangeItem.
        :type: dict(str, str)
        """

        self._min = min

    @property
    def type(self):
        """
        Gets the type of this V1LimitRangeItem.
        Type of resource that this limit applies to.

        :return: The type of this V1LimitRangeItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1LimitRangeItem.
        Type of resource that this limit applies to.

        :param type: The type of this V1LimitRangeItem.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1LimitRangeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other