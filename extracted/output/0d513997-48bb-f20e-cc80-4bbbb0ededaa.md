

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
BRepBuilderPersistentIds Methods  
[BRepBuilderPersistentIds Class](c9dd5c21-1d35-9f12-ec28-553e699a6ee2.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [BRepBuilderPersistentIds](c9dd5c21-1d35-9f12-ec28-553e699a6ee2.md) type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [AddSubTag](c8bf3c16-6864-8323-3c57-c132e9282473.md) | Adds a correspondence between an ExternalGeometryId and a BRepBuilderGeometryId. Note that an existing correspondence in the map cannot be updated and that a particular BRepBuilderGeometryId may be related to at most one ExternalGeometryId. |
|  | [Dispose](73d61523-7280-b04d-480f-9ae04a9373af.md) |  |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [IsAssociatedBRepBuilderValid](817496ab-6542-91cf-247d-6455add3df09.md) | Validates the associated (in the constructor) BRepBuilder for this BRepBuilderPersistentIds. |
|  | [IsBRepBuilderGeometryIdFaceOrEdge](22fae990-9618-4ea0-3fc7-775000c40a94.md) | Validates the input BRepBuilderGeometryId that will be used to create a correspondence. In order to be valid, the input BRepBuilderGeometryId must represent the ID of either a Face or an Edge. |
|  | [IsValidBRepBuilderGeometryIdForNewCorrespondence](1d7e2823-e05b-2519-a55b-1b3075744497.md) | Validates the input BRepBuilderGeometryId that will be used to create a correspondence. In order to be valid, a correspondence for the input BRepBuilderGeometryId must not already exist. |
|  | [IsValidExternalGeometryIdForNewCorrespondence](634779e5-d3d2-c68c-ccc8-07731fe44486.md) | Validates the input ExternalGeometryId that will be used to create a correspondence. In order to be valid, a correspondence for the input ExternalGeometryId must not already exist. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# See Also

[BRepBuilderPersistentIds Class](c9dd5c21-1d35-9f12-ec28-553e699a6ee2.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)