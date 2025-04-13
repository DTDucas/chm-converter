

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Plane..::..CreateByThreePoints Method   
[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a Plane object passing through three points supplied as arguments. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public static [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.md) CreateByThreePoints(
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) point1,
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) point2,
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) point3
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function CreateByThreePoints ( _
    	point1 As [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md), _
    	point2 As [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md), _
    	point3 As [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) _
    ) As [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.md)  
  
Visual C++  
---  
      
    
    public:
    static [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.md)^ CreateByThreePoints(
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^ point1, 
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^ point2, 
    	[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^ point3
    )  
  
#### Parameters

point1
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) First of the three points that define a unique plane. The created Plane object will pass through these points. 

point2
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) Second of the three points that define a unique plane. 

point3
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) Third of the three points that define a unique plane. 

# Remarks

The points supplied as arguments must fully define a plane: they may not lie on a straight line or be too close to each other. The points must lie within the Revit design limits. This function does not guarantee a specific parameterization of the created Plane. Use Plane.Create(Frame) to enforce a specific parameterization of the created Plane object. All three points are expected to lie within the Revit design limits [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.md). 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The input point lies outside of Revit design limits. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md) | Throws if the input points do not define a unique plane. This is typically caused by points being too close to each other, or all three points being on or close to a straight line. |
  
# See Also

[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)