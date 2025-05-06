# SetClearAfterRollback Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
FailureHandlingOptions..::..SetClearAfterRollback Method   
[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md "FailureHandlingOptions Class") See Also  
---  
Sets a flag indicating that Revit should clear all posted failures silently when the failing transaction is being rolled back intentionally. If not set, the failures may still be displayed to the user during rollback. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public FailureHandlingOptions SetClearAfterRollback(
	bool bFlag
)
```
  
Visual Basic  
---  
```text
Public Function SetClearAfterRollback ( _
	bFlag As Boolean _
) As FailureHandlingOptions
```
  
Visual C++  
---  
```text
public:
FailureHandlingOptions^ SetClearAfterRollback(
	bool bFlag
)
```
  
# ### Parameters
bFlag
    Type: System..::..Boolean True to clear posted failures silently if the transaction is being rolled back, false to keep these failures in place (they may be displayed to the user). 
# ### Return Value
This FailureHandlingOptions object. 
# See Also
[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.md "FailureHandlingOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 