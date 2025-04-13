

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Wall..::..Create Method (Document, Curve, ElementId, ElementId, Double, Double, Boolean, Boolean)  
[Wall Class](b5891733-c602-12df-beab-da414b58d608.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new rectangular profile wall within the project using the specified wall type, height, and offset. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public static [Wall](b5891733-c602-12df-beab-da414b58d608.md) Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md) curve,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) wallTypeId,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) levelId,
    	double height,
    	double offset,
    	bool flip,
    	bool structural
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	curve As [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md), _
    	wallTypeId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md), _
    	levelId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md), _
    	height As Double, _
    	offset As Double, _
    	flip As Boolean, _
    	structural As Boolean _
    ) As [Wall](b5891733-c602-12df-beab-da414b58d608.md)  
  
Visual C++  
---  
      
    
    public:
    static [Wall](b5891733-c602-12df-beab-da414b58d608.md)^ Create(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md)^ curve, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ wallTypeId, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ levelId, 
    	double height, 
    	double offset, 
    	bool flip, 
    	bool structural
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document in which the new wall is created. 

curve
    Type: [Autodesk.Revit.DB..::..Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md) A curve representing the base line of the wall. 

wallTypeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) Id of the wall type to be used by the new wall instead of the default type. 

levelId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) Id of the level on which the wall is to be placed. 

height
    Type: System..::..Double The height of the wall other than the default height. 

offset
    Type: System..::..Double Modifies the wall's Base Offset parameter to determine its vertical placement. 

flip
    Type: System..::..Boolean Change which side of the wall is considered to be the inside and outside of the wall. 

structural
    Type: System..::..Boolean If set, specifies that the wall is structural in nature. 

#### Return Value

If successful a new wall object within the project. 

# Examples

CopyC#
    
    
    public Wall CreateWallUsingCurve2(Autodesk.Revit.DB.Document document, Level level, WallType wallType)
    {
        // Build a location line for the wall creation
        XYZ start = new XYZ(0, 0, 0);
        XYZ end = new XYZ(10, 10, 0);
        Line geomLine = Line.CreateBound(start, end);
    
        // Determine the other parameters
        double height = 15;
        double offset = 3;
    
        // Create a wall using the location line and wall type
        return Wall.Create(document, geomLine, wallType.Id, level.Id, height, offset, true, true);
    }

CopyVB.NET
    
    
    Public Function CreateWallUsingCurve2(document As Autodesk.Revit.DB.Document, level As Level, wallType As WallType) As Wall
        ' Build a location line for the wall creation
        Dim start As New XYZ(0, 0, 0)
        Dim [end] As New XYZ(10, 10, 0)
        Dim geomLine As Line = Line.CreateBound(start, [end])
    
        ' Determine the other parameters
        Dim height As Double = 15
        Dim offset As Double = 3
    
        ' Create a wall using the location line and wall type
        Return Wall.Create(document, geomLine, wallType.Id, level.Id, height, offset, _
            True, True)
    End Function

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The curve argument is not valid for wall creation. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | The given value for height must be greater than 0 and no more than 30000 feet. -or- The given value for offset must be no more than 30000 feet in absolute value. |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.md)

[Create Overload](3ef7e31c-b41b-c8cc-2713-8f098954613d.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)