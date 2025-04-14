# UsesLevelFiltering Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FilterElementIdRule..::..UsesLevelFiltering Method   
[FilterElementIdRule Class](4675442b-8c75-4e20-ba18-71df13b86896.md "FilterElementIdRule Class") See Also  
---  
This function checks if a parameter uses level filtering. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public static bool UsesLevelFiltering(
	Document doc,
	ElementId parameterId
)
```
  
Visual Basic  
---  
```text
Public Shared Function UsesLevelFiltering ( _
	doc As Document, _
	parameterId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool UsesLevelFiltering(
	Document^ doc, 
	ElementId^ parameterId
)
```
  
# ### Parameters
doc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document which owns the parameter. 
parameterId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The id of the parameter that will be tested to see if it uses level filtering. 
# ### Return Value
True if the parameter uses level filtering, false otherwise. 
# Remarks
When level-filtering parameters are compared, the comparisons will first compare the values of the levels' elevations, then compare the levels' names, and finally the levels' element ids to rank and sort the levels. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[FilterElementIdRule Class](4675442b-8c75-4e20-ba18-71df13b86896.md "FilterElementIdRule Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)