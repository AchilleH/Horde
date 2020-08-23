# Program Library
---

- ASUCLA Catering
- Data Collection
- Data Analysis

---
## ASUCLA Catering
 - **InvIntersect**
 
 A simple script making use of the xlrd library to compare inventory lists from 2 different departments that shared the same kitchen space. The goal was to simplify inventory management by narrowing down the responsibility of restocking certain items to a specific department. This normalized each inventory list and created a text document containing all the collisions found. Enabling discussion regarding which department would be in charge of each common item.
 
## Data Collection
- **DataRecord**

A java processing script written to continuously read and store data from the arduino serial channel into a formatted csv file for later analysis. This was a predecessor to a later optimized arduino script written to quickly record data from a paper rocket launcher. This was due to us reading the serial channel constantly, which imposes a speed limit on the rate which the arduino can record data.

## Data Analysis
- **FFT**

Python Script made to apply a fast fourier tranformation on 3 different hot wire anemometry samples. The goal was to determine the primary frequency of karman vorticies produced by the flow of air past a cylinder in a wind tunnel. It applied the transformation and plotted the results on a plot with  a shared x axis.
- **Polyfit**

Another python script which fits a fifth order polynomial to a set of data. Used to calibrate the hot wire.
