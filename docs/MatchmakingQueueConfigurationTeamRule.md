# MatchmakingQueueConfigurationTeamRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difference_value** | **float** | A value difference. Must be specified if team rule checks difference between values. | [optional] 
**property_key** | **str** | Player property key. Must be specified if a rule is applied to player properties. | 
**type** | **str** | Team rule type. | 

## Example

```python
from fenrir_api.models.matchmaking_queue_configuration_team_rule import MatchmakingQueueConfigurationTeamRule

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueConfigurationTeamRule from a JSON string
matchmaking_queue_configuration_team_rule_instance = MatchmakingQueueConfigurationTeamRule.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueConfigurationTeamRule.to_json()

# convert the object into a dict
matchmaking_queue_configuration_team_rule_dict = matchmaking_queue_configuration_team_rule_instance.to_dict()
# create an instance of MatchmakingQueueConfigurationTeamRule from a dict
matchmaking_queue_configuration_team_rule_form_dict = matchmaking_queue_configuration_team_rule.from_dict(matchmaking_queue_configuration_team_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


