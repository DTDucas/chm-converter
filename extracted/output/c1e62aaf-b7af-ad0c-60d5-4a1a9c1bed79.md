

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
MassLevelData Class  
[Members](7ad5d221-ce41-42af-c63e-e868e6ae6aa1.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
MassLevelData is a conceptual representation of an occupiable floor (Mass Floor) in a conceptual building model. It is defined by associating a particular level with a particular mass element in a Revit project. 

**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    public class MassLevelData : [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
Visual Basic  
---  
      
    
    Public Class MassLevelData _
    	Inherits [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
Visual C++  
---  
      
    
    public ref class MassLevelData : public [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)  
  
# Remarks

MassLevelData reports metrics, such as floor areas, related to conceptual space planning. MassLevelData contains information, such as ConceptualConstructionType, used as part of the Conceptual Energy Analytical model. The MassLevel data geometry is determined by combining all the geometry of a mass into a single geometry, and then taking the area of intersection with the level of the MassLevelData. 

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) Autodesk.Revit.DB.Analysis..::..MassLevelData

# See Also

[MassLevelData Members](7ad5d221-ce41-42af-c63e-e868e6ae6aa1.md)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)