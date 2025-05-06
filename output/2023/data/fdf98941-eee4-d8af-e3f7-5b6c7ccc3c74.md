# GetStatus Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Transaction..::..GetStatus Method   
[Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.md "Transaction Class") See Also  
---  
Returns the current status of the transaction. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public TransactionStatus GetStatus()
```
  
Visual Basic  
---  
```text
Public Function GetStatus As TransactionStatus
```
  
Visual C++  
---  
```text
public:
TransactionStatus GetStatus()
```
  
# ### Return Value
The current status of the transaction. 
# Remarks
If the status was set to TransactionStatus.Pending as the result of calling Commit or RollBack, the status will be changed later to either 'Committed' or 'RolledBack' after failure handling is finished. That status change will be made asynchronously. 
# See Also
[Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.md "Transaction Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 