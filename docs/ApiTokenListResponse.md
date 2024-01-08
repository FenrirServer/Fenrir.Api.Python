# ApiTokenListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_tokens** | [**List[ApiToken]**](ApiToken.md) | A list of API tokens | [optional] 

## Example

```python
from fenrir_api.models.api_token_list_response import ApiTokenListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenListResponse from a JSON string
api_token_list_response_instance = ApiTokenListResponse.from_json(json)
# print the JSON string representation of the object
print ApiTokenListResponse.to_json()

# convert the object into a dict
api_token_list_response_dict = api_token_list_response_instance.to_dict()
# create an instance of ApiTokenListResponse from a dict
api_token_list_response_form_dict = api_token_list_response.from_dict(api_token_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


