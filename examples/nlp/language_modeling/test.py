import sys
sys.path.remove('/opt/megatron-lm')
sys.path.insert(0,'/workspace/workspace/NeMo')  
sys.path.insert(0,'/workspace/workspace/Megatron-LM')
# sys.path.append('/workspace/workspace/Megatron-LM')  

for idx, p in enumerate(sys.path):
    print(f"{idx}: {p}")

print(sys.executable)
import google.protobuf
print(google.protobuf.__file__)
print(google.protobuf.__version__)

# import torch
# # 重置CUDA状态
# torch.cuda.init()
# # 调用cudaGetDeviceCount()函数
# device_count = torch.cuda.device_count()
# print(device_count)

# from megatron.core import mpu, tensor_parallel
# from megatron.core.datasets.blended_megatron_dataset_builder import BlendedMegatronDatasetBuilder
# from megatron.core.datasets.retro.config import RetroGPTChunkDatasets
# from megatron.core.datasets.retro.query.multi_split_gpt_dataset import (
#     MultiSplitGPTDataset,
#     MultiSplitGPTDatasetConfig,
# )
# from megatron.core.datasets.retro.query.retro_dataset import get_retro_datasets
# from megatron.core.datasets.utils import get_blend_from_list
# from megatron.core.models.retro import RetroConfig
# from megatron.core.datasets import bert_dataset
# from megatron.core.datasets.retro.query import multi_split_gpt_dataset
# from megatron.core import datasets

# from nemo.collections.nlp.models.language_modeling import BERTLMModel
# # from nemo.utils import app_state

# import inspect
# # import sys

# source_file = inspect.getsourcefile(BERTLMModel)
# print("BERTLMModel:", source_file)


from nemo.collections import nlp as nemo_nlp


list = nemo_nlp.modules.get_pretrained_lm_models_list()

print(list)