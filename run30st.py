import math as math
from math import *
import openseespy.opensees as ops



from openseespy.opensees import *

# from RC3D1Story import RC3D1Story
# from mat import mat
# from RC3D1Story import *
from BuildRCrectSection import *
import opsvis as opsvis

import opsvis as opsvis
import matplotlib.pyplot as plt
import math as math
import winsound
import os
import os.path
import shutil
import pathlib
import time 
import multiprocessing   



wipe()

# from openseespy.opensees import *

model('basic', '-ndm', 3, '-ndf', 6)

# from RC3D1Story import *
#from mat import *

# from BuildRCrectSection import BuildRCrectSection

# exec(open("mat.py").read())

#ops.mkdir('data3d')

#ops.source('mat.py')
#ops.source('RC3D1Story.py')
exec(open("BeamSecMat.py").read())
# from BuildRCrectSection import BuildRCrectSection
#beam sections
BuildRCrectSection( 1000  ,   0.40  ,   0.60  ,  0.04 ,  20000 , 50000  ,  60000  , 10 , 0.020  , 6   , 4  ,  20  , 20  , 10  , 10)
BuildRCrectSection(   2000   , 0.40  ,   0.60  ,  0.04 ,  20000 , 50000  , 60000   , 12     ,     0.020    ,    7     ,     5     ,    20   ,   20    ,   10    ,   10)
BuildRCrectSection(      3000       ,    0.55   ,  0.70  ,  0.04 ,  30000   ,     50000     ,      60000     ,      22       ,   0.022   ,     11     ,     11    ,     20   ,   20    ,   10    ,   10)
BuildRCrectSection(       4000    ,       0.55  ,   0.70  ,  0.04  , 40000    ,     50000     ,      60000      ,     24      ,    0.022   ,     12     ,     12    ,     20  ,    20   ,    10   ,    10)
# #girder sections
BuildRCrectSection(  101  ,   0.40  ,   0.60  ,  0.04  , 20000   ,     50000      ,     60000     ,      19       ,   0.020    ,    10    ,      9    ,     20  ,    20   ,    10    ,   10)
BuildRCrectSection(       102  ,         0.40  ,   0.60 ,   0.04 ,  20000   ,     50000      ,     60000     ,      20     ,     0.020   ,     10     ,     10    ,     20   ,   20   ,    10  ,     10)
BuildRCrectSection(      103   ,        0.55   ,  0.70  ,  0.04 ,  30000    ,    50000    ,       60000     ,      30     ,     0.022    ,    15     ,     15     ,    20   ,   20    ,   10    ,   10)
BuildRCrectSection(       104   ,       0.55  ,   0.70  ,  0.04 ,  40000    ,     50000     ,     60000    ,       24   ,       0.022  ,      12     ,     12    ,     20   ,   20    ,   10    ,   10)

# Procedure to build RC rectangular section
# def BuildRCrectSection(SecTag, BSec, HSec, cover, coreID, coverID, steelID, totalnumBars, barDiameter, numBarsTop, numBarsBot, nfCoreY, nfCoreZ, nfCoverY, nfCoverZ):
#     coverY = HSec / 2.0
#     coverZ = BSec / 2.0
#     coreY = coverY - cover
#     coreZ = coverZ - cover
#     numBarsInt = totalnumBars - (numBarsTop + numBarsBot) / 2
#     barArea = 3.14 * pow(barDiameter, 2) / 4.0
#     DisBarL = (HSec - 2 * cover) / (numBarsInt + 1)

