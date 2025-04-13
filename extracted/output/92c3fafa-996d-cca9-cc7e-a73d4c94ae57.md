

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarShapeSegmentEndReferenceType Enumeration  
See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
A choice of two reference points for one end of a constraint driving the length of a RebarShapeSegment. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 **Since:** 2012 

# Syntax

C#  
---  
      
    
    public enum RebarShapeSegmentEndReferenceType  
  
Visual Basic  
---  
      
    
    Public Enumeration RebarShapeSegmentEndReferenceType  
  
Visual C++  
---  
      
    
    public enum class RebarShapeSegmentEndReferenceType  
  
# Members

| Member name | Description |
| --- | --- |
| Straight | Refers to the end of the straight part of the segment: the point where the bend begins. |
| Exterior | Refers to the farthest point on the arc of the bend. Assuming the bend is 90 degrees or more, an Exterior constraint will be longer than a Straight constraint by an amount equal to the bend radius. |
  
# Remarks

The RebarShapeSegmentEndReferenceType of a constraint is meaningful only when the bend is [right](176a9649-853e-f173-c108-d6722fcd5b61.md) or [obtuse](176a9649-853e-f173-c108-d6722fcd5b61.md). If the bend is [acute](176a9649-853e-f173-c108-d6722fcd5b61.md), the reference type is ignored. 

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)