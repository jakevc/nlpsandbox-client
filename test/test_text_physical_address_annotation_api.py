# coding: utf-8

"""
    NLP Sandbox Physical Address Annotator API

    The OpenAPI specification implemented by NLP Sandbox Physical Address Annotators. # Overview This NLP tool detects references of physical addresses in the clinical notes given as input and returns a list of physical address annotations.   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import addressannotator
from addressannotator.api.text_physical_address_annotation_api import TextPhysicalAddressAnnotationApi  # noqa: E501
from addressannotator.rest import ApiException


class TestTextPhysicalAddressAnnotationApi(unittest.TestCase):
    """TextPhysicalAddressAnnotationApi unit test stubs"""

    def setUp(self):
        self.api = addressannotator.api.text_physical_address_annotation_api.TextPhysicalAddressAnnotationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_text_physical_address_annotations(self):
        """Test case for create_text_physical_address_annotations

        Annotate physical addresses in a clinical note  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
