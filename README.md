# Manufacturing Quality Control Dashboard

A Python + Power BI dashboard that monitors production line quality in real time — detecting when a process drifts out of statistical control and identifying the leading causes of defects.

## The Problem

Manufacturing lines generate thousands of quality measurements daily. Without systematic monitoring, defects are caught late — after scrap costs pile up — instead of the moment a process starts drifting.

## What This Project Does

- Ingests production line sensor/inspection data
- Builds SPC (Statistical Process Control) control charts to detect out-of-control conditions
- Calculates Cp/Cpk to assess whether the process is capable of meeting spec
- Identifies the top defect causes via Pareto analysis
- Presents findings in an interactive Power BI dashboard

    