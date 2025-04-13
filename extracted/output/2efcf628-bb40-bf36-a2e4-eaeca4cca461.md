

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
TransactionGroup..::..RollBack Method   
[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Rolls back the transaction group, which effectively undoes all transactions committed inside the group. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 

# Syntax

C#  
---  
      
    
    public [TransactionStatus](29b9a7a8-6754-8310-e063-622b569bb6d5.md) RollBack()  
  
Visual Basic  
---  
      
    
    Public Function RollBack As [TransactionStatus](29b9a7a8-6754-8310-e063-622b569bb6d5.md)  
  
Visual C++  
---  
      
    
    public:
    [TransactionStatus](29b9a7a8-6754-8310-e063-622b569bb6d5.md) RollBack()  
  
#### Return Value

If finished successfully, this method returns TransactionStatus.RolledBack. 

# Remarks

Note that once a group is rolled back, the undone transactions cannot be redone.

RollBack can be called only when all inner transaction groups and transactions are finished, i.e. after they were either committed or rolled back.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | The Transaction group has not been started (its status is not 'Started').. -or- The transaction's document is currently in failure mode. Transaction groups cannot be closed until failure handling is finished. You may use a transaction finalizer to close a group after the failure handling ends. |
  
# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)