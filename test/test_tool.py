"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.model.license import License
from nlpsandbox.model.tool_type import ToolType
globals()['License'] = License
globals()['ToolType'] = ToolType
from nlpsandbox.model.tool import Tool


class TestTool(unittest.TestCase):
    """Tool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTool(self):
        """Test Tool"""
        Tool(name="foo", version="1.0.0", license=License("apache-2.0"),
             repository="www.google.com", description="foobar",
             author="Bob", author_email="email@email.com", url="www.google.com",
             type=ToolType("nlpsandbox:date-annotator"), api_version="1.0.0")


if __name__ == '__main__':
    unittest.main()
