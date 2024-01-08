# ApplicationConfigurationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | [**List[ApplicationConfiguration]**](ApplicationConfiguration.md) | A list of application configurations. | [optional] 

## Example

```python
from fenrir_api.models.application_configuration_list_response import ApplicationConfigurationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationConfigurationListResponse from a JSON string
application_configuration_list_response_instance = ApplicationConfigurationListResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationConfigurationListResponse.to_json()

# convert the object into a dict
application_configuration_list_response_dict = application_configuration_list_response_instance.to_dict()
# create an instance of ApplicationConfigurationListResponse from a dict
application_configuration_list_response_form_dict = application_configuration_list_response.from_dict(application_configuration_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


