// Pseudocode for Algorithm Visualization Website

// Main Entry Point
FUNCTION main()
    InitializeWebsite()
    WHILE WebsiteIsRunning
        HandleUserInput()
        RenderPage()
    END WHILE
END FUNCTION

// Website Initialization
FUNCTION InitializeWebsite()
    LoadStaticAssets()  // CSS, JS, Images
    InitializeAlgorithmList()  // List of algorithms to visualize
    SetupEventListeners()  // Button clicks, form inputs, etc.
END FUNCTION

// Algorithm List Setup
FUNCTION InitializeAlgorithmList()
    Algorithms = [
        "Sorting Algorithms": ["Bubble Sort", "Merge Sort", "Quick Sort"],
        "Graph Algorithms": ["Dijkstra's", "A*", "BFS", "DFS"],
        "Search Algorithms": ["Binary Search", "Linear Search"]
    ]
END FUNCTION

// User Input Handling
FUNCTION HandleUserInput()
    IF UserClicksAlgorithm()
        SelectedAlgorithm = GetSelectedAlgorithm()
        AlgorithmData = FetchAlgorithmData(SelectedAlgorithm)
        VisualizeAlgorithm(AlgorithmData)
    END IF
    IF UserAdjustsSettings()
        Settings = GetUpdatedSettings()
        ApplySettings(Settings)
    END IF
END FUNCTION

// Algorithm Data Fetching
FUNCTION FetchAlgorithmData(algorithmName)
    SWITCH algorithmName
        CASE "Bubble Sort": RETURN GetBubbleSortSteps()
        CASE "Merge Sort": RETURN GetMergeSortSteps()
        CASE "Quick Sort": RETURN GetQuickSortSteps()
        CASE "Dijkstra's": RETURN GetDijkstraSteps()
        CASE "A*": RETURN GetAStarSteps()
        // Add cases for other algorithms
        DEFAULT: RETURN []
    END SWITCH
END FUNCTION

// Visualization Rendering
FUNCTION VisualizeAlgorithm(algorithmData)
    ClearVisualizationArea()
    FOR EACH step IN algorithmData
        RenderStep(step)
        IF Settings.ShowStepByStep
            Wait(Settings.StepDelay)
        END IF
    END FOR
END FUNCTION

// Rendering Steps
FUNCTION RenderStep(step)
    DrawOnCanvas(step.VisualRepresentation)
    UpdateSidebar(step.Description)
END FUNCTION

// Settings Application
FUNCTION ApplySettings(settings)
    Settings.StepDelay = settings.StepDelay
    Settings.ShowStepByStep = settings.ShowStepByStep
    Settings.HighlightChanges = settings.HighlightChanges
END FUNCTION

// Utility Functions
FUNCTION DrawOnCanvas(data)
    Canvas.Clear()
    Canvas.Draw(data)
END FUNCTION

FUNCTION UpdateSidebar(description)
    Sidebar.Clear()
    Sidebar.Display(description)
END FUNCTION

FUNCTION Wait(milliseconds)
    Sleep(milliseconds)
END FUNCTION
