# UpdaterData Members (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
UpdaterData Members  
[UpdaterData Class](58751d04-6f56-0346-e7ba-f21e61a459be.md "UpdaterData Class") Methods Properties See Also  
---  
The [UpdaterData](58751d04-6f56-0346-e7ba-f21e61a459be.md "UpdaterData Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Dispose](6ad46f9b-e128-d03a-c017-d5ed70d4438a.md "Dispose Method") | Releases all resources used by the [UpdaterData](58751d04-6f56-0346-e7ba-f21e61a459be.md "UpdaterData Class") |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| [GetAddedElementIds](b9676f82-ebc4-79f8-160e-4d3c4c1823a2.md "GetAddedElementIds Method") | Returns set of elements newly added to the document. This set is mutually exclusive of elements returned by getDeletedElementIds() and getModifiedElementIds(). |
| [GetDeletedElementIds](d19575f3-a6cb-c532-78a2-2b513378af4a.md "GetDeletedElementIds Method") | Returns set of elements that were deleted from the document. This set is mutually exclusive of elements returned by getAddedElementIds() and getModifiedElementIds(). |
| [GetDocument](cb58fbb1-e923-b2f3-8b74-9aac45ad2d0f.md "GetDocument Method") | Returns document associated with this UpdaterData |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| [GetModifiedElementIds](f06a0804-5756-47e7-3dc3-bcc828e5adaf.md "GetModifiedElementIds Method") | Returns set of elements that were modified. This set is mutually exclusive of elements returned by getAddedElementIds() and getDeletedElementIds(). |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [IsChangeTriggered](c5dcda11-ce70-52d3-f415-60dc4c2d88a2.md "IsChangeTriggered Method") | Allows updater to check if specific change has happened to an element. Compares input type to the types that caused Updater::execute() to be triggered. If input type was not registered as a trigger for the associated Updater, this method will always return false for that ChangeType. For example, if the only trigger registered for UpdaterX is ChangeTypeAny for Element A, then passing in ChangeTypeGeometry will return false even if the geometry of A changed because the registered trigger was ChangeTypeAny. However, passing in ChangeTypeAny will return true. |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [IsValidObject](d31d4b45-19e4-64c0-875b-f0bfd664320b.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity. |

# See Also
[UpdaterData Class](58751d04-6f56-0346-e7ba-f21e61a459be.md "UpdaterData Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 