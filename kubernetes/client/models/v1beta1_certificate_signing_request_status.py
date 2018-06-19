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


class V1beta1CertificateSigningRequestStatus(object):
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
        'certificate': 'str',
        'conditions': 'list[V1beta1CertificateSigningRequestCondition]'
    }

    attribute_map = {
        'certificate': 'certificate',
        'conditions': 'conditions'
    }

    def __init__(self, certificate=None, conditions=None):
        """
        V1beta1CertificateSigningRequestStatus - a model defined in Swagger
        """

        self._certificate = None
        self._conditions = None
        self.discriminator = None

        if certificate is not None:
          self.certificate = certificate
        if conditions is not None:
          self.conditions = conditions

    @property
    def certificate(self):
        """
        Gets the certificate of this V1beta1CertificateSigningRequestStatus.
        If request was approved, the controller will place the issued certificate here.

        :return: The certificate of this V1beta1CertificateSigningRequestStatus.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this V1beta1CertificateSigningRequestStatus.
        If request was approved, the controller will place the issued certificate here.

        :param certificate: The certificate of this V1beta1CertificateSigningRequestStatus.
        :type: str
        """
        if certificate is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', certificate):
            raise ValueError("Invalid value for `certificate`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self._certificate = certificate

    @property
    def conditions(self):
        """
        Gets the conditions of this V1beta1CertificateSigningRequestStatus.
        Conditions applied to the request, such as approval or denial.

        :return: The conditions of this V1beta1CertificateSigningRequestStatus.
        :rtype: list[V1beta1CertificateSigningRequestCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1beta1CertificateSigningRequestStatus.
        Conditions applied to the request, such as approval or denial.

        :param conditions: The conditions of this V1beta1CertificateSigningRequestStatus.
        :type: list[V1beta1CertificateSigningRequestCondition]
        """

        self._conditions = conditions

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
        if not isinstance(other, V1beta1CertificateSigningRequestStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other