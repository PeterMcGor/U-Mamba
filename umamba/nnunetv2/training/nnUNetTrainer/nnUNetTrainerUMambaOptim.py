from nnunetv2.training.nnUNetTrainer.nnUNetTrainerUMambaBot import nnUNetTrainerUMambaBot
from nnunetv2.training.nnUNetTrainer.nnUNetTrainerUMambaEnc import nnUNetTrainerUMambaEnc
from nnunetv2.training.nnUNetTrainer.nnUNetTrainerUMambaEncNoAMP import nnUNetTrainerUMambaEncNoAMP
from nnunetv2.training.nnUNetTrainer.variants.optimizer.nnUNetTrainerAdam import nnUNetTrainerAdam3en4

class nnUNetTrainerUMambaBotAdam3en4(nnUNetTrainerUMambaBot,nnUNetTrainerAdam3en4):
    pass

class nnUNetTrainerUMambaEncAdam3en4(nnUNetTrainerUMambaEnc,nnUNetTrainerAdam3en4):
    pass

class nnUNetTrainerUMambaEncNoAMPAdam3en4(nnUNetTrainerUMambaEncNoAMP,nnUNetTrainerAdam3en4):
    pass