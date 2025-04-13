

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
ImageTypeOptions Members  
[ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.md) Constructors Methods Properties See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [ImageTypeOptions](981135c3-777b-df9b-747f-60a35b74e00e.md) type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
|  | [ImageTypeOptions(ExternalResourceReference, ImageTypeSource)](df96413a-2ff3-128b-7276-28980e2689ce.md) | Constructs a new instance of the ImageTypeOptions object. |
|  | [ImageTypeOptions(String, Boolean, ImageTypeSource)](7dda4131-548f-7c39-4dcd-ba9b85846018.md) | Constructs a new instance of the ImageTypeOptions object.The provided string path must specify a local file. The path can be absolute or relative to the project's location.This constructor saves an additional setting that indicates whether the imagetype will be a link or an import. |
  
# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [Dispose](8665df9b-7082-9cd5-b4dd-b0f1aa650140.md) | Releases all resources used by the [ImageTypeOptions](981135c3-777b-df9b-747f-60a35b74e00e.md) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [IsValid](47f3832b-9cf5-4628-214d-7e7e7d705393.md) | If true the ImageTypeOptions can be used to create or reload an ImageType. |
|  | [SetExternalResourceReference](0b401f0d-2333-2686-254c-14003c967314.md) | Update the external resource reference to an image. |
|  | [SetPath(String)](3eeb55a9-ced3-165d-5a9e-d75a9d7f2f20.md) | Update the path of the file that specifies the image to be used.The provided string path must specify a local file. The path can be absolute or relative to the project's location. ImageType will respectively use an absolute or relative path. |
|  | [SetPath(String, Boolean)](9c707780-4777-d34b-adbc-3092b10b42bd.md) | Update the path of the file that specifies the image to be used.The provided string path must specify a local file. The path can be absolute or relative to the project's location.Additionally, indicate whether the path used by ImageType should be absolute or relative. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [IsValidObject](d6fccbef-3786-a1ae-cd60-0a54e9ea60e6.md) | Specifies whether the .NET object represents a valid Revit entity. |
|  | [PageNumber](33b28f56-d107-868c-3554-85fe06c32397.md) | The page in the file to be used for the image |
|  | [Path](322a4a54-839e-f1f4-68ad-7c6194d1c215.md) | The path of the file that specifies the image to be used. |
|  | [Resolution](858dcd6b-5231-fb9b-b43a-7c1397c4265e.md) | The Resolution of the image is expressed in dots-per-inch and hence determines the size of a pixel in the image. |
|  | [SourceType](1d275efe-88ad-da80-d321-b31884f1c369.md) | Indicates whether the image type is a link or an import. |
  
# See Also

[ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)