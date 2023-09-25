# Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET

The simulation and reconstruction for PET imaging are developed and maintained by Auer Benjamin from the Brigham and Women's Hospital and Harvard Medical School, Boston, MA, USA, and Roncali Emilie from the University of California, Davis, CA, USA.

**Contact:** Auer, Benjamin Ph.D <bauer@bwh.harvard.edu>

Table of contents:
```diff
- 1. Objective
- 2. Folder structure
- 2. Structure of the simulation
  - a) main.mac
  - b) mac/Verbose.mac
  - c) mac/world.mac
  - d) Data/GateMaterials.db
  - e) System and detector geometry: PET_head
  - f) Visualizing the geometry
  - g) Defining the attenuation object/patient
  - h) Setting up the source object
  - i) Setting up the physics
  - j) Setting up the acquisition parameters: Digitizer
  - k) Format the output data
- 4. How to run the simulation
- 5. How to analyze the simulation data
- 6. How to reconstruct the simulation data
```

# 1. Objective
In this tutorial, we offer a step-by-step walk through on how to build and analyze a realistic PET simulation in [GATE source page](http://www.opengatecollaboration.org).  

# 2. Folder Structure
The folder structure where to find the phantom data and GATE macro files can be seen below,

<p align="center">
<img width="954" alt="Screen Shot 2023-09-25 at 9 58 25 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/47685035-63b3-4be9-829e-0456d44af2a5">
</p>

# 3. Structure of the Simulation
## a) main.mac
The main.mac file contains all the reference to the geometry, physics, material database, and output needed to run the simulation

<p align="center">
<img width="871" alt="Screen Shot 2023-09-25 at 10 01 17 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/adc0a3c1-2492-4b53-b546-95a0aa876cd8">
</p>

## b) mac/Verbose.mac
Visualizing the print out of the simulation is helpful to check information on the events and verify that the physics and geometry are modeled properly.

<p align="center">
<img width="946" alt="Screen Shot 2023-09-25 at 10 44 17 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/6dc4655f-12d3-4282-87c6-3ba2a2c7ae7f">
</p>

## c) mac/world.mac
The world defines the experimental framework of the simulation. It must be large enough to contain the entire PET system and phantom. The tracking of particles is stopped once they leave the `world`. The `world` is shown as a gray wire frame in the visualization of the simulation shown below. `GateMaterials.db` must contain all elemental compositions and densities of materials which are defined later in the macro. 

<p align="center">
<img width="586" alt="Screen Shot 2023-09-25 at 10 46 51 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/ab0f979d-c5d6-4c0f-8a79-378c4ffa4d47">
</p>

<p align="center">
<img width="555" alt="Screen Shot 2023-09-25 at 10 47 07 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/201229dc-539c-4bb1-b134-d1a0c0191401">
</p>

## d) Data/GateMaterials.db
The `GateMaterials.db` contains all the material definition used in the simulation.

<p align="center">
<img width="759" alt="Screen Shot 2023-09-25 at 10 57 38 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/30299837-1c5d-48c4-99f9-c03a21bdcad1">
</p>

## e) System and Detector Geometry: PET_head
We defined the cylindrical geometry (size, position, and material) and the components of the the `PET_head` following a volume hierarchy (Head, Module, Block, Crystal, and Layer).

<p align="center">
<img width="596" alt="Screen Shot 2023-09-25 at 10 54 07 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/7cf219da-7a56-4ff3-8f42-768d6141b2f5">
</p>

The final layer is the crystal element,

<p align="center">
<img width="517" alt="Screen Shot 2023-09-25 at 10 54 59 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/dba24ce6-27df-4d35-841f-799da33d772f">
</p>

The detector ring is created by duplicating elements,

<p align="center">
<img width="565" alt="Screen Shot 2023-09-25 at 10 58 52 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/7502d64b-b056-42aa-bf8b-cf02f280a9a0">
</p>

<p align="center">
<img width="525" alt="Screen Shot 2023-09-25 at 10 59 06 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/270ae769-eb10-4052-993f-56ac27469726">
</p>

The last step is to define which volumes are sensitive to interactions. The simulation record the events in the output files only for sensitive volumes.

<p align="center">
<img width="510" alt="Screen Shot 2023-09-25 at 11 01 12 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/5d887832-4388-47be-b1ab-4064eb6ef5db">
</p>

## f) Visualizing the Geometry

<p align="center">
https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/3da38cc7-16e9-44e2-8fed-aca31684c4ba
</p>

## g) Defining the attenuation object/patient
The benchmark is a simple example of a water cylinder, but antropomorphic phantoms or CT-based phantoms can be created from patient data. Any of the phantoms available [here](https://github.com/BenAuer2021/Phantoms-For-Nuclear-Medicine-Imaging-Simulation#readme) can be used. The attenuation phantom can also be defined as a series of STL-based objects, we provide several STL-based phantoms [here](https://github.com/BenAuer2021/Mesh-based-Human-Phantom-for-Simulation/edit/main/README.md)

<p align="center">
<img width="517" alt="Screen Shot 2023-09-25 at 11 22 46 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/586ede10-fda2-4b09-9407-a358c6bfdf22">
</p>

## h) Setting up the source object
We use in the benchmark a F-18 source analytically defined. The source can also be voxelized (i.e. from an actual patient activity distribution, or corresponding to a voxelized phantom). Any of the source phantoms available [here](https://github.com/BenAuer2021/Phantoms-For-Nuclear-Medicine-Imaging-Simulation#readme) can be used. [Voxelized activity source phantoms](https://github.com/BenAuer2021/Mesh-based-Human-Phantom-for-Simulation/edit/main/README.md) can also be used in combination with the STL-based XCAT phantom.

## i) Setting up the physics

The physics model plus range and energy cuts for different particles and medium need to be set. 

<p align="center">
<img width="595" alt="Screen Shot 2023-09-25 at 11 28 47 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/628a12aa-9065-464b-b883-e9c39ebf1784">
</p>

## j) Setting up the acquisition parameters: Digitizer
The digitizer is the critical module in modeling the detection mechanism. It can include modeling of the electronics and create waveforms, energy resolution, and dead-time. 

<p align="center">
<img width="672" alt="Screen Shot 2023-09-25 at 11 48 40 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/b1fefe05-c090-40c2-a60a-59bcadfa9b62">
</p>

## k) Format the output data
The simulation output can be controlled via the following command lines to create a binary ROOT listmode file output.

<p align="center">
<img width="430" alt="Screen Shot 2023-09-25 at 11 55 43 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/3d2112e0-edd1-47cf-8ce5-b0940e973df5">
</p>

# 4. How to run the simulation
The acquisition time and the random generator can be controlled from the main macro (main.mac).

<p align="center">
<img width="277" alt="Screen Shot 2023-09-25 at 12 48 41 PM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/208be92c-c281-4549-a25c-e1beb28760cd">
</p>

It is recomended to run the simulation with a low statistics to verify that it completes without issues and crashes.
<p align="center">
https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/4af005e5-6fbe-443f-b461-32c3a72ebe86
</p>

The simulation can then be run with the desired statistics,
<p align="center">
https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/873993e6-85db-4f33-b306-646de946fd37
</p>

# 5. How to analyze the simulation data
We provide a python script to analyze the simulation data `runAnalysis.py`.

Run the analysis with,
```ruby
python ./runAnalysis.py output
```
The output of this script for a 10,000 Bq simulation looks like below,

<p align="center">
<img width="853" alt="Screen Shot 2023-09-25 at 1 01 21 PM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/d8cd2c73-d110-4362-aa57-7323c213f7d5">
</p>

# 6. How to Reconstruct the simulation data
The GATE simulated data can be reconstructed via the CASToR software that allows for histogram and list-mode PET reconstruction with Time-Of-Flight modeling. CASToR provides tools to transform GATE macro and data to CASToR format files used in reconstruction. Details on CASToR and benchmarks can be found [here](https://castor-project.org/documentation_v3).



