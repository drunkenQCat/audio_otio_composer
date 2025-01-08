# 音频到达芬奇 OTIO 生成器

该工程的目的是从一个包含多个 WAV 音频文件的文件夹中，生成一份达芬奇 (DaVinci) 可用的 OpenTimelineIO (OTIO) 文件。

[English](README_EN.md)
## 安装

1. 安装包管理器 `uv`：

    ```bash
    pip install uv
    ```

2. 同步虚拟环境：

    ```bash
    uv sync
    ```

## 运行

使用以下命令运行脚本：
```python
uv run otio_generator.py
```

## 项目背景

本项目借鉴自 [IgorRidanovic/randomOTIO](https://github.com/IgorRidanovic/randomOTIO)，旨在简化从音频文件生成 OTIO 文件的流程，方便在达芬奇中进行后期制作。

## 许可证

本项目采用 [MIT 许可证](LICENSE) 进行许可。