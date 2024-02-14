# ApplicationStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**ApplicationStats**](ApplicationStats.md) | Application stats. | [optional] 

## Example

```python
from fenrir_api.models.application_stats_response import ApplicationStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationStatsResponse from a JSON string
application_stats_response_instance = ApplicationStatsResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationStatsResponse.to_json()

# convert the object into a dict
application_stats_response_dict = application_stats_response_instance.to_dict()
# create an instance of ApplicationStatsResponse from a dict
application_stats_response_form_dict = application_stats_response.from_dict(application_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


