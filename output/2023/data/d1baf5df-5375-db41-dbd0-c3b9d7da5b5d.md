# DocumentClosingEventArgs Members (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2023 API  
---  
DocumentClosingEventArgs Members  
[DocumentClosingEventArgs Class](939d187e-051c-6a8a-0bb9-6c030b0911a4.md "DocumentClosingEventArgs Class") Methods Properties See Also  
---  
The [DocumentClosingEventArgs](939d187e-051c-6a8a-0bb9-6c030b0911a4.md "DocumentClosingEventArgs Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Cancel](88fa78de-0fff-a85f-0de3-b631673e9e51.md "Cancel Method") | When the event is cancellable, may call the Cancel() method to cancel it.  (Inherited from [RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.md "RevitAPIPreEventArgs Class").) |
| [Dispose](697794d0-db4b-41ee-90a3-388296ffeefb.md "Dispose Method") | (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [IsCancelled](5627aeaa-9d9c-dcbe-b34f-db40f1c025be.md "IsCancelled Method") | Indicates whether the event is being cancelled.  (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.md "Cancellable Property") | Indicates whether an event may be cancelled by an event delegate.  (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |
| [Document](ccbc5e47-3964-cf1e-4cac-fa023d3b8e63.md "Document Property") | The document associated with the event.  (Inherited from [RevitAPIPreDocEventArgs](ef0073c4-f86b-64b9-12f2-268f4e1b8bbe.md "RevitAPIPreDocEventArgs Class").) |
| [DocumentId](c1f2fa0f-0071-caef-34d7-b966458fc60b.md "DocumentId Property") | Id of the document that is about to be closed. |
| [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |

# See Also
[DocumentClosingEventArgs Class](939d187e-051c-6a8a-0bb9-6c030b0911a4.md "DocumentClosingEventArgs Class")
[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")
Send comments on this topic to 