# MatchmakingQueueConfigurationTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_players** | **int** | A maximum number of players this team may have. | 
**min_players** | **int** | A minimum number of players this team must have. | [optional] 
**name** | **str** | A unique name of the team. | 

## Example

```python
from fenrir_api.models.matchmaking_queue_configuration_team import MatchmakingQueueConfigurationTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueConfigurationTeam from a JSON string
matchmaking_queue_configuration_team_instance = MatchmakingQueueConfigurationTeam.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueConfigurationTeam.to_json()

# convert the object into a dict
matchmaking_queue_configuration_team_dict = matchmaking_queue_configuration_team_instance.to_dict()
# create an instance of MatchmakingQueueConfigurationTeam from a dict
matchmaking_queue_configuration_team_form_dict = matchmaking_queue_configuration_team.from_dict(matchmaking_queue_configuration_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


