# ApiToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_uuid** | **str** | A uuid of the application this token is limited to. | [optional] 
**created** | **datetime** | Time when the token was created. | [optional] [readonly] 
**label** | **str** | A label for the token. | [optional] 
**token_plaintext** | **object** | A plain text value of the token. Only returned when the token is created. | [optional] [readonly] 
**updated** | **datetime** | Time when the token was last updated. | [optional] [readonly] 
**uuid** | **str** | A unique id of the api token. | [optional] [readonly] 

## Example

```python
from fenrir_api.models.api_token import ApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToken from a JSON string
api_token_instance = ApiToken.from_json(json)
# print the JSON string representation of the object
print ApiToken.to_json()

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of ApiToken from a dict
api_token_form_dict = api_token.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


