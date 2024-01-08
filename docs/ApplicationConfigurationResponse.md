# ApplicationConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ApplicationConfiguration**](ApplicationConfiguration.md) |  | [optional] 

## Example

```python
from fenrir_api.models.application_configuration_response import ApplicationConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationConfigurationResponse from a JSON string
application_configuration_response_instance = ApplicationConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationConfigurationResponse.to_json()

# convert the object into a dict
application_configuration_response_dict = application_configuration_response_instance.to_dict()
# create an instance of ApplicationConfigurationResponse from a dict
application_configuration_response_form_dict = application_configuration_response.from_dict(application_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


