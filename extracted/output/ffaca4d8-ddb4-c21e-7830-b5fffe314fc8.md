

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarShapeDefinitionBySegments..::..AddConstraintToSegment Method   
[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Add a constraint that helps determine the length of a segment. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public void AddConstraintToSegment(
    	int iSegment,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) paramId,
    	double constraintDirCoordX,
    	double constraintDirCoordY,
    	int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir,
    	bool measureToOutsideOfBend0,
    	bool measureToOutsideOfBend1
    )  
  
Visual Basic  
---  
      
    
    Public Sub AddConstraintToSegment ( _
    	iSegment As Integer, _
    	paramId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md), _
    	constraintDirCoordX As Double, _
    	constraintDirCoordY As Double, _
    	signOfZCoordOfCrossProductOfConstraintDirBySegmentDir As Integer, _
    	measureToOutsideOfBend0 As Boolean, _
    	measureToOutsideOfBend1 As Boolean _
    )  
  
Visual C++  
---  
      
    
    public:
    void AddConstraintToSegment(
    	int iSegment, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ paramId, 
    	double constraintDirCoordX, 
    	double constraintDirCoordY, 
    	int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, 
    	bool measureToOutsideOfBend0, 
    	bool measureToOutsideOfBend1
    )  
  
#### Parameters

iSegment
    Type: System..::..Int32 Index of the segment (0 to NumberOfSegments - 1). 

paramId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) Id of a parameter to drive the constraint. To obtain the id of a shared parameter, call RebarShape.GetElementIdForExternalDefinition(). 

constraintDirCoordX
    Type: System..::..Double The x-coordinate of a 2D vector specifying the constraint direction. 

constraintDirCoordY
    Type: System..::..Double The y-coordinate of a 2D vector specifying the constraint direction. 

signOfZCoordOfCrossProductOfConstraintDirBySegmentDir
    Type: System..::..Int32 Legal values are 1 and -1. For a fixed-direction segment, this value is ignored. For a variable-direction segment, this value is combined with the constraint length (the nonnegative value associated with 'param') to determine the direction of the segment. For example, a segment whose direction vector lies in the upper-right quadrant of the plane, and whose x-axis projected length is A and whose y-axis projected length is B, could be created by calling: AddConstraintToSegment(iSegment, paramA, 1.0, 0.0, 1, ...) AddConstraintToSegment(iSegment, paramB, 0.0, 1.0, -1, ...) 

measureToOutsideOfBend0
    Type: System..::..Boolean Choose between two possibilities for the first reference of the length dimension. If false, the reference is at the point where the bend begins; equivalently, at the projection of the bend centerpoint onto the segment. If true, the reference is moved outward by a distance equal to the bend radius plus the bar diameter; if the bend is a right angle or greater, this is equivalent to putting the reference at the outer face of the bend. 

measureToOutsideOfBend1
    Type: System..::..Boolean Choose between two possibilities for the second reference of the length dimension. 

# Remarks

The vector defined by (constraintDirCoordX, constraintDirCoordY) must have a positive dot product with the desired direction of the segment. This restriction, combined with the value of signOfZCoordOfCrossProductOfConstraintDirBySegmentDir, defines a quadrant of the plane that limits the variable-angle segment. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | iSegment is not between 0 and NumberOfSegments. -or- paramId is not the id of a shared parameter in the current document, or its unit type is not UT_Reinforcement_Length or UT_Angle. -or- The length of the vector (constraintDirCoordX, constraintDirCoordY) is too close to zero. -or- signOfZCoordOfCrossProductOfConstraintDirBySegmentDir is neither -1 nor 1. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)