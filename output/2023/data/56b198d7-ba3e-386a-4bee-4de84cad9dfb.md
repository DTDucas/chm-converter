# DocumentSaveToLocalProgressChangedEventArgs Properties (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2023 API  
---  
DocumentSaveToLocalProgressChangedEventArgs Properties  
[DocumentSaveToLocalProgressChangedEventArgs Class](a3a774b8-2913-5de6-e7ad-5daa24a9c172.md "DocumentSaveToLocalProgressChangedEventArgs Class") See Also  
---  
The [DocumentSaveToLocalProgressChangedEventArgs](a3a774b8-2913-5de6-e7ad-5daa24a9c172.md "DocumentSaveToLocalProgressChangedEventArgs Class") type exposes the following members.
# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [BeforeSaveToCentral](88c6bc2d-aaa4-a2fe-7b0b-a062f7d96c52.md "BeforeSaveToCentral Property") | True if the "save to local" operation is occurring before "save to central"; false if after. |
| [Cancellable](a393138a-34b5-1724-aa69-92cef651482b.md "Cancellable Property") | Indicates whether an event may be cancelled by an event delegate.  (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |
| [FinishedStreams](1982859e-6c03-40c8-3816-eede2eed6d68.md "FinishedStreams Property") | The number of streams finished since the last time this event was raised. |
| [IsValidObject](35c0066a-b3dc-9d37-c79e-c29f90713b2d.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.md "RevitAPIEventArgs Class").) |
| [Location](3fcaf146-8612-2046-e6f1-7fff92f4246b.md "Location Property") | Full path of the central model which is to be operated.  (Inherited from [WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.md "WorksharedOperationProgressChangedEventArgs Class").) |
| [SaveToLocalFinished](38186363-5ff6-0676-1e7f-4341ddefeac7.md "SaveToLocalFinished Property") | Indicates if the current "save to local" operation has finished. |
| [Status](eb9b8675-b0c9-38bc-038d-beac4983aaaa.md "Status Property") | Gets API event status, reflect current operation execution status.  (Inherited from [WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.md "WorksharedOperationProgressChangedEventArgs Class").) |
| [TotalStreams](529c6a0e-c331-6079-e1d7-94cd1af90f59.md "TotalStreams Property") | The total expected number of streams to save to local. |

# See Also
[DocumentSaveToLocalProgressChangedEventArgs Class](a3a774b8-2913-5de6-e7ad-5daa24a9c172.md "DocumentSaveToLocalProgressChangedEventArgs Class")
[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.md "Autodesk.Revit.DB.Events Namespace")
Send comments on this topic to 