

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
StairsPath..::..Create Method   
[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new stairs path for the specified stairs with the specified stairs path type only in the plan view. 

**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public static [StairsPath](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md) stairsId,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) typeId,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) planViewId
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	stairsId As [LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md), _
    	typeId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md), _
    	planViewId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) _
    ) As [StairsPath](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md)  
  
Visual C++  
---  
      
    
    public:
    static [StairsPath](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md)^ stairsId, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ typeId, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ planViewId
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document. 

stairsId
    Type: [Autodesk.Revit.DB..::..LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md) The id of the stairs element either in the host document or in a linked document. 

typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) The type of stairs path. 

planViewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) The plan view in which the stairs path will be shown. 

#### Return Value

The new stairs path. 

# Examples

CopyC#
    
    
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

CopyVB.NET
    
    
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

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The stairsId is not a valid stairs. -or- The typeId is not a valid stairs path type. -or- The planViewId is not a valid plan view. -or- The stairsId already has a stairs path. -or- The stairsId is not visible in planViewId. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)