

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
ExternalResourceReference Members  
[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md) Constructors Methods Properties See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md) type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
|  | [ExternalResourceReference(ExternalResourceReference)](23eafbee-60c6-6c26-e4e1-5ed224d3bd08.md) | Creates a new ExternalResourceReference from the given ExternalResourceReference. |
|  | [ExternalResourceReference(Guid, IDictionary<(Of <<'(String, String>)>>), String, String)](583b476f-68a7-2671-d5f6-0b38834bb39a.md) | Creates a new ExternalResourceReference from the given data. |
  
# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [CreateLocalResource](457745f0-5346-77ed-444b-554295ebb14b.md) | Creates an ExternalResourceReference representing a local file managed by Revit's built-in server. |
|  | [Dispose](d550b72c-00fd-18e9-c345-721f08a67c4c.md) | Releases all resources used by the [ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | [GetReferenceInformation](f02de1b9-6f2b-3c93-f7b1-8db6fa2476fb.md) | Returns a copy of an object containing previously-stored reference or lookup information about the specific resource provided by the server. |
|  | [GetResourceShortDisplayName](f2573abd-b662-1c0c-0005-3bcee6649877.md) | Gets the short display name of the external resource. |
|  | [GetResourceVersionStatus](deda452b-a0de-4431-450e-f2299c81d6d7.md) | Checks whether this ExternalResourceReference corresponds to the current version of the resource. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [HasValidDisplayPath](a79b2db7-2ef5-fd11-71e2-ecfc84f3acc5.md) | Checks whether this external Resource has a valid display path. |
|  | [IsValidReference](7df2f669-5190-1777-f5d3-6da110240711.md) | Checks whether the reference is in a valid format. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [InSessionPath](8f8d1ee6-26e4-fbad-b000-709cdc6df801.md) | The path stores the full display path which includes the server name plus the path provided by ExternalResourceServer.The path that Revit will present for user recognizing and browsing to this resource during one session of Revit.This property allows ExternalResourceServers to handle cases where the path to a resource may vary between Revit sessions. For example, if this ExternalResourceReference refers to a resource in a folder, this property can be used to store the current path of the resource. If the resource is moved to another folder later, the ExternalResourceServer could calculate the correct path for the resource from resource identification information when it is loaded and store it in this property, so that it will work correctly even if the rvt file is opened in a different location.Do not rely on this path to look up an ExternalResourceReference, as the path is neither unique nor stable. It isn't unique because multiple servers might use the same server name and display name format. It isn't stable because some servers allow renaming, and because a server might change its name at some point. |
|  | [IsValidObject](19caed9b-7603-1775-a6e4-ab0c148c0f2c.md) | Specifies whether the .NET object represents a valid Revit entity. |
|  | [ServerId](1f2b2899-334f-b018-7e5a-6c3e17e910ec.md) | The id of the server that Revit is expecting to provide the external resource. |
|  | [Version](04796691-0778-07c2-9b90-ebabeabcb1dc.md) | The version of the external data that was most recently loaded in Revit. |
  
# See Also

[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)