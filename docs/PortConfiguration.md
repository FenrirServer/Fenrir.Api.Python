# PortConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_number** | **int** | Port number to expose. | 
**protocol** | **str** | Protocol. This may be \&quot;tcp\&quot;, \&quot;udp\&quot; or empty for both. | [optional] 

## Example

```python
from fenrir_api.models.port_configuration import PortConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortConfiguration from a JSON string
port_configuration_instance = PortConfiguration.from_json(json)
# print the JSON string representation of the object
print PortConfiguration.to_json()

# convert the object into a dict
port_configuration_dict = port_configuration_instance.to_dict()
# create an instance of PortConfiguration from a dict
port_configuration_form_dict = port_configuration.from_dict(port_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


