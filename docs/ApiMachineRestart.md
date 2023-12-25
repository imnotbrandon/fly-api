# ApiMachineRestart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_retries** | **int** | When policy is on-failure, the maximum number of times to attempt to restart the Machine before letting it stop. | [optional] 
**policy** | **str** | * no - Never try to restart a Machine automatically when its main process exits, whether that’s on purpose or on a crash. * always - Always restart a Machine automatically and never let it enter a stopped state, even when the main process exits cleanly. * on-failure - Try up to MaxRetries times to automatically restart the Machine if it exits with a non-zero exit code. Default when no explicit policy is set, and for Machines with schedules. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


