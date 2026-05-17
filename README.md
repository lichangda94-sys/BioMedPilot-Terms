# BioMedPilot-Terms

BioMedPilot-Terms is a public example and schema repository for biomedical term contribution related to BioMedPilot.

This repository does not contain the full private BioMedPilot vocabulary. It does not publish private high-value term libraries, production query logic, prompt logic, ranking logic, routing logic, or commercial search assets.

The files here are intended to help outside contributors understand:

- how to add biomedical term candidates
- how to structure Chinese-English medical vocabulary entries
- how to submit candidate synonyms and abbreviations
- how to submit database-specific query fragment candidates
- how term entries are reviewed
- how contributed material may later be integrated into BioMedPilot public or private resources

Examples in this repository are examples only. They are not production coverage and should not be interpreted as the full BioMedPilot vocabulary.

## Short Chinese Intro

这是 BioMedPilot 的公开词条贡献规范和示例仓库，不是完整私有词库，也不是生产级核心检索引擎。这里仅开放 schema、示例、贡献规则和校验逻辑，现有私有工作与核心词库继续保留在私有资源中。

## What Contributors Can Add

- Chinese-English biomedical term candidates
- candidate synonyms
- candidate abbreviations
- disease, tissue, method, biomarker, organism, intervention, outcome, database, or general entries
- database-specific query fragment candidates
- review notes and source notes that support normalization

## What Must Not Be Submitted

- patient data
- private institutional data
- copied proprietary vocabulary
- commercial thesaurus content without permission
- full copyrighted database content
- API keys
- user query logs
- private BioMedPilot assets
- private prompts
- private search or routing logic
- private ranking or scoring logic

## Repository Layout

```text
BioMedPilot-Terms/
  schemas/
  examples/
  docs/
  tests/
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Validation

```bash
pytest
```

## Contribution Terms

Contributions are voluntary and are submitted as candidate resources. Maintainers may review, modify, normalize, accept, reject, or integrate contributed material into BioMedPilot public or private resources.

Contributed material may be used in BioMedPilot and related editions, including free, commercial, AI-assisted, cloud-based, premium, or future versions. A contribution does not create any employment, contractor, compensation, equity, ownership, or revenue-sharing relationship.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## BioMedPilot Integration Boundary

This repository may contain:

- schemas
- a few example terms
- a few example query fragments
- contribution rules
- validation tests
- public review documentation

BioMedPilot private resources continue to retain:

- the full vocabulary
- core high-value term mappings
- the production query builder
- Chinese intent parsing
- AI prompts
- search ranking and scoring
- database routing logic
- commercial search logic
- user query logs
- private feedback data
- premium vocabulary assets

See [docs/private_asset_boundary.md](docs/private_asset_boundary.md) for the explicit boundary.

## License

This repository is licensed under Apache-2.0. See [LICENSE](LICENSE).
