# Feature Engineering Logic

This document explains how raw system metrics are transformed into model-ready inputs.

## 1. Upload & Download Speed Calculation

Upload and download speeds are calculated using byte differences over time.

Formula:

Upload Speed = (Current Bytes Sent - Previous Bytes Sent) / Time Difference  
Download Speed = (Current Bytes Received - Previous Bytes Received) / Time Difference  

## 2. Error Count Logic

Error count is derived based on system stress conditions.

Example Logic:

- CPU > 85% → +1 error  
- Memory > 85% → +1 error  
- Temperature > 80°C → +1 error  

Total error count is the sum of triggered conditions.

## 3. Default Handling

If certain metrics are unavailable:

- Temperature → Use default value (e.g., 60°C)  
- Uptime → Use system uptime or fallback value  
- Network → Set to 0 if unavailable  

## 4. Data Consistency

- Ensure all values are in correct units.
- Ensure consistent time intervals for speed calculation.
- Avoid sudden unrealistic spikes.

## 5. Important Note

This logic must be implemented in the target system (C/C++ or other language) if Python is not supported.