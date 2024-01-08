# MatchmakingQueueConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**MatchmakingQueueConfiguration**](MatchmakingQueueConfiguration.md) |  | [optional] 

## Example

```python
from fenrir_api.models.matchmaking_queue_configuration_response import MatchmakingQueueConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueConfigurationResponse from a JSON string
matchmaking_queue_configuration_response_instance = MatchmakingQueueConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueConfigurationResponse.to_json()

# convert the object into a dict
matchmaking_queue_configuration_response_dict = matchmaking_queue_configuration_response_instance.to_dict()
# create an instance of MatchmakingQueueConfigurationResponse from a dict
matchmaking_queue_configuration_response_form_dict = matchmaking_queue_configuration_response.from_dict(matchmaking_queue_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


