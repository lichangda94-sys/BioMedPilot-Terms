# How to Add Terms

## Basic Flow

1. Choose the right category for the entry.
2. Create a JSON file that follows `schemas/term_entry.schema.json`.
3. Fill in the required fields: `id`, `category`, `zh`, `en`, and `status`.
4. Add synonyms carefully and only when they are genuinely useful candidates.
5. Avoid copyrighted, proprietary, confidential, or private source material.
6. Run the repository tests.
7. Open a pull request with brief source and review context.

## Category Selection

Use one of the public categories:

- `disease`
- `tissue`
- `biomarker`
- `method`
- `organism`
- `intervention`
- `outcome`
- `database`
- `general`

## File Creation Guidance

- Prefer descriptive IDs such as `disease_thyroid_cancer`.
- Keep one candidate concept per file.
- Use `status` values intended for public contribution review: `example`, `candidate`, or `review_required`.

## Synonym Guidance

- Add synonyms conservatively.
- Do not include overbroad wording that can change search intent.
- Flag uncertain synonym mappings in `review_notes`.

## Source and Compliance

- Avoid copyrighted or proprietary vocabulary dumps.
- Do not copy commercial thesaurus content without permission.
- Do not include patient, institutional, or private BioMedPilot data.
