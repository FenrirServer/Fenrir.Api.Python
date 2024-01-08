# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ApplicationConfiguration**](ApplicationConfiguration.md) |  | 
**created** | **datetime** | Time when the application was created. | [optional] [readonly] 
**name** | **str** | A unique name of the application. | 
**updated** | **datetime** | Time when the application was last updated. | [optional] [readonly] 
**uuid** | **str** | A unique id of the application. | [optional] [readonly] 

## Example

```python
from fenrir_api.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print Application.to_json()

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_form_dict = application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


