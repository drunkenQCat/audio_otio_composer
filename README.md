# 音频到达芬奇 OTIO 生成器  

该工程的目的是从一个包含多个 WAV 音频文件的文件夹中，生成一份达芬奇 (DaVinci) 可用的 OpenTimelineIO (OTIO) 文件。

[English](README_EN.md)

---

## 安装  

1. 安装包管理器 `uv`：  

    ```bash  
    pip install uv  
    ```  

2. 同步虚拟环境：  

    ```bash  
    uv sync  
    ```  

---

## 运行  

使用以下命令运行脚本：  

```bash  
uv run otio_generator.py  
```  

不带参数默认会读取test_data中的文件。可选参数：
```python
@click.option(
    "--path",
    "-p",
    default="test_data",
    help="输入数据路径，通常是包含音频文件的文件夹路径。",
)
@click.option("--output", "-o", help="输出文件名，用于生成 OTIO 时间轴文件。")
```
```
```

---

## 项目背景  

本项目借鉴自 [IgorRidanovic/randomOTIO](https://github.com/IgorRidanovic/randomOTIO)，旨在简化从音频文件生成 OTIO 文件的流程，为后期制作人员提供高效的工具链支持。  

工程特色：  
- **自动化时间线生成**：从 WAV 音频中读取元数据，自动创建带有精确时间码和音频范围的 OTIO 文件。  
- **对接达芬奇**：生成的 OTIO 文件可以直接导入达芬奇进行后期制作，减少手动调整的工作量。  
- **元数据深度解析**：支持读取 WAV 文件中的时间偏移、角色信息、通道数，映射到达芬奇时间线中的对应字段。  

---

## 准备音频数据  

**重要提醒：**  
在使用本工具之前，请确保准备的wav音频文件符合以下元数据要求，否则可能导致生成的时间线错误或不符合预期。  

### 必需的音频元数据  
工具依赖以下元数据生成 OTIO 文件：  
1. **时间码（time reference）**  
    - 用于标记音频的起始偏移时间。如果没有时间码，所有音频都会从时间线的零点开始，生成的时间线会出现异常（如所有音频垂直堆叠）。  

### 可选的音频元数据  
1. **艺术家信息（artist/角色名）**  
    - 将被映射为达芬奇时间线中的轨道名称。  

---

## 如何生成时间码  

如果 WAV 文件缺少时间码（time reference），需要手动添加时间码。以下是在 Reaper 中生成时间码的步骤：  

1. 在批量生成音频 Item 时：  
    - **取消**：`Preserve start offset` 和 `Preserve metadata`。  
    - **勾选**：`Add new metadata`。  

2. 生成的 WAV 文件将自动把每个音频在时间线上的偏移量写入 bext.time reference。  

**其他元数据生成方式：**  
- 艺术家信息和通道数可以根据实际需求自行研究和编辑 WAV 文件的元数据。  

---

## 许可证  

本项目采用 [MIT 许可证](LICENSE) 进行许可。  

