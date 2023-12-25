# ApiMachineConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_destroy** | **bool** | Optional boolean telling the Machine to destroy itself once it’s complete (default false) | [optional] 
**checks** | [**dict(str, ApiMachineCheck)**](ApiMachineCheck.md) |  | [optional] 
**disable_machine_autostart** | **bool** | Deprecated: use Service.Autostart instead | [optional] 
**dns** | [**ApiDNSConfig**](ApiDNSConfig.md) |  | [optional] 
**env** | **dict(str, str)** | An object filled with key/value pairs to be set as environment variables | [optional] 
**files** | [**list[ApiFile]**](ApiFile.md) |  | [optional] 
**guest** | [**ApiMachineGuest**](ApiMachineGuest.md) |  | [optional] 
**image** | **str** | The docker image to run | [optional] 
**init** | [**ApiMachineInit**](ApiMachineInit.md) |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**metrics** | [**ApiMachineMetrics**](ApiMachineMetrics.md) |  | [optional] 
**mounts** | [**list[ApiMachineMount]**](ApiMachineMount.md) |  | [optional] 
**processes** | [**list[ApiMachineProcess]**](ApiMachineProcess.md) |  | [optional] 
**restart** | [**ApiMachineRestart**](ApiMachineRestart.md) |  | [optional] 
**schedule** | **str** |  | [optional] 
**services** | [**list[ApiMachineService]**](ApiMachineService.md) |  | [optional] 
**size** | **str** | Deprecated: use Guest instead | [optional] 
**standbys** | **list[str]** | Standbys enable a machine to be a standby for another. In the event of a hardware failure, the standby machine will be started. | [optional] 
**statics** | [**list[ApiStatic]**](ApiStatic.md) |  | [optional] 
**stop_config** | [**ApiStopConfig**](ApiStopConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


