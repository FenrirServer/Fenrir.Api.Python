# coding: utf-8

# flake8: noqa

"""
    Fenrir Api

    # Introduction  The Fenrir Cloud API allows you to interact with Fenrir Cloud  and manage Applications, Deployments, and other resources  using conventional HTTP requests.    ## Authentication  The Fenrir Cloud API uses API keys for the authentication.  You can create new API keys in your Fenrir Cloud dashboard.  Your bearer API key must be set in the \"Authorization\" header, for example:  ```bash curl https://api.fenrircloud.com/1.0/api/applications \\    -H \"Accept: application/json\" \\    -H \"Authorization: Bearer FENRIR_API_KEY\" ```  ## Responses  When a request is successful, a response body will typically contain a JSON object.  For DELETE requests, a response with successful HTTP 204 NO_CONTENT status and a simple status will be returned.  For other request, a JSON object will contain a requested object. If list of objects is requested, an array of them will be returned instead.   ### Example Response (Single Object)  ```json {   \"application\": {     \"name\": \"my-app\",     ...   } } ```  ### Example Response (Multiple Objects)  ```json {   \"applications\":      [         {           \"name\": \"my-app\",           ...         },         {           \"name\": \"another-app\",           ...         }     ] } ```  ## Error Handling  Depending on the issue, a *4XX* status code will be returned.  A body will contain a JSON object with the details of the message.  Inside a JSON object, an error message will be included.   For 400 Bad Request errors caused by validation issues, additional `errors` key will be set. That key will contain a list of   ### Example Error Response  ```json {   \"message\": \"Invalid Request\",   \"errors\": [     {       \"field\": \"configuration.name\",       \"error\": \"must not contain special characters\"]     },     ...   ] } ```  

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.0"

# import apis into sdk package
from fenrir_api.api.fenrir_api import FenrirApi

# import ApiClient
from fenrir_api.api_response import ApiResponse
from fenrir_api.api_client import ApiClient
from fenrir_api.configuration import Configuration
from fenrir_api.exceptions import OpenApiException
from fenrir_api.exceptions import ApiTypeError
from fenrir_api.exceptions import ApiValueError
from fenrir_api.exceptions import ApiKeyError
from fenrir_api.exceptions import ApiAttributeError
from fenrir_api.exceptions import ApiException

# import models into sdk package
from fenrir_api.models.api_token import ApiToken
from fenrir_api.models.api_token_list_response import ApiTokenListResponse
from fenrir_api.models.api_token_response import ApiTokenResponse
from fenrir_api.models.application import Application
from fenrir_api.models.application_configuration import ApplicationConfiguration
from fenrir_api.models.application_configuration_list_response import ApplicationConfigurationListResponse
from fenrir_api.models.application_configuration_response import ApplicationConfigurationResponse
from fenrir_api.models.application_instance import ApplicationInstance
from fenrir_api.models.application_instance_list_response import ApplicationInstanceListResponse
from fenrir_api.models.application_instance_port import ApplicationInstancePort
from fenrir_api.models.application_instance_response import ApplicationInstanceResponse
from fenrir_api.models.application_instance_stats import ApplicationInstanceStats
from fenrir_api.models.application_list_response import ApplicationListResponse
from fenrir_api.models.application_response import ApplicationResponse
from fenrir_api.models.application_stats import ApplicationStats
from fenrir_api.models.application_stats_response import ApplicationStatsResponse
from fenrir_api.models.bad_request_response import BadRequestResponse
from fenrir_api.models.deployment import Deployment
from fenrir_api.models.deployment_list_response import DeploymentListResponse
from fenrir_api.models.deployment_response import DeploymentResponse
from fenrir_api.models.deployment_stats import DeploymentStats
from fenrir_api.models.deployment_stats_response import DeploymentStatsResponse
from fenrir_api.models.image import Image
from fenrir_api.models.image_list_response import ImageListResponse
from fenrir_api.models.instance_logs import InstanceLogs
from fenrir_api.models.instance_logs_preview import InstanceLogsPreview
from fenrir_api.models.matchmaking_queue import MatchmakingQueue
from fenrir_api.models.matchmaking_queue_configuration import MatchmakingQueueConfiguration
from fenrir_api.models.matchmaking_queue_configuration_list_response import MatchmakingQueueConfigurationListResponse
from fenrir_api.models.matchmaking_queue_configuration_player_property import MatchmakingQueueConfigurationPlayerProperty
from fenrir_api.models.matchmaking_queue_configuration_player_rule import MatchmakingQueueConfigurationPlayerRule
from fenrir_api.models.matchmaking_queue_configuration_response import MatchmakingQueueConfigurationResponse
from fenrir_api.models.matchmaking_queue_configuration_team import MatchmakingQueueConfigurationTeam
from fenrir_api.models.matchmaking_queue_configuration_team_rule import MatchmakingQueueConfigurationTeamRule
from fenrir_api.models.matchmaking_queue_list_response import MatchmakingQueueListResponse
from fenrir_api.models.matchmaking_queue_response import MatchmakingQueueResponse
from fenrir_api.models.not_found_response import NotFoundResponse
from fenrir_api.models.port_configuration import PortConfiguration
from fenrir_api.models.response import Response
from fenrir_api.models.validation_error import ValidationError