# GJ = 1.e10
# section('Fiber', SecTag ,'-GJ',GJ)
#     # Define fiber section
# patch('rect', coreID, nfCoreZ, nfCoreY, -coreY, coreZ, -coreY, -coreZ, coreY, -coreZ, coreY, coreZ)
# patch('rect', coverID, 2, nfCoverY, -coverY, coverZ, -coreY, coreZ, coreY, coreZ, coverY, coverZ)
# patch('rect', coverID, 2, nfCoverY, -coreY, -coreZ, -coverY, -coverZ, coverY, -coverZ, coreY, -coreZ)
# patch('rect', coverID, nfCoverZ, 2, -coverY, coverZ, -coverY, -coverZ, -coreY, -coreZ, -coreY, coreZ)
# patch('rect', coverID, nfCoverZ, 2, coreY, coreZ, coreY, -coreZ, coverY, -coverZ, coverY, coverZ)

# layer('straight', steelID, numBarsInt, barArea, -coreY + DisBarL, coreZ, coreY - DisBarL + 0.01, coreZ)
# layer('straight', steelID, numBarsInt, barArea, -coreY + DisBarL, -coreZ, coreY - DisBarL + 0.01, -coreZ)
# layer('straight', steelID, numBarsTop, barArea, coreY, coreZ, coreY, -coreZ)
# layer('straight', steelID, numBarsBot, barArea, -coreY, coreZ, -coreY, -coreZ)


  # some parameters
# colWidth = 0.15
# colDepth = 0.24

# cover = 0.015
# As = 0.000314  # area of no. 7 bars

# # some variables derived from the parameters
# y1 = colDepth / 2.0
# z1 = colWidth / 2.0


# section('Fiber', 3000,'-GJ', 1.e10)

# # Create the concrete core fibers
# patch('rect', 20000, 10, 1, cover - y1, cover - z1, y1 - cover, z1 - cover)

# # Create the concrete cover fibers (top, bottom, left, right)
# patch('rect', 20000, 10, 1, -y1, z1 - cover, y1, z1)
# patch('rect', 20000, 10, 1, -y1, -z1, y1, cover - z1)
# patch('rect', 20000, 2, 1, -y1, cover - z1, cover - y1, z1 - cover)
# patch('rect', 20000, 2, 1, y1 - cover, cover - z1, y1, z1 - cover)

# # Create the reinforcing fibers (left, middle, right)
# layer('straight',  60000, 3, As, y1 - cover, z1 - cover, y1 - cover, cover - z1)
# layer('straight', 60000, 2, As, 0.0, z1 - cover, 0.0, cover - z1)
# layer('straight', 60000, 3, As, cover - y1, z1 - cover, cover - y1, cover - z1)
# # from openseespy.opensees import *

# Define constants
# fc = -52.0e6
# Ec = 33892180000.0
# nu = 0.2
# Gc = Ec / (2.0 * (1 + nu))

# # # Define materials
# uniaxialMaterial('Concrete02', 20000, fc, -0.002801329, -14.5896e6, -0.014006643, 0.1, 4.617798447e6, 1590115.428)

# uniaxialMaterial('Steel02', 60000, 491.5e6, 2.0e11, 0.02, 20, 0.925, 0.15)


# # Define section tags
# BeamSecAggTag = 1000
# GirdSecAggTag = 101
# BeamSecTagFiber = 901
# GirdSecTagFiber = 9001
# matTagTorsion = 70
# Ubig = 1.0e10




# # # Core concrete (confined)
# # uniaxialMaterial('Concrete01', 1, -6.0, -0.004, -5.0, -0.014)

# # # Cover concrete (unconfined)
# # uniaxialMaterial('Concrete01', 2, -5.0, -0.002, 0.0, -0.006)

# # STEEL
# # # Reinforcing steel
# # fy = 60.0;  # Yield stress
# # E = 30000.0;  # Young's modulus
# # #                         tag  fy E0    b
# # uniaxialMaterial('Steel01', 3, fy, E, 0.01)


#  some parameters
# colWidth = 15
# colDepth = 24

# cover = 1.5
# As = 0.60  # area of no. 7 bars

# # some variables derived from the parameters
# y1 = colDepth / 2.0
# z1 = colWidth / 2.0


# section('Fiber', 3000,'-GJ', 1.e10)

