# coding: utf-8

"""
    Fenrir Api

    # Introduction  The Fenrir Cloud API allows you to interact with Fenrir Cloud  and manage Applications, Deployments, and other resources  using conventional HTTP requests.    ## Authentication  The Fenrir Cloud API uses API keys for the authentication.  You can create new API keys in your Fenrir Cloud dashboard.  Your bearer API key must be set in the \"Authorization\" header, for example:  ```bash curl https://api.fenrircloud.com/1.0/api/applications \\    -H \"Accept: application/json\" \\    -H \"Authorization: Bearer FENRIR_API_KEY\" ```  ## Responses  When a request is successful, a response body will typically contain a JSON object.  For DELETE requests, a response with successful HTTP 204 NO_CONTENT status and a simple status will be returned.  For other request, a JSON object will contain a requested object. If list of objects is requested, an array of them will be returned instead.   ### Example Response (Single Object)  ```json {   \"application\": {     \"name\": \"my-app\",     ...   } } ```  ### Example Response (Multiple Objects)  ```json {   \"applications\":      [         {           \"name\": \"my-app\",           ...         },         {           \"name\": \"another-app\",           ...         }     ] } ```  ## Error Handling  Depending on the issue, a *4XX* status code will be returned.  A body will contain a JSON object with the details of the message.  Inside a JSON object, an error message will be included.   For 400 Bad Request errors caused by validation issues, additional `errors` key will be set. That key will contain a list of   ### Example Error Response  ```json {   \"message\": \"Invalid Request\",   \"errors\": [     {       \"field\": \"configuration.name\",       \"error\": \"must not contain special characters\"]     },     ...   ] } ```  

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from fenrir_api.models.api_token import ApiToken
from typing import Optional, Set
from typing_extensions import Self

class ApiTokenResponse(BaseModel):
    """
    ApiTokenResponse
    """ # noqa: E501
    api_token: Optional[ApiToken] = None
    __properties: ClassVar[List[str]] = ["api_token"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiTokenResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of api_token
        if self.api_token:
            _dict['api_token'] = self.api_token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict]) -> Optional[Self]:
        """Create an instance of ApiTokenResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "api_token": ApiToken.from_dict(obj["api_token"]) if obj.get("api_token") is not None else None
        })
        return _obj


