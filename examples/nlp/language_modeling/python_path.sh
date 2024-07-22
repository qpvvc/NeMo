#!/bin/bash

# 获取脚本所在的目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 构建nemo_path和megatron_path的绝对路径
NEMO_PATH=$(realpath "$SCRIPT_DIR/../../../")
MEGATRON_PATH=$(realpath "$SCRIPT_DIR/../../../../Megatron-LM")

# 更新PYTHONPATH环境变量
export PYTHONPATH="$NEMO_PATH:$MEGATRON_PATH:$PYTHONPATH"

# 如果/opt/megatron-lm在PYTHONPATH中，则移除
export PYTHONPATH=$(echo $PYTHONPATH | sed -e 's|:/opt/megatron-lm||' -e 's|/opt/megatron-lm:||' -e 's|/opt/megatron-lm||')

# 打印当前的PYTHONPATH，用于调试（可选）
echo $PYTHONPATH