# # Create the concrete core fibers
# patch('rect', 20000, 10, 1, cover - y1, cover - z1, y1 - cover, z1 - cover)

# # Create the concrete cover fibers (top, bottom, left, right)
# patch('rect', 20000, 10, 1, -y1, z1 - cover, y1, z1)
# patch('rect', 20000, 10, 1, -y1, -z1, y1, cover - z1)
# patch('rect', 20000, 2, 1, -y1, cover - z1, cover - y1, z1 - cover)
# patch('rect', 20000, 2, 1, y1 - cover, cover - z1, y1, z1 - cover)

# # Create the reinforcing fibers (left, middle, right)
# layer('straight',  60000, 3, As, y1 - cover, z1 - cover, y1 - cover, cover - z1)
# layer('straight', 60000, 2, As, 0.0, z1 - cover, 0.0, cover - z1)
# layer('straight', 60000, 3, As, cover - y1, z1 - cover, cover - y1, cover - z1)



# exec(open("BeamSecMat.py").read())
# exec(open("BuildRCrectSection.py").read())

exec(open("SWsection.py").read())
exec(open("RCStory3D.py").read())
# exec(open("DefineBeamLoading.py").read())


# import  mat.py
# import  RC3D1Story.py

# # Eigenvalue analysis
# eigen(1)
# T1model = 2 * 3.1416 / math.sqrt(ops.eigen(1)[0])
# print(f'T1model={T1model} sec')



#pi=3.14
pi = math.pi
#print(pi)
num_eig = 1
eig = eigen(num_eig)
T=[]
W=[]
for e in range(0,num_eig):
    T.append((2*pi)/(eig[e])**0.5)
    W.append(math.sqrt(eig[e]))
     
print("moodal OK")    
    
# opsvis.plot_model(node_labels=1, element_labels=0)
#opsvis.plot_defo()

# eigen = eigen('-fullGenLapack', 2)
# system('BandGeneral')
# eigen = eigen('-genBandArpack', 10)
# eig = eigen('-genBandArpack', 10)
# eig = eigen(10)
# W1 = math.pow(eigen[0], 0.5)
# print ("W1=", W1)
# W2 = math.pow(eigen[1], 0.5)
# print ("W2=", W2)
# # Apply Rayleigh damping
# xDamp = 0.025
# alphaM = (2*xDamp*W1*W2)/(W1+W2)
# betaKcomm = 2.0*xDamp /(W1+W2)
# betaK=0.0
# betaKinit=0.0
# #rayleigh(alphaM, betaK, betaKinit, betaKcomm)
# rayleigh(alphaM, betaK, betaKinit, betaKcomm)











# # Damping parameters
# xDamp = 0.025
# MpropSwitch = 1.0
# KcurrSwitch = 0.0
# KcommSwitch = 1.0
# KinitSwitch = 0.0
# nEigenI = 1
# nEigenJ = 1
# lambdaN = ops.eigen(nEigenJ)
# lambdaI = lambdaN[nEigenI - 1]
# lambdaJ = lambdaN[nEigenJ - 1]
# omegaI = math.sqrt(lambdaI)
# omegaJ = math.sqrt(lambdaJ)
# alphaM = MpropSwitch * xDamp * (2 * omegaI * omegaJ) / (omegaI + omegaJ)
# betaKcurr = KcurrSwitch * 2.0 * xDamp / (omegaI + omegaJ)
# betaKcomm = KcommSwitch * 2.0 * xDamp / (omegaI + omegaJ)
# betaKinit = KinitSwitch * 2.0 * xDamp / (omegaI + omegaJ)
# rayleigh(alphaM, betaKcurr, betaKinit, betaKcomm)



