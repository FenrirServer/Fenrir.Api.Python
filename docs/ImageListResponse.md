# ImageListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[Image]**](Image.md) |  | [optional] 

## Example

```python
from fenrir_api.models.image_list_response import ImageListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageListResponse from a JSON string
image_list_response_instance = ImageListResponse.from_json(json)
# print the JSON string representation of the object
print ImageListResponse.to_json()

# convert the object into a dict
image_list_response_dict = image_list_response_instance.to_dict()
# create an instance of ImageListResponse from a dict
image_list_response_form_dict = image_list_response.from_dict(image_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


