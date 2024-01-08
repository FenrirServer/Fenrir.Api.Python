# MatchmakingQueueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue** | [**MatchmakingQueue**](MatchmakingQueue.md) |  | [optional] 

## Example

```python
from fenrir_api.models.matchmaking_queue_response import MatchmakingQueueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueResponse from a JSON string
matchmaking_queue_response_instance = MatchmakingQueueResponse.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueResponse.to_json()

# convert the object into a dict
matchmaking_queue_response_dict = matchmaking_queue_response_instance.to_dict()
# create an instance of MatchmakingQueueResponse from a dict
matchmaking_queue_response_form_dict = matchmaking_queue_response.from_dict(matchmaking_queue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


