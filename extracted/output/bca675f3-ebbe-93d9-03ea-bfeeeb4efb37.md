# CreateRelatedFileProgressChangedEventArgs Members

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
CreateRelatedFileProgressChangedEventArgs Members  
[CreateRelatedFileProgressChangedEventArgs Class](94a4184c-e0d2-a846-ba1d-52cea6b0a29f.md "CreateRelatedFileProgressChangedEventArgs Class") Methods Properties See Also  
---  
The [CreateRelatedFileProgressChangedEventArgs](94a4184c-e0d2-a846-ba1d-52cea6b0a29f.md "CreateRelatedFileProgressChangedEventArgs Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
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
| [CreatingCloudSharedLocal](34a1b78a-db34-0c9e-1444-9bb306ce5625.md "CreatingCloudSharedLocal Property") | Indicates if it is creating cloud shared local model. |
| [DownloadFinished](3c4bca7d-e030-22e2-cb4b-634dcb9a30f9.md "DownloadFinished Property") | Indicates if all data downloads are finished. |
| [FinishedSize](e1f72113-d1ce-4fc7-39b2-c854563ca6bb.md "FinishedSize Property") | The transferred data size, in bytes, since the last time this event was raised.  (Inherited from [DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.md "DataTransferProgressChangedEventArgs Class").) |
| [FullDownload](103ccd84-2094-1dfe-c7b5-19d0c314045a.md "FullDownload Property") | Indicates if download the full data of the document, which will take longer than subsequent downloads. |
| [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |
| [Location](3fcaf146-8612-2046-e6f1-7fff92f4246b.md "Location Property") | Full path of the central model which is to be operated.  (Inherited from [WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.md "WorksharedOperationProgressChangedEventArgs Class").) |
| [Speed](62fdd863-88f8-aa92-d93a-445b57971471.md "Speed Property") | Speed(bytes/second) in this event.  (Inherited from [DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.md "DataTransferProgressChangedEventArgs Class").) |
| [Status](eb9b8675-b0c9-38bc-038d-beac4983aaaa.md "Status Property") | Gets API event status, reflect current operation execution status.  (Inherited from [WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.md "WorksharedOperationProgressChangedEventArgs Class").) |
| [TotalSize](c92d243d-ee90-f05c-e745-cb63d7a0b2b2.md "TotalSize Property") | Total expected data size to transfer, in bytes.  (Inherited from [DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.md "DataTransferProgressChangedEventArgs Class").) |
| [TransferMode](1e471493-fb1a-9c29-4e64-81e79d9440e4.md "TransferMode Property") | Data transfer mode in this event.  (Inherited from [DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.md "DataTransferProgressChangedEventArgs Class").) |

# See Also
[CreateRelatedFileProgressChangedEventArgs Class](94a4184c-e0d2-a846-ba1d-52cea6b0a29f.md "CreateRelatedFileProgressChangedEventArgs Class")
[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)