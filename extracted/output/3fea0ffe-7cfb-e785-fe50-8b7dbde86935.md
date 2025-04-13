

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
DetailElementOrderUtils Members  
[DetailElementOrderUtils Class](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.md) Methods See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [DetailElementOrderUtils](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.md) type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [AreDetailElements](950de8f3-daa2-1023-eb83-cd0695ebb565.md) | Indicates if the elements are all detail elements that participate in detail draw ordering in the view. |
|  | [BringForward(Document, View, ElementId)](3110546a-c758-af2d-d5b1-2d5581f18555.md) | Moves the given detail instance one step closer to the front of all other detail instances in the view. |
|  | [BringForward(Document, View, ICollection<(Of <<'(ElementId>)>>))](fbf91f76-0c21-37dc-c69f-609c85753209.md) | Moves the given detail instances one step closer to the front of all other detail instances in the view, while keeping the order of the given ones. |
|  | [BringToFront(Document, View, ElementId)](734b7f03-6c46-b4b8-f3ed-c370df205e7b.md) | Places the given detail instance in the front of all other detail instances in the view. |
|  | [BringToFront(Document, View, ICollection<(Of <<'(ElementId>)>>))](b6cec4f5-c4ef-d4c6-cdb8-1e92997e019c.md) | Places the given detail instances in the front of all other detail instances in the view, while keeping the order of the given ones. |
|  | [GetDrawOrderForDetails](686020d6-9ca3-c51f-47fc-a54438e3f608.md) | Returns the given detail elements according to the currently specified draw order for the detail elements in a given view. |
|  | [IsDetailElement](8c7d0547-19ec-6ee0-5e96-02bbf717c54e.md) | Indicates if the element is a detail element that participates in detail draw ordering in the view. |
|  | [SendBackward(Document, View, ElementId)](9d2f8369-7929-06a9-98c2-cff426963ba2.md) | Moves the given detail instance one step closer to the back of all other detail instances in the view. |
|  | [SendBackward(Document, View, ICollection<(Of <<'(ElementId>)>>))](0d971884-a987-7ca9-6e13-e7c9fe030109.md) | Moves the given detail instances one step closer to the back with relation to all other detail instances in the view, while keeping the order of the given ones. |
|  | [SendToBack(Document, View, ElementId)](28209b7b-e75e-36d9-f916-d1cdaebe051d.md) | Places the given detail instance behind all detail instances in the view. |
|  | [SendToBack(Document, View, ICollection<(Of <<'(ElementId>)>>))](edd4a515-1f60-c99f-09f5-865be893ea24.md) | Places the given detail instances behind all other detail instances in the view, while keeping the order of the given ones. |
  
# See Also

[DetailElementOrderUtils Class](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)