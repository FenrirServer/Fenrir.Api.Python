# ApplicationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[Application]**](Application.md) | A list of applications. | [optional] 

## Example

```python
from fenrir_api.models.application_list_response import ApplicationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationListResponse from a JSON string
application_list_response_instance = ApplicationListResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationListResponse.to_json()

# convert the object into a dict
application_list_response_dict = application_list_response_instance.to_dict()
# create an instance of ApplicationListResponse from a dict
application_list_response_form_dict = application_list_response.from_dict(application_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


