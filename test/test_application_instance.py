# coding: utf-8

"""
    Fenrir Api

    # Introduction  The Fenrir Cloud API allows you to interact with Fenrir Cloud  and manage Applications, Deployments, and other resources  using conventional HTTP requests.    ## Authentication  The Fenrir Cloud API uses API keys for the authentication.  You can create new API keys in your Fenrir Cloud dashboard.  Your bearer API key must be set in the \"Authorization\" header, for example:  ```bash curl https://api.fenrircloud.com/1.0/api/applications \\    -H \"Accept: application/json\" \\    -H \"Authorization: Bearer FENRIR_API_KEY\" ```  ## Responses  When a request is successful, a response body will typically contain a JSON object.  For DELETE requests, a response with successful HTTP 204 NO_CONTENT status and a simple status will be returned.  For other request, a JSON object will contain a requested object. If list of objects is requested, an array of them will be returned instead.   ### Example Response (Single Object)  ```json {   \"application\": {     \"name\": \"my-app\",     ...   } } ```  ### Example Response (Multiple Objects)  ```json {   \"applications\":      [         {           \"name\": \"my-app\",           ...         },         {           \"name\": \"another-app\",           ...         }     ] } ```  ## Error Handling  Depending on the issue, a *4XX* status code will be returned.  A body will contain a JSON object with the details of the message.  Inside a JSON object, an error message will be included.   For 400 Bad Request errors caused by validation issues, additional `errors` key will be set. That key will contain a list of   ### Example Error Response  ```json {   \"message\": \"Invalid Request\",   \"errors\": [     {       \"field\": \"configuration.name\",       \"error\": \"must not contain special characters\"]     },     ...   ] } ```  

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fenrir_api.models.application_instance import ApplicationInstance

class TestApplicationInstance(unittest.TestCase):
    """ApplicationInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationInstance:
        """Test ApplicationInstance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationInstance`
        """
        model = ApplicationInstance()
        if include_optional:
            return ApplicationInstance(
                application_uuid = '7bc16159acff4b689fe7224a7c79fb96',
                container_id = '0d65495b663f42ef835cc2801fb9feba',
                created = '2024-01-22T19:28:42Z',
                deployment_uuid = 'f01ffac3b2774b0fb95c0b510292e3f7',
                desired_state = 'running',
                hostname = 'host001.fenrircloud.com',
                ports = [
                    fenrir_api.models.application_instance_port.ApplicationInstancePort(
                        protocol = 'udp', 
                        published_port = 27012, 
                        target_port = 27000, )
                    ],
                state = 'created',
                updated = '2024-01-22T19:28:42Z',
                uuid = 'be29c08199514affa4580f4d4d2fecd1'
            )
        else:
            return ApplicationInstance(
        )
        """

    def testApplicationInstance(self):
        """Test ApplicationInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
