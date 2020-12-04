# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from datanodeclient.configuration import Configuration


class PageOfAnnotations(object):
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
        'offset': 'int',
        'limit': 'int',
        'links': 'ResponsePageMetadataLinks',
        'annotations': 'list[Annotation]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'links': 'links',
        'annotations': 'annotations'
    }

    def __init__(self, offset=None, limit=None, links=None, annotations=None, local_vars_configuration=None):  # noqa: E501
        """PageOfAnnotations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._offset = None
        self._limit = None
        self._links = None
        self._annotations = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.links = links
        if annotations is not None:
            self.annotations = annotations

    @property
    def offset(self):
        """Gets the offset of this PageOfAnnotations.  # noqa: E501

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfAnnotations.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfAnnotations.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfAnnotations.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfAnnotations.  # noqa: E501

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfAnnotations.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfAnnotations.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfAnnotations.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfAnnotations.  # noqa: E501


        :return: The links of this PageOfAnnotations.  # noqa: E501
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfAnnotations.


        :param links: The links of this PageOfAnnotations.  # noqa: E501
        :type: ResponsePageMetadataLinks
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def annotations(self):
        """Gets the annotations of this PageOfAnnotations.  # noqa: E501

        An array of annotations  # noqa: E501

        :return: The annotations of this PageOfAnnotations.  # noqa: E501
        :rtype: list[Annotation]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this PageOfAnnotations.

        An array of annotations  # noqa: E501

        :param annotations: The annotations of this PageOfAnnotations.  # noqa: E501
        :type: list[Annotation]
        """

        self._annotations = annotations

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
        if not isinstance(other, PageOfAnnotations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageOfAnnotations):
            return True

        return self.to_dict() != other.to_dict()
