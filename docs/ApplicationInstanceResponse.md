# ApplicationInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**ApplicationInstance**](ApplicationInstance.md) |  | [optional] 

## Example

```python
from fenrir_api.models.application_instance_response import ApplicationInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstanceResponse from a JSON string
application_instance_response_instance = ApplicationInstanceResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationInstanceResponse.to_json()

# convert the object into a dict
application_instance_response_dict = application_instance_response_instance.to_dict()
# create an instance of ApplicationInstanceResponse from a dict
application_instance_response_form_dict = application_instance_response.from_dict(application_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


