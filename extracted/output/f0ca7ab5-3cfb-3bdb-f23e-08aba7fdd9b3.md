# GetCurrent Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FilteredWorksetIterator..::..GetCurrent Method   
[FilteredWorksetIterator Class](c80ff08f-7511-ebed-dc44-233d18ad8e87.md "FilteredWorksetIterator Class") See Also  
---  
The current workset found by the iterator. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public Workset GetCurrent()
```
  
Visual Basic  
---  
```text
Public Function GetCurrent As Workset
```
  
Visual C++  
---  
```text
public:
Workset^ GetCurrent()
```
  
# ### Return Value
The workset. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | There are no more worksets in the iterator. -or- The FilteredWorksetCollector that yielded this iterator has been reset by another operation. No further iteration is permitted with this iterator. |

# See Also
[FilteredWorksetIterator Class](c80ff08f-7511-ebed-dc44-233d18ad8e87.md "FilteredWorksetIterator Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)