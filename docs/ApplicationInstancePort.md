# ApplicationInstancePort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | A protocol of the port. May be \&quot;tcp\&quot;, \&quot;udp\&quot; or empty if both. | [optional] 
**published_port** | **int** | A published port of the container. This is the port exposed from the external network. | [optional] 
**target_port** | **int** | A target port on the container. | [optional] 

## Example

```python
from fenrir_api.models.application_instance_port import ApplicationInstancePort

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstancePort from a JSON string
application_instance_port_instance = ApplicationInstancePort.from_json(json)
# print the JSON string representation of the object
print ApplicationInstancePort.to_json()

# convert the object into a dict
application_instance_port_dict = application_instance_port_instance.to_dict()
# create an instance of ApplicationInstancePort from a dict
application_instance_port_form_dict = application_instance_port.from_dict(application_instance_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


