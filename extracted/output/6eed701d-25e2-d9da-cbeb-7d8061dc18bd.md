

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
ClassificationEntry Members  
[ClassificationEntry Class](11e0e748-358f-47f7-565d-e2e848d97fe8.md) Constructors Methods Properties See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [ClassificationEntry](11e0e748-358f-47f7-565d-e2e848d97fe8.md) type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
|  | [ClassificationEntry](54aea4a8-c569-8667-7816-d9d8a2c93abd.md) | Constructs a ClassificationEntry object |
  
# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [Dispose](1facc428-7054-9be5-1e69-bf15f10be55b.md) | (Inherited from [KeyBasedTreeEntry](119355ca-f9b6-3d6a-b315-6977ac95edbe.md).) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | [GetChildrenKeys](f3bfae7c-ab5a-41ec-8f10-e1fdab0383ef.md) | Gets a collection containing the keys of all children entry objects from this entry.  (Inherited from [KeyBasedTreeEntry](119355ca-f9b6-3d6a-b315-6977ac95edbe.md).) |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [HasBadCategoryId](995f6795-6527-4ac1-5bef-a24d4972fab7.md) | Checks if the category id is Revit BuiltInCategory id. |
|  | [HasBadLevel](69b9940f-9890-8aa7-c935-67c5c80b2f24.md) | Checks if the level is an integer in range between 1 and 5 inclusive. |
|  | [HasInvalidKey](4f632955-9e4f-80e8-6220-75fdfa15298d.md) | Checks if the key matches the level and parent key. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [CategoryId](0df469ce-96b5-5f05-3a04-b0a4f191c131.md) | The id of the category associated with this entry. |
|  | [Description](192f2f9f-cd1e-af85-1a85-daa474bb5086.md) | The description associated with this entry. |
|  | [IsValidObject](45dd48e4-2b94-5484-9050-d77a56d25f90.md) | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [KeyBasedTreeEntry](119355ca-f9b6-3d6a-b315-6977ac95edbe.md).) |
|  | [Key](a9234c64-9ec4-7c5e-e94e-70e69452ca1c.md) | The key of this entry.  (Inherited from [KeyBasedTreeEntry](119355ca-f9b6-3d6a-b315-6977ac95edbe.md).) |
|  | [Level](7a781ba4-66bd-1433-75ec-5babb73f3a6a.md) | The entry level in the classification table. The expected range is between 1 and 5 inclusive. |
|  | [ParentKey](6fa8dcd2-5fc4-5ec2-033a-a9dd09e5ff99.md) | The parent key of this entry.  (Inherited from [KeyBasedTreeEntry](119355ca-f9b6-3d6a-b315-6977ac95edbe.md).) |
  
# See Also

[ClassificationEntry Class](11e0e748-358f-47f7-565d-e2e848d97fe8.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)