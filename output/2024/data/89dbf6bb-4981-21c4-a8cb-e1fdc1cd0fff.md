# RevolvedSurface Members (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2024 API  
---  
RevolvedSurface Members  
[RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.md "RevolvedSurface Class") Methods Properties See Also  
---  
The [RevolvedSurface](ce0b47e0-2b24-61f5-1434-87fe3ff70390.md "RevolvedSurface Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Create(Frame, Curve)](2d14496c-47da-ef50-2a99-7386041361eb.md "Create Method \(Frame, Curve\)") | Creates a Surface object coincident with the surface of revolution defined by a coordinate frame and a profile curve. |
| [Create(XYZ, XYZ, Curve)](98484dd5-746c-02e1-d8d8-5ad18e250810.md "Create Method \(XYZ, XYZ, Curve\)") | Creates a Surface object coincident with the surface of revolution defined by an axis and a profile curve. |
| [Create(Frame, Curve, Double, Double)](f3e8c800-d92d-d09a-17ba-212d7ebf3b59.md "Create Method \(Frame, Curve, Double, Double\)") | Creates a Surface object coincident with the surface of revolution defined by a coordinate frame, a profile curve, and start and end angles of revolution. |
| [Create(XYZ, XYZ, Curve, Double, Double)](2fdabf9d-39d6-5739-9d28-6ceca0ecf2f5.md "Create Method \(XYZ, XYZ, Curve, Double, Double\)") | Creates a Surface object coincident with the surface of revolution defined by an axis, a profile curve, and start and end angles of revolution. |
| [Dispose](c9ee1344-bc19-d833-52e7-dcc4931fe085.md "Dispose Method") | (Inherited from [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class").) |
| Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
| [GetBoundingBoxUV](5084214f-219f-780f-fe03-f16b62b2660d.md "GetBoundingBoxUV Method") | Gets the UV bounding box of the surface.  (Inherited from [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class").) |
| GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
| [GetProfileCurve](fb30e6fc-5fbf-c96d-b66e-b22124fd6394.md "GetProfileCurve Method") | Returns a copy of the profile curve expressed in the surface's coordinate system. |
| [GetProfileCurveInWorldCoordinates](fd977456-eb4a-caf2-1d09-dedc8e1a4317.md "GetProfileCurveInWorldCoordinates Method") | Returns a copy of the profile curve expressed in the world coordinate system. |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [IsValidProfileCurve(Frame, Curve)](b0b32fa1-32f7-22bd-a4ae-f62aa777b4c8.md "IsValidProfileCurve Method \(Frame, Curve\)") | Checks if the input profile curve is valid to create a surface of revolution in the given frame of reference. |
| [IsValidProfileCurve(XYZ, XYZ, Curve)](3391c6e4-35e9-23de-7875-374fe5beeb0d.md "IsValidProfileCurve Method \(XYZ, XYZ, Curve\)") | Checks if the input profile curve is valid to create a surface of revolution around the given axis. |
| [Project](802cc09b-d0a4-dfc5-8ca1-e8c5e8cd4ced.md "Project Method") | Project a 3D point orthogonally onto a surface (to find the nearest point). Throws InvalidOperationException if the projection fails.  (Inherited from [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class").) |
| [ProjectWithGuessPoint](db8cc42a-9f34-611a-d9c5-852f3935887f.md "ProjectWithGuessPoint Method") | Project a 3D point orthogonally onto a surface (to find the nearest point). This method is meant to be used when a good approximate solution for the projection is available. Throws InvalidOperationException if the projection fails.  (Inherited from [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class").) |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Axis](e8aafaed-78d3-3845-8275-ea8ce0031275.md "Axis Property") | Axis of the revolved surface. This is the Z axis of the local coordinate system associated with this revolved surface. |
| [IsValidObject](6429595a-a6e1-2501-1e60-9c53814a9108.md "IsValidObject Property") | Specifies whether the .NET object represents a valid Revit entity.  (Inherited from [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class").) |
| [OrientationMatchesParametricOrientation](451b549f-2bc4-4f37-9f32-981fe18868a8.md "OrientationMatchesParametricOrientation Property") | Indicates whether this Surface's orientation is the same as or opposite to its parametric orientation.  (Inherited from [Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class").) |
| [Origin](14bcd3af-0f67-8d52-e16d-74b7baf3e513.md "Origin Property") | Center of the circle that defines the base of the revolved surface. This is the origin of the local coordinate system associated with this revolved surface. |
| [XDir](ba8f06da-2b43-a964-292e-79b37a7dd97e.md "XDir Property") | X axis of the local coordinate system associated with this revolved surface. |
| [YDir](4344a317-7751-0c0d-7feb-285b50f91db7.md "YDir Property") | X axis of the local coordinate system associated with this revolved surface. |

# See Also
[RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.md "RevolvedSurface Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 