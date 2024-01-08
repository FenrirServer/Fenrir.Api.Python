# MatchmakingQueueConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_required** | **bool** | A boolean value indicating if match confirmation is required. If set to true, players will receive confirmation event before the match is formed. All matched players must confirm their participation within a time specified with \&quot;confirmation_time_seconds\&quot;, otherwise match is aborted. | [optional] 
**confirmation_time_seconds** | **float** | A number of seconds given to players to confirm their match participation. | [optional] 
**created** | **datetime** | Time when the configuration was created. | [optional] [readonly] 
**deployment_uuid** | **str** | A uuid of the deployment this matchmaking queue will point at. When a match is formed, a server is selected from the specified deployment. | 
**player_properties** | [**List[MatchmakingQueueConfigurationPlayerProperty]**](MatchmakingQueueConfigurationPlayerProperty.md) | An array of player properties. | [optional] 
**player_rules** | [**List[MatchmakingQueueConfigurationPlayerRule]**](MatchmakingQueueConfigurationPlayerRule.md) | An array of player rules. | [optional] 
**team_rules** | [**List[MatchmakingQueueConfigurationTeamRule]**](MatchmakingQueueConfigurationTeamRule.md) | An array of team rules. | [optional] 
**teams** | [**List[MatchmakingQueueConfigurationTeam]**](MatchmakingQueueConfigurationTeam.md) | An array of teams. | [optional] 
**uuid** | **str** | A unique id of the matchmaking queue configuration. | [optional] [readonly] 
**version** | **str** | A configuration schema version. | 

## Example

```python
from fenrir_api.models.matchmaking_queue_configuration import MatchmakingQueueConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueConfiguration from a JSON string
matchmaking_queue_configuration_instance = MatchmakingQueueConfiguration.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueConfiguration.to_json()

# convert the object into a dict
matchmaking_queue_configuration_dict = matchmaking_queue_configuration_instance.to_dict()
# create an instance of MatchmakingQueueConfiguration from a dict
matchmaking_queue_configuration_form_dict = matchmaking_queue_configuration.from_dict(matchmaking_queue_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


