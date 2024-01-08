# MatchmakingQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uuid** | **str** | A uuid of the application this queue is for. | [optional] [readonly] 
**configuration** | [**MatchmakingQueueConfiguration**](MatchmakingQueueConfiguration.md) |  | 
**created** | **datetime** | Time when the matchmaking queue was created. | [optional] [readonly] 
**name** | **str** | A name of the matchmaking queue. | 
**updated** | **datetime** | Time when the matchmaking queue was last updated. | [optional] [readonly] 
**uuid** | **str** | A unique id of the matchmaking queue. | [optional] [readonly] 

## Example

```python
from fenrir_api.models.matchmaking_queue import MatchmakingQueue

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueue from a JSON string
matchmaking_queue_instance = MatchmakingQueue.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueue.to_json()

# convert the object into a dict
matchmaking_queue_dict = matchmaking_queue_instance.to_dict()
# create an instance of MatchmakingQueue from a dict
matchmaking_queue_form_dict = matchmaking_queue.from_dict(matchmaking_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


