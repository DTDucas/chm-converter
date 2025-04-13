

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
MultistoryStairs..::..Unpin Method   
[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Removes a particular story of the stairs (identified by its base level id) from a stairs group. 

**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 

# Syntax

C#  
---  
      
    
    public [Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.md) Unpin(
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) levelId
    )  
  
Visual Basic  
---  
      
    
    Public Function Unpin ( _
    	levelId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) _
    ) As [Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.md)  
  
Visual C++  
---  
      
    
    public:
    [Stairs](45e2c068-7e52-c84a-cfb8-a53c531d28fa.md)^ Unpin(
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ levelId
    )  
  
#### Parameters

levelId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) The base level id. If the level id belongs to the base level of a unpinned stairs element, it returns the stairs id directly. 

#### Return Value

The unpinned stairs element. 

# Remarks

If the story at the given level is in a group, it will separate an individual stairs element from the group with "unpinned" status. Changes you make to the returned stairs element will not affect any other stairs. If the story of stairs is already an individual stairs element, the status will be changed to "unpinned". 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | There is no stairs instance at the given base levelId. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.md)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)