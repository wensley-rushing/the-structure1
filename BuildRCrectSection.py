
# Procedure to build RC rectangular section
def BuildRCrectSection(m, SecTag, BSec, HSec, cover, coreID, coverID, steelID, totalnumBars, barDiameter, numBarsTop, numBarsBot, nfCoreY, nfCoreZ, nfCoverY, nfCoverZ):
    coverY = HSec / 2.0
    coverZ = BSec / 2.0
    coreY = coverY - cover
    coreZ = coverZ - cover
    numBarsInt = int( totalnumBars - (numBarsTop + numBarsBot) / 2)
    barArea = 3.14 * pow(barDiameter, 2) / 4.0
    DisBarL = (HSec - 2 * cover) / (numBarsInt + 1)

    GJ = 1.e10
    m.section('Fiber', SecTag ,'-GJ', GJ)
    # Define fiber section
    m.patch('quad', coreID, nfCoreZ, nfCoreY, -coreY, coreZ, -coreY, -coreZ, coreY, -coreZ, coreY, coreZ)
    m.patch('quad', coverID, 2, nfCoverY, -coverY, coverZ, -coreY, coreZ, coreY, coreZ, coverY, coverZ)
    m.patch('quad', coverID, 2, nfCoverY, -coreY, -coreZ, -coverY, -coverZ, coverY, -coverZ, coreY, -coreZ)
    m.patch('quad', coverID, nfCoverZ, 2, -coverY, coverZ, -coverY, -coverZ, -coreY, -coreZ, -coreY, coreZ)
    m.patch('quad', coverID, nfCoverZ, 2, coreY, coreZ, coreY, -coreZ, coverY, -coverZ, coverY, coverZ)

    m.layer('straight', steelID, numBarsInt, barArea, -coreY + DisBarL, coreZ, coreY - DisBarL + 0.01, coreZ)
    m.layer('straight', steelID, numBarsInt, barArea, -coreY + DisBarL, -coreZ, coreY - DisBarL + 0.01, -coreZ)
    m.layer('straight', steelID, numBarsTop, barArea, coreY, coreZ, coreY, -coreZ)
    m.layer('straight', steelID, numBarsBot, barArea, -coreY, coreZ, -coreY, -coreZ)
