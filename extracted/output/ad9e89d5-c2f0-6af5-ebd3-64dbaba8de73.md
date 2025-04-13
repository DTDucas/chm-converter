

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
BuiltInFailures..::..DividedSurfaceFailures Properties  
[BuiltInFailures..::..DividedSurfaceFailures Class](6c670503-f89e-7ee3-1883-af2a9576f390.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [BuiltInFailures..::..DividedSurfaceFailures](6c670503-f89e-7ee3-1883-af2a9576f390.md) type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [DividedSurfaceCannotApplyDivideSettings](583f6984-6695-4b04-7c40-c15abb91efcb.md) | Default Divide settings were not applied to Divided Surface. Please adjust grid spacing values manually. |
|  | [DividedSurfaceCoincidingSplittingWorkplanes](f7031339-4f12-c620-28f5-b1d6b76ff56f.md) | Coinciding splitting workplanes are encountered |
|  | [DividedSurfaceCurveChainBelongsToMultipleBeltIntervals](7cab4452-00e0-3fc1-f406-15af853a059b.md) | A chain formed by these curve elements defines a splitter belonging to multiple belt intervals and will be ignored |
|  | [DividedSurfaceCurveChainBothUandV](e8f7ed48-e8a2-5e8e-f037-64deec6eca32.md) | A chain formed by these curve elements is trying to be both U- and V- splitter |
|  | [DividedSurfaceCurveChainDoesNotEngageUorV](28ed6d25-bbae-9632-1563-403406769720.md) | A chain formed by these curve elements does engage any gridlines on the face to be divided and will be ignored |
|  | [DividedSurfaceCurveChainGeneralProblem](ba4d6919-3156-fe06-fbdb-1b044e4202f1.md) | The chain formed by these curve elements cannot be processed and will be ignored. |
|  | [DividedSurfaceCurveChainIntersection](6992f766-4683-589e-7777-417949bf3d1a.md) | A chain formed by these curve elements intersects other chain with the same grid orientation. Both chains will be ignored |
|  | [DividedSurfaceCurveChainIsTooClosedToGridlines](08b2e534-f9ac-c1c2-a19d-19ca12a793d4.md) | A chain formed by these curve elements defines a splitter which lies too close to gridlines and will be ignored |
|  | [DividedSurfaceCurveChainMultipleSeqIntersWithDivLine](7fb3c3a4-2a66-a0be-db85-5f1472ecafde.md) | The chain formed by these curve elements has multiple sequential intersections with a gridline and so the chain will be ignored |
|  | [DividedSurfaceCurveChainNonSeqIntersWithDivLines](8c823a6a-d617-6f4b-3369-24d3fb06850f.md) | The chain formed by these curve elements has multiple non-sequential intersections with the same gridline and will be ignored |
|  | [DividedSurfaceCurveChainUnsortableBucket](a2243b2f-5eed-78ff-fe2c-57f72ea2b33b.md) | The chains formed by these curve elements cannot be ordered consistently in the their grid interval and will be ignored |
|  | [DividedSurfaceCurveFromChainMultipleIntersWithDivLine](e3b65deb-5e55-422b-21a7-e5d6c3829803.md) | A curve from the chain formed by these curve elements either intersects a gridline more than once or coincides with it and so the chain will be ignored |
|  | [DividedSurfaceCurveLoopChainIntersectedByExtensions](c3fac636-f26e-2ce3-c21c-b2bf667020ac.md) | Curve elements forming a chain which is intersected by extensions of the chain ends cannot be used as splitters and are ignored. |
|  | [DividedSurfaceCuttingSurfaceDoesNotCutMeshFace](66203ee7-0f4d-a05f-553f-88e27feaf87d.md) | The surface-based splitter does not intersect a face to be divided and will be ignored |
|  | [DividedSurfaceCuttingSurfaceGeneralProblem](c548133b-7ba8-a7bf-701a-002382af8487.md) | Cannot process a surface-based splitter |
|  | [DividedSurfaceCuttingSurfaceMakesMultipleCuts](eb6f1f59-8be9-41f7-9200-7b7b8540b32b.md) | The surface-based splitter intersects a face to be divided in multiple places and this case is not currently supported |
|  | [DividedSurfaceDidNotRegenerateProperly](59839404-b061-9c51-7144-e21b4c2514ce.md) | Divided Surface gridlines could not be generated. |
|  | [DividedSurfaceDiscardedSplittersWarning](f0c492b3-a59f-e768-a3eb-23fd0bd55a40.md) | Not all intersecting references (levels, reference planes or lines) could be used to intersect the surface |
|  | [DividedSurfaceIgnoresSplitters](460af8bc-51c2-2332-74ee-b311ed146056.md) | Revit cannot create a rectangular grid by intersecting the current selection of elements (levels, reference planes, or curves drawn on reference planes) with the surface. Make sure that curves do not form closed loops. It is helpful if curves start and end outside the surface, rather than inside it. |
|  | [DividedSurfaceInvalidSpacing](e1c3f547-1802-f5fd-17cc-f43562a92c60.md) | Constraints not satisfied, cannot generate gridlines. |
|  | [DividedSurfaceLoopsOfSplittingCurves](072e1e86-5ddf-b23c-9f18-9ead2ed9899d.md) | Curve elements forming a closed loop currently cannot be used as splitters and are ignored. |
|  | [DividedSurfaceMultipleIntersBetweenOppositeVirtualGrids](aac55848-0ee4-d9fd-7fa0-cd2100b56eb0.md) | There are multiple intersections between splitting chain of virtual splitters defined by these elements and so one of the virtual splitters will be ignored |
|  | [DividedSurfaceSelfIntersectingCurveLoopChain](113138fc-90f4-227d-e39f-62e48af19297.md) | Curve elements forming a self-intersecting chain cannot be used as splitters and are ignored. |
|  | [DividedSurfaceSingleCurveLoopsAsSplitters](18e4b294-33fe-6fde-106b-bc9953b5f951.md) | Curve elements forming a single curve loop cannot be used as splitters and are ignored. |
|  | [DividedSurfaceSingleCurveMultipleIntersBetweenOppositeVirtualGrids](c378ea43-dc1d-a2e6-cc09-927d42b6d8cb.md) | There are curves in splitting chain of virtual splitters defined by these elements which intersect each other multiple times and so one of the virtual splitters will be ignored |
|  | [DividedSurfaceSplitManagerProblem1dNonWPCurve](fa1113f5-8ae4-d627-5058-4a7ff6582594.md) | Divided Surface cannot be split by a one dimensional curve without workplane |
|  | [DividedSurfaceSplitManagerProblemClosedArcOrEllipse](903174dc-a936-f665-980c-b8bcca410ae5.md) | Divided Surface cannot be split by a closed arc or ellipse. |
|  | [DividedSurfaceSplitRefInvisible](8a2eab49-c89b-e685-5846-2f4b860b1c55.md) | Some of the splitting references of this Divided Surface are invisible in the current view. |
|  | [DividedSurfaceSplittingCurveChainsBetweenMultipleNeighbors](3fc99836-c4d1-1ce1-b2dd-846dab8d8bfc.md) | Curve elements which form chains connecting points shared by more than two curve elements are ignored. |
|  | [DividedSurfaceSplittingCurvesWithMultipleNeighbors](a92c8d26-83f3-3bdd-943f-6cf63f30e41a.md) | A point cannot coincide with end points of more than two curve elements. All curve elements adjacent to such a point are ignored. |
|  | [DividedSurfaceZeroLengthSplittingCurve](626e7993-fe15-b8ba-26c9-e1b464619fa6.md) | Curve element with zero length cannot be used as a splitter and ignored. |
|  | [MeshTopologicalSortFailed](a5b260de-5dfb-a79e-8d81-41fa977ab014.md) | Splitters and grids do not define a consistent rectangular mesh on the face. |
  
# See Also

[BuiltInFailures..::..DividedSurfaceFailures Class](6c670503-f89e-7ee3-1883-af2a9576f390.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)