#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import collections as mc
import scipy.stats as ss
import scipy
import numpy as np
import os
from pathlib import Path
import uproot
import re
import click
import gatetools as gt
import gatetools.phsp as phsp
import itk
import sys
import logging
logger=logging.getLogger(__name__)
sys.settrace


# --------------------------------------------------------------------------
# it is faster to access to root array like this dont know exactly why
def tget(t, array_name):
    return t.arrays([array_name], library="numpy")[array_name]

# --------------------------------------------------------------------------
def get_stat_value(s, v):
    g = r''+v+'\w+'
    a = re.search(g, s)
    if a == None:
        return -1
    a = a.group(0)[len(v):]
    return float(a)
    
def getValues(array, key):
    values = tget(array, key)
    return values

def analyse_pet(output_folder, ax, i):
    if not os.path.isdir(output_folder):
        return
    filename = os.path.join(output_folder, "pet.root")
    print('Filename', filename)
    coinc = []
    delays = []
    singles = []
    times = []
    if os.path.isfile(filename):

        f = uproot.open(filename)
        #print("List of keys: \n", f.keys())
        with uproot.open(filename) as f_tmp:
            for keyname in f_tmp:
                if keyname == "Singles;1":
                    print("singles")
                    singles = f_tmp['Singles']
                    times = tget(singles, 'time')
                else:
                    if keyname == "Singles_BGO;1" :
                        singles = f_tmp['Singles_BGO']
                        times = tget(singles, 'time')
                    

        print("th following")                
        # get timing
        #singles = f['Singles']
        #times = tget(singles, 'time')
        
        #singles = f['Singles']
        print('nb of singles ', len(singles))
        #times = tget(singles, 'time')
         
        coinc = f['Coincidences']
        print('nb of coincidences', len(coinc))
        
        delays = f['delay']
        print('nb of delays', len(delays))
    try:
        stat_filename = os.path.join(Path(filename).parent, 'stat.txt')
        print('Open stat file', stat_filename)
        fs = open(stat_filename, 'r').read()
        n_events = get_stat_value(fs, '# NumberOfEvents = ')
        start_simulation_time = get_stat_value(fs, '# StartSimulationTime        = ')
        stop_simulation_time = get_stat_value(fs, '# StopSimulationTime         = ')
    except:
        print('nope')
        

    #
    n_events = 1
    start_simulation_time = 0
    stop_simulation_time = 240
    print("Detector positions by run")
    times = getValues(coinc, 'time1')
    start_time = min(times)
    end_time = max(times)
    slice_time = (end_time-start_time)/2
    print(f'Times : {start_time} {slice_time} {end_time}')
    runID = getValues(coinc, 'runID')
    gpx1 = getValues(coinc, 'globalPosX1')
    gpx2 = getValues(coinc, 'globalPosX2')
    gpy1 = getValues(coinc, 'globalPosY1')
    gpy2 = getValues(coinc, 'globalPosY2')
    # only consider coincidences  with time lower than time_slice
    # (assuming 2 time slices only)
    mask = (times < slice_time)
    n = 1000 # restrict to the n first values
    r0_gpx1 = gpx1[mask][:n]
    r0_gpx2 = gpx2[mask][:n]
    r0_gpy1 = gpy1[mask][:n]
    r0_gpy2 = gpy2[mask][:n]
    r0x = np.concatenate((r0_gpx1,r0_gpx2, r0_gpx1))
    r0y = np.concatenate((r0_gpy1,r0_gpy2, r0_gpy1))
    a = ax[(i+0,0)]
    a.scatter(r0x, r0y, s=1)
    mask = (times > slice_time)
    r1_gpx1 = gpx1[mask][:n]
    r1_gpx2 = gpx2[mask][:n]
    r1_gpy1 = gpy1[mask][:n]
    r1_gpy2 = gpy2[mask][:n]
    r1x = np.concatenate((r1_gpx1,r1_gpx2, r1_gpx1))
    r1y = np.concatenate((r1_gpy1,r1_gpy2, r1_gpy1))
    a = ax[(i+0,0)]
    a.scatter(r1x, r1y, s=1)
    a.set_aspect('equal', adjustable='box')
    a.set_xlabel('mm')
    a.set_ylabel('mm')
    a.set_title('Transaxial detection position ({} first events only)'.format(n))

    # Axial Detection
    print('Axial Detection')
    ad1 = getValues(coinc, 'globalPosZ1')
    ad2 = getValues(coinc, 'globalPosZ2')
    print(len(ad1))
    ad = np.concatenate((ad1, ad2))
    a = ax[(i+0,1)]

    a.hist(ad, histtype='step', bins=100)
    print(len(ad1))
    a.set_xlabel('mm')
    a.set_ylabel('counts')
    a.set_title('Axial coincidences detection position')

    # True unscattered coincidences (tuc)
    # True scattered coincindences (tsc)
    print('True scattered and unscattered coincindences')
    z = (ad1+ad2)*0.5
    compt1 = getValues(coinc, 'comptonPhantom1')
    compt2 = getValues(coinc, 'comptonPhantom2')
    rayl1 = getValues(coinc, 'RayleighPhantom1')
    rayl2 = getValues(coinc, 'RayleighPhantom2')
    mask =  ((compt1==0) & (compt2==0) & (rayl1==0) & (rayl2==0))
    tuc = z[mask]
    tsc = z[~mask]
    print("\tscattered", len(tsc))
    print("\tunscattered", len(tuc))
    a = ax[i+0,2]
    a.hist(tuc, bins=100)
    a.set_xlabel('mm')
    a.set_ylabel('counts')
    a.set_title('Axial Sensitivity Detection')
    a = ax[i+1,0]
    countsa, binsa = np.histogram(tsc, bins=100)
    countsr, binsr = np.histogram(z, bins=100)
    a.hist(binsa[:-1], bins=100, weights=countsa/countsr)
    a.set_xlabel('mm')
    a.set_ylabel('%')
    a.set_title('Axial Scatter fraction')

    # Delays and Randoms
    print("Delays and Randoms")
    time = getValues(coinc, 'time1')
    sourceID1 = getValues(coinc, 'sourceID1')
    sourceID2 = getValues(coinc, 'sourceID2')
    mask = (sourceID1==0) & (sourceID2==0)
    decayF18 = time[mask]
    mask = (sourceID1==1) & (sourceID2==1)
    decayO15 = time[mask]

    ## FIXME -> measured and expected HL
    # F18 109.771(20) minutes 6586.2 sec
    # O15 122.24 seconds

    # histogram of decayO15
    bin_heights, bin_borders = np.histogram(np.array(decayO15), bins='auto', density=True)
    bin_widths = np.diff(bin_borders)
    bin_centers = bin_borders[:-1] + bin_widths / 2

    # expo fit
    def exponential_func(x, a, b):
        return a*np.exp(-b*x)
    popt, pcov = scipy.optimize.curve_fit(exponential_func, bin_centers, bin_heights)
    xx = np.linspace(0, end_time, int(end_time))
    yy = exponential_func(xx, *popt)
    hl = np.log(2)/popt[1]

    # plot
    a = ax[i+1,1]
    a.hist(decayO15, bins=100, label='O15 HL = 122.24 sec', histtype='stepfilled', alpha=0.5, density=True)
    a.hist(decayF18, bins=100, label='F18 HL = 6586.2 sec', histtype='stepfilled', alpha=0.5, density=True)
    a.plot(xx, yy, label='O15 fit HL = {:.2f} sec'.format(hl))
    a.legend()
    a.set_xlabel('time (s)')
    a.set_ylabel('decay')
    a.set_title('Rad decays')

    # Randoms
    eventID1 = getValues(coinc, 'eventID1')
    eventID2 = getValues(coinc, 'eventID2')
    randoms = time[eventID1 != eventID2]
    print(len(delays))
    t1 = getValues(delays, 'time1')
    print('nb of randoms', len(randoms))
    print('nb of delays', len(delays))
    a = ax[i+1,2]
    a.hist(randoms, bins=100, histtype='stepfilled', alpha=0.6, label='Random = {}'.format(len(randoms)))
    a.hist(t1, bins=100, histtype='step', label="Delays with coinc sorter = {}".format(len(delays)))
    a.legend()
    a.set_xlabel('time (s)')
    a.set_ylabel('events')
    a.set_title('Randoms')

    # info
    ntrue = len(tuc)
    absolute_sensitivity = ntrue/n_events
    line1 = 'Number of events {:.0f}'.format(n_events)
    #line1 = line1+'\nNumber of singles {:.0f}'.format(len(singles))
    line1 = line1+'\nNumber of coincidences {:.0f}'.format(len(coinc))
    line1 = line1+'\nNumber of true {:.0f}'.format(len(tuc))
    line1 = line1+'\nNumber of randoms {:.0f}'.format(len(randoms))
    line1 = line1+'\nNumber of scatter {:.0f}'.format(len(tsc))
    line1 = line1+'\nAbsolute sensibility {:.2f} %'.format(absolute_sensitivity*100.0)
    line1 = line1+'\nStart time {:.1f} s'.format(start_time)
    line1 = line1+'\nSlice time {:.1f} s'.format(slice_time)
    line1 = line1+'\nStop time {:.1f} s'.format(end_time)
    a = ax[i+2,0]
    a.plot([0], [0], '')
    a.plot([1], [1], '')
    a.set_xticks([])
    a.set_yticks([])
    a.axis('off')
    a.text(0.2, 0.5, line1)

    dictTest = {
        "coincidences": len(coinc),
        "true":         len(tuc),
        "random":       len(randoms),
        "scatter":      len(tsc),
        "delay":        len(delays),
        "hl":           hl
    }

    return dictTest


