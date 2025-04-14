# FailureProcessingResult Enumeration

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FailureProcessingResult Enumeration  
See Also  
---  
An enumerated type representing the result achieved by any of the available types of failure handlers: FailuresPreprocessor, the handler of FailuresProcessing event or a FailuresProcessor. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public enum FailureProcessingResult
```
  
Visual Basic  
---  
```text
Public Enumeration FailureProcessingResult
```
  
Visual C++  
---  
```text
public enum class FailureProcessingResult
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| Continue | This value should be used if no action was taken and/or caller should continue with default failure processing for the open transaction. In the absence of any other available handlers, this means that the Revit user interface will display any errors to the user for resolution. (Warnings will not be displayed if they have been deleted already by the failure handler). If a FailuresProcessor returns Continue with unresolved failures, Revit will instead act as if ProceedWithRollBack was returned. |
| ProceedWithCommit | This value should be used if some or all failures were resolved by the handler. It instructs the Revit failure processing/transaction mechanism to try to repeat the transaction committing process. Despite the request to commit to the transaction, there is no guarantee that the commit will succeed. If errors remain unresolved the handler will likely be called again. Handler code should be careful not to try to repeatedly commit if it is unable to deal with all the errors. ProceedWithCommit cannot be used if the transaction is already being rolled back, and will be treated as ProceedWithRollBack in this case. |
| ProceedWithRollBack | This value should be returned if the transaction was originally requested to be committed and the failure handler requires it to be rolled back instead. In order to rollback silently, before ProceedWithRollBack is returned the failure handler should set the FailureHandlingOptions to clear errors after rollback. This will cause all failures to be deleted. If this is not set, default failure processing will continue, and failures may be delivered to the user even though the transaction will be rolled back. |
| WaitForUserInput | This value should only be returned by a FailuresProcessor - and only if it is waiting for something to happen externally. Typically this would be some sort of user input needed to complete failures processing. If this value is set from any other processor, it will be treated as ProceedWithRollback. |

# Remarks
The ability to return certain values may be restricted for certain methods or for certain contexts. 
# See Also
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)