

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ConicalSurface..::..Create Method   
[ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a conical surface defined by a local reference frame and a half angle. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public static [ConicalSurface](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md) Create(
    	[Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.md) frameOfReference,
    	double halfAngle
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	frameOfReference As [Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.md), _
    	halfAngle As Double _
    ) As [ConicalSurface](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md)  
  
Visual C++  
---  
      
    
    public:
    static [ConicalSurface](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md)^ Create(
    	[Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.md)^ frameOfReference, 
    	double halfAngle
    )  
  
#### Parameters

frameOfReference
    Type: [Autodesk.Revit.DB..::..Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.md) frameOfReference is an orthonormal frame that defines a local coordinate system for the cone. 

  * Frame.Origin is a point on the cylinder's axis.
  * Frame.BasisZ points along the axis, while Frame.BasisX and Frame.BasisY are orthogonal to the axis. 
  * The frame may be either left-handed or right-handed (see Frame.IsRightHanded). Note that the "handedness" of the frame does not, by itself, determine the surface's orientation.



halfAngle
    Type: System..::..Double Cone angle. Must be not 0, lesser than PI/2 and greater than -PI/2. 

#### Return Value

The created ConicalSurface. 

# Remarks

The parametric equation of the cone is S(u, v) = Frame.Origin + v*[sin(halfAngle)(cos(u)*Frame.BasisX + sin(u)*Frame.BasisY) + cos(halfAngle)*Frame.BasisZ] This implies the following facts: 

  * Frame.BasisX points from the axis point to the point on the cylinder with coordinates (0, 0).
  * Frame.BasisY points in the direction of the partial derivative dS/du at (0, 0).
  * Frame.BasisZ points in the direction of the partial derivative dS/dv at (0, 0).

Only the branch of the cone with v >= 0 should be used. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | This Frame object may not be used as a local frame of reference. -or- The supplied value must be not 0, lesser than PI/2 and greater than -PI/2. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)