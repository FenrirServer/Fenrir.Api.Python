# ApplicationStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccu_total** | **int** | A number of players currently connected. | [optional] 
**cpu_avg** | **float** | The average CPU utilization of the application across all instances. | [optional] 
**mem_avg** | **float** | The average memory utilization of the application across all instances, in megabytes. | [optional] 
**num_deployments** | **int** | The total number of deployments of the application. | [optional] 
**num_instances** | **int** | The total number of instances of the application across all deployments | [optional] 

## Example

```python
from fenrir_api.models.application_stats import ApplicationStats

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationStats from a JSON string
application_stats_instance = ApplicationStats.from_json(json)
# print the JSON string representation of the object
print ApplicationStats.to_json()

# convert the object into a dict
application_stats_dict = application_stats_instance.to_dict()
# create an instance of ApplicationStats from a dict
application_stats_form_dict = application_stats.from_dict(application_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


