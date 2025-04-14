# ToElementIds Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FilteredElementCollector..::..ToElementIds Method   
[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.md "FilteredElementCollector Class") See Also  
---  
Returns the complete set of element ids that pass the filter(s). 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public ICollection<ElementId> ToElementIds()
```
  
Visual Basic  
---  
```text
Public Function ToElementIds As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ICollection<ElementId^>^ ToElementIds()
```
  
# ### Return Value
The complete set of element ids. 
# Remarks
This will reset the collector to the beginning and extract all elements that pass the applied filter(s). If you have an active iterator to this same collector it will be stopped by this call. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The collector does not have a filter applied. Extraction or iteration of elements is not permitted without a filter. |

# See Also
[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.md "FilteredElementCollector Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)