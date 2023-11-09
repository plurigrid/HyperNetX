# sheaf_diffusion_adapter.py

class SheafDiffusionAdapter:
    def __init__(self, sheaf_diffusion):
        self.sheaf_diffusion = sheaf_diffusion

    def update_state(self, delta_F):
        self.sheaf_diffusion.update_state(delta_F)