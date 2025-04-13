

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
NurbsSurfaceData Members  
[NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.md) Constructors Methods Properties See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [NurbsSurfaceData](7d65dbde-8aac-7d7d-e811-a6c91a541de4.md) type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
|  | [NurbsSurfaceData](6fdc9f8a-a443-a69f-2d9b-82cad9bf7544.md) | Copy constructor. |
  
# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [Create](94b4c433-5458-d1ab-d5c9-f526f288d1ff.md) | Construct NurbsSurfaceData based on NURBS surface data, where the weights are supplied. The NURBS surface will be (piecewise) polynomial if all the weights are equal, rational if not. Note: A rational polynomial is a quotient of two polynomials; this includes a polynomial, which can be thought of as a quotient with denominator equal to 1. |
|  | [Dispose](27a918fc-a321-7712-4594-9dd7eb2d2140.md) | Releases all resources used by the [NurbsSurfaceData](7d65dbde-8aac-7d7d-e811-a6c91a541de4.md) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | [GetControlPoints](409fe43e-03a5-b9d6-5bf4-4f6427e3606e.md) | Get the list of control points. |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | [GetKnotsU](e280fd98-bad6-3fb3-547f-a829ab23a9de.md) | Get the list of knots in the u-direction. |
|  | [GetKnotsV](1b0fea7f-4fd0-bee4-cc1b-773b13b2e36b.md) | Get the list of knots in the v-direction. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [GetWeights](a1eec836-1db9-00ef-98eb-923c6a77a952.md) | Get the list of weights. |
|  | [IsValid](6ca835bb-02f9-fe37-01ef-618310cef5ab.md) | Check if the object contains a valid NurbsSurfaceData. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [DegreeU](fc2de49b-75ef-b407-cecf-3dd0199b775a.md) | The degree of the spline in the u-direction. |
|  | [DegreeV](7bc890a0-c3d3-8e7f-5d9d-148a69de4813.md) | The degree of the spline in the v-direction. |
|  | [IsRational](da17256f-3c20-22c0-1619-5fe2d847752a.md) | Tells if the spline is rational or not. If it is true (rational), then the NURBS is a piecewise rational polynomial function. If it is false (non-rational), then the NURBS is a piecewise polynomial function. |
|  | [IsValidObject](b9517067-344b-5d1b-8c5d-664b7e7115e1.md) | Specifies whether the .NET object represents a valid Revit entity. |
|  | [ReverseOrientation](57ca8156-bae7-58fc-89a4-88f08aa1f756.md) | If true, the surface's orientation is opposite to the canonical parametric orientation, otherwise it is the same. The canonical parametric orientation is a counter-clockwise sense of rotation in the uv-parameter plane. Extrinsically, the oriented normal vector for the canonical parametric orientation points in the direction of the cross product dS/du x dS/dv, which S(u, v) is the parameterized surface. |
  
# See Also

[NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)