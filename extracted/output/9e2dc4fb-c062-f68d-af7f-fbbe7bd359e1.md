# RegisterSpaceBoundingElementHandle Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ExporterIFC..::..RegisterSpaceBoundingElementHandle Method   
[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class") See Also  
---  
Stores a handle representing a space bounding element to the ExporterIFC's internal cache. 
**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public void RegisterSpaceBoundingElementHandle(
	IFCAnyHandle instanceHandle,
	ElementId id,
	ElementId levelId
)
```
  
Visual Basic  
---  
```text
Public Sub RegisterSpaceBoundingElementHandle ( _
	instanceHandle As IFCAnyHandle, _
	id As ElementId, _
	levelId As ElementId _
)
```
  
Visual C++  
---  
```text
public:
void RegisterSpaceBoundingElementHandle(
	IFCAnyHandle^ instanceHandle, 
	ElementId^ id, 
	ElementId^ levelId
)
```
  
# ### Parameters
instanceHandle
    Type: [Autodesk.Revit.DB.IFC..::..IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.md "IFCAnyHandle Class") The handle to the space bounding element. 
id
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The Revit element id associated to this handle. 
levelId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The level id assigned to the space bounding object. 
# Remarks
The cache of space bounding elements will be used during completion of export to create relationship objects such as IfcRelSpaceBoundary and IfcRelConnectsPathElements. The types of Revit elements accepted by this function are: 
  * Walls
  * Curtain walls
  * Roofs
  * Floors
  * Doors
  * Windows

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.md "ExporterIFC Class")
[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)