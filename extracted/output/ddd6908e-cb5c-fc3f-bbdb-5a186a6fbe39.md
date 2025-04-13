

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
DockablePaneState Properties  
[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [DockablePaneState](0255200b-8af3-3254-ca6b-043f5cc291cf.md) type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [DockPosition](3d87dd54-a970-c09b-c113-d2e700cd2f0f.md) | Which part of the Revit application frame the pane should dock to. |
|  | [FloatingRectangle](d1dcb64c-2f08-d2a6-ddc7-01c76c1a6a59.md) | When %dockPosition% is Floating, this rectangle determines the size and position of the pane. Coordinates are relative to the upper-left-hand corner of the main Revit window. Note: the returned Rectangle is a copy. In order to change the pane state, you must call SetFloatingRectangle with a modified rectangle. |
|  | [IsValidObject](9a1720f3-3bd2-61ae-37d6-0b1ca8104d30.md) | Specifies whether the .NET object represents a valid Revit entity. |
|  | [MinimumHeight](09e43d6f-77c2-0c81-654a-47a135280d43.md) | When %dockPosition% is anything other than floating, the minimum height to use for the pane. Default is 200 pixels. |
|  | [MinimumWidth](f22b8f98-87c8-7a8f-45c7-5d8b67034a14.md) | When %dockPosition% is anything other than floating, the minimum width to use for the pane. Default is 200 pixels. |
|  | [TabBehind](05fde7c9-8b43-bb29-e37f-0386a00b2525.md) | Ignored unless %dockPosition% is Tabbed. The new pane will appear in a tab behind the specified existing pane ID. |
  
# See Also

[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.md)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)