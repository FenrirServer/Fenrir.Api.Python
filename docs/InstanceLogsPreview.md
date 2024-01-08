# InstanceLogsPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_lines** | **List[str]** | Most recent log lines. | [optional] 

## Example

```python
from fenrir_api.models.instance_logs_preview import InstanceLogsPreview

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceLogsPreview from a JSON string
instance_logs_preview_instance = InstanceLogsPreview.from_json(json)
# print the JSON string representation of the object
print InstanceLogsPreview.to_json()

# convert the object into a dict
instance_logs_preview_dict = instance_logs_preview_instance.to_dict()
# create an instance of InstanceLogsPreview from a dict
instance_logs_preview_form_dict = instance_logs_preview.from_dict(instance_logs_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


