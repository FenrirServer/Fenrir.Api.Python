# ApplicationConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uuid** | **str** | A uuid of the application this configuration is for. | [optional] [readonly] 
**created** | **datetime** | Time when the configuration was created. | [optional] [readonly] 
**max_instances** | **int** | Maximum number of instances. | 
**min_instances** | **int** | Minimum number of instances. | 
**ports** | [**List[PortConfiguration]**](PortConfiguration.md) | Ports used by the application. | [optional] 
**updated** | **datetime** | Time when the configuration was last updated. | [optional] [readonly] 
**uuid** | **str** | A unique id of this application configuration. | [optional] [readonly] 

## Example

```python
from fenrir_api.models.application_configuration import ApplicationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationConfiguration from a JSON string
application_configuration_instance = ApplicationConfiguration.from_json(json)
# print the JSON string representation of the object
print ApplicationConfiguration.to_json()

# convert the object into a dict
application_configuration_dict = application_configuration_instance.to_dict()
# create an instance of ApplicationConfiguration from a dict
application_configuration_form_dict = application_configuration.from_dict(application_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