# Set damping 
# ------------------------------------------------------------------------
# Using mass and committed stiffness proportional damping 
# rayleigh coefficients are calculated based on first two modes 
# xi = 0.025                               # Damping ratio
# Lambda = ops.eigen('-genBandArpack', 2) # Eigen values
# w1 = Lambda[0]**0.5                     # Natural circular frequency for the 1st mode
# w2 = Lambda[1]**0.5                     # Natural circular frequency for the 2nd mode
# alpha = 2.0 * xi * w1 * w2 / (w1 + w2)  # Factor applied to elements or nodes mass matrix
# beta = 2.0 * xi / (w1 + w2)             # Factor applied to elements commited stiffness matrix
# ops.rayleigh(alpha, 0.0, 0.0, beta)     # Assign rayleigh damping

#  # set damping based on first eigen mode
# eigen_1 = op.eigen('-genBandArpack', 1)
# angular_freq = eigen_1[0] ** 0.5
# alpha_m = 0.0
# beta_k = 2 * xi / angular_freq
# beta_k_comm = 0.0
# beta_k_init = 0.0

# op.rayleigh(alpha_m, beta_k, beta_k_init, beta_k_comm)

 # Defining Damping
        # Applying Rayleigh Damping from $xDamp
        # D=$alphaM*M + $betaKcurr*Kcurrent + $betaKcomm*KlastCommit + $beatKinit*$Kinitial
# xDamp = 0.025;								# 5% damping ratio
# alphaM 		= 0.;								# M-prop. damping; D = alphaM*M
# betaKcurr 	= 0.;         						# K-proportional damping;      +beatKcurr*KCurrent
# betaKcomm 	= 2.*xDamp/omega;   				# K-prop. damping parameter;   +betaKcomm*KlastCommitt
# betaKinit 	= 0.;         						# initial-stiffness proportional damping      +beatKinit*Kini
# rayleigh(alphaM,betaKcurr,betaKinit,betaKcomm); # RAYLEIGH damping

modalDamping(0.025)

print("damping OK")



# opsvis.plot_model(node_labels=0, element_labels=0)






# #_______________________________________________________
    
#timeSeries('Linear', tag, '-factor', factor=1.0, '-tStart', tStart=0.0)
# timeSeries('Linear', 1)


# # pattern('Plain', patternTag, tsTag, '-fact', fact)
# # eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint', Py, <Pz>, xL, Px=0.0, '-beamThermal', *tempPts)
# pattern('Plain', 1, 1)
# Wy=-4.526e3

# eleTags=[    1001130, 1000249, 1000347, 1000455, 1000548, 1000650, 1002730, 1300813, 1300991, 
#     1301095, 1301195, 1301292, 1301314, 1001501, 2709, 103615, 102715, 2909, 1002002, 
#     1102070, 1102178, 1002278, 1002370]


# eleLoad('-ele', *eleTags, '-type', '-beamUniform', Wy, 0.0, 0.0)




# # Define beam loading pattern
# # timeSeries('Linear', 1)
# # pattern('Plain', 1, 1)
# # from openseespy.opensees import *

# # Define pattern
# pattern('Plain', 101)

# # List of element IDs
# element_ids = [
#     1001130, 1000249, 1000347, 1000455, 1000548, 1000650, 1002730, 1300813, 1300991, 
#     1301095, 1301195, 1301292, 1301314, 1001501, 2709, 103615, 102715, 2909, 1002002, 
#     1102070, 1102178, 1002278, 1002370
# ]

# # Load magnitude
# load_magnitude = -4.526e3

# # Apply uniform beam load to each element
# for ele_id in element_ids:
#     eleLoad('-ele', ele_id, '-type', '-beamUniform', load_magnitude, 0.0)












num_cores = multiprocessing.cpu_count() 

stime = time.time()

















# Analysis parameters
ops.wipeAnalysis()
ops.constraints('Lagrange')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.test('EnergyIncr', 1.0e-5, 10)
ops.algorithm('ModifiedNewton')
ops.integrator('LoadControl', 0.1)
ops.analysis('Static')
ops.analyze(10)
ops.loadConst('-time', 0.0)

