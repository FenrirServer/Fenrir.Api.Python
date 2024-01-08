# InstanceLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | A url at which the log file can be downloaded. | [optional] 

## Example

```python
from fenrir_api.models.instance_logs import InstanceLogs

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceLogs from a JSON string
instance_logs_instance = InstanceLogs.from_json(json)
# print the JSON string representation of the object
print InstanceLogs.to_json()

# convert the object into a dict
instance_logs_dict = instance_logs_instance.to_dict()
# create an instance of InstanceLogs from a dict
instance_logs_form_dict = instance_logs.from_dict(instance_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


