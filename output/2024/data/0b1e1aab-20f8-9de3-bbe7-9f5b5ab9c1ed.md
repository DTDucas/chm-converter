# ChangeSize Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FabricationNetworkChangeService..::..ChangeSize Method   
[FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.md "FabricationNetworkChangeService Class") See Also  
---  
Changes the size of the selection of fabrication parts. 
**Namespace:** [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.md "Autodesk.Revit.DB.Fabrication Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018.2 
# Syntax
C#  
---  
```text
public FabricationNetworkChangeServiceResult ChangeSize(
	ISet<ElementId> selection,
	ISet<FabricationPartSizeMap> fabricationPartSizeMaps
)
```
  
Visual Basic  
---  
```text
Public Function ChangeSize ( _
	selection As ISet(Of ElementId), _
	fabricationPartSizeMaps As ISet(Of FabricationPartSizeMap) _
) As FabricationNetworkChangeServiceResult
```
  
Visual C++  
---  
```text
public:
FabricationNetworkChangeServiceResult ChangeSize(
	ISet<ElementId^>^ selection, 
	ISet<FabricationPartSizeMap^>^ fabricationPartSizeMaps
)
```
  
# ### Parameters
selection
    Type: System.Collections.Generic..::..ISet<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> The set of element identifiers of fabrication parts to change the size for. 
fabricationPartSizeMaps
    Type: System.Collections.Generic..::..ISet<(Of <(<'[FabricationPartSizeMap](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.md "FabricationPartSizeMap Class")>)>)> The map containing the original sizes for the straights to the new sizes. 
# Remarks
After this method has been invoked, call: 
  * [GetStraightsThatWereNotChanged()()()()](644c47d9-806b-cd68-bf3e-0f8997c89f50.md "GetStraightsThatWereNotChanged Method") to get a set of fabrication part straight element identifiers that were not changed.
  * [GetElementsThatFailed()()()()](7bc30db4-1cae-1acb-c346-d164d5b90822.md "GetElementsThatFailed Method") to get a set of fabrication part element identifiers that had failures.

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The selection contains invalid elements to change. -or- The fabrication size map is empty. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | No fabrication configuration is loaded. |

# See Also
[FabricationNetworkChangeService Class](ddd58cb0-54bc-a864-9688-b890a7140112.md "FabricationNetworkChangeService Class")
[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.md "Autodesk.Revit.DB.Fabrication Namespace")
Send comments on this topic to 