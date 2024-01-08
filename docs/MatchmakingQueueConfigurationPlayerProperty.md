# MatchmakingQueueConfigurationPlayerProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** | A default value for a property. If \&quot;required\&quot; is set to false, this default value will be used for tickets that did not specify this property. | [optional] 
**key** | **str** | A unique key of the property. | 
**required** | **bool** | A boolean value indicating if this property is required. If set to true, all matchmaking tickets must have this property. | [optional] 
**type** | **str** | Player property type. Must be \&quot;int\&quot;, \&quot;string\&quot;, \&quot;bool\&quot; or \&quot;float\&quot;. | 

## Example

```python
from fenrir_api.models.matchmaking_queue_configuration_player_property import MatchmakingQueueConfigurationPlayerProperty

# TODO update the JSON string below
json = "{}"
# create an instance of MatchmakingQueueConfigurationPlayerProperty from a JSON string
matchmaking_queue_configuration_player_property_instance = MatchmakingQueueConfigurationPlayerProperty.from_json(json)
# print the JSON string representation of the object
print MatchmakingQueueConfigurationPlayerProperty.to_json()

# convert the object into a dict
matchmaking_queue_configuration_player_property_dict = matchmaking_queue_configuration_player_property_instance.to_dict()
# create an instance of MatchmakingQueueConfigurationPlayerProperty from a dict
matchmaking_queue_configuration_player_property_form_dict = matchmaking_queue_configuration_player_property.from_dict(matchmaking_queue_configuration_player_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


