# DeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | [**Deployment**](Deployment.md) | An application deployment. | [optional] 

## Example

```python
from fenrir_api.models.deployment_response import DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentResponse from a JSON string
deployment_response_instance = DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentResponse.to_json()

# convert the object into a dict
deployment_response_dict = deployment_response_instance.to_dict()
# create an instance of DeploymentResponse from a dict
deployment_response_form_dict = deployment_response.from_dict(deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


