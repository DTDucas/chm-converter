

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PathReinforcement..::..AlternatingBarOrientation Property   
[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Orientation of alternating bars of Path Reinforcement. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 

# Syntax

C#  
---  
      
    
    public [ReinforcementBarOrientation](b67e1240-752a-316d-0e41-2000d19aa088.md) AlternatingBarOrientation { get; set; }  
  
Visual Basic  
---  
      
    
    Public Property AlternatingBarOrientation As [ReinforcementBarOrientation](b67e1240-752a-316d-0e41-2000d19aa088.md)
    	Get
    	Set  
  
Visual C++  
---  
      
    
    public:
    property [ReinforcementBarOrientation](b67e1240-752a-316d-0e41-2000d19aa088.md) AlternatingBarOrientation {
    	[ReinforcementBarOrientation](b67e1240-752a-316d-0e41-2000d19aa088.md) get ();
    	void set ([ReinforcementBarOrientation](b67e1240-752a-316d-0e41-2000d19aa088.md) value);
    }  
  
# Remarks

The orientation corresponds to the bars' rotation in the Path Reinforcement element. It indicates the postion of the major segment of the alternating Rebar Shape relative to the edges of a rectangular region which bounds the Path Reinforcement, where the top/exterior and bottom/interior come from the cover boundaries of the host, the near side edge is defined by the Path Reinforcement sketch line, and the far side edge is derived from bar length (defaulting to 5'). 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | When setting this property: This orientation is not allowed for alternating bars. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
  
# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)