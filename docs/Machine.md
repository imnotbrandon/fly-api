# Machine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**list[CheckStatus]**](CheckStatus.md) |  | [optional] 
**config** | [**ApiMachineConfig**](ApiMachineConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**events** | [**list[MachineEvent]**](MachineEvent.md) |  | [optional] 
**id** | **str** |  | [optional] 
**image_ref** | [**ImageRef**](ImageRef.md) |  | [optional] 
**instance_id** | **str** | InstanceID is unique for each version of the machine | [optional] 
**name** | **str** |  | [optional] 
**nonce** | **str** | Nonce is only every returned on machine creation if a lease_duration was provided. | [optional] 
**private_ip** | **str** | PrivateIP is the internal 6PN address of the machine. | [optional] 
**region** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


