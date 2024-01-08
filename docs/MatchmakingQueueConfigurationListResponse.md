# MatchmakingQueueConfigurationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | [**List[MatchmakingQueueConfiguration]**](MatchmakingQueueConfiguration.md) | A list of matchmaking queue configurations. | [optional] 

## Example

```python
from fenrir_api.models.matchmaking_queue_configuration_list_response import MatchmakingQueueConfigurationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueConfigurationListResponse from a JSON string
matchmaking_queue_configuration_list_response_instance = MatchmakingQueueConfigurationListResponse.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueConfigurationListResponse.to_json()

# convert the object into a dict
matchmaking_queue_configuration_list_response_dict = matchmaking_queue_configuration_list_response_instance.to_dict()
# create an instance of MatchmakingQueueConfigurationListResponse from a dict
matchmaking_queue_configuration_list_response_form_dict = matchmaking_queue_configuration_list_response.from_dict(matchmaking_queue_configuration_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