print("Gravity OK")



file_1 = pathlib.Path("timehistory_output3")
if file_1.exists ():
    shutil.rmtree("timehistory_output3")
os.mkdir("timehistory_output3")
recorder('Node', '-file', 'timehistory_output3/disp9901.txt', '-node', 9901, '-dof', 1, 'disp')
recorder('Node', '-file', 'timehistory_output3/disp9930.txt', '-node', 9930, '-dof', 1, 'disp')
recorder('Node', '-file', 'timehistory_output3/disp9929.txt', '-node', 9929, '-dof', 1, 'disp')




# Define earthquake excitation
# mm = 2
# accelX = f'Series -dt 0.01 -filePath R11-900X-dt=0.01-Et=21.99-pga=1.txt -factor {mm * 9.86 / 10}'
# accelZ = f'Series -dt 0.01 -filePath R11-900X-dt=0.01-Et=21.99-pga=1.txt -factor {mm * 9.86 / 10}'

# ops.pattern('UniformExcitation', 3, 1, '-accel', accelX)
# ops.pattern('UniformExcitation', 4, 3, '-accel', accelZ)

dt = 0.01
ops.timeSeries('Path', 10, '-filePath', 'R11-900X-dt=0.01-Et=21.99-pga=1.txt', '-dt', dt, '-factor', 9.86)
ops.pattern('UniformExcitation', 3, 1 ,'-accel', 10, '-fact',1)

ops.timeSeries('Path', 11, '-filePath', 'R11-900X-dt=0.01-Et=21.99-pga=1.txt', '-dt', dt, '-factor', 9.86)
ops.pattern('UniformExcitation', 4, 3 ,'-accel', 11, '-fact',1)

print(f'groundmotion start!. Time: {ops.getTime()}')

Endtime = 21.99
nt= int (Endtime/dt)

ops.wipeAnalysis()

# # THA Solver

wipeAnalysis()
constraints('Transformation')
numberer('RCM')
system('SparseGeneral')
tol = 1.e-4
test('EnergyIncr', 1.e-4, 20)
# test('NormDispIncr', tol, 200, 2)
defaultAlgorithmType = 'KrylovNewton'
algorithm(defaultAlgorithmType)
integrator('Newmark', 0.5, 0.25)
analysis('Transient')


print(f'groundmotion start!. Time: {ops.getTime()}')

# Set parameters
dt = 0.01
dteq = 0.01
q = 3000
record_length = dteq * q
tFinal = 21.99

# Perform the transient analysis
tCurrent = getTime()
ok = 0

# Start timing
begin = time.time()

while ok == 0 and tCurrent < tFinal:
    ok = analyze(1, dt)
    print(getTime())
    
    # if the analysis fails try initial tangent iteration
    if ok != 0:
        print("regular time step failed .. lets try a smaller step and a less stringent test")
        test('NormDispIncr', 1.0e-1, 165, 1)
        ok = analyze(1, dt * 0.005)
        if ok == 0:
            print("that worked .. back to regular time step and test criteria")
        test('NormDispIncr', 1.0e-3, 50)
    
    tCurrent = getTime()

# Print a message to indicate if analysis successful or not
if ok == 0:
    print("################################################")
    print("Transient analysis completed SUCCESSFULLY")
    print("################################################")
else:
    print("################################################")
    print("Transient analysis FAILED")
    print("################################################")

# End timing
endt = time.time()
totaltime = endt - begin
totaltimem = totaltime / 60.0

print(f"Time in hours: {totaltimem / 60.}")
print(f"{totaltimem} is the total time in minutes")







wipe()

