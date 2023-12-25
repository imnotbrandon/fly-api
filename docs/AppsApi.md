# flyio.AppsApi

All URIs are relative to *https://api.machines.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_create**](AppsApi.md#apps_create) | **POST** /apps | 
[**apps_delete**](AppsApi.md#apps_delete) | **DELETE** /apps/{app_name} | 
[**apps_list**](AppsApi.md#apps_list) | **GET** /apps | 
[**apps_show**](AppsApi.md#apps_show) | **GET** /apps/{app_name} | 


# **apps_create**
> apps_create(request)



### Example
```python
from __future__ import print_function
import time
import flyio
from flyio.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flyio.AppsApi()
request = flyio.CreateAppRequest() # CreateAppRequest | App body

try:
    api_instance.apps_create(request)
except ApiException as e:
    print("Exception when calling AppsApi->apps_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateAppRequest**](CreateAppRequest.md)| App body | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_delete**
> apps_delete(app_name)



### Example
```python
from __future__ import print_function
import time
import flyio
from flyio.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flyio.AppsApi()
app_name = 'app_name_example' # str | Fly App Name

try:
    api_instance.apps_delete(app_name)
except ApiException as e:
    print("Exception when calling AppsApi->apps_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Fly App Name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_list**
> ListAppsResponse apps_list(org_slug)



### Example
```python
from __future__ import print_function
import time
import flyio
from flyio.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flyio.AppsApi()
org_slug = 'org_slug_example' # str | The org slug, or 'personal', to filter apps

try:
    api_response = api_instance.apps_list(org_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**| The org slug, or &#39;personal&#39;, to filter apps | 

### Return type

[**ListAppsResponse**](ListAppsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_show**
> App apps_show(app_name)



### Example
```python
from __future__ import print_function
import time
import flyio
from flyio.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flyio.AppsApi()
app_name = 'app_name_example' # str | Fly App Name

try:
    api_response = api_instance.apps_show(app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Fly App Name | 

### Return type

[**App**](App.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

