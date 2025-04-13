

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ElementTransformUtils..::..CopyElements Method (Document, ICollection<(Of <(<'ElementId>)>)>, Document, Transform, CopyPasteOptions)  
[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Copies a set of elements from source document to destination document. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    public static ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> CopyElements(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) sourceDocument,
    	ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> elementsToCopy,
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) destinationDocument,
    	[Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md) transform,
    	[CopyPasteOptions](d8f58fd5-2106-7a88-6218-106a30415791.md) options
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function CopyElements ( _
    	sourceDocument As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	elementsToCopy As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)), _
    	destinationDocument As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	transform As [Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md), _
    	options As [CopyPasteOptions](d8f58fd5-2106-7a88-6218-106a30415791.md) _
    ) As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md))  
  
Visual C++  
---  
      
    
    public:
    static ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ CopyElements(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ sourceDocument, 
    	ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ elementsToCopy, 
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ destinationDocument, 
    	[Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md)^ transform, 
    	[CopyPasteOptions](d8f58fd5-2106-7a88-6218-106a30415791.md)^ options
    )  
  
#### Parameters

sourceDocument
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document that contains the elements to copy. 

elementsToCopy
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)> The set of elements to copy. 

destinationDocument
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The destination document to paste the elements into. 

transform
    Type: [Autodesk.Revit.DB..::..Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md) The transform for the new elements. Can be nullNothingnullptra null reference (Nothing in Visual Basic) if no transform is required. 

options
    Type: [Autodesk.Revit.DB..::..CopyPasteOptions](d8f58fd5-2106-7a88-6218-106a30415791.md) Optional settings. Can be nullNothingnullptra null reference (Nothing in Visual Basic) if default settings should be used. 

#### Return Value

The ids of the newly created copied elements. 

# Remarks

Copies are placed at their respective original locations or locations specified by the optional transformation.

This method can be used for copying non-view specific elements only. For copying view-specific elements, use the view-specific form of the CopyElements method.

The destination document can be the same as the source document.

This method performs rehosting of elements where applicable.

# Examples

CopyC#
    
    
    // Copy wall element.
    public void CopyWall(Autodesk.Revit.DB.Document sourceDocument, Autodesk.Revit.DB.Document destinationDocument, Autodesk.Revit.DB.Wall wall)
    {
       Transform transform = Transform.CreateTranslation(new XYZ(150, 150, 0));
       CopyPasteOptions options = new CopyPasteOptions();
    
       ElementTransformUtils.CopyElements(sourceDocument, new List<ElementId> { wall.Id }, destinationDocument, transform, options);
    }
    
    // The method copies existing Sketch curves inside of the Floor sketch.
    public void CopySketchMembersInsideOfSketch(Autodesk.Revit.DB.Document document, Autodesk.Revit.DB.Floor floor)
    {
       var floorSketch = document.GetElement(floor.SketchId) as Sketch;
    
       // Start Sketch edit mode to copy Sketch members inside of the Sketch
       SketchEditScope sketchScope = new SketchEditScope(document, "Edit floor sketch");
       sketchScope.Start(floor.SketchId);
    
       // Start transaction to be able to modify the document
       using (Transaction tr = new Transaction(document, "Copy sketch members"))
       {
          tr.Start();
    
          var transform = Transform.CreateTranslation(new XYZ(150, 150, 0));
          var copiedIds = ElementTransformUtils.CopyElements(
             document, floorSketch.GetAllElements(), document, transform, new CopyPasteOptions());
    
          tr.Commit();
       }
    
       sketchScope.Commit(new CustomFailuresPreprocessor());
    }
    
    // The method copies Sketch members from the Floor to the Ceiling Sketch.
    public void CopySketchMembersBetweenSketch(Autodesk.Revit.DB.Floor floor, Autodesk.Revit.DB.Ceiling ceiling)
    {
       var ceilingSketch = ceiling.Document.GetElement(ceiling.SketchId) as Sketch;
       var floorSketch = floor.Document.GetElement(floor.SketchId) as Sketch;
    
       // Sketch members can be copied only between parallel Sketches.
       if (!MathComparisonUtils.IsAlmostEqual(
          Math.Abs(floorSketch.SketchPlane.GetPlane().Normal.DotProduct(ceilingSketch.SketchPlane.GetPlane().Normal)), 1.0))
       {
          return;
       }
    
       // Start Sketch edit mode, for the ceiling sketch, to copy and paste floor Sketch members to the ceiling
       SketchEditScope sketchScope = new SketchEditScope(ceiling.Document, "Edit ceiling sketch");
       sketchScope.Start(ceiling.SketchId);
    
       // Start transaction to be able to modify the document
       using (Transaction tr = new Transaction(ceiling.Document, "Copy sketch members"))
       {
          tr.Start();
    
          var transform = Transform.CreateTranslation(new XYZ(150, 150, 0));
          var copiedIds = ElementTransformUtils.CopyElements(
             floor.Document, floorSketch.GetAllElements(), ceiling.Document, transform, new CopyPasteOptions());
    
          tr.Commit();
       }
    
       sketchScope.Commit(new CustomFailuresPreprocessor());
    }
    
    // The method copies ModelCurves from the document to the Sketch.
    public void CopyModelCurvesFromDocumentToSketch(Autodesk.Revit.DB.Sketch sketch, List<ElementId> modelCurveIds)
    {
       // Start Sketch edit mode to insert ModelCurves into the Floor Sketch.
       SketchEditScope sketchScope = new SketchEditScope(sketch.Document, "Edit floor sketch");
       sketchScope.Start(sketch.Id);
    
       // Start transaction to be able to modify the document
       using (Transaction tr = new Transaction(sketch.Document, "Copy sketch members"))
       {
          tr.Start();
    
          var transform = Transform.CreateTranslation(new XYZ(150, 150, 0));
          var copiedIds = ElementTransformUtils.CopyElements(
             sketch.Document, modelCurveIds, sketch.Document, transform, new CopyPasteOptions());
    
          tr.Commit();
       }
    
       // Sketch curves should not have open loops or intersections to be successfully committed.
       sketchScope.Commit(new CustomFailuresPreprocessor());
    }

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The given element id set is empty. -or- One or more elements in elementsToCopy do not exist in the document. -or- Some of the elements cannot be copied, because they are view-specific. -or- The input set of elements contains Sketch members along with other elements or there is no active Sketch edit mode. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | It is not allowed to copy Sketch members between non-parallel sketches. -or- The elements cannot be copied. |
| [Autodesk.Revit.Exceptions..::..OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.md) | User cancelled the operation. |
  
# See Also

[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.md)

[CopyElements Overload](7b56b5c2-3aff-f42b-ab47-de1f89a1070f.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)