# ops.constraints('Lagrange')
# ops.numberer('RCM')
# # ops.system('SparseGeneral')
# ops.system('BandGen')
# ops.test('NormDispIncr', 1.0e-4, 100)
# # ops.test('EnergyIncr', 1.0e-4, 100)
# #ops.algorithm('ModifiedNewton')
# algorithm('KrylovNewton')
# ops.integrator('Newmark', 0.5, 0.25)
# ops.analysis('Transient')
# ops.analyze(nt,dt)

# print(f'groundmotion done!. End Time: {ops.getTime()}')

# THA Solver
# ops.constraints('Transformation')
# ops.numberer('RCM')
# ops.system('BandGeneral')
# tol = 1.e-5
# ops.test('NormDispIncr', tol, 200, 2)
# defaultAlgorithmType = 'KrylovNewton'
# ops.algorithm(defaultAlgorithmType)
# ops.integrator('Newmark', 0.5, 0.25)
# ops.analysis('Transient')

# dt = 0.01
# Nsteps = int(21.99 / dt)
# step1 = 10
# dt1 = dt / step1

# for step in range(1, Nsteps + 1):
#     ok = ops.analyze(int(21.99 / dt1))
#     if ok != 0:
#         print('\n******************* reduced time step dt/n ******************\n')
#         ops.test('NormDispIncr', tol, 2000, 2)
#         for i in range(1, step1 + 1):
#             print(f'\nTrying {defaultAlgorithmType} (dt/n)...\n')
#             ops.algorithm(defaultAlgorithmType)
#             ok = ops.analyze(int(21.99 / dt1))
#             if ok != 0:
#                 print(f'\nTrying Newton with Initial Tangent (dt/n)...\n')
#                 ops.algorithm('Newton', '-initial')
#                 ok = ops.analyze(int(21.99 / dt1))
#             if ok != 0:
#                 print(f'\nTrying Broyden (dt/n)...\n')
#                 ops.algorithm('Broyden', 8)
#                 ok = ops.analyze(int(21.99 / dt1))
#             if ok != 0:
#                 print(f'\nTrying NewtonWithLineSearch (dt/n)...\n')
#                 ops.algorithm('NewtonLineSearch', 0.8)
#                 ok = ops.analyze(int(21.99 / dt1))
#             if ok != 0:
#                 print(f'\nTrying ModifiedNewton (dt/n)...\n')
#                 ops.algorithm('ModifiedNewton')
#                 ok = ops.analyze(int(21.99 / dt1))
#         print('\n******************* normal time step dt ******************\n')
#     ops.test('NormDispIncr', tol, 200, 2)
#     ops.algorithm(defaultAlgorithmType)

# print('\n\nTIME HISTORY ANALYSIS DONE.')
# print(f'groundmotion done!. End Time: {ops.getTime()}')

# Set parameters
# dt = 0.01
# dteq = 0.01
# q = 3000
# record_length = dteq * q
# tFinal = 21.99

# # Perform the transient analysis
# tCurrent = getTime()
# ok = 0

# # Start timing
# begin = time.time()

# while ok == 0 and tCurrent < tFinal:
#     ok = analyze(1, dt)
#     print(getTime())
    
#     # if the analysis fails try initial tangent iteration
#     if ok != 0:
#         print("regular time step failed .. lets try a smaller step and a less stringent test")
#         test('NormDispIncr', 1.0e-1, 165, 1)
#         ok = analyze(1, dt * 0.005)
#         if ok == 0:
#             print("that worked .. back to regular time step and test criteria")
#         test('NormDispIncr', 1.0e-3, 50)
    
#     tCurrent = getTime()

# # Print a message to indicate if analysis successful or not
# if ok == 0:
#     print("################################################")
#     print("Transient analysis completed SUCCESSFULLY")
#     print("################################################")
# else:
#     print("################################################")
#     print("Transient analysis FAILED")
#     print("################################################")

# # End timing
# endt = time.time()
# totaltime = endt - begin
# totaltimem = totaltime / 60.0

# print(f"Time in hours: {totaltimem / 60.}")
# print(f"{totaltimem} is the total time in minutes")



