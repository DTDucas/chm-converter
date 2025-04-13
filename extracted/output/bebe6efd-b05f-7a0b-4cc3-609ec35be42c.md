

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FailureHandlingOptions..::..SetClearAfterRollback Method   
[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Sets a flag indicating that Revit should clear all posted failures silently when the failing transaction is being rolled back intentionally. If not set, the failures may still be displayed to the user during rollback. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 

# Syntax

C#  
---  
      
    
    public [FailureHandlingOptions](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md) SetClearAfterRollback(
    	bool bFlag
    )  
  
Visual Basic  
---  
      
    
    Public Function SetClearAfterRollback ( _
    	bFlag As Boolean _
    ) As [FailureHandlingOptions](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md)  
  
Visual C++  
---  
      
    
    public:
    [FailureHandlingOptions](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md)^ SetClearAfterRollback(
    	bool bFlag
    )  
  
#### Parameters

bFlag
    Type: System..::..Boolean True to clear posted failures silently if the transaction is being rolled back, false to keep these failures in place (they may be displayed to the user). 

#### Return Value

This FailureHandlingOptions object. 

# See Also

[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)