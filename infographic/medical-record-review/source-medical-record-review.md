# Health Records an Agent Can Audit

*A two-layer skill for AI-assisted review of personal and family medical records: a generic procedure, project-local facts, and no clinical authority.*

**Source:** the `medical-record-review` skill, extracted on 21 October 2026 from a private record set that had accumulated several years of lab rounds, prescriptions, imaging, and conflicts. The skill is the how; this article is the why.

**Thesis:** the value of an agent in this domain is not cleverer analysis. It is a procedure that **refuses to guess** — one that stops on conflict, cites what it used, separates record from inference, and cannot silently rewrite a data row.

**Verdict:** the evidence discipline transfers, the clinical judgement does not. Ship the procedure, keep the facts local, and label the output loudly enough that nobody mistakes it for a doctor.

> ⚠️ **Disclaimer.** This is a practice of AI × medical combination, not a medical device and not official medical advice, diagnosis, prescription, or treatment decision. The author assumes no liability for consequences of use or misuse. Read the full statement at the top of the skill before adopting it.

## Why a procedure, not a prompt

Medical records do not arrive as a clean dataset. They arrive as a pile of PDFs from several institutions over many years, many of them scans, with the same metric printed under three abbreviations and two units. The interesting failures are not "the model did not know LDL matters". They are: the model read the wrong row, averaged two institutions that report different reference ranges, or quietly "corrected" a number that looked wrong.

Each of those failure modes has a fix, and none of the fixes is a better prompt. They are a conflict protocol, an append-only rule, a change gate, and evidence grading. That is what this skill is.

There is a second constraint. These records are the most sensitive files a person owns, and a hosted model means every file read is a file transmitted, irreversibly. So the skill opens with an egress pre-check rather than with an analysis technique — the first decision is whether to work at all.

## Two layers, one authority chain

The skill is split because its two halves have different lifetimes.

```
AGENTS.md            ← project constitution: privacy, egress, evidence standard
  └─ project-layer skill   ← configuration, precedent table, family rules
       └─ generic skill    ← procedure only, no patient data, no paths
```

- **The generic layer** holds the workflow: intake, profile, registry, comparison, conflict protocol, evidence grading, output skeleton, merge and rename, compression, and a Traditional Chinese Medicine (TCM) sub-flow. It carries no values, no paths, no names — that is what makes it publishable.
- **The project layer** holds what is true only for one record set: nine config keys, the language conventions, and a **precedent table** of real mistakes and their rulings.
- **`AGENTS.md` outranks both.** The generic layer points at it for privacy and egress instead of restating it, because a restated rule drifts from its source.

The split was not cosmetic. Before it, the derived skill had patient demographics hard-coded into an analysis rule — violating its own "no patient data" clause. Genericising a rule forced the anchor out of the procedure and into configuration, which is where it belonged.

## The rules that carry the weight

Ten rules do most of the work. Every one of them came from an incident, not from good taste. Three of them arrived during the review of this skill, when an old analysis line could no longer be traced back to the model that wrote it.

| Rule | What it forbids |
|---|---|
| **Append-only data rows** | Editing a historical value in place. A wrong row goes through the conflict protocol instead |
| **Conflict protocol** | Silently picking one of two versions. Stop, name both, classify, hand it to the user |
| **Change gate** | Any data edit without "old value → new value + basis" and a human yes |
| **Exemption scope** | A user waiver covering data rows. It covers process notes and analysis lines only |
| **Evidence five** | Claims that fail safety, factuality, verifiability, specificity, or credibility. They drop to `low-confidence` and route to clinician review |
| **Applicability** | Borrowing a general-population range as a target for someone with long-standing disease |
| **Attribution timeline** | Blaming a new drug for a symptom that started during a gap in medication |
| **Single copy** | A second copy of a derived view. Copies drift, and drift is how two values for the same day entered the record |
| **Derived-value arithmetic** | A calculated eGFR or index shown without its formula, inputs, and unit — a silent miscalculation is harder to catch than a wrong measurement |
| **Provenance stamp** | An analysis block with no `model · date · skill version` line, which makes it impossible to re-judge years later |

