

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ViewSchedule..::..RowHeightOverride Property   
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Defines the override that is applied to the row height. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 

# Syntax

C#  
---  
      
    
    public [RowHeightOverrideOptions](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) RowHeightOverride { get; set; }  
  
Visual Basic  
---  
      
    
    Public Property RowHeightOverride As [RowHeightOverrideOptions](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md)
    	Get
    	Set  
  
Visual C++  
---  
      
    
    public:
    property [RowHeightOverrideOptions](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) RowHeightOverride {
    	[RowHeightOverrideOptions](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) get ();
    	void set ([RowHeightOverrideOptions](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) value);
    }  
  
#### Field Value

  * [None](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) to disable row height override.
  * [All](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) enables row height override for all the body rows in the schedule.
  * [ImageRows](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) enables row height override for all the schedule body rows that contains images or custom graphics.



# Remarks

Setting this property to anything but [None](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md) will allow setting the [RowHeight](aca396e1-2fec-666c-005d-7e36d5153999.md) property. This is taken into account when the schedule is viewed as a ScheduleSheetInstance on a ViewSheet.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
  
# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)