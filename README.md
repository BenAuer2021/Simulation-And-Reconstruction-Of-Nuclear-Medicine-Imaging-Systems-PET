# Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET

The simulation and reconstruction in PET imaging are developed and maintained by Auer Benjamin from the Brigham and Women's Hospital and Harvard Medical School, Boston, MA, USA, and Roncali Emilie from the University of California, Davis, CA, USA.

**Contact:** Auer, Benjamin Ph.D <bauer@bwh.harvard.edu>

Table of contents:
```diff
- 1. Objective
- 2. Defrise Phantom
  - 2.1 Description
  - 2.2 Usage in GATE
- 3. Derenzo Phantom
  - 3.1 Description
  - 3.2 Usage in GATE  
```

# 1. Objective
In this tutorial, we offer a step-by-step walk through on how to build a realistic PET simulation in [GATE source page](http://www.opengatecollaboration.org).  

# 2. Folder Structure
The folder structure where the find the phantom data and GATE macro files can be seen below,

<img width="954" alt="Screen Shot 2023-09-25 at 9 58 25 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/47685035-63b3-4be9-829e-0456d44af2a5">

# 3. Structure of the Simulation
## a) main.mac
The main.mac file contains all the reference to the geometry, physics, material database, and output needed to run the simulation

<img width="871" alt="Screen Shot 2023-09-25 at 10 01 17 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/adc0a3c1-2492-4b53-b546-95a0aa876cd8">

## b) mac/Verbose.mac
Visualizing the print out of the simulation is helpful to check information on the events and verify that the physics and geometry are modeled properly.

<img width="946" alt="Screen Shot 2023-09-25 at 10 44 17 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/6dc4655f-12d3-4282-87c6-3ba2a2c7ae7f">

## c) mac/world.mac
The world defines the experimental framework of the simulation. It must be large enough to contain the entire PET system and phantom. The tracking of particles is stopped once they leave the `world`. The `world` is shown as a gray wire frame in the visualization of the simulation shown below. `GateMaterials.db` must contain all elemental compositions and densities of materials which are defined later in the macro. 

<img width="586" alt="Screen Shot 2023-09-25 at 10 46 51 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/ab0f979d-c5d6-4c0f-8a79-378c4ffa4d47">

<img width="555" alt="Screen Shot 2023-09-25 at 10 47 07 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/201229dc-539c-4bb1-b134-d1a0c0191401">

## d) Data/GateMaterials.db
The `GateMaterials.db` contains all the material definition used in the simulation.

<img width="759" alt="Screen Shot 2023-09-25 at 10 57 38 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/30299837-1c5d-48c4-99f9-c03a21bdcad1">

## e) System and Detector Geometry: PET_head
We defined the cylindrical geometry (size, position, and material) and the components of the the PET_head following a volume hierarchy (Head, Module, Block, Crystal, and Layer).

<img width="596" alt="Screen Shot 2023-09-25 at 10 54 07 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/7cf219da-7a56-4ff3-8f42-768d6141b2f5">

The final layer is the crystal element,

<img width="517" alt="Screen Shot 2023-09-25 at 10 54 59 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/dba24ce6-27df-4d35-841f-799da33d772f">

The detector ring is created by duplicating elements,

<img width="565" alt="Screen Shot 2023-09-25 at 10 58 52 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/7502d64b-b056-42aa-bf8b-cf02f280a9a0">

<img width="525" alt="Screen Shot 2023-09-25 at 10 59 06 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/270ae769-eb10-4052-993f-56ac27469726">

The last step is to define which volumes are sensitive to interactions. The simulation record the events in the output files only for sensitive volumes.

<img width="510" alt="Screen Shot 2023-09-25 at 11 01 12 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/5d887832-4388-47be-b1ab-4064eb6ef5db">

## f) Visualizing the Geometry
https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/2054ebb3-c7c5-4df3-a70e-d19855110869

## g) Defining the attenuation object/patient
The benchmark is a simple example of a water cylinder, but antropomorphic phantoms or CT-based phantoms can be created from patient data. Any of the phantoms available [here](https://github.com/BenAuer2021/Phantoms-For-Nuclear-Medicine-Imaging-Simulation#readme) can be used. The attenuation phantom can also be defined as a series of STL-based objects, we provide several STL-based phantoms [here](https://github.com/BenAuer2021/Mesh-based-Human-Phantom-for-Simulation/edit/main/README.md)

<img width="517" alt="Screen Shot 2023-09-25 at 11 22 46 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/586ede10-fda2-4b09-9407-a358c6bfdf22">

## h) Setting up the source object
We use in the benchmark a F-18 source analytically defined. The source can also be voxelized (i.e. from an actual patient activity distribution, or corresponding to a voxelized phantom). Any of the source phantoms available [here](https://github.com/BenAuer2021/Phantoms-For-Nuclear-Medicine-Imaging-Simulation#readme) can be used. [Voxelized activity source phantoms](https://github.com/BenAuer2021/Mesh-based-Human-Phantom-for-Simulation/edit/main/README.md) can also be used in combination with the STL-based XCAT phantom.

## i) Setting up the physics

The physics model and range and energy cuts for different particles and medium need to be set. 

<img width="595" alt="Screen Shot 2023-09-25 at 11 28 47 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/628a12aa-9065-464b-b883-e9c39ebf1784">

## j) Setting up the acquisition parameters: Digitizer
The digitizer is the critical module in modeling the detection mechanism. It can include modeling of the electronics and create waveforms, energy resolution, and deadtime. 

<img width="672" alt="Screen Shot 2023-09-25 at 11 48 40 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/b1fefe05-c090-40c2-a60a-59bcadfa9b62">

## k) Format the output data
The simulation output can be controlled via the following command lines to create a binary ROOT listmode file output.

<img width="430" alt="Screen Shot 2023-09-25 at 11 55 43 AM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/3d2112e0-edd1-47cf-8ce5-b0940e973df5">

# 4. How to Run the Simulation
The acquisition time and the random generator can be controlled from the main macro (main.mac).

<img width="277" alt="Screen Shot 2023-09-25 at 12 48 41 PM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/208be92c-c281-4549-a25c-e1beb28760cd">

It is recomended to run the simulation with a low statistics to verify that it complete without issues and crashes.

https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/4af005e5-6fbe-443f-b461-32c3a72ebe86

The simulation can then be run with the desired statistics,

https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/873993e6-85db-4f33-b306-646de946fd37

# 5. How to Analyze the Simulaton Data
We provide a python script to analyze the simulation data `runAnalysis.py`.

Run the analysis with,
```ruby
python ./runAnalysis.py output
```
The output of this script for a 10,000 Bq simulation looks like below,
<img width="853" alt="Screen Shot 2023-09-25 at 1 01 21 PM" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/d8cd2c73-d110-4362-aa57-7323c213f7d5">


# 6. How to Reconstruct the Simulaton Data
The GATE simulated data can be reconstructed via the CASToR software that allows for histogram and list-mode PET reconstruction with Time-Of-Flight modeling. CASToR provides tools to transform GATE macro and data to CASToR format files used in reconstruction. Details on CASToR and benchmarks can be found [here](https://castor-project.org/documentation_v3).