# -----------------------------------------------------------------------------
def plot_all(output_folders, ax):
    test = False
    previousDictTest = {
        "coincidences": 0,
        "true":         0,
        "random":       0,
        "scatter":      0,
        "delay":        0,
        "hl":           0
    }
    for o, i in zip(output_folders, range(len(output_folders))):
        dictTest = analyse_pet(o, ax, 3*i)
        print(dictTest)
        print(previousDictTest)
        test = (0.99*previousDictTest["coincidences"] <= dictTest["coincidences"] <= 1.01*previousDictTest["coincidences"]) and \
               (0.99*previousDictTest["true"]         <= dictTest["true"]         <= 1.01*previousDictTest["true"]) and \
               (0.95*previousDictTest["random"]       <= dictTest["random"]       <= 1.05*previousDictTest["random"]) and \
               (0.99*previousDictTest["scatter"]      <= dictTest["scatter"]      <= 1.01*previousDictTest["scatter"]) and \
               (0.90*previousDictTest["delay"]        <= dictTest["delay"]        <= 1.10*previousDictTest["delay"]) and \
               (0.95 * 122.24                         <= dictTest["hl"]           <= 1.05 * 122.24)
        previousDictTest = dictTest
    return test

# -----------------------------------------------------------------------------
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('output_folders',
                nargs=-1,
                required=True,
                type=click.Path(exists=True, file_okay=True, dir_okay=True))
@gt.add_options(gt.common_options)
def analyse_click(output_folders, **kwargs):
    '''
    TODO
    '''
    r = analyse_all_folders(output_folders)
    print("Last test return: " + str(r))

def analyse_all_folders(output_folders, **kwargs):
    # logger
    gt.logging_conf(**kwargs)
    
    # take correct folder:
    outputFolders = []
    for o in output_folders:
        if os.path.isdir(o):
            outputFolders.append(o)

    # plot
    ncols=3
    nrows=3*len(outputFolders)
    fig, ax = plt.subplots(ncols=ncols, nrows=nrows, figsize=(15, 10))

    r = plot_all(outputFolders, ax)

    for o in range(len(outputFolders)):
      fig.delaxes(ax[3*o+2][1])
      fig.delaxes(ax[3*o+2][2])
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('output.pdf')
    plt.show()
    print(outputFolders)
    return r


# --------------------------------------------------------------------------
if __name__ == '__main__':
    analyse_click()
