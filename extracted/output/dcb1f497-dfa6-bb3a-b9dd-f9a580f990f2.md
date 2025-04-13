

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Document..::..GetUnusedElements Method   
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Returns the list of element ids that are not used and can be deleted from the document. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 

# Syntax

C#  
---  
      
    
    public ISet<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> GetUnusedElements(
    	ISet<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> categories
    )  
  
Visual Basic  
---  
      
    
    Public Function GetUnusedElements ( _
    	categories As ISet(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)) _
    ) As ISet(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md))  
  
Visual C++  
---  
      
    
    public:
    ISet<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ GetUnusedElements(
    	ISet<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ categories
    )  
  
#### Parameters

categories
    Type: System.Collections.Generic..::..ISet<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)> Collection of categories to check for unused elements. 

#### Return Value

Unused elements that can be deleted from the document. 

# Remarks

This method returns unused element ids that are available in the Purge Unused window in the Revit. To get unused elements that do not have a category assigned add [INVALID](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.md) to the collection of categories. If the input categories collection is empty, the method returns all unused elements in the document. 

# Examples

CopyC#
    
    
    public void DeleteAllUnused(Autodesk.Revit.DB.Document document)
    {
       using (Transaction transaction = new Transaction(document, "Delete unused elements"))
       {
          transaction.Start();
    
          ISet<ElementId> unusedElementIds = document.GetUnusedElements(new HashSet<ElementId>());
          while (unusedElementIds.Any())
          {
             document.Delete(unusedElementIds);
             unusedElementIds = document.GetUnusedElements(new HashSet<ElementId>());
          }
    
          transaction.Commit();
       }
    }
    
    public void GetUnusedElements(Autodesk.Revit.DB.Document document)
    {
       // Get all unused elements in the document
       var allUnusedElementIds = document.GetUnusedElements(new HashSet<ElementId>());
    
       // Get unused elements without a category
       var unusedElementIdsWithNoCategory = document.GetUnusedElements(new HashSet<ElementId>() { new ElementId(BuiltInCategory.INVALID) });
    
       // Get unused wall and floors types
       HashSet<ElementId> categoriesToPurge = new HashSet<ElementId>
       {
          new ElementId(BuiltInCategory.OST_Walls),
          new ElementId(BuiltInCategory.OST_Floors)
       };
    
       var unusedElementIds = document.GetUnusedElements(categoriesToPurge);
    }

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)