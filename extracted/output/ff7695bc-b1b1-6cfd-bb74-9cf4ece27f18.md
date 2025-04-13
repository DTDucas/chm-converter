

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
View..::..UnhideElements Method   
[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Sets the elements to be shown in the given view if they are currently hidden.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public void UnhideElements(
    	ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> elementIdSet
    )  
  
Visual Basic  
---  
      
    
    Public Sub UnhideElements ( _
    	elementIdSet As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)) _
    )  
  
Visual C++  
---  
      
    
    public:
    void UnhideElements(
    	ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ elementIdSet
    )  
  
#### Parameters

elementIdSet
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)>A set of ElementIds to be unhidden.

# Remarks

This change is permanent until the elements are hidden again. All elements in the set must be currently hidden. An application can check this with [IsHidden(View)](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.md).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | Thrown when argument is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | Thrown when the set of elements to be unhidden is empty or one of the elements can not be unhidden. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown when document regeneration failed. |
  
# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)