# Create Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
StairsPath..::..Create Method   
[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md "StairsPath Class") Example See Also  
---  
Creates a new stairs path for the specified stairs with the specified stairs path type only in the plan view. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static StairsPath Create(
	Document document,
	LinkElementId stairsId,
	ElementId typeId,
	ElementId planViewId
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	stairsId As LinkElementId, _
	typeId As ElementId, _
	planViewId As ElementId _
) As StairsPath
```
  
Visual C++  
---  
```text
public:
static StairsPath^ Create(
	Document^ document, 
	LinkElementId^ stairsId, 
	ElementId^ typeId, 
	ElementId^ planViewId
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
stairsId
    Type: [Autodesk.Revit.DB..::..LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md "LinkElementId Class") The id of the stairs element either in the host document or in a linked document. 
typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The type of stairs path. 
planViewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The plan view in which the stairs path will be shown. 
# ### Return Value
The new stairs path. 
# Examples
CopyC#
```text
private void CreateStairsPath(Document document, Stairs stairs)
{
    Transaction transNewPath = new Transaction(document, "New Stairs Path");
    transNewPath.Start();

    // Find StairsPathType
    FilteredElementCollector collector = new FilteredElementCollector(document);
    ICollection<ElementId> stairsPathIds = collector.OfClass(typeof(StairsPathType)).ToElementIds();

    // Find a FloorPlan
    ElementId planViewId = ElementId.InvalidElementId;
    FilteredElementCollector viewCollector = new FilteredElementCollector(document);
    ICollection<ElementId> viewIds = viewCollector.OfClass(typeof(View)).ToElementIds();
    foreach (ElementId viewId in viewIds)
    {
        View view = document.GetElement(viewId) as View;
        if (view.ViewType == ViewType.FloorPlan)
        {
            planViewId = view.Id;
            break;
        }
    }

    LinkElementId stairsLinkId = new LinkElementId(stairs.Id);
    StairsPath.Create(stairs.Document, stairsLinkId, stairsPathIds.First(), planViewId);
    transNewPath.Commit();
}
```

CopyVB.NET
```text
Private Sub CreateStairsPath(document As Document, stairs As Stairs)
    Dim transNewPath As New Transaction(document, "New Stairs Path")
    transNewPath.Start()

    ' Find StairsPathType
    Dim collector As New FilteredElementCollector(document)
    Dim stairsPathIds As ICollection(Of ElementId) = collector.OfClass(GetType(StairsPathType)).ToElementIds()

    ' Find a FloorPlan
    Dim planViewId As ElementId = ElementId.InvalidElementId
    Dim viewCollector As New FilteredElementCollector(document)
    Dim viewIds As ICollection(Of ElementId) = viewCollector.OfClass(GetType(View)).ToElementIds()
    For Each viewId As ElementId In viewIds
        Dim view As View = TryCast(document.GetElement(viewId), View)
        If view.ViewType = ViewType.FloorPlan Then
            planViewId = view.Id
            Exit For
        End If
    Next

    Dim stairsLinkId As New LinkElementId(stairs.Id)
    StairsPath.Create(stairs.Document, stairsLinkId, stairsPathIds.First(), planViewId)
    transNewPath.Commit()
End Sub
```

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The stairsId is not a valid stairs. -or- The typeId is not a valid stairs path type. -or- The planViewId is not a valid plan view. -or- The stairsId already has a stairs path. -or- The stairsId is not visible in planViewId. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md "StairsPath Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 