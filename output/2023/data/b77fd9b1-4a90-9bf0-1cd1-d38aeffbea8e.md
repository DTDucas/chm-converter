# GroupNode Members (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2023 API  
---  
GroupNode Members  
[GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.md "GroupNode Class") Methods Properties See Also  
---  
The [GroupNode](8b1cabde-3c37-1735-a186-2ce026555ce0.md "GroupNode Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Dispose](8ee082fe-ab92-67e6-f2bd-b285d419a005.md "Dispose Method") | (Inherited from [RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.md "RenderNode Class").) |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| [GetSymbolId](dfcbb10c-a314-be18-0eef-b7f07f08c59d.md "GetSymbolId Method") | **Obsolete.** The Id of the symbol associated with the node. This property is deprecated in Revit 2023 and may be removed in a future version of Revit. For an InstanceNode please use the GetSymbolGeometryId().SymbolId. For a LinkNode please use SymbolId property. In Revit 2023 we introduced instance nodes that point to a part of the symbol's geometry. For comparing if two such nodes point to the same geometry, the SymbolId isn't enough. SymbolGeometryId can be used to identify a piece of geometry managed by a symbol element. |
| [GetTransform](13e9ba28-e94a-c79f-689c-4367883d62bd.md "GetTransform Method") | A transformation matrix associated with the node. |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [IsValidObject](5e642162-fd60-8697-24d2-b2c8574d4fb2.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.md "RenderNode Class").) |
| [NodeName](f00a73db-fecc-70eb-c81a-67ef27212de5.md "NodeName Property") | A readable name of the output node.  (Inherited from [RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.md "RenderNode Class").) |

# See Also
[GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.md "GroupNode Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 