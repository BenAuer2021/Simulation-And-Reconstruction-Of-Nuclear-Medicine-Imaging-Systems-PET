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
<img width="740" alt="image" src="https://github.com/BenAuer2021/Simulation-And-Reconstruction-Of-Nuclear-Medicine-Imaging-Systems-PET/assets/84809217/ba77f477-54f0-4783-8dc7-59eb3fa0e48e">




