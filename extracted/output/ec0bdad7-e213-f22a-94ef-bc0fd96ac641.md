

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FamilyInstanceFilter Class  
[Members](0ab03be9-6cb6-27b2-32b1-25057f96492e.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
A filter used to find elements that are family instances of the given family symbol. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 

# Syntax

C#  
---  
      
    
    public class FamilyInstanceFilter : [ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.md)  
  
Visual Basic  
---  
      
    
    Public Class FamilyInstanceFilter _
    	Inherits [ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.md)  
  
Visual C++  
---  
      
    
    public ref class FamilyInstanceFilter : public [ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.md)  
  
# Remarks

This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded. 

# Examples

CopyC#
    
    
    // Creates a FamilyInstance filter for elements that are family instances of the given family symbol in the document
    
    // Find all family symbols whose name is "W10X49"
    FilteredElementCollector collector = new FilteredElementCollector(document);
    collector = collector.OfClass(typeof(FamilySymbol));
    
    // Get Element Id for family symbol which will be used to find family instances
    var query = from element in collector where element.Name == "W10X49" select element;
    List<Element> famSyms = query.ToList<Element>();
    ElementId symbolId = famSyms[0].Id;
    
    // Create a FamilyInstance filter with the FamilySymbol Id
    FamilyInstanceFilter filter = new FamilyInstanceFilter(document, symbolId);
    
    // Apply the filter to the elements in the active document
    collector = new FilteredElementCollector(document);
    ICollection<Element> familyInstances = collector.WherePasses(filter).ToElements();

CopyVB.NET
    
    
    ' Creates a FamilyInstance filter for elements that are family instances of the given family symbol in the document
    
    
    ' Find all family symbols whose name is "W10X49"
    Dim collector As New FilteredElementCollector(document)
    collector = collector.OfClass(GetType(FamilySymbol))
    
    ' Get Element Id for family symbol which will be used to find family instances
    Dim query As System.Collections.Generic.IEnumerable(Of Autodesk.Revit.DB.Element)
    query = From element In collector _
     Where element.Name = "Level 1" _
     Select element
    
    Dim famSyms As List(Of Element) = query.ToList()
    Dim symbolId As ElementId = famSyms(0).Id
    
    ' Create a FamilyInstance filter with the FamilySymbol Id
    Dim filter As New FamilyInstanceFilter(document, symbolId)
    
    ' Apply the filter to the elements in the active document
    collector = New FilteredElementCollector(document)
    Dim familyInstances As ICollection(Of Element) = collector.WherePasses(filter).ToElements()

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md) [Autodesk.Revit.DB..::..ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.md) Autodesk.Revit.DB..::..FamilyInstanceFilter

# See Also

[FamilyInstanceFilter Members](0ab03be9-6cb6-27b2-32b1-25057f96492e.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)