Two of these are unusual enough to spell out. **Exemption scope** exists because "let me clean this up" and "let me fix this number" arrive in the same sentence and deserve different answers. **Attribution timeline** exists because the most convincing wrong conclusion in the whole record was a symptom attributed to a new treatment that began weeks after the patient had already stopped the previous one.

The workflow itself is mapped in four phases — ingest, analyse, output, maintain — with a fast-path table beside it. A thirty-second answer may skip ASCII trends and optional modules. It may never skip the egress check, the conflict gate, or the evidence grading.

## What the skill refuses to do

- Diagnose, assign a disease subtype, prescribe, or adjust a dose.
- Complete a gap by inference. Missing means missing, and it is named.
- Subtract across institutions, or merge their trends.
- Bulk-replace a filename. A bulk replace once rewrote a historical log line, which is precisely what logs exist to prevent.
- Cite a line number as a location. Section heading plus item name only; line numbers drift.
- Claim the analysis is official. Every output is a draft that may be confidently wrong.

## Adopting it

You need one thing before you start: an agent that loads skills from a directory and can read files on the machine. The procedure assumes nothing beyond that.

1. **Copy the generic skill** unchanged into the directory your agent loads skills from — for OpenCode, `<project>/.opencode/skills/medical-record-review/SKILL.md`. Do not edit the procedure to fit your records; that is what the project layer is for.
2. **Fill the nine keys.** `AUTHORITY`, `PROFILE`, `DOCS_DIR`, `IMGS_DIR`, `REGISTRY`, `INDEX` / `INDEX_CMD`, `LANG`, `MODULES`, `UNWRAP_CMD`. An unresolved required key means stop, not default.
3. **Write a profile.** Age, sex, diagnosis and duration, medication with dosing times, measurement conditions for weight, and two or three things this person actually cares about. Keep it free of names.
4. **Start a precedent table.** Three columns: what happened, what to do next time, where it came from. This is the part that compounds.
5. **Run it once and let it stop.** The first real conflict is the test: if the agent reports it instead of resolving it, the skill is working.

For a family, the rule is one folder per person. Configuration and profile are injected per folder, and folders never reference each other. Cross-person comparison is clinically meaningless and leaks.

## What the review changed, and what still strains

The first version of this skill was reviewed against its own standards. Four gaps closed. Three became rules in the table above; the fourth became a schema in the registry section:

- **The index could be hand-maintained**, which reintroduced the second-copy risk the skill forbids elsewhere. Now a hand-maintained index must declare `hand-maintained: true`, and readers re-verify every field against the file.
- **Non-metric series had no schema.** Symptoms, formulas, and imaging now get minimal columns — onset, attribution status; herb count, doses; modality, follow-up — instead of living wherever the last editor left them.
- **Derived scores could be silently miscalculated.** Formula, inputs, and unit are now mandatory, and an incomplete one drops to `low-confidence`.
- **Model drift was unrecorded.** Every analysis block now ends with `provenance: model · date · skill version`.

Two things still strain, and probably always will:

- **A disclaimer is not legal advice.** Jurisdiction-specific terms are missing, and no lawyer has read the liability language.
- **The rules are prose, not a linter.** Nothing enforces the provenance stamp or the derived-value triple; both depend on the agent remembering, which is exactly what a skill is supposed to fix.

## What would falsify the approach

Three structural conditions would falsify it.

If the records are too sparse, the evidence discipline has nothing to stand on and the honest output is "insufficient data" — which users will read as a failure of the tool. If a hosted model is unacceptable, the whole workflow has to run locally, and quality drops. And if a clinician never sees the output, the skill's careful separation of record from inference buys nothing.

The procedure is worth keeping only while someone acts on its output with a professional in the loop.

## Files

- [`medical-record-review/SKILL.md`](https://github.com/j3ffyang/ai-thoughts/blob/main/.opencode/skills/medical-record-review/SKILL.md) — the generic procedure: config keys, workflow, evidence grading, appendices for trends, frontmatter, precedents, boundaries, and locale profiles. The article explains why, the skill defines how.
- the project layer — not published. It is a small skill that supplies the nine keys, the language conventions, the precedent table, and one profile per person.
- [`LICENSE`](https://github.com/j3ffyang/ai-thoughts/blob/main/LICENSE) — MIT. Copy the procedure, keep the copyright notice.

btw, i use arch
