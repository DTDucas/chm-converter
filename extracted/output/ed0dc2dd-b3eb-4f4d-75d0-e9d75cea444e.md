

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarContainerItem..::..NumberOfBarPositions Property   
[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The number of potential bars in the set. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 

# Syntax

C#  
---  
      
    
    public int NumberOfBarPositions { get; set; }  
  
Visual Basic  
---  
      
    
    Public Property NumberOfBarPositions As Integer
    	Get
    	Set  
  
Visual C++  
---  
      
    
    public:
    property int NumberOfBarPositions {
    	int get ();
    	void set (int value);
    }  
  
# Remarks

The number of positions is equal to the number of actual bars (the Quantity), plus one or two more positions depending on IncludeFistBar and IncludeLastBar. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | When setting this property: the number of bar positions numberOfBarPositions is less than 1 or more than 1002. |
| [Autodesk.Revit.Exceptions..::..InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.md) | When setting this property: This rebar element represents a single bar (the layout rule is Single). |
  
# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)