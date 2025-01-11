from custom_node_helper import CustomNodeHelper

CHECKPOINTS = [
    "SDXL-TURBO/sd_xl_turbo_1.0_fp16.safetensors"
]

class My_Custom_Checkpoints(CustomNodeHelper):
    @staticmethod
    def models():
        return CHECKPOINTS

    @staticmethod
    def add_weights(weights_to_download, node):
        # This will add your weights regardless of node type
        weights_to_download.extend(CHECKPOINTS)
    
    @staticmethod
    def weights_map(base_url):
        return {
            "SDXL-TURBO/sd_xl_turbo_1.0_fp16.safetensors": {
                "url": "https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0_fp16.safetensors?download=true",
                "dest": "ComfyUI/models/checkpoints/SDXL-TURBO"
            }
        } 