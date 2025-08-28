# Project: ROS2 MCAP Visualization and Trimming Tool

## Purpose
Develop an open-source tool for handling ROS2 MCAP files (bags) to:
- Read and visualize MCAP files.
- Filter and select specific topics.
- Plot data dynamically over time (interactive).
- Trim and save new MCAP files based on user-defined intervals.
- Export data to other formats (CSV, Parquet) for further analysis.

Designed for roboticists and developers to quickly analyze and process ROS2 data.

## Features (MVP)
1. **File Loading:** Load MCAP/SQLite2 files, list all topics.
2. **Visualization:** Interactive Plotly graph (time vs. data points), multi-topic selection.
3. **Filtering:** Filter by topic, mark intervals for trimming.
4. **Trim & Save:** Extract selected time intervals, save as MCAP, CSV, or Parquet.
5. **Future Enhancements:** Drag-and-drop GUI, real-time visualization, Python/C++ backend integration, advanced data analysis.

## Data Format
- **MCAP:** Generated via ROS2 `ros2 bag record`.
- **Structure:** Timestamps, topics, messages (sensor/control data).

## Technology Stack
- **Frontend:** Python with PyQt + Plotly.
- **Backend:** C++ for high-performance MCAP reading/writing.
- **Data Processing:** Pandas, NumPy.
- **Optional:** ROS2 integration, other robotic frameworks.

## Use Cases
- Analyze sensor data from robot test runs.
- Trim long MCAP files for AI model training.
- Compare and visualize control signals across runs.


## project structure

ros2_mcap_tool/
├─ README.md
├─ requirements.txt          # Python dependencies (PyQt, Plotly, polars, etc.)
├─ setup.py                  # Package setup
├─ /docs                     # Project documentation
│   └─ architecture.md
├─ /src
│   ├─ /gui
│   │   ├─ main_window.py
│   │   ├─ plots.py
│   │   └─ controls.py
│   ├─ /core
│   │   ├─ session_manager.py
│   │   ├─ trim_engine.py
│   │   ├─ export_engine.py
│   │   └─ visualization_engine.py
│   ├─ /data_access
│   │   ├─ mcap_reader.cpp
│   │   ├─ mcap_reader_py.py
│   │   └─ topic_indexer.py
│   └─ main.py
├─ /tests
│   ├─ test_trim.py
│   ├─ test_export.py
│   └─ test_visualization.py
└─ /examples
    └─ sample.bag

### Notes
- `mcap_reader.cpp` implements high-performance backend for reading/writing MCAP files.
- `gui/plots.py` handles interactive Plotly visualizations within PyQt.
- `core/session_manager.py` orchestrates workflow between GUI, trim/export engines, and data access.
- Tests ensure correctness of trimming, exporting, and plotting logic.