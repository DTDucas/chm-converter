# GetModifiedElementIds Method (ElementFilter) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DocumentChangedEventArgs..::..GetModifiedElementIds Method (ElementFilter)  
[DocumentChangedEventArgs Class](8fd170b2-df48-209b-438e-54ec7b01b664.md "DocumentChangedEventArgs Class") See Also  
---  
Returns set of elements that were modified according to the given element filter. 
**Namespace:** [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public ICollection<ElementId> GetModifiedElementIds(
	ElementFilter filter
)
```
  
Visual Basic  
---  
```text
Public Function GetModifiedElementIds ( _
	filter As ElementFilter _
) As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ICollection<ElementId^>^ GetModifiedElementIds(
	ElementFilter^ filter
)
```
  
# ### Parameters
filter
    Type: [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md "ElementFilter Class") The element filter to be applied. 
# ### Return Value
The set of ElementId for modified elements that pass the filter. Returns empty set if no elements are found which pass the filter. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DocumentChangedEventArgs Class](8fd170b2-df48-209b-438e-54ec7b01b664.md "DocumentChangedEventArgs Class")
[GetModifiedElementIds Overload](eb5eab82-7e48-958b-9999-dc8826ca26f3.md "GetModifiedElementIds Method")
[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")
Send comments on this topic to 