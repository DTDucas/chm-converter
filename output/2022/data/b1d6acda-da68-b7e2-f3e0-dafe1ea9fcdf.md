# BuiltInFailures.RoomFailures Members (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2022 API  
---  
BuiltInFailures..::..RoomFailures Members  
[BuiltInFailures..::..RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.md "BuiltInFailures.RoomFailures Class") Properties See Also  
---  
Provides a container of all Revit built-in FailureDefinitionId instances.
The [BuiltInFailures..::..RoomFailures](7bece7b1-6ad8-1153-a15a-5b16feabe08b.md "BuiltInFailures.RoomFailures Class") type exposes the following members.
# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [AreaTagBadViewType](eb8d5688-3a68-2782-69c1-f6467dce6a31.md "AreaTagBadViewType Property") | Can't Copy Area Tags. The target view doesn't have the same Area Scheme as the original view. |
| [AreaUnplaceWarning](dce88637-bbde-8c04-8282-e811776dfa00.md "AreaUnplaceWarning Property") | An Area was deleted from all model views but still remains in this project. \n The area can be removed from any schedule or placed back in the model using the Area command. |
| [CannotMakeRoomsGeometry](65d75bca-24ee-c12d-11c3-6b5eb03ef755.md "CannotMakeRoomsGeometry Property") | Could not create geometry for [Room]. |
| [ExtensionsOverlapWarning](66a9b9d1-f915-b85b-39e0-5ba41c03ffc9.md "ExtensionsOverlapWarning Property") | Vertical Extensions on these Walls overlap. This can cause undesirable Joins. Try starting with no overlap and extend the Walls toward one another. |
| [InvalidReflectivityPercentage](4ce5817d-edc6-8b74-3b36-6cabd8444137.md "InvalidReflectivityPercentage Property") | The value for Reflectivity must be between 0 and 1. |
| [InvisibleRoomBoundElemement](a5f15b21-838e-1123-8584-c16a4904b4eb.md "InvisibleRoomBoundElemement Property") | [Room] Bounding element is invisible in current view. |
| [OptionConflictBoundariesVaryMainAddToOptionSet](d73d5909-c162-066b-562c-698dd77c5903.md "OptionConflictBoundariesVaryMainAddToOptionSet Property") | Option Conflict between Rooms.\nRoom boundary in the Main Model differs from the apparent boundary in view '[View Name]'.\nTo resolve, select the Main Model Room and use the Add to Design Option Set command. |
| [OptionConflictBoundariesVaryMainSeparate](d37cc652-16bd-8863-5575-891738100ec2.md "OptionConflictBoundariesVaryMainSeparate Property") | Option Conflict between Rooms.\nRoom boundary in the Main Model differs from the apparent boundary in view '[View Name]'.\nTo resolve, divide space with Room Separation Lines in the Main Model. |
| [OptionConflictBoundariesVaryOptionSeparate](c4216663-7601-84ce-fcbe-b2b062dea379.md "OptionConflictBoundariesVaryOptionSeparate Property") | Option Conflict between Rooms.\nRoom boundary differs from the apparent boundary in view '[View Name]'.\nTo resolve, divide space with Room Separation Lines in the Main Model. |
| [OptionConflictInLinkBoundariesVaryMainAddToOptionSet](641a3afa-f3af-c665-c4eb-d5b43b21e98e.md "OptionConflictInLinkBoundariesVaryMainAddToOptionSet Property") | Option conflict between rooms in the Revit link '[Link Instance Name]'.\nThe room boundary in the main model of the Revit link differs from the apparent boundary in the linked view '[View Name from Link]'.\nTo resolve the issue, open the Revit link file for editing, select the main model room, and use the Add to Design Option Set tool. |
| [OptionConflictInLinkBoundariesVaryMainSeparate](e735d3ab-75ef-c51f-81be-6cac90ef1c26.md "OptionConflictInLinkBoundariesVaryMainSeparate Property") | Option conflict between rooms in the Revit link '[Link Instance Name]'.\nThe room boundary in the main model of the Revit link differs from the apparent boundary in the linked view '[View Name from Link]'.\nTo resolve the issue, open the Revit link file for editing, and use room separation lines to divide the space in the main model. |
| [OptionConflictInLinkBoundariesVaryOptionSeparate](8e04df89-1ea3-4e04-5e19-41af26bef00e.md "OptionConflictInLinkBoundariesVaryOptionSeparate Property") | Option conflict between rooms in the Revit link '[Link Instance Name]'.\nThe room boundary differs from the apparent boundary in the linked view '[View Name from Link]'.\nTo resolve the issue, open the Revit link file for editing, and use room separation lines to divide the space in the main model. |
| [OptionConflictInLinkRoomOverlapMain](aac4d444-df89-cb31-3c00-6acbf4924318.md "OptionConflictInLinkRoomOverlapMain Property") | Option conflict between rooms in the Revit link '[Link Instance Name]'.\nThe room in the Revit link's option '[Option Name in Link]' overlaps a room in the main model.\nTo resolve the issue, open the Revit link file for editing, select the main model room, and use the Add to Design Option Set tool. |
| [OptionConflictInLinkRoomOverlapOption](2b855aff-0da4-486e-fc20-ec493ccd6798.md "OptionConflictInLinkRoomOverlapOption Property") | Option conflict between rooms in the Revit link '[Link Instance Name]'.\nA room in the Revit link's option '[Option #1 Name in Link]' overlaps a room in the Revit link's option '[Option #2 Name in Link]'.\nTo resolve the issue, open the Revit link file for editing, and delete the duplicate room or use room separation lines to divide the space in the main model. |
| [OptionConflictRoomOverlapMain](076780c2-e62f-9795-b6f6-eeee24e44e8e.md "OptionConflictRoomOverlapMain Property") | Option Conflict between Rooms.\nRoom in Option '[Option Name]' overlaps Room in the Main Model.\nTo resolve, select the Main Model Room and use the Add to Design Option Set command. |
| [OptionConflictRoomOverlapOption](c1a22e1d-c836-5759-8245-66c2e5b0c71c.md "OptionConflictRoomOverlapOption Property") | Option Conflict between Rooms.\nRoom in Option '[Option Name]' overlaps Room in Option '[Option Name]'.\nTo resolve, delete the duplicate Room or divide space with Room Separation Lines in the Main Model. |
| [RoomBaseAboveComputationHeight](e55251f0-3607-538f-1649-e225e24f8129.md "RoomBaseAboveComputationHeight Property") | [RoomBase]'s lower offset is above the Computation Height |
| [RoomBelowCompHeight](c255ac0d-0096-e7ec-3e8e-179e310bc219.md "RoomBelowCompHeight Property") | [Room] Volume is being calculated above the Upper Limit of this [Room]. Change the Upper Limit and Offset or change the height of volume calculations. |
| [RoomBoundaryMisalignment](44412913-995a-6a76-742d-9654e683013e.md "RoomBoundaryMisalignment Property") | [Room] bounding element might be misaligned. |
| [RoomHeightNegative](fda07eca-edab-6dfb-9621-70410454de07.md "RoomHeightNegative Property") | [Room] must have a height greater than 0. |
| [RoomLevelElevs](91b85bbf-4ae5-883f-3f51-f7720b1ca964.md "RoomLevelElevs Property") | A [Room]s Upper Limit must be above its Base Level. |
| [RoomNotEnclosed](4656a84f-b64c-a5ee-e1a1-58bc330d9319.md "RoomNotEnclosed Property") | [Room] is not in a properly enclosed region |
| [RoomNotEnclosedAreas](245e503c-8614-16d2-cbe5-6ae350d06c40.md "RoomNotEnclosedAreas Property") | [Room] is not in a properly enclosed region |
| [RoomNotEnclosedLoadAreas](9c991fd0-6c19-dcca-6bce-a5e9b180838d.md "RoomNotEnclosedLoadAreas Property") | [Room] is not in a properly enclosed region |
| [RoomNotEnclosedRooms](ecce1bf6-3ccd-9da9-70ad-e3abc566d723.md "RoomNotEnclosedRooms Property") | [Room] is not in a properly enclosed region |
| [RoomNotEnclosedSpaces](47cec0d1-b41d-5c79-8c64-be8a4b375647.md "RoomNotEnclosedSpaces Property") | [Room] is not in a properly enclosed region |
| [RoomsCreatedAutomatically](e9979888-9cdd-7aec-35c0-e2682a315f5d.md "RoomsCreatedAutomatically Property") | [Room] [Room] created automatically. |
| [RoomsFailed](acb05e43-e442-b9b6-d7dc-41d276ac9176.md "RoomsFailed Property") | [Room] computations only succeeded without considering the following elements. |
| [RoomsInSameRegion](b37ffa39-c5b3-c7d5-b510-13c718cefa09.md "RoomsInSameRegion Property") | Multiple [Room] are in the same enclosed region. The correct area and perimeter will be assigned to one [Room] and the others will display "Redundant [Room]." You should separate the regions, delete the extra [Room], or move them into different regions. |
| [RoomsInSameRegionAreas](1458218b-908a-8b69-cf09-fad368f2c30b.md "RoomsInSameRegionAreas Property") | Multiple [Room] are in the same enclosed region. The correct area and perimeter will be assigned to one [Room] and the others will display "Redundant [Room]." You should separate the regions, delete the extra [Room], or move them into different regions. |
| [RoomsInSameRegionLoadAreas](de7cd931-8db1-b191-566f-558113e4c7a2.md "RoomsInSameRegionLoadAreas Property") | Multiple [Room] are in the same enclosed region. The correct area and perimeter will be assigned to one [Room] and the others will display "Redundant [Room]." You should separate the regions, delete the extra [Room], or move them into different regions. |
| [RoomsInSameRegionRooms](174307f9-0c72-6fdc-1db1-8ee1f4cbc861.md "RoomsInSameRegionRooms Property") | Multiple [Room] are in the same enclosed region. The correct area and perimeter will be assigned to one [Room] and the others will display "Redundant [Room]." You should separate the regions, delete the extra [Room], or move them into different regions. |
| [RoomsInSameRegionSpaces](6e5bceec-5c87-f083-bd4d-12fa7ba78383.md "RoomsInSameRegionSpaces Property") | Multiple [Room] are in the same enclosed region. The correct area and perimeter will be assigned to one [Room] and the others will display "Redundant [Room]." You should separate the regions, delete the extra [Room], or move them into different regions. |
| [RoomsOverlapInHeight](866da556-7bec-09c1-c9b4-0db07c50113d.md "RoomsOverlapInHeight Property") | [Room] volumes overlap. Adjust the Upper Limit and Limit Offset properties of the [rooms]. |
| [RoomsReallyFailed](476ef27c-5eca-ba6c-f177-93ef66de2bf2.md "RoomsReallyFailed Property") | [Room] computations failed. Try to modify the following elements. |
| [RoomTagBadViewType](fccbe64c-8621-f8cc-6b63-b61581a2775a.md "RoomTagBadViewType Property") | [Room] Tags can only be placed in Floor Plan, Reflected Ceiling Plan and Section Views. |
| [RoomTagDeleted](c3dfb88b-e0ec-f184-f0b8-167f9a85f0e5.md "RoomTagDeleted Property") | A [Room] Tag was deleted, but the corresponding [Room] still exists. You can place another tag for the [Room] using the [Room] Tag tool or select the [Room] and delete it. |
| [RoomTagNotInRoom](3414edaf-ce4a-fc42-9c3f-baeec8a60459.md "RoomTagNotInRoom Property") | [Room] Tag is outside of its [Room]. Enable Leader or move [Room] Tag within its [Room]. |
| [RoomTagNotInRoomToArea](32a4092d-e263-97e7-130b-7ef052ff23d0.md "RoomTagNotInRoomToArea Property") | [Room] Tag is outside of its [Room]. Enable Leader or move [Room] Tag within its [Room]. |
| [RoomTagNotInRoomToRoom](b8b91f15-a046-7354-8abe-17c930153e50.md "RoomTagNotInRoomToRoom Property") | [Room] Tag is outside of its [Room]. Enable Leader or move [Room] Tag within its [Room]. |
| [RoomTagNotInRoomToSpace](43cff7ce-8e52-2512-7ba6-086b1a8854dd.md "RoomTagNotInRoomToSpace Property") | [Room] Tag is outside of its [Room]. Enable Leader or move [Room] Tag within its [Room]. |
| [RoomTagVolumeNotComputed](163fa54b-ebe5-5109-8f07-3c8f02da0e55.md "RoomTagVolumeNotComputed Property") | [Room] Tag is displaying volume that can't be computed. |
| [RoomTooShort](1d394b24-af0b-f2c9-eda9-6c317d5d9a18.md "RoomTooShort Property") | [Room] is very short. If this is not intended, change its Upper Limit and Offset. |
| [RoomUnplaceWarning](6de63393-1fd3-937a-de8b-bf486105cfe4.md "RoomUnplaceWarning Property") | A Room was deleted from all model views but still remains in this project. \n The room can be removed from any schedule or placed back in the model using the Room command. |
| [ShowRoomBoundingElements](a04bd2e5-a70f-3176-74aa-7c3f6c1e0dbc.md "ShowRoomBoundingElements Property") | [Room] Bounding elements are highlighted. |
| [SpaceUnplaceWarning](ccf50328-eb14-8474-e0cb-2142d96bab73.md "SpaceUnplaceWarning Property") | A Space was deleted from all model views but still remains in this project. \n The Space can be removed from any schedule or placed back in the model using the Space command. |

# See Also
[BuiltInFailures..::..RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.md "BuiltInFailures.RoomFailures Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 