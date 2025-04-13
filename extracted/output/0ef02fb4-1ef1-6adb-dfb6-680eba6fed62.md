

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
NurbSpline..::..CreateCurve Method (IList<(Of <(<'XYZ>)>)>, IList<(Of <(<'Double>)>)>)  
[NurbSpline Class](65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new geometric Curve object from NURBS curve data containing just control points and weights. The created curve may be a NURBSpline or a simpler curve such as line or arc. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public static [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md) CreateCurve(
    	IList<[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)> controlPoints,
    	IList<double> weights
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function CreateCurve ( _
    	controlPoints As IList(Of [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)), _
    	weights As IList(Of Double) _
    ) As [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md)  
  
Visual C++  
---  
      
    
    public:
    static [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md)^ CreateCurve(
    	IList<[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^>^ controlPoints, 
    	IList<double>^ weights
    )  
  
#### Parameters

controlPoints
    Type: System.Collections.Generic..::..IList<(Of <(<'[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)>)>)> The control points of the NURBSpline. 

weights
    Type: System.Collections.Generic..::..IList<(Of <(<'Double>)>)> The weights of the NURBSpline. 

#### Return Value

The new Curve object. 

# Remarks

There must be at least 2 control points. The number of weights must be equal to the the number of control points. The values of all weights must be positive. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The number of control points must be at least 2. -or- The number of weights must be the same as the number of control points and all weights must be positive. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md) | Curve length is too small for Revit's tolerance (as identified by Application.ShortCurveTolerance). |
  
# See Also

[NurbSpline Class](65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.md)

[CreateCurve Overload](774a9983-44a1-6cd9-36f2-0e40a819c5f7.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)