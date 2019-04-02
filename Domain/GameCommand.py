class GameCommand(object):

    def __init__(self, nTransformationX, nTransformationY, nTransformationZ, isTeleportingX, isTeleportingZ, isDoingABarrelRoll):
        self.nTransformationX = nTransformationX
        self.nTransformationY = nTransformationY
        self.nTransformationZ = nTransformationZ

        self.isTeleportingX = isTeleportingX
        self.isTeleportingZ = isTeleportingZ

        self.isDoingABarrelRoll = isDoingABarrelRoll

