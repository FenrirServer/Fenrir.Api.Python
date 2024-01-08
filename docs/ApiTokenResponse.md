# ApiTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | [**ApiToken**](ApiToken.md) |  | [optional] 

## Example

```python
from fenrir_api.models.api_token_response import ApiTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenResponse from a JSON string
api_token_response_instance = ApiTokenResponse.from_json(json)
# print the JSON string representation of the object
print ApiTokenResponse.to_json()

# convert the object into a dict
api_token_response_dict = api_token_response_instance.to_dict()
# create an instance of ApiTokenResponse from a dict
api_token_response_form_dict = api_token_response.from_dict(api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


