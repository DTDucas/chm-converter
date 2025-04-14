# RollBack Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
TransactionGroup..::..RollBack Method   
[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.md "TransactionGroup Class") See Also  
---  
Rolls back the transaction group, which effectively undoes all transactions committed inside the group. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public TransactionStatus RollBack()
```
  
Visual Basic  
---  
```text
Public Function RollBack As TransactionStatus
```
  
Visual C++  
---  
```text
public:
TransactionStatus RollBack()
```
  
# ### Return Value
If finished successfully, this method returns TransactionStatus.RolledBack. 
# Remarks
Note that once a group is rolled back, the undone transactions cannot be redone.
RollBack can be called only when all inner transaction groups and transactions are finished, i.e. after they were either committed or rolled back.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The Transaction group has not been started (its status is not 'Started').. -or- The transaction's document is currently in failure mode. Transaction groups cannot be closed until failure handling is finished. You may use a transaction finalizer to close a group after the failure handling ends. |

# See Also
[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.md "TransactionGroup Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)