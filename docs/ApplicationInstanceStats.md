# ApplicationInstanceStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccu** | **int** | A number of players connected to this instance. | [optional] 
**cpu** | **float** | CPU utilization by this instance. | [optional] 
**mem** | **float** | Memory used by this instance, in megabytes. | [optional] 

## Example

```python
from fenrir_api.models.application_instance_stats import ApplicationInstanceStats

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstanceStats from a JSON string
application_instance_stats_instance = ApplicationInstanceStats.from_json(json)
# print the JSON string representation of the object
print ApplicationInstanceStats.to_json()

# convert the object into a dict
application_instance_stats_dict = application_instance_stats_instance.to_dict()
# create an instance of ApplicationInstanceStats from a dict
application_instance_stats_form_dict = application_instance_stats.from_dict(application_instance_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


