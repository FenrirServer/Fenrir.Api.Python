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

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from fenrir_api.models.matchmaking_queue_configuration_player_property import MatchmakingQueueConfigurationPlayerProperty
from fenrir_api.models.matchmaking_queue_configuration_player_rule import MatchmakingQueueConfigurationPlayerRule
from fenrir_api.models.matchmaking_queue_configuration_team import MatchmakingQueueConfigurationTeam
from fenrir_api.models.matchmaking_queue_configuration_team_rule import MatchmakingQueueConfigurationTeamRule
from typing import Optional, Set
from typing_extensions import Self

class MatchmakingQueueConfiguration(BaseModel):
    """
    MatchmakingQueueConfiguration
    """ # noqa: E501
    confirmation_required: Optional[StrictBool] = Field(default=None, description="A boolean value indicating if match confirmation is required. If set to true, players will receive confirmation event before the match is formed. All matched players must confirm their participation within a time specified with \"confirmation_time_seconds\", otherwise match is aborted.")
    confirmation_time_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A number of seconds given to players to confirm their match participation.")
    created: Optional[datetime] = Field(default=None, description="Time when the configuration was created.")
    deployment_uuid: StrictStr = Field(description="A uuid of the deployment this matchmaking queue will point at. When a match is formed, a server is selected from the specified deployment.")
    player_properties: Optional[List[MatchmakingQueueConfigurationPlayerProperty]] = Field(default=None, description="An array of player properties.")
    player_rules: Optional[List[MatchmakingQueueConfigurationPlayerRule]] = Field(default=None, description="An array of player rules.")
    team_rules: Optional[List[MatchmakingQueueConfigurationTeamRule]] = Field(default=None, description="An array of team rules.")
    teams: Optional[List[MatchmakingQueueConfigurationTeam]] = Field(default=None, description="An array of teams.")
    uuid: Optional[StrictStr] = Field(default=None, description="A unique id of the matchmaking queue configuration.")
    version: StrictStr = Field(description="A configuration schema version.")
    __properties: ClassVar[List[str]] = ["confirmation_required", "confirmation_time_seconds", "created", "deployment_uuid", "player_properties", "player_rules", "team_rules", "teams", "uuid", "version"]

    @field_validator('version')
    def version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['1.0']):
            raise ValueError("must be one of enum values ('1.0')")
        return value

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
        """Create an instance of MatchmakingQueueConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created",
            "uuid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in player_properties (list)
        _items = []
        if self.player_properties:
            for _item in self.player_properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['player_properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in player_rules (list)
        _items = []
        if self.player_rules:
            for _item in self.player_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['player_rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in team_rules (list)
        _items = []
        if self.team_rules:
            for _item in self.team_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['team_rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict['teams'] = _items
        # set to None if confirmation_time_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.confirmation_time_seconds is None and "confirmation_time_seconds" in self.model_fields_set:
            _dict['confirmation_time_seconds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchmakingQueueConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confirmation_required": obj.get("confirmation_required"),
            "confirmation_time_seconds": obj.get("confirmation_time_seconds"),
            "created": obj.get("created"),
            "deployment_uuid": obj.get("deployment_uuid"),
            "player_properties": [MatchmakingQueueConfigurationPlayerProperty.from_dict(_item) for _item in obj["player_properties"]] if obj.get("player_properties") is not None else None,
            "player_rules": [MatchmakingQueueConfigurationPlayerRule.from_dict(_item) for _item in obj["player_rules"]] if obj.get("player_rules") is not None else None,
            "team_rules": [MatchmakingQueueConfigurationTeamRule.from_dict(_item) for _item in obj["team_rules"]] if obj.get("team_rules") is not None else None,
            "teams": [MatchmakingQueueConfigurationTeam.from_dict(_item) for _item in obj["teams"]] if obj.get("teams") is not None else None,
            "uuid": obj.get("uuid"),
            "version": obj.get("version")
        })
        return _obj


