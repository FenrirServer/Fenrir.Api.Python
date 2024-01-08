# ApplicationInstanceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[ApplicationInstance]**](ApplicationInstance.md) | A list of application instances. | [optional] 

## Example

```python
from fenrir_api.models.application_instance_list_response import ApplicationInstanceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstanceListResponse from a JSON string
application_instance_list_response_instance = ApplicationInstanceListResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationInstanceListResponse.to_json()

# convert the object into a dict
application_instance_list_response_dict = application_instance_list_response_instance.to_dict()
# create an instance of ApplicationInstanceListResponse from a dict
application_instance_list_response_form_dict = application_instance_list_response.from_dict(application_instance_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


