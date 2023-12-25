# UpdateMachineRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**CreateMachineRequestConfig**](CreateMachineRequestConfig.md) |  | [optional] 
**current_version** | **str** |  | [optional] 
**lease_ttl** | **int** |  | [optional] 
**lsvd** | **bool** |  | [optional] 
**name** | **str** | Unique name for this Machine. If omitted, one is generated for you | [optional] 
**region** | **str** | The target region. Omitting this param launches in the same region as your WireGuard peer connection (somewhere near you). | [optional] 
**skip_launch** | **bool** |  | [optional] 
**skip_service_registration** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


