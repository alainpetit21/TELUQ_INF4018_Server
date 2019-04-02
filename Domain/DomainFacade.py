from Domain.GameCommand import GameCommand
from Domain.RawSensorsCommand import RawSensorsCommand
from CrossCuttingConcerns.Helpers import SingletonDecorator


@SingletonDecorator
class DomainFacade(object):

    def __init__(self):
        # self.lstGameCommand: list = []
        # self.lstRawSensorsCommand: list = []
        self.dicPerUser: dict = {"UserEmpty" : ([], [])}

    def AddUser(self, strIdUser:str):
        self.dicPerUser[strIdUser]= ([], [])

    def AddGameCommand(self, strIdUser:str, objGameCommand:GameCommand):
        self.dicPerUser[strIdUser][0].append(objGameCommand)

    def AddRawSensorsCommand(self, strIdUser:str, objRawSensorsCommand: RawSensorsCommand):
        self.dicPerUser[strIdUser][1].append(objRawSensorsCommand)
