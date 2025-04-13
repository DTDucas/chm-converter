

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ViewSchedule..::..SplitSegment Method   
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Splits the schedule segment by the given heights of new segments. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022.1 

# Syntax

C#  
---  
      
    
    public void SplitSegment(
    	int segmentIndex,
    	IList<double> segmentHeights
    )  
  
Visual Basic  
---  
      
    
    Public Sub SplitSegment ( _
    	segmentIndex As Integer, _
    	segmentHeights As IList(Of Double) _
    )  
  
Visual C++  
---  
      
    
    public:
    void SplitSegment(
    	int segmentIndex, 
    	IList<double>^ segmentHeights
    )  
  
#### Parameters

segmentIndex
    Type: System..::..Int32 The index of segment, starting with 0. 

segmentHeights
    Type: System.Collections.Generic..::..IList<(Of <(<'Double>)>)> An array contains the height for each new segment except the last segment. The height of the last segment will be determined by the height of previous new segments and the height of the split segment. 

# Remarks

The height values are used to set the height of schedule instance for each segment shown on sheet view. Each input height must be greater than 0 and the total height must be less than the height of the split segment. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The height of a schedule segment must be greater than 0. The total height must be less than the split segment height. The total segment count must be greater than 0 and less than 10000. -or- The segment index should start from 0 and be less than the total segment count. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | This ViewSchedule is not split yet. |
  
# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)