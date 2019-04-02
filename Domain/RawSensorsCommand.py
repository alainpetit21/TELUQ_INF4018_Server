class RawSensorsCommand(object):

    def __init__(self, nRotationRoll, nRotationPitch, nAcceleratingX, nAcceleratingY, nAcceleratingZ, nAcceleratingRotationRoll):
        self.nRotationRoll= nRotationRoll
        self.nRotationPitch= nRotationPitch

        self.nAcceleratingX= nAcceleratingX
        self.nAcceleratingY= nAcceleratingY
        self.nAcceleratingZ= nAcceleratingZ

        self.nAcceleratingRotationRoll= nAcceleratingRotationRoll

    def GetRotationalSensorByDirectionalIdx(self, nDirectionalIdx):
        arDirectionalIdx = [self.nRotationRoll, self.nRotationPitch, -self.nRotationRoll, -self.nRotationPitch]
        return arDirectionalIdx[nDirectionalIdx]

    def GetAccelerationSensorByDirectionalIdx(self, nDirectionalIdx):
        arDirectionalIdx= [self.nAcceleratingX, self.nAcceleratingY, -self.nAcceleratingX, -self.nAcceleratingY];

        return arDirectionalIdx[nDirectionalIdx];
