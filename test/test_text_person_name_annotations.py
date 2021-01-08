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

import annotator
from annotator.models.text_person_name_annotations import TextPersonNameAnnotations  # noqa: E501
from annotator.rest import ApiException

class TestTextPersonNameAnnotations(unittest.TestCase):
    """TextPersonNameAnnotations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TextPersonNameAnnotations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = annotator.models.text_person_name_annotations.TextPersonNameAnnotations()  # noqa: E501
        if include_optional :
            return TextPersonNameAnnotations(
                text_person_name_annotations = [
                    {"start":42,"length":11,"text":"Chloe Price"}
                    ]
            )
        else :
            return TextPersonNameAnnotations(
        )

    def testTextPersonNameAnnotations(self):
        """Test TextPersonNameAnnotations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()