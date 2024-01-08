# Deployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uuid** | **str** | A uuid of the application this deployment is for. | [optional] [readonly] 
**configuration_uuid** | **str** | A uuid of the current application configuration. | [optional] [readonly] 
**created** | **datetime** | Time when the deployment was created. | [optional] [readonly] 
**image_tag** | **str** | An image tag for your application. Possible image tags can be obtained by calling \&quot;GET /application/&lt;application_uuid&gt;/images\&quot; endpoint | 
**label** | **str** | A label for your deployment | 
**updated** | **datetime** | Time when the deployment was last updated. | [optional] [readonly] 
**uuid** | **str** | A unique id of the deployment. | [optional] [readonly] 

## Example

```python
from fenrir_api.models.deployment import Deployment

# TODO update the JSON string below
json = "{}"
# create an instance of Deployment from a JSON string
deployment_instance = Deployment.from_json(json)
# print the JSON string representation of the object
print Deployment.to_json()

# convert the object into a dict
deployment_dict = deployment_instance.to_dict()
# create an instance of Deployment from a dict
deployment_form_dict = deployment.from_dict(deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


