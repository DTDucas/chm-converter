

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
BuiltInFailures..::..AutoRouteFailures Members  
[BuiltInFailures..::..AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.md) Properties See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Provides a container of all Revit built-in FailureDefinitionId instances.

The [BuiltInFailures..::..AutoRouteFailures](7cf86d0a-85aa-b09e-5378-36e02948233b.md) type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [AttemptToConnectNonSlopingElementToSlopedPipeError](ddc05c68-6eaf-2e63-9000-e346562189b2.md) | You have specified that sloped pipe be drawn, but are trying to connect to an element that doesn't support sloping connections. |
|  | [AttemptToConnectNonSlopingElementToSlopedPipeWarning](213eaf22-602c-6f16-2aa2-a8fdb9aec60b.md) | You have specified that sloped pipe be drawn, but are trying to connect to an element that doesn't support sloping connections. |
|  | [DesignOptionConflictError](8b12e569-c0d5-fc14-3539-41833c360c85.md) | The solution is failing to do the elements are not in the same Design Option. |
|  | [DesignOptionConflictWarning](22465692-04e2-e5de-3d57-30823ea817bc.md) | The solution is failing to do the elements are not in the same Design Option. |
|  | [DistributionTypeInvalid](b1690d9e-cbfd-974c-cc81-13311238bec6.md) | Selected distribution system type is invalid! |
|  | [ElementHasFlowCalculation](18e44b11-889c-6566-c029-f2281f76e8f5.md) | This element has an open connection. This may not be an error, but for flow calculations to work correctly all connections should be sealed with an end cap. |
|  | [ElementHasOpenConnection](a91f20a3-f54e-4f8b-9bc5-b3a54db81f32.md) | This element has an open connection. This may not be an error, but all open connections should be sealed with an end cap. |
|  | [FailedDowngradeCrossToElbow](fb91d76a-10a0-bc20-1292-5d6919205b28.md) | Failed to downgrade tee type to elbow type. |
|  | [FailedDowngradeCrossToTee](400cfa09-d1b6-85dd-e0c7-f75d38ae0bc6.md) | Failed to downgrade cross type to tee type. |
|  | [FailedDowngradeTeeToCross](33f867b9-f879-caab-a24a-5aee6c480b25.md) | Failed to upgrade tee type to cross type. |
|  | [FailToDoCompatiblePhaseError](b60beeb2-d7a3-2427-4a48-da9c0ef5fecd.md) | The solution is failing to do the elements Phases are compatible. |
|  | [FailToDoCompatiblePhaseWarning](6e4896ea-147f-e79e-79b7-f17f4039452f.md) | The solution is failing to do the elements Phases are compatible. |
|  | [FailToIntersectParallelSegmentsError](92647d59-b1c4-6e88-6df1-b81d2955f096.md) | The solution is failing to do segments which are parallel and should intersect. |
|  | [FailToIntersectParallelSegmentsWarning](92295dca-9fee-cf90-e41f-3c5d1bdb8ba0.md) | The solution is failing to do segments which are parallel and should intersect. |
|  | [FittingParamsCauseGeometryToFailError](fe2f7a27-62ee-0006-0c8d-1b7491a79a29.md) | The one of parameters for the fitting is causing the geometry to fail. |
|  | [FittingParamsCauseGeometryToFailWarning](de321733-7302-0954-f9b2-379e1bbe21a2.md) | The one of parameters for the fitting is causing the geometry to fail. |
|  | [HighlightedElementDisconnected](de010e28-e38e-510d-ede2-f8767456c2e8.md) | The highlighted element has been disconnected. |
|  | [InappropriateSlopeForPipe](26a0e05e-7c28-dc2d-9eb6-8ced935b6a28.md) | The slope that you specified could not be applied to this pipe. Please check the items that it is connected to and make sure that they aren't constraining the slope of them. |
|  | [MismatchedSystemClassificationHasSystemWarning](c05a100e-7f4b-bcb8-72bd-58d71e5fbd5e.md) | The selected fixture is part of a system with different classification. System calculations (e.g. flow analysis) are not possible between systems with different classifications. |
|  | [MismatchedSystemClassificationNoSystemWarning](f267fdf2-1828-53db-1bee-f615f6bf65e0.md) | The selected fixture is assigned to a system with different classification. |
|  | [MismatchedSystemTypeWarning](5f8f992d-2534-dbfb-453f-acf55d7470b5.md) | The selected fixture is part of a different system. You may want to edit the system type and merge two systems. |
|  | [NoAutoRouteSolutionFoundError](2bfa4d09-a91e-7e7b-599f-d005284ee69b.md) | No auto-route solution was found. |
|  | [NoAutoRouteSolutionFoundWarning](fd41e15d-e934-e769-bc40-e468247d13d4.md) | No auto-route solution was found. |
|  | [NoFittingInProjectError](5b743cdd-3049-e09f-aaf4-3a1d6f5c1745.md) | The routing solution failed because there is no default fitting type specified or the fitting cannot be found in the project. Ensure the fitting is loaded in the project and try again. |
|  | [NoFittingInProjectWarning](49310dcf-7b89-2462-75b6-6b150f84adb6.md) | The routing solution failed because there is no default fitting type specified or the fitting cannot be found in the project. Ensure the fitting is loaded in the project and try again. |
|  | [NoFittingInRoutingError](46f74c41-257c-9ef1-86f7-474320ad0eee.md) | The fitting that is converted to was not defined. Please assign one in the routing preference. |
|  | [NoFittingLoadedInProjectError](335e5734-93f4-f96b-fdb8-5cdbb46a0136.md) | The fitting that is converted to was not defined. Please load one fitting family and assign it in the routing preference. |
|  | [NoSolutionInView](dc12a791-f27a-7ba0-5f1e-d475c1d5e2d4.md) | There is no solution for this view. All the elements have been filtered for this view, select another view, and select solutions. |
|  | [NotAllPartsWereConvertedCannotAddPlaceholderWarning](3cca92eb-843c-45a3-d4d6-6b6880b0ff61.md) | Not all parts were converted. Placeholders could not be added to fill the gap (the gap was too small). Check the fabrication service definition for the system. |
|  | [NotAllPartsWereConvertedPlaceholdersWereAddedWarning](f33d0b25-dbfb-4974-0d01-aa3b7ba5ee5d.md) | Not all parts were converted. Placeholders were added to fill the gaps. Check the fabrication service definition for the system. |
|  | [NotEnoughRoomForFittingsError](31927be0-218f-31fd-c52b-7af3c38afca3.md) | There was not enough room to place the required fittings. Consider increasing the length of the segments, or moving them farther apart to generate a solution. |
|  | [NotEnoughRoomForFittingsWarning](4307b04a-e71c-dee4-5350-10f7ae1a377d.md) | There was not enough room to place the required fittings. Consider increasing the length of the segments, or moving them farther apart to generate a solution. |
|  | [NoValidSolutionAtSelectedPoint](7f499cff-bf0c-712d-b80c-5d90d409a62d.md) | No valid auto-route solution at selected point. |
|  | [OverrideFabricationPartFailed](af28b65a-fb46-4804-ac09-a04e6c7f1aab.md) | The fabrication part cannot be overridden. The button code you specified does not match the fabrication service. Please specify a different button code or check the fabrication service and try again. |
|  | [SegmentDrawnFromWrongSideError](eda29af1-7a31-9acd-288c-fbaddc8755bc.md) | The segment is being drawn from the wrong side to connect to the location you indicated. |
|  | [SegmentDrawnFromWrongSideWarning](26603f29-5650-1dd7-be31-7596af2ad296.md) | The segment is being drawn from the wrong side to connect to the location you indicated. |
|  | [SegmentsAngleTooGreatError](16a03e7a-6b13-b2d6-7095-d56147ac6711.md) | The resulting angle between the segments is too great. |
|  | [SegmentsAngleTooGreatWarning](63915a37-5c94-724f-1b0e-7ef5f4f95213.md) | The resulting angle between the segments is too great. |
|  | [SolutionIsOppositeToConnectionError](ac5bad91-1c17-543e-4819-4c9eae57ab3a.md) | The solution is in the opposite direction of the connection direction. |
|  | [SolutionIsOppositeToConnectionWarning](431a80b9-3c62-b1b0-51bb-38aed8eeca0f.md) | The solution is in the opposite direction of the connection direction. |
|  | [SpecifiedAnglesNotCompatibleWithLayoutError](f8db6aee-7a19-d798-8aa9-871c8fdfd234.md) | The specified angles are not compatible with current layout. |
|  | [SpecifiedAnglesNotCompatibleWithLayoutWarning](ee9c32a9-5f9c-b976-128e-32381e1096f7.md) | The specified angles are not compatible with current layout. |
|  | [UnableToMakeConnectionInDirection](3b3a2c2f-32ff-92ee-68d8-41f98e35e0de.md) | The application is unable to make a connection in that direction. If the connectors are pointing up, make sure that the elevations of the segments (ducts and pipes) are above them. If the connectors are pointing down, make sure that the elevations of the segments (ducts and pipes) are below them. |
|  | [UtilizationCoefficientOutOfRange](a9819040-de6b-a782-cc1c-4868a2d932aa.md) | The value for Coefficient of Utilization must be between 0 and 1. |
|  | [ZeroLengthSegmentError](1d58b4ff-59e8-d628-7cca-171e1201a274.md) | The solution is failing to do segments which are zero length. |
|  | [ZeroLengthSegmentWarning](3d6f0d5d-fa47-adac-3c9c-fa4f1c4691d1.md) | The solution is failing to do segments which are zero length. |
  
# See Also

[BuiltInFailures..::..AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)