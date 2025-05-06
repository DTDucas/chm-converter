# GetApplicableResolutionTypes Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FailureDefinitionAccessor..::..GetApplicableResolutionTypes Method   
[FailureDefinitionAccessor Class](2abf9897-5ebf-a3bc-d40f-46632b0159fc.md "FailureDefinitionAccessor Class") See Also  
---  
Retrieves a list of resolution types applicable to the failure. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public IList<FailureResolutionType> GetApplicableResolutionTypes()
```
  
Visual Basic  
---  
```text
Public Function GetApplicableResolutionTypes As IList(Of FailureResolutionType)
```
  
Visual C++  
---  
```text
public:
IList<FailureResolutionType>^ GetApplicableResolutionTypes()
```
  
# ### Return Value
The list of resolution types applicable to the failure. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The FailureDefinitionAccessor has not been properly initialized. |

# See Also
[FailureDefinitionAccessor Class](2abf9897-5ebf-a3bc-d40f-46632b0159fc.md "FailureDefinitionAccessor Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 