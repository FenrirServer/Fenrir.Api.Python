# DeploymentStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**DeploymentStats**](DeploymentStats.md) | Deployment stats. | [optional] 

## Example

```python
from fenrir_api.models.deployment_stats_response import DeploymentStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatsResponse from a JSON string
deployment_stats_response_instance = DeploymentStatsResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentStatsResponse.to_json()

# convert the object into a dict
deployment_stats_response_dict = deployment_stats_response_instance.to_dict()
# create an instance of DeploymentStatsResponse from a dict
deployment_stats_response_form_dict = deployment_stats_response.from_dict(deployment_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


