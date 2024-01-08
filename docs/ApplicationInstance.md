# ApplicationInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uuid** | **str** | A uuid of the application. | [optional] 
**container_id** | **str** | A unique id of the container | [optional] 
**created** | **datetime** | Time when the instance was created. | [optional] [readonly] 
**deployment_uuid** | **str** | A uuid of the deployment | [optional] 
**desired_state** | **str** | Desired state of the instance. Corresponds with docker container states. | [optional] 
**hostname** | **str** | A hostname of the node the instance is running on. | [optional] 
**ports** | [**List[ApplicationInstancePort]**](ApplicationInstancePort.md) | A list of ports exposed on the instance.  | [optional] 
**state** | **str** | State of the running instance. Corresponds with docker container states. | [optional] 
**updated** | **datetime** | Time when the instance was last updated. | [optional] [readonly] 
**uuid** | **str** | A unique id of the instance. | [optional] 

## Example

```python
from fenrir_api.models.application_instance import ApplicationInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstance from a JSON string
application_instance_instance = ApplicationInstance.from_json(json)
# print the JSON string representation of the object
print ApplicationInstance.to_json()

# convert the object into a dict
application_instance_dict = application_instance_instance.to_dict()
# create an instance of ApplicationInstance from a dict
application_instance_form_dict = application_instance.from_dict(application_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


