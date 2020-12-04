# coding: utf-8

"""
    NLP Sandbox Date Annotator API

    The OpenAPI specification implemented by NLP Sandbox Date Annotators. # Overview This NLP tool detects date references in the clinical note specified and returns a list of date annotations.   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import datanodeclient
from datanodeclient.models.text_date_annotations import TextDateAnnotations  # noqa: E501
from datanodeclient.rest import ApiException

class TestTextDateAnnotations(unittest.TestCase):
    """TextDateAnnotations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TextDateAnnotations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = datanodeclient.models.text_date_annotations.TextDateAnnotations()  # noqa: E501
        if include_optional :
            return TextDateAnnotations(
                text_date_annotations = [
                    {"start":42,"length":10,"text":"10/26/2020","dateFormat":"MM/DD/YYYY"}
                    ]
            )
        else :
            return TextDateAnnotations(
        )

    def testTextDateAnnotations(self):
        """Test TextDateAnnotations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
