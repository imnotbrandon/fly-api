# ApiMachineCheck

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_period** | **str** | The time to wait after a VM starts before checking its health | [optional] 
**headers** | [**list[ApiMachineHTTPHeader]**](ApiMachineHTTPHeader.md) |  | [optional] 
**interval** | **str** | The time between connectivity checks | [optional] 
**method** | **str** | For http checks, the HTTP method to use to when making the request | [optional] 
**path** | **str** | For http checks, the path to send the request to | [optional] 
**port** | **int** | The port to connect to, often the same as internal_port | [optional] 
**protocol** | **str** | For http checks, whether to use http or https | [optional] 
**timeout** | **str** | The maximum time a connection can take before being reported as failing its health check | [optional] 
**tls_server_name** | **str** | If the protocol is https, the hostname to use for TLS certificate validation | [optional] 
**tls_skip_verify** | **bool** | For http checks with https protocol, whether or not to verify the TLS certificate | [optional] 
**type** | **str** | tcp or http | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


