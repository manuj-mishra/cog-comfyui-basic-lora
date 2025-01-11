from custom_node_helper import CustomNodeHelper

LORAS = [
    "princess_xl_v2.safetensors"
]

class My_Custom_Loras(CustomNodeHelper):
    @staticmethod
    def models():
        return LORAS

    @staticmethod
    def add_weights(weights_to_download, node):
        # This will add your weights regardless of node type
        weights_to_download.extend(LORAS)
    
    @staticmethod
    def weights_map(base_url):
        return {
            "princess_xl_v2.safetensors": {
                "url": "https://civitai.com/api/download/models/244808?type=Model&format=SafeTensor",
                "dest": "ComfyUI/models/loras"
            }
        } 