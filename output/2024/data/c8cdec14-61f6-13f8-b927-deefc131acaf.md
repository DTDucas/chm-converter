# GetInstanceShapeHandlePointElementRefIds Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AdaptiveComponentInstanceUtils..::..GetInstanceShapeHandlePointElementRefIds Method   
[AdaptiveComponentInstanceUtils Class](786db8ac-a051-37e4-7b4c-dbf286fe9a7c.md "AdaptiveComponentInstanceUtils Class") See Also  
---  
Gets Shape Handle Adaptive Point Element Ref ids to which the instance geometry adapts. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public static IList<ElementId> GetInstanceShapeHandlePointElementRefIds(
	FamilyInstance famInst
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetInstanceShapeHandlePointElementRefIds ( _
	famInst As FamilyInstance _
) As IList(Of ElementId)
```
  
Visual C++  
---  
```text
public:
static IList<ElementId^>^ GetInstanceShapeHandlePointElementRefIds(
	FamilyInstance^ famInst
)
```
  
# ### Parameters
famInst
    Type: [Autodesk.Revit.DB..::..FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md "FamilyInstance Class") The FamilyInstance 
# ### Return Value
The Shape Handle Adaptive Point Element Ref ids to which the instance geometry adapts. 
# Remarks
The output contains shape handle point ref ids. If there are no shape handle points defined in the Family then the output is empty. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The FamilyInstance famInst is not an Adaptive Family Instance. -or- The FamilyInstance famInst does not have an Adaptive Family Symbol. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | This operation failed. |

# See Also
[AdaptiveComponentInstanceUtils Class](786db8ac-a051-37e4-7b4c-dbf286fe9a7c.md "AdaptiveComponentInstanceUtils Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 