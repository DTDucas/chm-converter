

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarShapeDefinitionByArc Constructor (Document, RebarShapeDefinitionByArcType)  
[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Create a non-spiral shape definition. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    public RebarShapeDefinitionByArc(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) doc,
    	[RebarShapeDefinitionByArcType](555907d2-578b-026a-347c-8900bcf538d8.md) type
    )  
  
Visual Basic  
---  
      
    
    Public Sub New ( _
    	doc As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	type As [RebarShapeDefinitionByArcType](555907d2-578b-026a-347c-8900bcf538d8.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    RebarShapeDefinitionByArc(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ doc, 
    	[RebarShapeDefinitionByArcType](555907d2-578b-026a-347c-8900bcf538d8.md) type
    )  
  
#### Parameters

doc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)

type
    Type: [Autodesk.Revit.DB.Structure..::..RebarShapeDefinitionByArcType](555907d2-578b-026a-347c-8900bcf538d8.md)

# Remarks

Replaces RebarShape.NewDefinitionByArc() from prior versions. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The arc type cannot be set directly to Spiral. Instead, call SetArcTypeSpiral() to provide defaults for spiral parameters. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | A value passed for an enumeration argument is not a member of that enumeration |
  
# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.md)

[RebarShapeDefinitionByArc Overload](69c14c72-4c10-1840-014b-b48646d003f1.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)