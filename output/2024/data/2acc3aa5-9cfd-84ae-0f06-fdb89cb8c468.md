# IndexBuffer Methods (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
IndexBuffer Methods  
[IndexBuffer Class](186f6b15-38c7-cee7-6163-396cfdea43ee.md "IndexBuffer Class") See Also  
---  
The [IndexBuffer](186f6b15-38c7-cee7-6163-396cfdea43ee.md "IndexBuffer Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Dispose](b20fe037-d539-7b78-25ca-fa9841e57eba.md "Dispose Method") |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| [GetIndexStreamLine](ebc0cd34-62cd-9eed-0eb5-9b54c0a260b6.md "GetIndexStreamLine Method") | Gets a stream that can be used to write [IndexLine](3b22e25e-f934-3931-6f22-e451ffcc11b0.md "IndexLine Class") segment primitives into the buffer. |
| [GetIndexStreamPoint](4ec45b4f-4565-7724-bf92-25a723ee315e.md "GetIndexStreamPoint Method") | Gets a stream that can be used to write [IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md "IndexPoint Class") primitives into the buffer. |
| [GetIndexStreamTriangle](02ba04da-3f69-65e9-1070-5ba51467c13a.md "GetIndexStreamTriangle Method") | Gets a stream that can be used to write [IndexTriangle](96cdfb77-c6e0-7866-c1f7-799f3dda0ad5.md "IndexTriangle Class") primitives into the buffer. |
| [GetMappedHandle](b817304d-d9e7-6503-31ba-a8b058ac2377.md "GetMappedHandle Method") | Gets a handle to the buffer's memory that has been mapped. Writing data to the buffer using the handle is an alternative to using stream objects. |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [IsValid](e1c07c2d-42f4-f2d8-0a10-219ad78a1fd6.md "IsValid Method") | Tests whether the buffer is valid for rendering. |
| [Map](f330f770-6571-abb2-9615-6c5eb0e4f525.md "Map Method") | Maps a portion of the index buffer into memory, so that indices can be written into it. see [IndexStream](9c300586-7f1f-41db-270b-797d6ad967d8.md "IndexStream Class"). |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |
| [Unmap](c3d125d9-e95e-5466-8818-1959f87e2889.md "Unmap Method") | Unmaps the buffer so that it can be used for rendering. |

# See Also
[IndexBuffer Class](186f6b15-38c7-cee7-6163-396cfdea43ee.md "IndexBuffer Class")
[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")
Send comments on this topic to 