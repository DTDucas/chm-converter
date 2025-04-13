

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FamilyItemFactory..::..NewSymbolicCurve Method   
[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Create a symbolic curve in an Autodesk Revit family document.

**Namespace:** [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public [SymbolicCurve](c6c3bde4-4aa9-1b08-cd71-2fad0613d276.md) NewSymbolicCurve(
    	[Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md) curve,
    	[SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.md) sketchPlane
    )  
  
Visual Basic  
---  
      
    
    Public Function NewSymbolicCurve ( _
    	curve As [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md), _
    	sketchPlane As [SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.md) _
    ) As [SymbolicCurve](c6c3bde4-4aa9-1b08-cd71-2fad0613d276.md)  
  
Visual C++  
---  
      
    
    public:
    [SymbolicCurve](c6c3bde4-4aa9-1b08-cd71-2fad0613d276.md)^ NewSymbolicCurve(
    	[Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md)^ curve, 
    	[SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.md)^ sketchPlane
    )  
  
#### Parameters

curve
    Type: [Autodesk.Revit.DB..::..Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md)The geometry curve of the newly created symbolic curve.

sketchPlane
    Type: [Autodesk.Revit.DB..::..SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.md)The sketch plane for the symbolic curve.

#### Return Value

The newly created symbolic curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | Thrown when argument is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown when regeneration failed. Thrown when symbolic curve creation failed. |
  
# See Also

[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.md)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)