

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ViewSchedule..::..KeyScheduleParameterName Property   
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
In a key schedule, the name of the parameter for choosing one of the keys. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public string KeyScheduleParameterName { get; set; }  
  
Visual Basic  
---  
      
    
    Public Property KeyScheduleParameterName As String
    	Get
    	Set  
  
Visual C++  
---  
      
    
    public:
    property String^ KeyScheduleParameterName {
    	String^ get ();
    	void set (String^ value);
    }  
  
#### Field Value

The name of the key schedule parameter. 

# Remarks

When a key schedule is created, elements of the schedule's category receive a new parameter for choosing one of the keys defined in the key schedule. This is the name of that parameter. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | This ViewSchedule is not key schedule. |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | When setting this property: The document containing this ViewSchedule is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- When setting this property: The document containing this ViewSchedule is being loaded, or is in the midst of another sensitive process. -or- When setting this property: This ViewSchedule is an internal element, such as a component of a loaded family or a group type. -or- When setting this property: The document containing this ViewSchedule is in Group Edit Mode, Sketch Edit Mode, or Paste Mode, and the element is not a member of the group, sketch, or clipboard. -or- When setting this property: This ViewSchedule is a member of a group or sketch, and the document is not currently editing the group or sketch. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | When setting this property: The document containing this ViewSchedule has no open transaction. |
  
# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)