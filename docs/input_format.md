# Input Format Specification

This document defines the exact input format required by the Health Prediction Model.

## Feature Order (STRICT)

The model expects input in the following order:

1. CPU Usage (%)  
2. Memory Usage (%)  
3. Temperature (°C)  
4. Uptime (seconds)  
5. Upload Speed (bytes/second)  
6. Download Speed (bytes/second)  
7. Error Count  

## Input Shape

- Format: 2D Array
- Shape: [1 x 7]
- Data Type: float32

Example:

[50.0, 65.0, 70.0, 1200.0, 300.0, 500.0, 1.0]

## Important Notes

- Feature order must NOT be changed.
- All values must be numeric.
- Units must match the specification.
- Missing values should be handled before passing to the model.