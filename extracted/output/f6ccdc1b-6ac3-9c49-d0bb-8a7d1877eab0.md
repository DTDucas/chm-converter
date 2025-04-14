# PostableCommand Enumeration

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PostableCommand Enumeration  
See Also  
---  
Enumerates all of the built-in commands which can be posted by an API application. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public enum PostableCommand
```
  
Visual Basic  
---  
```text
Public Enumeration PostableCommand
```
  
Visual C++  
---  
```text
public enum class PostableCommand
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| RoofByFace | Creates a roof using a non-vertical face of a mass. |
| Soffit | Creates a roof soffit in the building model. |
| LoadAsGroupIntoOpenProjects | Loads the current project as a group into another open project or family. |
| LoadIntoProject | Loads the rebar shape into open projects or family files. |
| RepeatComponent | Repeats the selected applied component along a divide path or surface. |
| ConnectionSettings | Opens the Structural Connections Settings dialog in which you can load and unload add-in connections into Revit. If no add-ins are present, no connections are available in the Connections tab. |
| StructuralConnection | Adds a structural connection to structural elements. |
| ShowWarningsInViews | Select to show structural connection warning marks in your project views. Deselect to hide warning marks. |
| ViewList | Creates a schedule of the views in the project. |
| LinearDimensionTypes | Defines attributes for linear (horizontal and vertical) dimensions. |
| AngularDimensionTypes | Defines attributes for angular dimensions. |
| SplitElement | Cuts an element (such as a wall or line) at a selected point, or removes a segment between 2 points. |
| SpotElevation | Displays the elevation of a selected point. |
| SpotCoordinate | Displays the North/South and East/West coordinates of points in a project. |
| AlignmentStation | Add an individual alignment station annotation. |
| AlignmentStationSet | Add a series of alignment station annotations. |
| RoofByFootprint | Creates a roof using the building footprint to define its boundaries. |
| RoofByExtrusion | Creates a roof by extruding a profile that you sketch. |
| RadialDimensionTypes | Defines attributes for radial dimensions. |
| ReloadLatest | Loads updates from the central model to your local copy of the project. |
| Render | Creates a photorealistic image of a building model. |
| ShowHistory | Displays a list of all the times a workshared file (the central model or a local copy of the central model) was saved and who saved it. |
| SplitSurface | Splits a toposurface into 2 distinct surfaces, so that each can be edited independently. |
| DrawOnFace | Draws lines on existing surfaces. |
| DrawOnWorkPlane | Draws lines on the active work plane. |
| GrayInactiveWorksets | Displays elements in inactive worksets as gray to visually distinguish them from elements in active worksets. |
| ImportGBXML | Imports analysis data from a gbXML file. |
| ExportReportsRoomOrAreaReport | Saves a schedule or Room/Area report. |
| SheetIssuesOrRevisions | Specifies revision information for the project. |
| RevisionSchedule | Adds a revision schedule to a custom title block. |
| CalloutTags | Specifies the callout head for callout tags, and the radius of the callout bubble. |
| ElevationTags | Defines properties for elevation tags. |
| SectionTags | Specifies the shape of heads and tails for section tags. |
| FloorByFaceFloor | Converts a mass floor into a floor of the building model. |
| HideCategory | Hides all elements that belong to a selected category in the current view. |
| RunInterferenceCheck | Locates invalid intersections between elements in a project. |
| SpecifyCoordinatesAtPoint | Relocates a model and rotates the model to True North by specifying coordinates for North/South, East/West, and Elevation. |
| ExportIFC | Saves an IFC file. |
| SystemBrowser | Displays the System Browser. Displays a hierarchical list of all the components in each discipline in a project, either by system or by zone. |
| ExportOptionsIFCOptions | Sets export options for CAD and IFC. |
| ExportDWFOrDWFx | Creates DWF or DWFx files. |
| ExportCADFormatsDWG | Creates DWG, DXF, DGN, OBJ, SAT, or STL files. |
| ExportCADFormatsDXF | Creates DWG, DXF, DGN, OBJ, SAT, or STL files. |
| ExportCADFormatsDGN | Creates DWG, DXF, DGN, OBJ, SAT, or STL files. |
| ExportCADFormatsACIS_SAT | Creates DWG, DXF, DGN, OBJ, SAT, or STL files. |
| ExportPDF | Creates PDF files. |
| ExportCADFormatsSTL | Creates DWG, DXF, DGN, OBJ, SAT, or STL files. |
| ExportCADFormatsOBJ | Creates DWG, DXF, DGN, OBJ, SAT, or STL files. |
| OpenIFC | Opens an IFC file. |
| RelinquishAllMine | Releases ownership of worksets and borrowed elements that have not been changed. |
| MaterialTakeoff | Creates a list of the sub-components or materials of any Revit family category. |
| DWFMarkup | Links marked-up DWF files into a Revit project so you can see the markups on corresponding sheets. |
| ImportTypes | Imports family types from a text (.txt) file into the current family. |
| ExportExportTypes | Exports family types from the current family to a text (.txt) file. |
| OpenIFCOptions | Sets options for the IFC template and class mapping. |
| KeynoteLegend | Creates a list of the keynotes used in a project, and their definitions. |
| KeynotingSettings | Specifies the location of the keynote table and the numbering method for keynotes. |
| Web | Draws the web elements between the chords. |
| TopChord | Draws the top chord of the truss family. |
| BottomChord | Draws the bottom chord of the truss family. |
| ShapeStatus | When enabled, this button indicates that the rebar shape is not valid. |
| TogglePropertiesPalette | Displays or hides a palette where you can view and edit instance properties. |
| StatusBarWorksets | For a workshared project, displays the active workset and the number of Others' pending Editing Requests in the status bar. |
| StatusBarDesignOptions | Displays the active design option in the status bar. |
| ReinforcementNumbers | Defines or edits numbering sequences by partition for rebar and fabric sheets. |
| FamilyCategoryAndParameters | Assigns the properties of a predefined family category to the component you are creating. |
| ExportImagesandAnimationsWalkthrough | Saves animations or image files. |
| ExportImagesandAnimationsSolarStudy | Saves animations or image files. |
| SunSettings | Specifies the location of the sun for solar studies, walkthroughs, and rendered images. |
| Grid | Places column grid lines in the building design. |
| ArchitecturalWall | Creates a non-structural wall in the building model. |
| Door | Adds doors to the building model. |
| Window | Adds windows to the building model. |
| Delete | Removes selected elements from the building model. |
| Space | Places analytical spaces to account for the entire volume within the model. This includes rooms, plenums and chases. |
| SpaceTag | Labels spaces in a project. |
| SpaceSeparator | Draws a space separation line to divide space. |
| TypeProperties | Displays properties for the family type to which the selected element belongs. |
| Level | Adds a level to the model. |
| FramingElevation | Creates a framing elevation to show vertical bracing. |
| ArchitecturalFloor | Creates a floor for the current level of the building model. |
| Stair | Adds a stair to the building model by creating common run, landing, and support components. |
| ArchitecturalColumn | Adds architectural columns to the building model. |
| MirrorProject | Flips the position of a project around a selected axis. |
| RotateProjectNorth | Changes the relationship of elements relative to Project North (the top of the drawing area) in plan views. |
| Rotate | Rotates selected elements around an axis. |
| MirrorPickAxis | Reverses the position of selected elements, using an existing line or edge as the mirror axis. |
| LineWeights | Creates or modifies line weights. |
| ObjectStyles | Specifies line weights, colors, and patterns, and materials for model objects, annotation objects, and imported objects. |
| AnalysisDisplayStyles | Specifies a presentation format for visualizing analysis results. |
| Snaps | Specifies snap increments, and enables or disables snap points. |
| ProjectUnits | Specifies the display format for units of measure. |
| StructuralPlan | Creates a structural plan view. |
| FloorPlan | Creates a floor plan view. |
| Section | Creates a section view. |
| Camera | Creates a 3D view from the perspective of a camera placed in the view. |
| ProjectBrowser | Displays the Project Browser. |
| NewSheet | Creates a page for a document set. |
| ImportCAD | Imports data or 3D geometry from other CAD programs to a Revit model or family. |
| LinkCAD | Links a CAD file to the current Revit project. |
| PointCloud | Links a Point Cloud file (*.rcp or *.rcs) into the current project. |
| NewFamily | Creates a set of custom components to use in projects. |
| LoadShapes | Loads a Revit family into the current file. |
| NewConceptualMass | Opens a template for creating a conceptual massing model. |
| LoadAutodeskFamily | Load an Autodesk family from the cloud. |
| Pin | Locks a model element in place. |
| Walkthrough | Creates an animated 3D walkthrough of a model. |
| Unpin | Unlocks a model element so it can move. |
| SolidExtrusion | Creates a 3D solid by extruding a 2D shape (profile). |
| PlaceAComponent | Places an element in the building model, based on a selected element type. |
| ModelLine | Creates a line that exists in 3D space and is visible in all views of a project. |
| StairPath | Annotates the slope direction and walk line of a stair. |
| ReferencePlane | Creates a reference plane using drawing tools. |
| Redo | Reverses the effects of the previous UNDO command |
| Undo | Reverses the most recent action |
| Control | Adds a flip arrow to the view. |
| PickAPlane | Select a plane in the view to define a new workplane. |
| Filters | Creates a filter to modify the visibility and graphics of elements in views based on element parameters. |
| TemporaryDimensions | Specifies the placement and component references for temporary dimensions. |
| LinePatterns | Creates or modifies line patterns. |
| Array | Creates a linear or radial array of selected elements. |
| Move | Moves selected elements to the specified location in the current view. |
| Copy | Copies selected elements and places them in the specified location in the current view. |
| PlaceView | Adds a view to a sheet. |
| Text | Adds text annotations (notes) to the current view. |
| NewTitleBlock | Opens a template for creating a Title Block family. |
| AutomaticCeiling | Creates a ceiling at a specified distance above the level in which it resides. |
| FillPatterns | Creates or modifies drafting patterns and model patterns. |
| Default3DView | Opens the default orthographic 3D view. |
| Label | Creates a label for the annotation symbol. |
| VisibilityOrGraphics | Overrides the default visibility and graphic display of model elements and annotations in the current view. |
| Opening | Creates an opening in a host, such as a wall or ceiling. |
| NewProject | Creates a Revit project file. |
| ActivateView | Enables you to modify the selected view without leaving the sheet. |
| Materials | Specifies the materials and associated properties to apply to model elements or families. |
| DeactivateView | Deactivates the view, so you can no longer change the view from the sheet. |
| MaterialAssets | Modifies the assets that define a material. |
| DecalTypes | Creates a decal that you can use to place images on surfaces of a building model for rendering. |
| Options | Display Revit Options Dialog. |
| Room | Creates a room bounded by model elements (such as walls, floors, and ceilings) and separation lines. |
| CurtainGrid | Creates a grid line in a curtain wall or curtain system. |
| CurtainWallMullion | Creates a horizontal or vertical mullion on a curtain grid. |
| FamilyTypes | Allows you to enter parameter values for existing family types, add parameters to the family, or create new types within the family. |
| FilledRegion | Creates a 2D, view-specific graphic with a fill pattern and a boundary line. |
| RoomTag | Tags the selected room. |
| Align | Aligns one or more elements with a selected element. |
| Symbol | Places a 2D annotation drawing symbol in the current view. |
| DuplicateView | Creates a view that contains only the model geometry from the current view. |
| ExportOptionsExportSetupsDGN | Sets export options for CAD and IFC. |
| ExportOptionsExportSetupsDWGOrDXF | Sets export options for CAD and IFC. |
| ColorFillLegend | Places a legend in a view to indicate the meanings of color fills for rooms or areas. |
| BuildingElevation | Creates an elevation view. |
| JoinOrUnjoinRoof | Connects roofs to other roofs or walls, or reverses a previous join. |
| SolidBlend | Creates a solid 3D shape that changes along its length, blending from a starting shape to an ending shape. |
| ManageLinks | Provides options for managing links to building models, CAD files, DWF markup files, and point clouds. |
| SolidRevolve | Creates a 3D shape by sweeping a 2D profile around an axis. |
| ScheduleOrQuantities | Creates a key schedule or a schedule of building components. |
| Callout | Creates a rectangular callout in the view. |
| SolidSweep | Creates a 3D shape by sweeping a 2D profile along a path. |
| CreateGroup | Creates a group of elements for easy reuse. |
| Ramp | Adds a ramp to the building model. |
| RoomSeparator | Creates a separation line to bound rooms where no walls or other room-bounding elements exist. |
| AlignedToCurrentView | Pastes elements that were cut or copied from another view into the current view. |
| AlignedToPickedLevel | Pastes the selected elements into a elevation view or a section view. |
| WallJoins | Changes how walls join together (butt, miter, square off). |
| StartingView | Specifies the view that first displays when you open the model. |
| AlignedToSelectedLevels | Pastes multiple elements from one level to specified levels. |
| TagByCategory | Attaches a tag to an element based on the element category. |
| AlignedToSelectedViews | Pastes selected elements, including view-specific elements such as dimensions, into specified views. |
| LoadedTagsAndSymbols | Lists the tags and symbols that will be used for each element category. |
| NewAnnotationSymbol | Creates a tag or symbol to identify elements in the project. |
| AlignedToSamePlace | Pastes the elements to the same place from which they were cut or copied. |
| SpotSlopeTypes | Defines attributes for spot slopes. |
| Arrowheads | Specifies line weights, fills, and styles for annotation arrowheads. |
| SpotElevationTypes | Defines attributes for spot elevations. |
| SpotCoordinateTypes | Defines attributes for spot coordinates. |
| ReviewWarnings | Displays a list of messages that you can ignore or resolve. |
| AlignmentStationLabelTypes | Defines attributes for Alignment Station Labels. |
| LineStyles | Creates or modifies line styles. |
| ReflectedCeilingPlan | Creates a reflected ceiling plan view. |
| DetailLevel | Specifies the detail level (coarse, medium, or fine) that applies to each view scale by default. |
| VoidExtrusion | Creates a 3D shape that is then used to remove part of a solid 3D shape. |
| VoidBlend | Creates a 3D blend, which is then used to remove part of a solid 3D shape. |
| VoidRevolve | Creates a 3D shape by sweeping a 2D profile around an axis, and uses the 3D shape to remove part of a solid 3D shape. |
| VoidSweep | Creates a 3D shape by sweeping a 2D profile along a path, and uses the resulting 3D shape to remove part of a solid 3D shape. |
| CutGeometry | Selects the geometry to cut. |
| UncutGeometry | Selects which geometry does not get cut when you join geometry. |
| PlaceDetailGroup | Places an instance of a detail group in the view. |
| OverrideByCategory | Changes the graphic display settings for all elements that belong to the same category as the selected element in the current view. |
| DetailComponent | Adds a view-specific detail component to a view. |
| DetailLine | Creates view-specific lines. |
| Insulation | Places a batt insulation graphic in a detail view. |
| CreateSimilar | Places an element of the same type as the selected element |
| Worksets | Creates worksets and adds elements to them. |
| Phases | Specifies project phases, phase filters, and graphic overrides for phases. |
| PropertyLine | Creates a property line in a plan view. |
| BuildingPad | Adds a building pad from a closed loop that you sketch on a toposurface. |
| ImportImage | Imports a raster image into a Revit project to use as a background image or visual aid during the creation or presentation of the model. |
| ImportPDF | Inserts a PDF file into a model view to use as a background image or visual aid. |
| MatchTypeProperties | Converts one or more elements to match the type of another element in the same view. |
| ScopeBox | Controls the visibility of datum elements (grids, levels, and reference planes) in specific views. |
| Linework | Overrides the line style for a selected line in the active view only. |
| SetWorkPlane | Specifies the work plane for the current view or for a selected work-plane-based element. |
| DraftingView | Creates a view showing details that are not directly associated with the building model. |
| Legend | Creates a list of building components and annotations used in a project. |
| Demolish | Marks elements as demolished in the current phase. |
| RevisionCloud | Adds a revision cloud to the current view or sheet to indicate design areas that have changed. |
| SynchronizeAndModifySettings | Allows you to specify options for the synchronization operation. |
| ProjectInformation | Specifies basic information about the project, including the project status and client information. |
| ModelInPlace | Creates a component that is unique to the project. |
| SheetList | Creates a schedule that lists the drawings in the project. |
| AreaPlan | Creates an area plan view. |
| GradedRegion | Modifies topography to indicate changes during the construction process. |
| Toposurface | Defines a topographical surface in a site plan or a 3D view. |
| ManageImages | Lists all raster images used in the project. |
| ApplyTemplatePropertiesToCurrentView | Applies properties stored in a view template to the current view. |
| RevealWall | Extrudes a profile along a path to create a cutout in a wall. |
| SweepWall | Creates a wall sweep by extruding a profile along a path. |
| Paint | Applies a material to the face of an element. |
| RemovePaint | Removes paint from selected faces. |
| NoteBlock | Creates a schedule of annotations added using the Symbol tool. |
| ModelText | Adds 3D text to the building model. |
| ShowHiddenLinesByElement | Displays hidden lines for individual model elements and detail elements that are obscured by other elements in the current view. |
| RemoveHiddenLinesByElement | Removes hidden lines for model elements and detail elements that are obscured by other elements in the active view only. |
| ManageViewTemplates | Displays parameters for view templates in the project. |
| CreateTemplateFromCurrentView | Creates a view template using the properties of the current view as the basis for the new template. |
| SplitFace | Divides the face of an element (such as a wall or floor) into regions for the application of different materials. |
| RestoreBackup | Rolls back changes made to a workshared project, or saves a selected backup version to be the current working model. |
| ExportODBCDatabase | Saves model data to an ODBC database. |
| LoadAsGroup | Loads a Revit file as a group. |
| SaveAsLibraryGroup | Saves a copy of all loaded families, the selected family, group, or view to your library. |
| ParkingComponent | Adds parking spaces to a toposurface. |
| TransferProjectStandards | Copies selected project settings from another open project to the current project. |
| SymbolicLine | Creates lines that are meant for symbolic purposes only, and are not part of the actual geometry of the component or building model. |
| CutProfile | Changes the shape of elements that are cut in a view, such as roofs, walls, floors, and the layers of compound structures. |
| ExportReportsSchedule | Saves a schedule or Room/Area report. |
| CloseInactiveViews | Closes open views except for the currently active view. The current view remains open in the drawing area. |
| AreaTag | Tags the selected area. |
| AreaBoundary | Defines boundaries for areas. |
| Area | Creates an area defined by walls and boundary lines. |
| JoinGeometry | Creates clean joins between 2 or more host elements that share a common face, such as walls and floors. |
| UnjoinGeometry | Removes a join between 2 or more elements. |
| SwitchJoinOrder | Changes the order in which elements join with one another. |
| TagAllNotTagged | Adds tags to multiple elements in one step. |
| MergeSurfaces | Combines 2 toposurfaces to create one toposurface. |
| SharedParameters | Specifies parameters that can be used in multiple families and projects. |
| LegendComponent | Adds a graphic representation of a selected model element to a legend view. |
| Offset | Copies or moves a selected element (such as a line, wall, or beam) a specified distance perpendicular to its length. |
| PurgeUnused | Removes unused families and types from a project. |
| PlaceDecal | Places an image on surfaces of a building model for rendering. |
| TitleBlock | Creates a title block element in a sheet view. |
| RebarLine | Defines lines and geometry of the rebar shape. |
| LabelContours | Displays the elevations of contour lines. |
| SplitWithGap | Splits a wall, pipe, duct, cable tray, or conduit into 2 segments with a defined gap. |
| ThinLines | Displays all lines on screen as a single width, regardless of zoom level. |
| LinkRevit | Links another Revit model to the current model. |
| ExportImagesandAnimationsImage | Saves animations or image files. |
| ProjectParameters | Specifies parameters that can be added to categories of elements in a project, and used in schedules. |
| RelocateProject | Moves the model relative to the shared coordinate system. |
| RotateTrueNorth | Changes the angle for a project relative to True North. |
| DuplicateWithDetailing | Creates a view that includes model geometry and view-specific elements from the current view. |
| Location | Specifies the geographic location for the project. |
| AcquireCoordinates | Determines the coordinates used in a linked project, and uses them for the current project. |
| ReportSharedCoordinates | Displays shared coordinates of a linked model within a host model. |
| IdsOfSelection | Displays unique identifiers for the selected elements. |
| SelectById | Uses an element's unique identifier to locate and select the element in the current view. |
| PublishCoordinates | Determines the coordinates used in the current model, and uses them for a linked model. |
| ParametersService | Use the Parameters Service to manage shared parameters and import them into a Revit session. |
| PlanRegion | Creates a plan region within a view. |
| BrowserOrganization | Changes the way that views are listed in the Project Browser. |
| Matchline | Adds matchlines to indicate where a view is split. |
| ViewReference | Adds an annotation indicating the sheet number and detail number for a selected view. |
| DesignOptions | Creates and manages design option sets and individual design options for the project. |
| AddToSet | Moves selected elements from the main model to one or more design options in a set. |
| PickToEdit | Opens a design option for editing by selecting an element contained in the option. |
| EditingRequests | Displays a list of other users' requests to borrow elements in your worksets, and your pending requests. |
| SaveAsLibraryFamily | Saves a copy of all loaded families, the selected family, group, or view to your library. |
| Subregion | Defines an area within a toposurface. |
| Railing | Creates a railing by sketching the railing path. |
| Beam | Adds individual beams, a chain of beams, or beams along grid lines. |
| Brace | Adds diagonal structural members connected to beams and columns. |
| StructuralColumn | Adds a vertical load-bearing element to the building model. |
| StructuralWall | Creates a load-bearing or shear wall in the building model. |
| SpanDirectionSymbol | Places a span direction symbol on a structural floor. |
| StructuralFloor | Creates a structural floor (slab) for the current level of the building model. |
| Scale | Resizes the selected item. |
| StructuralSettings | Defines settings for analytical elements and the display of structural framing. |
| ReferenceLine | Creates a reference line that you can use when creating a new family, or to create constraints for the family. |
| RebarCoverSettings | Adds, removes, or modifies the default rebar cover settings. |
| ShowMassFormAndFloors | Displays mass forms and any mass floors you have specified in all views. |
| CurtainSystemByFace | Creates a curtain system on the face of a mass or generic model. |
| WallByFaceWall | Creates walls using faces of a mass or generic model. |
| ShowMassByViewSettings | Displays masses based on the settings for the current view. By default, masses are turned off. |
| ShowMassSurfaceTypes | Displays mass faces, including any glazing and shades that have been specified. |
| ShowMassZonesAndShades | Displays mass zones, glazing, and shades if they have been specified. |
| StructuralRebar | Places planar, multi-planar or free form rebar. |
| CopyMonitorUseCurrentProject | Monitors grids, levels, columns, walls, floors, and openings within the current project. |
| CopyMonitorSelectLink | Copies selected elements from a linked project to the host project, and monitors changes to these elements. |
| CoordinationReviewUseCurrentProject | Displays warnings for monitored elements in the current project. |
| CoordinationSelectLink | Displays warnings for monitored elements between linked projects and the host project. |
| Wall | Creates foundations hosted by walls. |
| Isolated | Adds footings or pile caps to the building model. |
| MaterialTag | Tags a selected element using the description specified for its material. |
| CoordinationSettings | Specifies mapping behavior when copying MEP fixtures from a linked model into the current project. |
| Slab | Adds a foundation slab to the building model. |
| ElementKeynote | Tags a selected element using the keynote specified for the element type. |
| MaterialKeynote | Tags a selected element using the keynote specified for its material. |
| UserKeynote | Tags an element with a keynote that you select. |
| LoadSelection | Loads a previously saved selection set. |
| SaveSelection | Saves the currently selected elements as a set. |
| EditSelection | Edits a previously saved selection set. |
| ActivateControlsAndDimensions | Enable or disable the visibility of pins, constraints, and temporary dimensions when multiple elements are selected. |
| ShowWorksharingMakeEditableControls | Enables/Disables display of "Make Editable" controls when elements are selected. |
| MultiCategoryTag | Attaches tags to elements of multiple categories, based on a shared parameter. |
| BoundaryConditions | Defines point, line, and area boundary conditions in an analytical model. |
| StructuralPathReinforcement | Sketches the path of evenly placed reinforcing bars that are created perpendicular to the sketch. |
| PathReinforcementSymbol | Places a symbol that shows extents and hook types for the selected path reinforcement. |
| OpeningByFace | Creates an opening that is perpendicular to the selected face of a roof, floor, or ceiling. |
| VerticalOpening | Cuts a vertical opening through a roof, floor, or ceiling. |
| DormerOpening | Cuts a roof to create an opening for a dormer. |
| WallOpening | Cuts a rectangular opening in a straight or curved wall. |
| ShaftOpening | Creates a vertical opening that spans multiple levels, cutting through intervening roofs, floors, and ceilings. |
| SpotSlope | Displays the slope at a specific point on a face or an edge of a model element. |
| HideElements | Hides selected elements in the current view. |
| ToggleRevealHiddenElementsMode | Toggle reveal hidden elements mode. |
| OverrideByElement | Changes the graphic display settings for selected elements in the current view. |
| OverrideByFilter | Changes the graphic display settings for all elements in the view that meet the criteria specified in a filter. |
| DuplicateAsDependent | Creates a view that is dependent on the original view. |
| MaskingRegion | Creates a graphic that obscures elements in a project or family. |
| MajorSegment | Identifies one segment of the rebar shape that maintains its general position in rotation and auto-expansion behaviors. |
| ReinforcementSettings | Customizes reinforcement settings such as rounding parameters, rebar hosting and abbreviations of area/path reinforcement tagging. |
| ExportFBX | Saves a 3D view as an FBX file. |
| OpenFamily | Opens a Revit family. |
| CreateParts | Creates parts from the layers or subcomponents of a selected element. |
| ViewCube | Shows or hides the ViewCube, which allows you to change the orientation of a 3D view. |
| BeamAnnotations | Places multiple beam tags, annotations, and spot elevations. |
| AllowableBarTypes | Defines the allowable rebar types (diameters) of the shape type. |
| MacroManager | Opens the Macro Manager to run, create, or delete a macro. |
| MacroSecurity | Specifies the default security settings for macros in the Revit application or a document. |
| NavigationBar | Shows or hides the navigation bar, which provides access to the ViewCube, SteeringWheels, and zoom/pan functions. |
| FormWorkPlaneView | Enables the Workplane Viewer. |
| ReconcileHosting | Lists tags and elements hosted by the linked model that require review, due to changes in the linked model. |
| DiameterDimension | Places a dimension that measures the diameter of an arc or circle. |
| DiameterDimensionTypes | Defines attributes for diameter dimensions. |
| StructuralFabricArea | Located on the Reinforcement panel of the Structure tab (or Modify tab for floors, walls and foundation slabs).Sketches the boundary of a fabric area to populate with fabric sheets. |
| FabricReinforcementSymbol | Located on the Symbol panel of the Annotate tab.Places a symbol that represents the fabric sheet. |
| PlaceOnStairOrRamp | Places a railing on a stair or ramp. |
| DuctPressureLossReport | Generates a pressure loss report for one or more duct systems. |
| PipePressureLossReport | Generates a pressure loss report for one or more pipe systems. |
| OpenSampleFiles | Opens a Revit sample file. |
| SingleFabricSheetPlacement | Located on the Reinforcement panel of the Structure tab (or Modify tab for floors, walls and foundation slabs).Places a single fabric sheet on floors, walls, and foundation slabs. |
| AlignedMultiRebarAnnotation | Tags multiple elements with a single annotation that displays aligned dimensions between references as well as parameters from the referenced elements. For example, all rebar in a rebar set can be referenced with a single tag. |
| LinearMultiRebarAnnotation | Tags multiple elements with a single annotation that displays linear dimensions between references as well as parameters from the referenced elements. For example, all rebar in a rebar set can be referenced with a single tag. |
| FabricationSettings | Opens the Fabrication Settings dialog. |
| LinkIFC | Links an IFC file to the current project to reference its information for additional design work. |
| SelectionBox | Isolates selected elements in the current view (if a 3D isometric view) or the default 3D view. |
| InsertCoupler | Places a reinforcement coupler element to join rebar in a host. |
| PAndIDModeler | Create a 3D piping model directly from a 2D P&ID drawing in the cloud. |
| PAndIDSettings | Manage the mappings between elements, such as services and families, between the P&ID drawing and the Revit model. |
| TogglePAndIDModelerBrowser | Toggle P&ID Modeler browser. |
| DuctAccessory | Places a duct accessory. These accessories include dampers, filters and smoke detectors. |
| AirTerminal | Places a register, grille, or diffuser. |
| Duct | Draws rigid round, rectangular, or oval ductwork. |
| MechanicalEquipment | Places mechanical equipment such as boilers, furnaces, or fans. |
| DuctFitting | Places a duct fitting. These fittings include elbows, tees, wyes, crosses, and other types of fittings. |
| FlexDuct | Draws round and rectangular flexible ductwork. |
| ConvertToFlexDuct | Changes a length of ductwork connected to an air terminal from rigid duct to flexible duct. |
| DuctLegend | Places a legend to indicate the color fills associated with ductwork in duct systems. |
| PanelSchedules | Generates a panel schedule for a specified panel. |
| ElectricalSettings | Opens the Electrical Settings dialog to define distribution systems, wire types, cable tray and conduit sizes, and demand factors. |
| LoadClassifications | Assigns and specifies demand factors to a load classification. |
| LightingFixture | Places lighting fixtures such as ceiling, wall, and recessed lights. |
| ElectricalEquipment | Places electrical equipment such as panels and switch gear. |
| ElectricalFixture | Places electrical devices such as receptacles, junction boxes, and other power devices. |
| CheckCircuits | Verifies all circuits for proper connections to panels and valid system assignments. Errors are reported in a warning dialog. |
| DemandFactors | Applies demand factors to a panel. |
| Pipe | Draws rigid piping. |
| FlexPipe | Draws flexible piping. |
| PipeFitting | Places a pipe fitting. These fittings include elbows, tees, wyes, crosses, unions, and other types of fittings. |
| PipeAccessory | Places a pipe accessory. These accessories include connectors, valves, and inline water heaters. |
| ArcWire | Draws arced wire runs. |
| PipeLegend | Places a legend to indicate the color fills associated with piping systems. |
| CheckPipeSystems | Verifies all pipe systems for properly connected pipes and valid system assignments. |
| CheckDuctSystems | Verifies all duct systems for properly connected ductwork and valid system assignments. |
| MechanicalSettings | Opens the Mechanical Settings dialog. |
| PlumbingFixture | Places plumbing fixtures. These fixtures include sinks, water closets, tubs, drains, and various appliances. |
| Sprinkler | Places a sprinkler. |
| ElectricalConnector | Adds an electrical connector to a component. |
| DuctConnector | Adds a duct connector to a component. |
| PipeConnector | Adds a pipe connector to a component. |
| Zone | Defines HVAC zones within a project. |
| BuildingOrSpaceTypeSettings | Opens the Building and Space Type Settings dialog to manage building and space parameters and schedules. |
| ChamferedWire | Draws chamfered wire runs. |
| SplineWire | Draws splined wire runs. |
| Communication | Places communication devices such as intercom system components. |
| Data | Places data devices such as ethernet and other network connections. |
| FireAlarm | Places fire alarm devices such as smoke detectors, manual pull stations, and annunciators. |
| Lighting | Places lighting switches such as daylight sensors, occupancy sensors, and manual switches. |
| NurseCall | Places nurse call devices such as call stations, code blue stations, and door lights. |
| Security | Places security devices such as door locks, motion sensors, and surveillance cameras. |
| Telephone | Places a telephone jack. |
| CableTrayConnector | Adds a cable tray connector to a component. |
| ConduitConnector | Adds a conduit connector to a component. |
| CableTrayFitting | Places a cable tray fitting. These fittings include elbows, tees, wyes, crosses, and other unions. |
| ConduitFitting | Places a conduit fitting. These fittings include elbows, tees, wyes, crosses, and other unions. |
| CableTray | Draws cable tray runs such as rigid ladder or channel cable tray. |
| Conduit | Draws rigid conduit runs. |
| ManageTemplates | Manages and applies panel schedule templates to existing schedules in the project. |
| EditATemplate | Modifies a specific panel schedule template. |
| ParallelConduits | Creates parallel runs of conduit based on an initial conduit run. |
| DuctPlaceholder | Draws placeholder duct without elbow or tee fittings. |
| PipePlaceholder | Draws placeholder pipe without elbow or tee fittings. |
| ParallelPipes | Creates parallel runs of pipe based on an initial pipe run. |
| ShowDisconnects | Controls the display of graphical disconnect warnings for duct, pipe, conduit, cable tray, electrical circuits, and fabrication hangers. |
| MultiPointRouting | Automatically build a run of connected MEP fabrication parts by clicking points in the model. |
| SystemZone | Create a system-zone for analytical spaces. |
| SiteComponent | Adds site-specific elements, such as trees, parking islands, and fire hydrants. |
| AreaAndVolumeComputations | Specifies how areas and volumes are calculated, and creates area schemes. |
| ShowWorkPlane | Displays or hides the active work plane in the view. |
| Fascia | Adds fascia to the edge of a roof, soffit, or other fascia, or to model lines. |
| Gutter | Adds a gutter to the edge of a roof, soffit, or fascia, or to model lines. |
| SlabEdgeFloor | Shapes the horizontal edge of a floor slab. |
| CheckSpelling | Checks the spelling of text notes in a selection or in the current view or sheet. |
| RepeatingDetailComponent | Repeats a detail component along a path. |
| InsertViewsFromFile | Copies specified views (sheets, schedules, or drafting views) from a project file and saves them in the current project. |
| Insert2DElementsFromFile | Copies 2D elements from a detail view (saved in another project) into a detail view in the current project. |
| SaveAsLibraryView | Saves a copy of all loaded families, the selected family, group, or view to your library. |
| AutomaticBeamSystem | Creates a layout that is used to control the number and spacing of a series of parallel beams. |
| PlaceMass | Places an instance of a mass family in the project. |
| InPlaceMass | Creates a mass that is unique to the project. |
| SynchronizeNow | Updates a local copy of a workshared project using settings from the Synchronize with Central dialog. |
| StructuralTrusses | Adds a truss to the structure model. |
| CreateAnAreaBasedLoad | Creates an area based load from the area defined by the area based load boundaries. |
| AreaBasedLoadBoundary | Places a boundary line for electrical area based loads. |
| EquipmentLoad | Opens the System Browser to define equipment loads, such as a chiller or other specific equipment. |
| ShowBoundaryOpenEnds | Displays dots on the open ends of area based load boundary lines. |
| MechanicalControlDevice | Places a mechanical control device such as thermostats, CO2 sensors, and humidistats. |
| PlumbingEquipment | Places plumbing equipment such as hot water heaters, domestic water pumps, and sewage pumps. |
| HideBoundaryOpenEnds | Hides dots that display on the open ends of area based load boundary lines. |
| ShowLastReport | Displays the most recent interference check report. |
| GraphicalColumnSchedule | Creates a graphical column schedule for the project. |
| ApplyCoping | Adds coping to steel beams and columns. |
| RemoveCoping | Removes coping from steel beams and columns. |
| BeamSystemSymbol | Places a beam system span tag. |
| StructuralAreaReinforcement | Sketches the boundary of an area to populate with rebar. |
| AreaReinforcementSymbol | Places a symbol that shows extents and hook types for the selected area reinforcement. |
| SolidSweptBlend | Creates a blend that sweeps along a defined path. |
| VoidSweptBlend | Creates a blend that sweeps along a defined path, and uses the resulting 3D shape to remove part of a solid 3D shape. |
| EditRebarCover | Edits the rebar cover references of an entire rebar host or an individual face. |
| ColorSchemes | Creates or modifies a color fill scheme for rooms and areas. |
| AnalyticalLink | Creates an analytical element that connects two separate analytical nodes. |
| TrimOrExtendToCorner | Trims or extends elements (such as walls or beams) to form a corner. |
| TrimOrExtendSingleElement | Trims or extends one element (such as a wall, line, or beam) to a boundary defined by another element. |
| TrimOrExtendMultipleElements | Trims or extends multiple elements (such as walls, lines, and beams) to a boundary defined by another element. |
| AlignedDimension | Places dimensions between parallel references, or between multiple points. |
| LinearDimension | Places horizontal or vertical dimensions that measure the distance between reference points. |
| AngularDimension | Places a dimension that measures the angle between reference points sharing a common intersection. |
| RadialDimension | Places a dimension that measures the radius of an inner curve or fillet. |
| ArcLengthDimension | Places a dimension that measures the length of a curved wall or other element. |
| MeasureBetweenTwoReferences | Measures the distance between two elements or references. |
| MeasureAlongAnElement | Measures the length of an element. |
| MirrorDrawAxis | Draws a temporary line to use as an axis for mirroring. |
| KeyboardShortcuts | Assigns key sequences to tools. |
| BeamOrColumnJoins | Adjusts how beams and columns frame into one another. |
| SaveAsTemplate | Saves the current Revit project file as a template. |
| SaveAsFamily | Saves the current family. |
| HalftoneOrUnderlay | Customizes halftone and underlay elements in view. |
| Multiplanar | Toggles the ability to define a rebar shape bent in more than one plane. |
| OpenProject | Opens a Revit project. |
| LoadCases | Adds and edits load cases for the analytical model. |
| LoadCombinations | Adds and edits load combinations for the analytical model. |
| BoundaryConditionsSettings | Selects the family symbol and adjusts the spacing for boundary conditions. |
| FindOrReplace | Finds and replaces text in an open project file. |
| EnergySettings | Specifies parameters used to create the energy analytical model. |
| Generate | Creates the energy analytical model and generates design options and potential performance outcomes with Insight. |
| ExportGBXML | Saves the model as a gbXML file. |
| GuideGrid | Creates a new guide element in the active sheet to help align elements within and between sheets. |
| CreateAssembly | Creates an assembly from elements you select in the drawing area. |
| StairTreadOrRiserNumber | Creates a sequence of tread or riser numbers for a run in plan, elevation, or section views. |
| ManageConnectionToARevitServerAccelerator | Specifies the Revit Server Accelerator to use for worksharing, or changes the accelerator to which you are connected. |
| RenderInCloud | Renders 3D views online to create still images or interactive panoramas. |
| RenderGallery | Opens your online gallery of completed and in-progress renderings in a web browser. |
| CreateEnergyModel | Creates the energy analytical model. |
| DisplaceElements | Creates a view-specific representation of model elements that can be displaced in the view. |
| GlobalParameters | Specifies parameters that can be added to a project, and used to define values of other parameters. |
| Collaborate | Enables collaboration so team members can work on a model simultaneously. |
| CollaborateInCloud | Enables collaboration in the cloud, which allows team members to work on a model simultaneously. |
| PublishSettings | Selects the views and sheets to publish to the cloud. |
| AssemblyCode | Specifies the location of the assembly code file or reloads the assembly code table from the current file. |
| RevealObstacles | Highlights categories that are considered obstacles in the view. |
| PathOfTravel | Creates a path of travel along the shortest distance between 2 selected points. |
| MultipleValuesIndication | Specifies the value indicated for a parameter when multiple elements with different parameter values are selected. |
| MultiplePaths | Places multiple paths of travel between two selected points using a specified minimum path separation for each path. |
| OneWayIndicator | Place a one-way annotation family into the view. |
| PeopleContent | Place a family to indicate a person and a physical distance radius into the view. |
| SpatialGrid | Place a square or hexagonal grid in a room element. |
| LoadFamilyIntoProjectAndClose | Loads the family into open projects or family files and closes the family after it loads. |
| FabricationPart | Displays the MEP Fabrication Parts palette. |
| LoadRebarShapeIntoProjectAndClose | Loads the rebar shape into open projects or family files and closes the family after it loads. |
| Dynamo | Provides access to Dynamo, an open source visual programming platform for designers. |
| DeleteEnergyModel | Removes the energy analytical model from the Revit project. |
| Shorten | Creates a shorten object on the selected beam that can trim or extend the beam. |
| CopeSkewed | Creates a skewed cope at the selected beam end, either at the top or at the bottom. |
| CornerCut | Creates a cut on the corner of a selected plate. |
| Welds | Inserts a weld on one of the available edges of the model elements to be connected. |
| Plate | Creates a structural plate in the building model. |
| Bolts | Inserts bolts and the related holes in the selected model elements. |
| Holes | Inserts holes on the selected face of model elements. |
| Anchors | Inserts anchors and the related holes in the selected model elements. |
| ShearStuds | Creates shear studs and the related welds on the selected face of model elements. |
| ContourCut | Creates a contour cut on the selected faces of a beam or a plate. |
| Cope | Creates a parametric cope on intersecting beams and the related connection between the beams. |
| Miter | Creates a miter cut vertically or at the bisecting line of two beams and the related connection between the beams. |
| SawCutFlange | Creates a cut on a beam adjusted according to the flange of another intersecting beam and the related connection between the beams. |
| SawCutWeb | Creates a cut on a beam adjusted according to the web of another intersecting beam and the related connection between the beams. |
| CutThrough | Creates a cut through a model element around the contour of another intersecting model element. The weld between the two elements is also created. |
| CutBy | Creates a cut on a model element along the shape of another intersecting model element and a cut through the intersecting element. The connection between the two elements is also created. |
| ToggleHome | Toggle Revit Home. |
| SaveAsCloudModel | Saves the current Revit model to the cloud. |
| SystemsAnalysis | Performs a systems analysis and generates a report for whole building energy simulation and analysis. |
| LinkPDF | Inserts a link to a PDF into a model view. |
| LinkImage | Inserts a link to an image into a model view. |
| AnalyticalMember | Places an analytical member in the project. |
| BatchPrint | Print a large number of drawings with a batch job. |
| WorksharingMonitor | Launches Worksharing Monitor to manage a file-based workshared model. |
| SharedViews | Opens and closes the Shared Views palette. |
| ResetSharedCoordinates | Eliminate shared coordinates in the host model. |
| ElectricalAnalyticalLoadTypeSettings | Opens the Electrical Analytical Load Type Settings dialog to define the power requirement for area-based loads. |
| GenerateAnalysis | Creates the energy analytical model and generates design options and potential performance outcomes. |
| ViewAnalysis | Access energy and environmental performance data in the cloud. |
| OpenCloudModel | Opens a Revit cloud model. |
| DynamoPlayerForSteel | Places steel connections on selected elements using pre-defined rules. |
| PanelByBoundary | Creates a planar analytical panel for the current work plane after a sketch of the contour. |
| AnalyticalAutomation | Automates the creation, element connection, and update of the analytical model, using the physical representation as context. |
| RebarBendingDetail |
| PanelByExtrusion | Creates an analytical panel perpendicular to the current work plane after a sketch of the path. |
| CoordinationModelLocal |
| CoordinationModelAutodeskDocs |
| Loads |
| SpaceNaming | Assigns the names and numbers from architectural rooms to MEP spaces used for building performance analysis. |
| DynamoPlayer | Preview, select, and run your Dynamo graphs from a single dialog. |
| RepairCentralModel | Repairs a corrupt central model. |
| LinkTopography | Links existing topography to the current Revit model. |
| Optimize | Access energy and environmental performance data in Insight. |
| OpenRevitFile | Opens any Revit file type. |
| Close | Close Revit. |
| Save | Saves the currently open project file. |
| SaveAsProject | Saves the current Revit project file. |
| PrintSetup | Specifies print options. |
| Print | Sends the current drawing area or selected views and sheets to a printer or a printable file. |
| PrintPreview | Displays a preview version of the current view or sheet to print. |
| CopyToClipboard | Copies selected elements to the clipboard. |
| CutToClipboard | Removes selected elements, and places them on the clipboard. |
| PasteFromClipboard | Pastes elements from the clipboard into the current view. |
| TabViews | Arranges all open views in the drawing area as tabs in a single window. |
| TileViews | Arranges all open views within the application window, tiled so you can see each one in the drawing area. |
| CanvasTheme | Sets the color theme of the canvas to dark or light. |
| ExitRevit | Exit Revit. |
| StatusBar | Displays the status bar at the bottom of the Revit window. |

# See Also
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)