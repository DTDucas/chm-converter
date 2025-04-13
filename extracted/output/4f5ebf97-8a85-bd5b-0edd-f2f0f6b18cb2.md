

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
DatumPlane..::..GetLeader Method   
[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Gets a copy of the leader applied to the indicated end of the datum plane. This method does not apply to Reference planes (which do not support leaders). 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 

# Syntax

C#  
---  
      
    
    public [Leader](66228564-d8b8-fc81-454c-e175528f7188.md) GetLeader(
    	[DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.md) datumEnd,
    	[View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) view
    )  
  
Visual Basic  
---  
      
    
    Public Function GetLeader ( _
    	datumEnd As [DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.md), _
    	view As [View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) _
    ) As [Leader](66228564-d8b8-fc81-454c-e175528f7188.md)  
  
Visual C++  
---  
      
    
    public:
    [Leader](66228564-d8b8-fc81-454c-e175528f7188.md)^ GetLeader(
    	[DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.md) datumEnd, 
    	[View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)^ view
    )  
  
#### Parameters

datumEnd
    Type: [Autodesk.Revit.DB..::..DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.md) The end of the datum plane. 

view
    Type: [Autodesk.Revit.DB..::..View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) The view on which the DatumPlane shows. 

#### Return Value

The Leader of the datum plane. Null will return if no leader applied. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The datum plane cannot be visible in the view. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | This datum plane has no leaders. |
  
# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)