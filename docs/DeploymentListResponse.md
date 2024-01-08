# DeploymentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployments** | [**List[Deployment]**](Deployment.md) | A list of application deployments. | [optional] 

## Example

```python
from fenrir_api.models.deployment_list_response import DeploymentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentListResponse from a JSON string
deployment_list_response_instance = DeploymentListResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentListResponse.to_json()

# convert the object into a dict
deployment_list_response_dict = deployment_list_response_instance.to_dict()
# create an instance of DeploymentListResponse from a dict
deployment_list_response_form_dict = deployment_list_response.from_dict(deployment_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


