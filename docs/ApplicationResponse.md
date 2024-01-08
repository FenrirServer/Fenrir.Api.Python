# ApplicationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | [optional] 

## Example

```python
from fenrir_api.models.application_response import ApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponse from a JSON string
application_response_instance = ApplicationResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationResponse.to_json()

# convert the object into a dict
application_response_dict = application_response_instance.to_dict()
# create an instance of ApplicationResponse from a dict
application_response_form_dict = application_response.from_dict(application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


