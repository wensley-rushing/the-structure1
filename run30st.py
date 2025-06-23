import math
from math import *

import xara
import veux

import os
import shutil
import pathlib
import time 
import multiprocessing   

# from RC3D1Story import RC3D1Story
# from mat import mat
# from RC3D1Story import *
from BuildRCrectSection import BuildRCrectSection
from SWsection import SWsection
from RCstory3D import RCstory3D

def BeamSecMat(model):
    ################## nominal concrete compressive strength ##############
    fc =   -52.e6
    Ec =  33892180000
    nu = 0.2
    Gc =  33892180000/(2.*(1+0.2))
    #BEAM IN ALL STORIES  B40x60
    fc1C = -54.5896e6
    eps1C = -0.002801329
    fc2C = -14.5896e6
    eps2C =  -0.014006643

    epsc0 = 0.002801329
    #tensile - Strength properties
    ftC = 4.617798447e6
    ftU = 0.000224286
    Ets = 0.000224286/0.002801329
    MatIDconcCoreB1 = 20000
    model.uniaxialMaterial( 'Concrete02' , 20000 , -54.5896e6 , -0.002801329 , -14.5896e6 , -0.014006643 , 0.1 , 4.617798447e6 , 0.08006414098451128)
    #BEAM IN STORIES 1-20 B55x70
    fc1C = -59.59e6
    eps1C = -0.003879712
    fc2C = -19.59e6
    eps2C =  -0.019398558

    #tensile - Strength properties
    ftC = 4.824659962e6
    ftU = 0.000224286
    Ets = 0.000224286/0.003879712
    MatIDconcCoreB2 = 30000
    model.uniaxialMaterial( 'Concrete02' , 30000 , -59.59e6 , -0.003879712 , -19.59e6 , -0.019398558 , 0.1 , 4.824659962e6 , 0.057809961151755594)
    #BEAM IN STORIES 21-30 B55x70
    fc1C = -58.07e6
    eps1C = -0.003551909
    fc2C = -18.07e6
    eps2C = -0.017759547

    epsc0 = 0.003551909
    #tensile - Strength properties
    ftC = 4.762729653e6
    ftU = 0.000224286
    Ets = 0.000224286/0.003551909
    MatIDconcCoreB3 = 40000
    model.uniaxialMaterial( 'Concrete02' , 40000 , -58.07e6 , -0.003551909 , -18.07e6 , -0.017759547 , 0.1 , 4.762729653e6 , 0.06314519882125359)
    #UNCONFINED CONCRETE
    fc1C = -52.e6
    eps1C = -0.002242857
    fc2C = -12.e6
    eps2C = -0.0036

    epsc0 = 0.002242857
    ftC = 4.506939094e6
    ftU = 0.000224286
    Ets = 0.000224286/0.002242857
    MatIDconcCoreB4 = 50000
    model.uniaxialMaterial( 'Concrete02' , 50000 , -52.e6 , -0.002242857 , -12.e6 , -0.0036 , 0.1 , 4.506939094e6 , 0.1000001337579703)
    Fy = 491.5e6
    Es = 200.0e9
    Bs = 0.02
    Bs = 0.02
    cR1 = 0.925
    cR2 = 0.15
    MatIDSteel = 60000
    model.uniaxialMaterial( 'Steel02' , 60000 , 491.5e6 , 200.0e9 , 0.02 , 20 , 0.925 , 0.15)


if __name__ == "__main__":

    model = xara.Model('basic', '-ndm', 3, '-ndf', 6)

    BeamSecMat(model)
    # beam sections
    BuildRCrectSection(model,  1000  ,   0.40  ,   0.60  ,  0.04 ,  20000 , 50000  ,  60000  , 10 , 0.020  , 6   , 4  ,  20  , 20  , 10  , 10)
    BuildRCrectSection(model,  2000   , 0.40  ,   0.60  ,  0.04 ,  20000 , 50000  , 60000   , 12     ,     0.020    ,    7     ,     5     ,    20   ,   20    ,   10    ,   10)
    BuildRCrectSection(model,  3000       ,    0.55   ,  0.70  ,  0.04 ,  30000   ,     50000     ,      60000     ,      22       ,   0.022   ,     11     ,     11    ,     20   ,   20    ,   10    ,   10)
    BuildRCrectSection(model,  4000    ,       0.55  ,   0.70  ,  0.04  , 40000    ,     50000     ,      60000      ,     24      ,    0.022   ,     12     ,     12    ,     20  ,    20   ,    10   ,    10)
    # girder sections
    BuildRCrectSection(model,   101  ,   0.40  ,   0.60  ,  0.04  , 20000   ,     50000      ,     60000     ,      19       ,   0.020    ,    10    ,      9    ,     20  ,    20   ,    10    ,   10)
    BuildRCrectSection(model,        102  ,         0.40  ,   0.60 ,   0.04 ,  20000   ,     50000      ,     60000     ,      20     ,     0.020   ,     10     ,     10    ,     20   ,   20   ,    10  ,     10)
    BuildRCrectSection(model,       103   ,        0.55   ,  0.70  ,  0.04 ,  30000    ,    50000    ,       60000     ,      30     ,     0.022    ,    15     ,     15     ,    20   ,   20    ,   10    ,   10)
    BuildRCrectSection(model,        104   ,       0.55  ,   0.70  ,  0.04 ,  40000    ,     50000     ,     60000    ,       24   ,       0.022  ,      12     ,     12    ,     20   ,   20    ,   10    ,   10)

    SWsection(model)
    RCstory3D(model)
    # exec(open("DefineBeamLoading.py").read())

    veux.serve(veux.render(model))
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
    eig = model.eigen(num_eig)
    T=[]
    W=[]
    for e in range(0,num_eig):
        T.append((2*pi)/(eig[e])**0.5)
        W.append(math.sqrt(eig[e]))
        
    print("modal OK")    
        
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

    model.modalDamping(0.025)

    print("damping OK")


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

    model.wipeAnalysis()

    # # THA Solver
    model.constraints('Transformation')
    model.numberer('RCM')
    model.system('SparseGeneral')
    tol = 1.e-4
    test('EnergyIncr', 1.e-4, 20)
    # test('NormDispIncr', tol, 200, 2)
    defaultAlgorithmType = 'KrylovNewton'
    model.algorithm(defaultAlgorithmType)
    model.integrator('Newmark', 0.5, 0.25)
    model.analysis('Transient')


    print(f'groundmotion start!. Time: {ops.getTime()}')

    # Set parameters
    dt = 0.01
    dteq = 0.01
    q = 3000
    record_length = dteq * q
    tFinal = 21.99

    # Perform the transient analysis
    tCurrent = model.getTime()
    ok = 0

    # Start timing
    begin = time.time()

    while ok == 0 and tCurrent < tFinal:
        ok = model.analyze(1, dt)
        print(model.getTime())
        
        # if the analysis fails try initial tangent iteration
        if ok != 0:
            print("regular time step failed .. lets try a smaller step and a less stringent test")
            model.test('NormDispIncr', 1.0e-1, 165, 1)
            ok = model.analyze(1, dt * 0.005)
            if ok == 0:
                print("that worked .. back to regular time step and test criteria")
            model.test('NormDispIncr', 1.0e-3, 50)
        
        tCurrent = model.getTime()

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
