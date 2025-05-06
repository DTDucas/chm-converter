# DockablePaneState Members (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2023 API  
---  
DockablePaneState Members  
[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.md "DockablePaneState Class") Constructors Methods Properties See Also  
---  
The [DockablePaneState](0255200b-8af3-3254-ca6b-043f5cc291cf.md "DockablePaneState Class") type exposes the following members.
# Constructors
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [DockablePaneState()()()()](a0cd9042-b64c-75ff-c45c-d0cb9db80c06.md "DockablePaneState Constructor") | Creates a new DockablePaneState object. |
| [DockablePaneState(DockablePaneState)](58c79873-9e2c-b9ac-2c5d-a3cf5538c90a.md "DockablePaneState Constructor \(DockablePaneState\)") | Constructs a new copy of the input DockablePaneState object. |

# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Dispose](68833347-063e-c708-5b6b-c12dec4efc5a.md "Dispose Method") | Releases all resources used by the [DockablePaneState](0255200b-8af3-3254-ca6b-043f5cc291cf.md "DockablePaneState Class") |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [SetFloatingRectangle](0dda1168-e11a-a276-1535-74c64c677c4c.md "SetFloatingRectangle Method") | When %dockPosition% is Floating, sets the rectangle used to determine the size and position of the pane when %dockPosition% is Floating. Coordinates are relative to the upper-left-hand corner of the main Revit window. |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [DockPosition](3d87dd54-a970-c09b-c113-d2e700cd2f0f.md "DockPosition Property") | Which part of the Revit application frame the pane should dock to. |
| [FloatingRectangle](d1dcb64c-2f08-d2a6-ddc7-01c76c1a6a59.md "FloatingRectangle Property") | When %dockPosition% is Floating, this rectangle determines the size and position of the pane. Coordinates are relative to the upper-left-hand corner of the main Revit window. Note: the returned Rectangle is a copy. In order to change the pane state, you must call SetFloatingRectangle with a modified rectangle. |
| [IsValidObject](9a1720f3-3bd2-61ae-37d6-0b1ca8104d30.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity. |
| [MinimumHeight](09e43d6f-77c2-0c81-654a-47a135280d43.md "MinimumHeight Property") | When %dockPosition% is anything other than floating, the minimum height to use for the pane. Default is 200 pixels. |
| [MinimumWidth](f22b8f98-87c8-7a8f-45c7-5d8b67034a14.md "MinimumWidth Property") | When %dockPosition% is anything other than floating, the minimum width to use for the pane. Default is 200 pixels. |
| [TabBehind](05fde7c9-8b43-bb29-e37f-0386a00b2525.md "TabBehind Property") | Ignored unless %dockPosition% is Tabbed. The new pane will appear in a tab behind the specified existing pane ID. |

# See Also
[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.md "DockablePaneState Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 