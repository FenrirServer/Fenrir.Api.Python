# BadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ValidationError]**](ValidationError.md) | An optional list of validation errors | [optional] 
**message** | **str** | An error message. | [optional] 

## Example

```python
from fenrir_api.models.bad_request_response import BadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestResponse from a JSON string
bad_request_response_instance = BadRequestResponse.from_json(json)
# print the JSON string representation of the object
print BadRequestResponse.to_json()

# convert the object into a dict
bad_request_response_dict = bad_request_response_instance.to_dict()
# create an instance of BadRequestResponse from a dict
bad_request_response_form_dict = bad_request_response.from_dict(bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


