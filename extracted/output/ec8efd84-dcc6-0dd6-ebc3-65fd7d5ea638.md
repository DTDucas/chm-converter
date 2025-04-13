

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
StructuralSectionLAngle Constructor   
[StructuralSectionLAngle Class](977c3aa9-0676-c93b-1546-c0db2d96c564.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new instance of Structural Section L Angle shape with the associated set of parameters, used to attach to structural element. 

**Namespace:** [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    public StructuralSectionLAngle(
    	double width,
    	double height,
    	double flangeThickness,
    	double webThickness,
    	double webFillet,
    	double flangeFillet,
    	double centroidHorizontal,
    	double centroidVertical,
    	double principalAxesAngle,
    	double sectionArea,
    	double perimeter,
    	double nominalWeight,
    	double momentOfInertiaStrongAxis,
    	double momentOfInertiaWeakAxis,
    	double elasticModulusStrongAxis,
    	double elasticModulusWeakAxis,
    	double plasticModulusStrongAxis,
    	double plasticModulusWeakAxis,
    	double torsionalMomentOfInertia,
    	double torsionalModulus,
    	double warpingConstant,
    	double shearAreaStrongAxis,
    	double shearAreaWeakAxis,
    	double boltSpacing1LongerFlange,
    	double boltSpacing2LongerFlange,
    	double boltSpacingShorterFlange,
    	double boltDiameterLongerFlange,
    	double boltDiameterShorterFlange,
    	double topWebFillet
    )  
  
Visual Basic  
---  
      
    
    Public Sub New ( _
    	width As Double, _
    	height As Double, _
    	flangeThickness As Double, _
    	webThickness As Double, _
    	webFillet As Double, _
    	flangeFillet As Double, _
    	centroidHorizontal As Double, _
    	centroidVertical As Double, _
    	principalAxesAngle As Double, _
    	sectionArea As Double, _
    	perimeter As Double, _
    	nominalWeight As Double, _
    	momentOfInertiaStrongAxis As Double, _
    	momentOfInertiaWeakAxis As Double, _
    	elasticModulusStrongAxis As Double, _
    	elasticModulusWeakAxis As Double, _
    	plasticModulusStrongAxis As Double, _
    	plasticModulusWeakAxis As Double, _
    	torsionalMomentOfInertia As Double, _
    	torsionalModulus As Double, _
    	warpingConstant As Double, _
    	shearAreaStrongAxis As Double, _
    	shearAreaWeakAxis As Double, _
    	boltSpacing1LongerFlange As Double, _
    	boltSpacing2LongerFlange As Double, _
    	boltSpacingShorterFlange As Double, _
    	boltDiameterLongerFlange As Double, _
    	boltDiameterShorterFlange As Double, _
    	topWebFillet As Double _
    )  
  
Visual C++  
---  
      
    
    public:
    StructuralSectionLAngle(
    	double width, 
    	double height, 
    	double flangeThickness, 
    	double webThickness, 
    	double webFillet, 
    	double flangeFillet, 
    	double centroidHorizontal, 
    	double centroidVertical, 
    	double principalAxesAngle, 
    	double sectionArea, 
    	double perimeter, 
    	double nominalWeight, 
    	double momentOfInertiaStrongAxis, 
    	double momentOfInertiaWeakAxis, 
    	double elasticModulusStrongAxis, 
    	double elasticModulusWeakAxis, 
    	double plasticModulusStrongAxis, 
    	double plasticModulusWeakAxis, 
    	double torsionalMomentOfInertia, 
    	double torsionalModulus, 
    	double warpingConstant, 
    	double shearAreaStrongAxis, 
    	double shearAreaWeakAxis, 
    	double boltSpacing1LongerFlange, 
    	double boltSpacing2LongerFlange, 
    	double boltSpacingShorterFlange, 
    	double boltDiameterLongerFlange, 
    	double boltDiameterShorterFlange, 
    	double topWebFillet
    )  
  
#### Parameters

width
    Type: System..::..Double Section width. 

height
    Type: System..::..Double Section height, depth. 

flangeThickness
    Type: System..::..Double Flange Thickness. 

webThickness
    Type: System..::..Double Web Thickness. 

webFillet
    Type: System..::..Double Web Fillet - fillet radius between web and flange. 

flangeFillet
    Type: System..::..Double Flange Fillet - fillet radius at the flange end. 

centroidHorizontal
    Type: System..::..Double Distance from centroid to the left extremites along horizontal axis. 

centroidVertical
    Type: System..::..Double Distance from centroid to the upper extremites along vertical axis. 

principalAxesAngle
    Type: System..::..Double Rotation angle between the principal axes and cross section reference planes. 

sectionArea
    Type: System..::..Double Cross section area. 

perimeter
    Type: System..::..Double Painting surface of the unit length. 

nominalWeight
    Type: System..::..Double Unit weight (not mass) per unit length, for self-weight calculation or quantity survey. 

momentOfInertiaStrongAxis
    Type: System..::..Double Moment of Inertia about main strong axis (I). 

momentOfInertiaWeakAxis
    Type: System..::..Double Moment of Inertia about main weak axis (I). 

elasticModulusStrongAxis
    Type: System..::..Double Elastic section modulus about main strong axis for calculation of bending stresses. 

elasticModulusWeakAxis
    Type: System..::..Double Elastic section modulus about main weak axis for calculation of bending stresses. 

plasticModulusStrongAxis
    Type: System..::..Double Plastic section modulus in bending about main strong axis (Z, Wpl) 

plasticModulusWeakAxis
    Type: System..::..Double Plastic section modulus in bending about main weak axis. 

torsionalMomentOfInertia
    Type: System..::..Double Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation 

torsionalModulus
    Type: System..::..Double Section modulus for calculations of torsion stresses (Ct) 

warpingConstant
    Type: System..::..Double Warping constant (Cw, Iomega, H) 

shearAreaStrongAxis
    Type: System..::..Double Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq). 

shearAreaWeakAxis
    Type: System..::..Double Shear area (reduced extreme shear stress coefficient) in the direction of weak axis (Wq). 

boltSpacing1LongerFlange
    Type: System..::..Double Standard bolt spacing first row in the longer flange, in. (mm) 

boltSpacing2LongerFlange
    Type: System..::..Double Standard bolt spacing second row in the longer flange, in. (mm) 

boltSpacingShorterFlange
    Type: System..::..Double Standard bolt spacing in the shorter flangI-split Parallel Flangee, in. (mm) 

boltDiameterLongerFlange
    Type: System..::..Double Maximum bolt hole diameter in the longer flange, in. (mm) 

boltDiameterShorterFlange
    Type: System..::..Double Maximum bolt hole diameter in the shorter flange, in. (mm) 

topWebFillet
    Type: System..::..Double Top Web Fillet - fillet radius at the top of web. 

# See Also

[StructuralSectionLAngle Class](977c3aa9-0676-c93b-1546-c0db2d96c564.md)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)