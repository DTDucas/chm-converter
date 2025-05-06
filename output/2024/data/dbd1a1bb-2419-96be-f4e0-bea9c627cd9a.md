# ExternalResourceReference Members (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
ExternalResourceReference Members  
[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md "ExternalResourceReference Class") Constructors Methods Properties See Also  
---  
The [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md "ExternalResourceReference Class") type exposes the following members.
# Constructors
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [ExternalResourceReference(ExternalResourceReference)](23eafbee-60c6-6c26-e4e1-5ed224d3bd08.md "ExternalResourceReference Constructor \(ExternalResourceReference\)") | Creates a new ExternalResourceReference from the given ExternalResourceReference. |
| [ExternalResourceReference(Guid, IDictionary<(Of <<'(String, String>)>>), String, String)](583b476f-68a7-2671-d5f6-0b38834bb39a.md "ExternalResourceReference Constructor \(Guid, IDictionary\(String, String\), String, String\)") | Creates a new ExternalResourceReference from the given data. |

# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [CreateLocalResource](457745f0-5346-77ed-444b-554295ebb14b.md "CreateLocalResource Method") | Creates an ExternalResourceReference representing a local file managed by Revit's built-in server. |
| [Dispose](d550b72c-00fd-18e9-c345-721f08a67c4c.md "Dispose Method") | Releases all resources used by the [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md "ExternalResourceReference Class") |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| [GetReferenceInformation](f02de1b9-6f2b-3c93-f7b1-8db6fa2476fb.md "GetReferenceInformation Method") | Returns a copy of an object containing previously-stored reference or lookup information about the specific resource provided by the server. |
| [GetResourceShortDisplayName](f2573abd-b662-1c0c-0005-3bcee6649877.md "GetResourceShortDisplayName Method") | Gets the short display name of the external resource. |
| [GetResourceVersionStatus](deda452b-a0de-4431-450e-f2299c81d6d7.md "GetResourceVersionStatus Method") | Checks whether this ExternalResourceReference corresponds to the current version of the resource. |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [HasValidDisplayPath](a79b2db7-2ef5-fd11-71e2-ecfc84f3acc5.md "HasValidDisplayPath Method") | Checks whether this external Resource has a valid display path. |
| [IsValidReference](7df2f669-5190-1777-f5d3-6da110240711.md "IsValidReference Method") | Checks whether the reference is in a valid format. |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [InSessionPath](8f8d1ee6-26e4-fbad-b000-709cdc6df801.md "InSessionPath Property") | The path stores the full display path which includes the server name plus the path provided by ExternalResourceServer.The path that Revit will present for user recognizing and browsing to this resource during one session of Revit.This property allows ExternalResourceServers to handle cases where the path to a resource may vary between Revit sessions. For example, if this ExternalResourceReference refers to a resource in a folder, this property can be used to store the current path of the resource. If the resource is moved to another folder later, the ExternalResourceServer could calculate the correct path for the resource from resource identification information when it is loaded and store it in this property, so that it will work correctly even if the rvt file is opened in a different location.Do not rely on this path to look up an ExternalResourceReference, as the path is neither unique nor stable. It isn't unique because multiple servers might use the same server name and display name format. It isn't stable because some servers allow renaming, and because a server might change its name at some point. |
| [IsValidObject](19caed9b-7603-1775-a6e4-ab0c148c0f2c.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity. |
| [ServerId](1f2b2899-334f-b018-7e5a-6c3e17e910ec.md "ServerId Property") | The id of the server that Revit is expecting to provide the external resource. |
| [Version](04796691-0778-07c2-9b90-ebabeabcb1dc.md "Version Property") | The version of the external data that was most recently loaded in Revit. |

# See Also
[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md "ExternalResourceReference Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 