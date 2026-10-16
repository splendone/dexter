# 数据集/代码库许可核查(填卡片库"待核"项)

> 核查时点:2026-09-27 班。方法:GitHub 仓库页/侧栏 + raw LICENSE 原文 + GitHub API
> license 字段交叉验证;HuggingFace 经数据集 API 读卡。对应 README.md 表中
> OXE / DROID / ALOHA / MimicGen 系四行"待核"。事实均读原文核实;「含义」列
> 是**判断**;商用边界属法律问题,按宪法转介专业人士。

| 数据集 | 仓库 | 许可 | 出处 URL | 对委托人研究使用的含义(判断) | 置信度 |
|---|---|---|---|---|---|
| Open X-Embodiment | google-deepmind/open_x_embodiment | 代码 **Apache-2.0**;非代码材料(数据)**CC-BY 4.0**(README「License and Disclaimer」分列) | https://raw.githubusercontent.com/google-deepmind/open_x_embodiment/HEAD/LICENSE ; https://raw.githubusercontent.com/google-deepmind/open_x_embodiment/HEAD/README.md (L63-73) | 宽松组合,聚合层研究与复用基本无障碍;但聚合内 60 个源数据集各受原许可约束,「整库商用」前需逐源看,不能只看本仓库声明 | 高(README 原文 + GitHub API 字段一致) |
| DROID(代码) | droid-dataset/droid | **无 LICENSE 文件,未给许可** | https://github.com/droid-dataset/droid (侧栏无许可、文件列表无 LICENSE);https://api.github.com/repos/droid-dataset/droid (license: null) | 无许可=默认保留所有权利:可看可跑于私有研究,但**复用/再分发官方代码无授权依据**,需要时联系作者 | 高(页面与 API 双证) |
| DROID(数据) | HuggingFace KarlP/droid | **CC BY 4.0**(数据卡 license 字段) | https://huggingface.co/datasets/KarlP/droid (API cardData.license=cc-by-4.0) | 数据按 CC BY 4.0 可宽松使用(含商用),署名即可;但这是单卡声明,未在官方论文/官网交叉验证 | 中(单一来源) |
| ALOHA | tonyzhaozh/aloha | **MIT**(Copyright (c) 2023 Tony Z. Zhao) | https://raw.githubusercontent.com/tonyzhaozh/aloha/HEAD/LICENSE | 宽松:硬件+软件均可自由使用/修改/再分发,保留版权与许可声明即可 | 高(读过 LICENSE 原文) |
| Mobile ALOHA | MarkFzp/mobile-aloha(项目站 mobile-aloha.github.io 指向) | **MIT**(Copyright (c) 2023 Tony Z. Zhao) | https://raw.githubusercontent.com/MarkFzp/mobile-aloha/HEAD/LICENSE ; https://github.com/MarkFzp/mobile-aloha | 同 ALOHA,宽松;整身遥操作栈可自由复用 | 高(读过 LICENSE 原文) |
| MimicGen | NVlabs/mimicgen_environments | 代码 **NVIDIA Source Code License**(自定义,非 OSI 标准开源);**数据集 CC-BY 4.0**(README License 节) | https://raw.githubusercontent.com/NVlabs/mimicgen_environments/HEAD/LICENSE ; https://github.com/NVlabs/mimicgen_environments | 用合成演示数据走 CC BY 4.0 较稳;代码本身受 NVIDIA 自定义条款约束(非商用/再分发限制以许可原文为准),勿默认按 MIT/Apache 处理 | 高(读过 LICENSE 原文与 README) |
| DexMimicGen | NVlabs/dexmimicgen | 代码 **NVIDIA Source Code License**;**数据集 CC-BY 4.0**(README License 节) | https://raw.githubusercontent.com/NVlabs/dexmimicgen/HEAD/LICENSE ; https://github.com/NVlabs/dexmimicgen | 同 MimicGen:数据宽松、代码受自定义条款约束;60 人演→2 万灵巧演示这条合成路线的数据可放心取用 | 高(读过 LICENSE 原文与 README) |
| **GRAB**(2026-09-30 补) | GRAB 官网(abs 页指向,未打开) | **研究用途**(abs 页逐字 "available for **research purposes**") | https://arxiv.org/abs/2008.11200 | **禁商用**;可作研究复现,再分发/衍生条款须看官网 LICENSE(未逐字核)→ 待核点 | 中(abs 页自述;官网条款未核) |
| **UMI**(2026-09-30 补) | umi-gripper.github.io | **开源**(软硬件均放;**具体类型未核**) | https://umi-gripper.github.io/ ; https://arxiv.org/abs/2402.10329 | 定位为采集框架,引用其数据/硬件前须查具体许可;**不得默认 MIT** | 低(仅 "open-sourced" 字样) |

## 待核余项

- DROID 数据许可的官方级出处(论文或 droid-dataset.github.io 声明)未取得:
  官网页面 grep "license/CC BY" 无命中(可能 JS 渲染),HF KarlP/droid 卡是
  目前唯一许可声明。已试:https://droid-dataset.github.io/ 、
  https://huggingface.co/api/datasets/droid/droid(返回空对象,疑似无此数据集名)。
- OXE 聚合内各源数据集(RLDS 化前的原始许可)未逐一核查,超出本次范围。
- **GRAB 官网 LICENSE 细条款**(再分发/衍生)未逐字核(2026-09-30 补记,低优先)。
- **UMI 软硬件许可类型**未核(2026-09-30 补记,低优先)。
- ~~GRAB 数据集许可(license-check 未覆盖)~~ → **✅ 已补(2026-09-30)**:
  GRAB 为**研究用途(禁商用)**,与 RH20T-NC / AgiBot World 同档;详见上表。
