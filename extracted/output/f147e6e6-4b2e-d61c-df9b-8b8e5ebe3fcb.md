

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FailureProcessingResult Enumeration  
See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
An enumerated type representing the result achieved by any of the available types of failure handlers: FailuresPreprocessor, the handler of FailuresProcessing event or a FailuresProcessor. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 

# Syntax

C#  
---  
      
    
    public enum FailureProcessingResult  
  
Visual Basic  
---  
      
    
    Public Enumeration FailureProcessingResult  
  
Visual C++  
---  
      
    
    public enum class FailureProcessingResult  
  
# Members

| Member name | Description |
| --- | --- |
| Continue | This value should be used if no action was taken and/or caller should continue with default failure processing for the open transaction. In the absence of any other available handlers, this means that the Revit user interface will display any errors to the user for resolution. (Warnings will not be displayed if they have been deleted already by the failure handler). If a FailuresProcessor returns Continue with unresolved failures, Revit will instead act as if ProceedWithRollBack was returned. |
| ProceedWithCommit | This value should be used if some or all failures were resolved by the handler. It instructs the Revit failure processing/transaction mechanism to try to repeat the transaction committing process. Despite the request to commit to the transaction, there is no guarantee that the commit will succeed. If errors remain unresolved the handler will likely be called again. Handler code should be careful not to try to repeatedly commit if it is unable to deal with all the errors. ProceedWithCommit cannot be used if the transaction is already being rolled back, and will be treated as ProceedWithRollBack in this case. |
| ProceedWithRollBack | This value should be returned if the transaction was originally requested to be committed and the failure handler requires it to be rolled back instead. In order to rollback silently, before ProceedWithRollBack is returned the failure handler should set the FailureHandlingOptions to clear errors after rollback. This will cause all failures to be deleted. If this is not set, default failure processing will continue, and failures may be delivered to the user even though the transaction will be rolled back. |
| WaitForUserInput | This value should only be returned by a FailuresProcessor - and only if it is waiting for something to happen externally. Typically this would be some sort of user input needed to complete failures processing. If this value is set from any other processor, it will be treated as ProceedWithRollback. |
  
# Remarks

The ability to return certain values may be restricted for certain methods or for certain contexts. 

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)