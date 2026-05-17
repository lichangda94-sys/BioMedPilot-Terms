# BioMedPilot-Terms

BioMedPilot-Terms 是面向 BioMedPilot 相关生物医学词条贡献的公开 schema 与示例仓库。

## 核心说明

- 这是公开词条贡献规范和示例仓库。
- 不是 BioMedPilot 的完整私有词库。
- 不是生产级核心检索引擎。
- 只开放 schema、示例、贡献规则、校验逻辑。
- 已有私有工作和核心词库继续保留在私有资源中。

本仓库用于帮助外部贡献者理解如何提交候选词条、候选同义词、缩写和数据库检索片段，而不是公开 BioMedPilot 的完整生产资源。

## 贡献者可以提交的内容

- 中英双语生物医学候选词条
- 候选同义词
- 候选缩写
- 疾病、组织、方法、标志物等类别词条
- 数据库特定的候选 query fragment
- 规范化说明、来源说明、review notes

## 严禁提交的内容

- 患者数据
- 机构内部私有数据
- 受限制或专有词库内容
- 未获许可的商业术语库内容
- 完整受版权保护的数据库内容
- API 凭据、Token、密码、证书
- 用户检索日志
- BioMedPilot 私有词库与私有搜索资产
- 私有 prompt、排序逻辑、路由逻辑、商业检索逻辑

## 安装与校验

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## 边界说明

公开仓库可包含：

- schema
- 示例词条
- 示例 query fragment
- 贡献规则
- 校验测试
- 公开文档

私有 BioMedPilot 资源继续保留：

- 完整词库
- 高价值核心词映射
- 生产级 query builder
- 中文意图解析
- AI prompts
- 检索排序与评分
- 数据库路由逻辑
- 商业搜索逻辑
- 用户日志与私有反馈数据
- 高级词汇资产

更多细节见 [docs/private_asset_boundary.md](docs/private_asset_boundary.md)。
