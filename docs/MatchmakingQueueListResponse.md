# MatchmakingQueueListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queues** | [**List[MatchmakingQueue]**](MatchmakingQueue.md) | A list of matchmaking queues. | [optional] 

## Example

```python
from fenrir_api.models.matchmaking_queue_list_response import MatchmakingQueueListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueListResponse from a JSON string
matchmaking_queue_list_response_instance = MatchmakingQueueListResponse.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueListResponse.to_json()

# convert the object into a dict
matchmaking_queue_list_response_dict = matchmaking_queue_list_response_instance.to_dict()
# create an instance of MatchmakingQueueListResponse from a dict
matchmaking_queue_list_response_form_dict = matchmaking_queue_list_response.from_dict(matchmaking_queue_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


