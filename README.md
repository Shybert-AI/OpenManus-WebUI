![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
![GitHub forks](https://img.shields.io/github/forks/Shybert-AI/OpenManusAI)
![GitHub Repo stars](https://img.shields.io/github/stars/Shybert-AI/OpenManusAI)
![GitHub](https://img.shields.io/github/license/Shybert-AI/OpenManusAI)

[English](README_en.md) | 简体中文

# OpenManusX 🙋

Manus和OpenManus 非常棒，非常优秀的工作，目前OpenManus暂无前端，于是本人花了2小时开发基于Flask框架一个简单的WebUI。 🛫！

##  本项目实质上是通过flask框架构建一个前端页面，进行OpenManus的调用，并对OpenManus生成的文件进行预览。
# News
- 2025-01-26 最小化简化网页资源包，gzip资源小于2MB。简化视频数据，数据大小减半
- 2025-02-09 增加ASR入口、增加一键切换形象。
- 2025-02-27 优化渲染、去除参照视频，目前只需要一段视频即可生成。

## 📑 前端页面需要不断的优化，计划
- OpenManusX
    - [x] 开源初版WebUI
    - [ ] OpenManusX文件预览区及保存区需要支持pdf、ppt、word、excel、代码高亮的预览;    
    - [ ] 大模型对话框需要对输出进行美化，需要对OpenManus运行log优化显示，如代码高亮等;    
    - [ ] 不断打磨前后端，完成自动化执行。


<div align="center">
    <img src="./assets/1.jpg">
</div>
<div align="center">
    <img src="./assets/2.jpg">
</div>
<div align="center">
    <img src="./assets/3.jpg">
</div>

用 OpenManusX 开启你的智能体之旅吧！  


## 安装指南

1. 创建新的 conda 环境：

```bash
conda create -n OpenManusX python=3.12
conda activate OpenManusX
```

2. 克隆仓库：先进行安装OpenManus，后续安装OpenManusX的webUI就快的很

```bash
https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```
4.安装OpenManusAI,2种方式

```bash
# 1 仓库安装
https://github.com/Shybert-AI/OpenManusAI.git
cd OpenManus
pip install -r requirements.txt

# 2 将OpenManus的运行代码拷贝到app.py文件

async def main(prompt):
    agent = Manus()
    await agent.run(prompt)

```

## 配置说明

OpenManusX配置API和OpenManus一样，需要配置使用的 LLM API，请按以下步骤设置，本文配置deepseek R1模型：

1. 在 `config` 目录创建 `config.toml` 文件（可从示例复制）：

```bash
cp config/config.example.toml config/config.toml
```

2. 编辑 `config/config.toml` 添加 API 密钥和自定义设置：

```toml
## Global LLM configuration
#[llm]
#model = "deepseek-chat"
#base_url = "https://api.deepseek.com/v1"
#api_key = "sk-xxxxxxxxxxxx"
#max_tokens = 4096
#temperature = 0.6
#
## Optional configuration for specific LLM models
#[llm.vision]
#model = "deepseek-chat"
#base_url = "https://api.deepseek.com/v1"
#api_key = "sk-xxxxxxxxxxxx"


# Global LLM configuration
[llm]
model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
base_url = "https://api.siliconflow.cn/v1/"
api_key = "sk-xxxxxxxxxxxxxxxxxx"
max_tokens = 4096
temperature = 0.6

# Optional configuration for specific LLM models
[llm.vision]
model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
base_url = "https://api.siliconflow.cn/v1/"
api_key = "sk-xxxxxxxxxxxxxxxxxx"
```

## 快速启动

一行命令运行 OpenManusX：

```bash
python app.py
```

## 致谢

特别感谢 [OpenManus](https://github.com/mannaandpoem/OpenManus)
和 [browser-use](https://github.com/browser-use/browser-use) 为本项目提供的基础支持！

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Shybert-AI/OpenManus-WebUI&type=Date)](https://star-history.com/#Shybert-AI/OpenManus-WebUI&Date)
