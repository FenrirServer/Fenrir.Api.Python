# fenrir_api.FenrirApi

All URIs are relative to *https://api.fenrircloud.com/1.0/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_token**](FenrirApi.md#create_api_token) | **POST** /api_tokens | 
[**create_application**](FenrirApi.md#create_application) | **POST** /applications | 
[**create_application_configuration**](FenrirApi.md#create_application_configuration) | **POST** /applications/{application_uuid}/configuration | 
[**create_deployment**](FenrirApi.md#create_deployment) | **POST** /applications/{application_uuid}/deployments | 
[**create_matchmaking_queue**](FenrirApi.md#create_matchmaking_queue) | **POST** /applications/{application_uuid}/matchmaking/queues | 
[**create_matchmaking_queue_configuration**](FenrirApi.md#create_matchmaking_queue_configuration) | **POST** /applications/{application_uuid}/matchmaking/queues/{queue_uuid}/configuration | 
[**delete_api_token**](FenrirApi.md#delete_api_token) | **DELETE** /api_tokens/{token_uuid} | 
[**delete_application**](FenrirApi.md#delete_application) | **DELETE** /applications/{application_uuid} | 
[**delete_deployment**](FenrirApi.md#delete_deployment) | **DELETE** /applications/{application_uuid}/deployments/{deployment_uuid} | 
[**delete_matchmaking_queue**](FenrirApi.md#delete_matchmaking_queue) | **DELETE** /applications/{application_uuid}/matchmaking/queues/{queue_uuid} | 
[**get_api_token**](FenrirApi.md#get_api_token) | **GET** /api_tokens/{token_uuid} | 
[**get_api_tokens**](FenrirApi.md#get_api_tokens) | **GET** /api_tokens | 
[**get_application**](FenrirApi.md#get_application) | **GET** /applications/{application_uuid} | 
[**get_application_configuration**](FenrirApi.md#get_application_configuration) | **GET** /applications/{application_uuid}/configurations/{configuration_uuid} | 
[**get_application_configurations**](FenrirApi.md#get_application_configurations) | **GET** /applications/{application_uuid}/configurations | 
[**get_application_stats**](FenrirApi.md#get_application_stats) | **GET** /applications/{application_uuid}/stats | 
[**get_applications**](FenrirApi.md#get_applications) | **GET** /applications | 
[**get_current_application_configuration**](FenrirApi.md#get_current_application_configuration) | **GET** /applications/{application_uuid}/configuration | 
[**get_current_matchmaking_queue_configuration**](FenrirApi.md#get_current_matchmaking_queue_configuration) | **GET** /applications/{application_uuid}/matchmaking/queues/{queue_uuid}/configuration | 
[**get_deployment**](FenrirApi.md#get_deployment) | **GET** /applications/{application_uuid}/deployments/{deployment_uuid} | 
[**get_deployment_stats**](FenrirApi.md#get_deployment_stats) | **GET** /applications/{application_uuid}/deployments/{deployment_uuid}/stats | 
[**get_deployments**](FenrirApi.md#get_deployments) | **GET** /applications/{application_uuid}/deployments | 
[**get_images**](FenrirApi.md#get_images) | **GET** /applications/{application_uuid}/images | 
[**get_instance**](FenrirApi.md#get_instance) | **GET** /applications/{application_uuid}/deployments/{deployment_uuid}/instances/{instance_uuid} | 
[**get_instance_logs**](FenrirApi.md#get_instance_logs) | **GET** /applications/{application_uuid}/deployments/{deployment_uuid}/instances/{instance_uuid}/logs | 
[**get_instance_logs_preview**](FenrirApi.md#get_instance_logs_preview) | **GET** /applications/{application_uuid}/deployments/{deployment_uuid}/instances/{instance_uuid}/logs/preview | 
[**get_instances**](FenrirApi.md#get_instances) | **GET** /applications/{application_uuid}/deployments/{deployment_uuid}/instances | 
[**get_matchmaking_queue**](FenrirApi.md#get_matchmaking_queue) | **GET** /applications/{application_uuid}/matchmaking/queues/{queue_uuid} | 
[**get_matchmaking_queue_configuration**](FenrirApi.md#get_matchmaking_queue_configuration) | **GET** /applications/{application_uuid}/matchmaking/queues/{queue_uuid}/configurations/{configuration_uuid} | 
[**get_matchmaking_queue_configurations**](FenrirApi.md#get_matchmaking_queue_configurations) | **GET** /applications/{application_uuid}/matchmaking/queues/{queue_uuid}/configurations | 
[**get_matchmaking_queues**](FenrirApi.md#get_matchmaking_queues) | **GET** /applications/{application_uuid}/matchmaking/queues | 
[**update_application**](FenrirApi.md#update_application) | **PUT** /applications/{application_uuid} | 
[**update_matchmaking_queue**](FenrirApi.md#update_matchmaking_queue) | **PUT** /applications/{application_uuid}/matchmaking/queues/{queue_uuid} | 


# **create_api_token**
> ApiTokenResponse create_api_token(api_token)



Creates a new API token.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.api_token import ApiToken
from fenrir_api.models.api_token_response import ApiTokenResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    api_token = fenrir_api.ApiToken() # ApiToken | 

    try:
        api_response = api_instance.create_api_token(api_token)
        print("The response of FenrirApi->create_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->create_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | [**ApiToken**](ApiToken.md)|  | 

### Return type

[**ApiTokenResponse**](ApiTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> ApplicationResponse create_application(application)



Creates a new application.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application import Application
from fenrir_api.models.application_response import ApplicationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application = fenrir_api.Application() # Application | 

    try:
        api_response = api_instance.create_application(application)
        print("The response of FenrirApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->create_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)|  | 

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_configuration**
> ApplicationConfigurationResponse create_application_configuration(application_uuid, application_configuration)



Creates an application configuration.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_configuration import ApplicationConfiguration
from fenrir_api.models.application_configuration_response import ApplicationConfigurationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 
    application_configuration = fenrir_api.ApplicationConfiguration() # ApplicationConfiguration | 

    try:
        api_response = api_instance.create_application_configuration(application_uuid, application_configuration)
        print("The response of FenrirApi->create_application_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->create_application_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 
 **application_configuration** | [**ApplicationConfiguration**](ApplicationConfiguration.md)|  | 

### Return type

[**ApplicationConfigurationResponse**](ApplicationConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment**
> DeploymentResponse create_deployment(application_uuid, deployment)



Crates a new application deployment.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.deployment import Deployment
from fenrir_api.models.deployment_response import DeploymentResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 
    deployment = fenrir_api.Deployment() # Deployment | 

    try:
        api_response = api_instance.create_deployment(application_uuid, deployment)
        print("The response of FenrirApi->create_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->create_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 
 **deployment** | [**Deployment**](Deployment.md)|  | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_matchmaking_queue**
> MatchmakingQueueResponse create_matchmaking_queue(application_uuid, matchmaking_queue)



Creates a new matchmaking queue.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue import MatchmakingQueue
from fenrir_api.models.matchmaking_queue_response import MatchmakingQueueResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 
    matchmaking_queue = fenrir_api.MatchmakingQueue() # MatchmakingQueue | 

    try:
        api_response = api_instance.create_matchmaking_queue(application_uuid, matchmaking_queue)
        print("The response of FenrirApi->create_matchmaking_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->create_matchmaking_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 
 **matchmaking_queue** | [**MatchmakingQueue**](MatchmakingQueue.md)|  | 

### Return type

[**MatchmakingQueueResponse**](MatchmakingQueueResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_matchmaking_queue_configuration**
> MatchmakingQueueConfigurationResponse create_matchmaking_queue_configuration(queue_uuid, application_uuid, matchmaking_queue_configuration)



Creates a new matchmaking queue configuration.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue_configuration import MatchmakingQueueConfiguration
from fenrir_api.models.matchmaking_queue_configuration_response import MatchmakingQueueConfigurationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 
    matchmaking_queue_configuration = fenrir_api.MatchmakingQueueConfiguration() # MatchmakingQueueConfiguration | 

    try:
        api_response = api_instance.create_matchmaking_queue_configuration(queue_uuid, application_uuid, matchmaking_queue_configuration)
        print("The response of FenrirApi->create_matchmaking_queue_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->create_matchmaking_queue_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 
 **matchmaking_queue_configuration** | [**MatchmakingQueueConfiguration**](MatchmakingQueueConfiguration.md)|  | 

### Return type

[**MatchmakingQueueConfigurationResponse**](MatchmakingQueueConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token**
> Response delete_api_token(token_uuid)



Deletes an API token.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.response import Response
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    token_uuid = 'token_uuid_example' # str | 

    try:
        api_response = api_instance.delete_api_token(token_uuid)
        print("The response of FenrirApi->delete_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->delete_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request fulfilled, nothing follows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> Response delete_application(application_uuid)



Deletes an application.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.response import Response
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.delete_application(application_uuid)
        print("The response of FenrirApi->delete_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->delete_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request fulfilled, nothing follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment**
> Response delete_deployment(deployment_uuid, application_uuid)



Deletes an application deployment.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.response import Response
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.delete_deployment(deployment_uuid, application_uuid)
        print("The response of FenrirApi->delete_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->delete_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request fulfilled, nothing follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_matchmaking_queue**
> Response delete_matchmaking_queue(queue_uuid, application_uuid)



Deletes a matchmaking queue.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.response import Response
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.delete_matchmaking_queue(queue_uuid, application_uuid)
        print("The response of FenrirApi->delete_matchmaking_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->delete_matchmaking_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request fulfilled, nothing follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token**
> ApiTokenListResponse get_api_token(token_uuid)



Retrieves an API token.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.api_token_list_response import ApiTokenListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    token_uuid = 'token_uuid_example' # str | 

    try:
        api_response = api_instance.get_api_token(token_uuid)
        print("The response of FenrirApi->get_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_api_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_uuid** | **str**|  | 

### Return type

[**ApiTokenListResponse**](ApiTokenListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_tokens**
> ApiTokenListResponse get_api_tokens()



Lists all API tokens on your account.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.api_token_list_response import ApiTokenListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)

    try:
        api_response = api_instance.get_api_tokens()
        print("The response of FenrirApi->get_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_api_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiTokenListResponse**](ApiTokenListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> ApplicationResponse get_application(application_uuid)



Retrieves an application.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_response import ApplicationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_application(application_uuid)
        print("The response of FenrirApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_configuration**
> ApplicationConfigurationResponse get_application_configuration(configuration_uuid, application_uuid)



Retrieves an application configuration.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_configuration_response import ApplicationConfigurationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    configuration_uuid = 'configuration_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_application_configuration(configuration_uuid, application_uuid)
        print("The response of FenrirApi->get_application_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_application_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**ApplicationConfigurationResponse**](ApplicationConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_configurations**
> ApplicationConfigurationListResponse get_application_configurations(application_uuid)



Lists all application configurations ever created.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_configuration_list_response import ApplicationConfigurationListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_application_configurations(application_uuid)
        print("The response of FenrirApi->get_application_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_application_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**ApplicationConfigurationListResponse**](ApplicationConfigurationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_stats**
> ApplicationStatsResponse get_application_stats(application_uuid, filter=filter)



Retrieves application stats.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_stats_response import ApplicationStatsResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 
    filter = ['filter_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.get_application_stats(application_uuid, filter=filter)
        print("The response of FenrirApi->get_application_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_application_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 
 **filter** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ApplicationStatsResponse**](ApplicationStatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> ApplicationListResponse get_applications()



Lists all applications on your account.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_list_response import ApplicationListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)

    try:
        api_response = api_instance.get_applications()
        print("The response of FenrirApi->get_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_applications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApplicationListResponse**](ApplicationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_application_configuration**
> ApplicationConfigurationResponse get_current_application_configuration(application_uuid)



Retrieves current application configuration.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_configuration_response import ApplicationConfigurationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_current_application_configuration(application_uuid)
        print("The response of FenrirApi->get_current_application_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_current_application_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**ApplicationConfigurationResponse**](ApplicationConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_matchmaking_queue_configuration**
> MatchmakingQueueConfigurationResponse get_current_matchmaking_queue_configuration(queue_uuid, application_uuid)



Retrieves current matchmaking queue configuration.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue_configuration_response import MatchmakingQueueConfigurationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_current_matchmaking_queue_configuration(queue_uuid, application_uuid)
        print("The response of FenrirApi->get_current_matchmaking_queue_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_current_matchmaking_queue_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**MatchmakingQueueConfigurationResponse**](MatchmakingQueueConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> DeploymentResponse get_deployment(deployment_uuid, application_uuid)



Retrieves an application deployment.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.deployment_response import DeploymentResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_deployment(deployment_uuid, application_uuid)
        print("The response of FenrirApi->get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**DeploymentResponse**](DeploymentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_stats**
> DeploymentStatsResponse get_deployment_stats(deployment_uuid, application_uuid, filter=filter)



Retrieves deployment stats.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.deployment_stats_response import DeploymentStatsResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 
    filter = ['filter_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.get_deployment_stats(deployment_uuid, application_uuid, filter=filter)
        print("The response of FenrirApi->get_deployment_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_deployment_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 
 **filter** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**DeploymentStatsResponse**](DeploymentStatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> DeploymentListResponse get_deployments(application_uuid)



Lists all application deployments.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.deployment_list_response import DeploymentListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_deployments(application_uuid)
        print("The response of FenrirApi->get_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**DeploymentListResponse**](DeploymentListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> ImageListResponse get_images(application_uuid)



Lists all application images.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.image_list_response import ImageListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_images(application_uuid)
        print("The response of FenrirApi->get_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**ImageListResponse**](ImageListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance**
> ApplicationInstanceResponse get_instance(deployment_uuid, instance_uuid, application_uuid)



Retrieves an application instance.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_instance_response import ApplicationInstanceResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    instance_uuid = 'instance_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_instance(deployment_uuid, instance_uuid, application_uuid)
        print("The response of FenrirApi->get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **instance_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**ApplicationInstanceResponse**](ApplicationInstanceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_logs**
> InstanceLogs get_instance_logs(deployment_uuid, instance_uuid, application_uuid)



Retrieves application instance logs.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.instance_logs import InstanceLogs
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    instance_uuid = 'instance_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_instance_logs(deployment_uuid, instance_uuid, application_uuid)
        print("The response of FenrirApi->get_instance_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_instance_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **instance_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**InstanceLogs**](InstanceLogs.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_logs_preview**
> InstanceLogsPreview get_instance_logs_preview(deployment_uuid, instance_uuid, application_uuid)



Retrieves a small number of most recent application instance logs.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.instance_logs_preview import InstanceLogsPreview
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    instance_uuid = 'instance_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_instance_logs_preview(deployment_uuid, instance_uuid, application_uuid)
        print("The response of FenrirApi->get_instance_logs_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_instance_logs_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **instance_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**InstanceLogsPreview**](InstanceLogsPreview.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instances**
> ApplicationInstanceListResponse get_instances(deployment_uuid, application_uuid)



Lists all application instances for a given deployment.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application_instance_list_response import ApplicationInstanceListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    deployment_uuid = 'deployment_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_instances(deployment_uuid, application_uuid)
        print("The response of FenrirApi->get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**ApplicationInstanceListResponse**](ApplicationInstanceListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matchmaking_queue**
> MatchmakingQueueResponse get_matchmaking_queue(queue_uuid, application_uuid)



Retrieves a matchmaking queue.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue_response import MatchmakingQueueResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_matchmaking_queue(queue_uuid, application_uuid)
        print("The response of FenrirApi->get_matchmaking_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_matchmaking_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**MatchmakingQueueResponse**](MatchmakingQueueResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matchmaking_queue_configuration**
> MatchmakingQueueConfigurationResponse get_matchmaking_queue_configuration(configuration_uuid, queue_uuid, application_uuid)



Retrieves a matchmaking queue configuration.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue_configuration_response import MatchmakingQueueConfigurationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    configuration_uuid = 'configuration_uuid_example' # str | 
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_matchmaking_queue_configuration(configuration_uuid, queue_uuid, application_uuid)
        print("The response of FenrirApi->get_matchmaking_queue_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_matchmaking_queue_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_uuid** | **str**|  | 
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**MatchmakingQueueConfigurationResponse**](MatchmakingQueueConfigurationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matchmaking_queue_configurations**
> MatchmakingQueueConfigurationListResponse get_matchmaking_queue_configurations(queue_uuid, application_uuid)



Lists matchmaking queue configurations.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue_configuration_list_response import MatchmakingQueueConfigurationListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_matchmaking_queue_configurations(queue_uuid, application_uuid)
        print("The response of FenrirApi->get_matchmaking_queue_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_matchmaking_queue_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 

### Return type

[**MatchmakingQueueConfigurationListResponse**](MatchmakingQueueConfigurationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matchmaking_queues**
> MatchmakingQueueListResponse get_matchmaking_queues(application_uuid)



Lists all matchmaking queues for a given application.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue_list_response import MatchmakingQueueListResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 

    try:
        api_response = api_instance.get_matchmaking_queues(application_uuid)
        print("The response of FenrirApi->get_matchmaking_queues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->get_matchmaking_queues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 

### Return type

[**MatchmakingQueueListResponse**](MatchmakingQueueListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> ApplicationResponse update_application(application_uuid, application)



Updates an application.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.application import Application
from fenrir_api.models.application_response import ApplicationResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    application_uuid = 'application_uuid_example' # str | 
    application = fenrir_api.Application() # Application | 

    try:
        api_response = api_instance.update_application(application_uuid, application)
        print("The response of FenrirApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->update_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  | 
 **application** | [**Application**](Application.md)|  | 

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_matchmaking_queue**
> MatchmakingQueueResponse update_matchmaking_queue(queue_uuid, application_uuid, matchmaking_queue)



Updates a matchmaking queue.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import fenrir_api
from fenrir_api.models.matchmaking_queue import MatchmakingQueue
from fenrir_api.models.matchmaking_queue_response import MatchmakingQueueResponse
from fenrir_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fenrircloud.com/1.0/api
# See configuration.py for a list of all supported configuration parameters.
configuration = fenrir_api.Configuration(
    host = "https://api.fenrircloud.com/1.0/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = fenrir_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fenrir_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fenrir_api.FenrirApi(api_client)
    queue_uuid = 'queue_uuid_example' # str | 
    application_uuid = 'application_uuid_example' # str | 
    matchmaking_queue = fenrir_api.MatchmakingQueue() # MatchmakingQueue | 

    try:
        api_response = api_instance.update_matchmaking_queue(queue_uuid, application_uuid, matchmaking_queue)
        print("The response of FenrirApi->update_matchmaking_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FenrirApi->update_matchmaking_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_uuid** | **str**|  | 
 **application_uuid** | **str**|  | 
 **matchmaking_queue** | [**MatchmakingQueue**](MatchmakingQueue.md)|  | 

### Return type

[**MatchmakingQueueResponse**](MatchmakingQueueResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

