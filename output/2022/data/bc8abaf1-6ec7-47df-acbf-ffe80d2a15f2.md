# CylindricalHelix Members (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
C#Visual BasicVisual C++
Include Protected MembersInclude Inherited Members
Revit 2022 API  
---  
CylindricalHelix Members  
[CylindricalHelix Class](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.md "CylindricalHelix Class") Methods Properties See Also  
---  
The [CylindricalHelix](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.md "CylindricalHelix Class") type exposes the following members.
# Methods
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [Clone](071f6ca9-f243-4655-924c-7beb881b100f.md "Clone Method") | Returns a copy of this curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [ComputeClosestPoints](04ab73d1-bc85-9b87-aace-4272a0c7c3e4.md "ComputeClosestPoints Method") | Find the closest points between two curves. Closest points mean closest pairs of points, each pair consisting of a point on this, say P1, and a point on other curve, say P2. P1 and P2 are closest locally. Each pairs of closest points will be represented by the corresponding parameter values with respect to the two curves and the 3d points. A closest pair is also known as a pair of critical points of the distance function between points of the two curves. If the input parameter returnAllCriticalPoints is set to false, then the function will return only pairs with minimum distance.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [ComputeDerivatives](93092a44-85f1-15be-a618-817c763f8994.md "ComputeDerivatives Method") | Returns the vectors describing the curve at the specified parameter.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [ComputeNormalizedParameter](d42c45a0-7525-aab6-2527-16148dd6dcc1.md "ComputeNormalizedParameter Method") | Computes the normalized curve parameter from the raw parameter. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [ComputeRawParameter](ac00deb9-9e8d-6bcb-60ac-b6f6a7520ea2.md "ComputeRawParameter Method") | Computes the raw parameter from the normalized parameter. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Create](851cb6a7-fcc3-a518-78ae-98c43c728b1b.md "Create Method") | Create a cylindrical helix. |
| [CreateOffset](450217f3-c0b5-42af-3a05-376ae383d28a.md "CreateOffset Method") | Creates a new curve that is an offset of the existing curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [CreateReversed](722a403d-a95c-557c-e92e-ad6757dc421c.md "CreateReversed Method") | Creates a new curve with the opposite orientation of the existing curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [CreateTransformed](4f014114-64f7-fff1-f24f-bfc6e0cad82a.md "CreateTransformed Method") | Crates a new instance of a curve as a transformation of this curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.md "Dispose Method") | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.md "APIObject Class").) |
| [Distance](95efa592-d444-acb8-6460-e2757b96e053.md "Distance Method") | Returns the shortest distance from the specified point to this curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Equals](26d6c913-b5b6-436f-dee9-19ceca7e53c6.md "Equals Method") | Determines whether the specified Object is equal to the current Object.  (Inherited from [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.md "GeometryObject Class").) |
| [Evaluate](1145f18e-3e01-60df-e438-e176c38c3ce9.md "Evaluate Method") | Evaluates and returns the point that matches a parameter along the curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [GetEndParameter](0f4b2c25-35f8-4e3c-c71a-0d41fb6935ce.md "GetEndParameter Method") | Returns the raw parameter value at the start or end of this curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [GetEndPoint](a02da994-2976-38c0-e16b-20292de9fe57.md "GetEndPoint Method") | Returns the 3D point at the start or end of this curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [GetEndPointReference](5619a3fd-38e1-fb56-7286-2e5f33a3b2b8.md "GetEndPointReference Method") | Returns a stable reference to the start point or the end point of the curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [GetHashCode](08e8412d-4002-22a5-858d-f55eba1bed34.md "GetHashCode Method") | Gets the integer value of the geometry object as hash code  (Inherited from [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.md "GeometryObject Class").) |
| GetType | Gets the Type of the current instance. (Inherited from Object.) |
| [Intersect(Curve)](90e86110-9bce-6e43-c18a-4d67380008bb.md "Intersect Method \(Curve\)") | Calculates the intersection of this curve with the specified curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Intersect(Curve, IntersectionResultArray%)](51961478-fb36-e00b-2d1b-7db27b0a09e6.md "Intersect Method \(Curve, IntersectionResultArray\)") | Calculates the intersection of this curve with the specified curve and returns the intersection results. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [IsInside(Double)](2782b130-915f-8467-22f1-629b9e0c1574.md "IsInside Method \(Double\)") | Indicates whether the specified parameter value is within this curve's bounds. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [IsInside(Double, Int32%)](64b9685d-b790-d2cb-f9f7-7184669a9ee0.md "IsInside Method \(Double, Int32\)") | Indicates whether the specified parameter value is within this curve's bounds and outputs the end index. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [MakeBound](f9bc51b4-50a3-de79-4d7e-401ab2dbebb2.md "MakeBound Method") | Changes the bounds of this curve to the specified values. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [MakeUnbound](31ef6a2e-0e39-a394-b6ee-4e4df56d8380.md "MakeUnbound Method") | Makes this curve unbound. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Project](b87fc3e4-ea25-2a75-5b5a-53065b099d2a.md "Project Method") | Projects the specified point on this curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [SetGraphicsStyleId](bd71365d-d2f2-2758-c220-a2a5c71cc6e4.md "SetGraphicsStyleId Method") | Sets the graphics style id for this curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Tessellate](f95f3199-3251-c708-c5a3-a0e9ef95ecfa.md "Tessellate Method") | Valid only if the curve is bound. Returns a polyline approximation to the curve.  (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| ToString | Returns a string that represents the current object. (Inherited from Object.) |

# Properties
| Name | Description |
| --- | --- |
| --- | --- | --- |
| [ApproximateLength](202c6c2c-23cf-aee3-fc9e-24b24a46e293.md "ApproximateLength Property") | The approximate length of the curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [BasePoint](23159307-9167-7a91-5d8f-87e8bac93571.md "BasePoint Property") | The base point of the axis of the cylindrical helix. |
| [GraphicsStyleId](4103f148-957e-3f44-9ccd-a5ed6702c689.md "GraphicsStyleId Property") | The ElementId of the GeometryObject's GraphicsStyle (Inherited from [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.md "GeometryObject Class").) |
| [Height](98caadf4-9780-2cf9-c089-e3501979250b.md "Height Property") | Height of the cylindrical helix. |
| [Id](abb781de-203f-4035-784b-713e65cca169.md "Id Property") | A unique integer identifying the GeometryObject in its associated non view-specific GeometryElement. (Inherited from [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.md "GeometryObject Class").) |
| [IsBound](cdf2a8e3-31fe-996a-1e94-e5eb77378279.md "IsBound Property") | Describes whether the parameter of the curve is restricted to a particular interval. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [IsClosed](a8297234-87a1-111c-fb24-ba1a9bd1d8a3.md "IsClosed Property") | Describes whether the curve is closed. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [IsCyclic](b3a443d0-db6d-332b-62b4-41b534987608.md "IsCyclic Property") | The boolean value that indicates whether this curve is cyclic. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [IsElementGeometry](be3ad18d-a9d3-25ed-6200-4f71d3cd4754.md "IsElementGeometry Property") | Indicates whether this geometry is obtained directly from an Element. (Inherited from [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.md "GeometryObject Class").) |
| [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.md "IsReadOnly Property") | Identifies if the object is read-only or modifiable. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.md "APIObject Class").) |
| [IsRightHanded](5fe9f7b7-332c-f33b-ecb2-d9ba1445562f.md "IsRightHanded Property") | True if the helix is right handed, false if the helix is left handed. |
| [Length](c6bca686-f136-ce45-8668-8d430267cd0d.md "Length Property") | The exact length of the curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Period](30b0f487-7728-9617-be52-616ca42da762.md "Period Property") | The period of this curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Pitch](9c11bf63-8235-b2bc-2f6b-7ce8af45f847.md "Pitch Property") | The pitch of the cylindrical helix. |
| [Radius](6a8ce591-5c0b-4712-f847-58a2996c7b7e.md "Radius Property") | The radius of the cylindrical helix. |
| [Reference](d5e10517-24fa-4627-43be-8981746d30c8.md "Reference Property") | Returns a stable reference to the curve. (Inherited from [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class").) |
| [Visibility](b504868c-1588-3488-8cdf-d8e45ef23fa0.md "Visibility Property") | The visibility. (Inherited from [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.md "GeometryObject Class").) |
| [XVector](cf831523-4e0d-1793-9163-06da91c0ac01.md "XVector Property") | The X direction vector. |
| [YVector](6d243b0d-672a-dfeb-3ce0-8f74fd8fc21a.md "YVector Property") | The Y direction vector. |
| [ZVector](79b811b5-a7cd-2e6b-bf62-a4942ea57ef9.md "ZVector Property") | The Z direction vector, which is same as the axis direction vector. |

# See Also
[CylindricalHelix Class](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.md "CylindricalHelix Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 