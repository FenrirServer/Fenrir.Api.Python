# DeploymentStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccu_total** | **int** | A number of players currently connected. | [optional] 
**cpu_avg** | **float** | The average CPU utilization of the application across all instances in this deployment. | [optional] 
**instance_stats** | [**Dict[str, ApplicationInstanceStats]**](ApplicationInstanceStats.md) | A dictionary of instance stats, per instance. | [optional] 
**mem_avg** | **float** | The average memory utilization of the application across all instances in this deployment, in megabytes. | [optional] 
**num_instances** | **int** | The total number of instances in this deployment. | [optional] 

## Example

```python
from fenrir_api.models.deployment_stats import DeploymentStats

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStats from a JSON string
deployment_stats_instance = DeploymentStats.from_json(json)
# print the JSON string representation of the object
print DeploymentStats.to_json()

# convert the object into a dict
deployment_stats_dict = deployment_stats_instance.to_dict()
# create an instance of DeploymentStats from a dict
deployment_stats_form_dict = deployment_stats.from_dict(deployment_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


