# Organization Naming #411 · Process Review v0.1

Status: process review / generation paused

This document reviews the live Adaptive Naming Fit Test in Issue #411. It does **not** select a final name and does not restart generation. The purpose is to convert the observed search behavior, Owner feedback, integrity incidents, commercial constraints, and repeated failure modes into method-level evidence.

Canonical task state: `03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml`

---

## 1. What happened

The live job produced several distinct learning phases rather than one linear naming funnel.

### 1.1 Semantic anchoring failure

After the organization philosophy was emphasized, generation repeatedly surfaced literal mission vocabulary such as Commons-related constructions. The Controller had correctly understood that meaning mattered, but operationalized `meaning-first` as `mission-keyword-first`.

Diagnosis: `semantic_mode_collapse / incumbent-style semantic anchoring`.

Key lesson: preserving meaning does not require lexicalizing the mission. The Mission / Value Model must be abstracted into relations, transformations and naming implications before generation.

### 1.2 Surface-form collapse despite semantic diversity

After literal mission tokens were quarantined, the semantic content improved but many Owner-visible candidates converged on natural-English relational phrases / compounds. The meanings differed while the identity architecture did not.

Diagnosis: `morphological_mode_collapse / Owner-visible morphotype undercoverage`.

Key lesson: semantic/search diversity is not the same as visible naming-form diversity.

### 1.3 Commercial constraints became first-class gates

The Owner clarified that the commercial umbrella organization ultimately needs practical control of the exact `.com` and good trademark registrability. `.org` became secondary, mainly for open-source/public-interest projects. A registered `.com` is not automatically fatal if realistic aftermarket acquisition is possible.

Key lesson: domain and trademark evidence must be separated from intrinsic name quality. Reality filtering may remove names but must not become the hidden generator that shapes all creative output toward awkward directly-available strings.

### 1.4 Positive reference: Multifinality

`Multifinality` produced a strong positive Owner reaction because it looked and felt like a coherent brand despite being an established concept. The later `Transindividuality` probe showed that conceptual depth does not remove the practical upper bound on visual/spoken burden.

Key lesson: the positive signal was **conceptual brandability**, not the suffix, academic register, length, or systems terminology itself.

### 1.5 Coined-name route promoted for trademark ownability

The Owner later explicitly deprioritized existing words because coined / semi-coined names generally provide better trademark ownability for a commercial umbrella brand. This changed the search allocation, but not the rule that coined names still need semantic backbone and mature identity quality.

Key lesson: `coined` is a commercial strategy preference here, not permission to generate empty SaaS-like syllable strings.

### 1.6 Merosophy became the strongest coined reference

`Merosophy` was accepted as broadly usable with no major intrinsic objection. The main weakness identified by the Owner was Chinese-speaker pronunciation friction.

Key lesson: semantic density and mature identity can outweigh perfect phonetic simplicity. Cross-language pronounceability is important, but it is a secondary optimization once a name has enough substance.

### 1.7 Larger Owner-visible batches improved feedback efficiency

The Owner explicitly requested 5–8 screened candidates per review turn rather than one-name-at-a-time exposure. A larger batch produced stronger comparative evidence: `Merosophy` remained clearly stronger; `Coemera` received only a weak-positive signal; most smoother coinages produced no pull.

Key lesson: Owner interaction itself has a budget. Candidate batching can increase information gain, but only when quality is screened first. Batch size must not become a quota that encourages filler.

### 1.8 Repeated morphology overfit to Merosophy

The most important new incident occurred after the system attempted to learn from the Merosophy success. The Controller correctly inferred that semantic density mattered, but then repeatedly generated names from similar classical roots, especially `mero-/noe-/poie-`, abstract learned suffixes, and `X + learned ending` structures.

The Owner detected that the entire batch looked structurally similar and explicitly called out the repetition.

Diagnosis: `controller_overfit_to_positive_reference`.

This is materially different from merely generating a few near variants. The system extracted the **surface morphology of the positive example** instead of the **latent reasons the example was liked**.

---

## 2. What the current Skill already gets right

The failure is not primarily caused by a missing word-formation toolbox.

Adaptive Naming v0.4.0 already states that:

- survivor / finalist names should not become implicit templates;
- workflow pattern and construction operator are different layers;
- semantic/search diversity must not be confused with Owner-visible morphotype diversity;
- incumbent anchoring and morphological mode collapse are integrity failures;
- multiple methods that still reuse the same material can indicate territory-material starvation;
- reality survivor shapes must not feed back into generation;
- positive Generation Briefs and Controller-only exclusions should be used under same-context constraints.

The current diagnostic reference already contains `semantic_mode_collapse`, `morphological_mode_collapse`, `scheduler_monoculture`, `territory_material_starvation`, `incumbent_anchoring`, and `rescue_overfit`.

Therefore the principal gap is **not conceptual vocabulary**. It is operational enforcement.

---

## 3. Main method gap: post-hoc diagnosis is stronger than pre-exposure prevention

The current system is good at explaining why a batch collapsed **after** the collapse becomes visible. In #411, the Owner detected morphology concentration more than once even though the stable Skill already warned against it.

This suggests a missing control layer between generation and Owner exposure:

> **Batch Generalization / Diversity Audit**

The audit should answer whether a batch genuinely generalizes the desired qualities or merely copies the morphology of a recent positive reference.

A batch should be blocked from Owner exposure when it passes individual-candidate quality checks but fails batch-level diversity / reference-distance checks.

---

## 4. Proposed improvement A · Positive Reference Abstraction

When an Owner likes a candidate, the Controller should explicitly split the evidence into two classes before using it:

### Latent positive properties

Examples:

- semantic density;
- mature standalone identity;
- restrained cleverness;
- coherent explanation;
- institutional scale;
- memorable structure;
- acceptable visual/spoken load.

### Surface properties that must **not** automatically become search directives

Examples:

- specific roots;
- suffixes;
- prefix family;
- syllable contour;
- language of origin;
- academic/classical register;
- word length;
- orthographic shape.

Only latent properties may flow into broad exploration by default. Surface properties require independent evidence before exploitation.

This can be treated as a `positive_reference_abstraction` step.

---

## 5. Proposed improvement B · Batch-level diversity contract

Before a 5–8 candidate Owner-visible batch is exposed, the Controller should record at least:

- construction architecture;
- semantic mechanism;
- material provenance / source family;
- phonological profile;
- orthographic profile;
- explanation pattern;
- distance from current positive reference(s).

The purpose is not to maximize diversity numerically. The purpose is to detect hidden monoculture.

A practical pre-exposure contract could be:

1. no single construction architecture dominates without an explicit exploitation hypothesis;
2. if a positive reference exists, at least part of the batch must preserve its **latent virtues** while changing its surface morphology substantially;
3. different semantic explanations do not count as structural diversity if the strings use the same root/suffix machine;
4. different spellings do not count as diversity if the same naming grammar generated them;
5. if the Owner asked for broad exploration, the Controller should reject a structurally homogeneous batch before presentation.

The exact class count should remain adaptive. The temporary `five materially distinct classes / max two per class` rule from snapshot v81 is useful as a regression test, not necessarily a permanent universal constant.

---

## 6. Proposed improvement C · Generalization test after positive feedback

Positive feedback should trigger a question analogous to model generalization:

> Can the system reproduce the **reason for success** without reproducing the **form of the successful example**?

A useful test batch would deliberately create several structurally distant candidates that all target the same latent qualities.

If quality collapses as soon as morphology changes, the system has not learned the preference; it has overfit the example.

This gives `overfitting` a precise operational meaning inside Adaptive Naming rather than using it only as a metaphor.

---

## 7. Proposed improvement D · Separate candidate quality from batch quality

Current evaluation is heavily candidate-centric. #411 shows that a batch may contain individually defensible names while still be poor as an exploration artifact.

Add a distinct batch-level object with signals such as:

- morphotype concentration;
- shared-root concentration;
- shared-suffix concentration;
- material-source concentration;
- explanation-template concentration;
- phonological similarity;
- reference similarity;
- information gain vs previous batch.

A batch can therefore be:

- `candidate_quality_pass + batch_diversity_fail`, or
- `candidate_quality_mixed + high_information_probe`, etc.

This prevents the Controller from treating 7 individually explainable variants as 7 independent explorations.

---

## 8. Proposed improvement E · Owner review throughput as a controlled variable

The Owner requested larger batches because one-at-a-time presentation wasted time. This is useful task evidence.

The stable method should not hard-code `5–8` globally, but could add an `owner_review_cadence` state variable:

- micro probe: 1–3 only when a single uncertainty is being tested;
- comparative batch: typically several screened candidates when preference learning benefits from side-by-side comparison;
- no exposure: when the batch fails diversity/intrinsic/reality readiness.

This extends the existing search cadence concept to human review cadence.

---

## 9. Proposed improvement F · Commercial ownability without availability-shaped creativity

#411 repeatedly showed the temptation to prefer strings simply because `.com` was free. The task correctly resisted this, but the pressure recurred.

For tasks with commercial trademark/domain hard gates:

- ownability can influence **which construction regions receive budget**;
- domain / trademark checks remain post-generation or post-intrinsic-screen;
- direct-registration vacancy must not become a proxy for name quality;
- a strong registered-domain name may remain viable through aftermarket acquisition;
- a weak coined string does not become stronger because both `.com` and `.org` are available.

This is already conceptually present in v0.4.0, but #411 provides strong live regression evidence.

---

## 10. Proposed improvement G · Cross-language pronounceability as an optimization layer

Merosophy showed that a strong name may survive despite moderate Chinese pronunciation friction. The later batch showed that optimizing smoothness too early can produce semantically thin names.

Recommended ordering:

1. minimum recoverability gate;
2. intrinsic semantic / identity quality;
3. cross-language pronounceability optimization;
4. reality / ownability validation according to task stage.

Do not let cross-language smoothness become a generator monoculture unless the Owner explicitly upgrades it to a hard requirement.

---

## 11. What should change now vs later

### Safe to record now

- repeated positive-reference overfit is a real #411 control failure;
- candidate-level diversity is insufficient; batch-level diversity needs explicit representation;
- positive feedback should be abstracted into latent virtues vs surface morphology;
- Owner review cadence is a legitimate adaptive variable;
- cross-language pronounceability should not outrank semantic substance by default.

### Not yet justified as a universal stable rule

- exactly five architecture classes;
- maximum two candidates per class;
- any fixed list of construction families;
- Merosophy-like semantic density as a universal naming preference;
- coined words as universally superior to existing words;
- 5–8 names as the universal batch size.

Those are task-specific or regression scaffolds until reproduced on another Naming Job.

---

## 12. Recommended method-evolution path

1. Add a new Experience Registry entry for repeated positive-reference morphology overfit.
2. Add a method hypothesis for `positive_reference_abstraction + batch_generalization_audit`.
3. Create regression cases using #411 incidents:
   - strong positive candidate followed by structurally cloned batch;
   - semantically diverse but morphologically homogeneous batch;
   - domain-available weak coinages vs stronger intrinsically good names;
   - pronunciation optimization that reduces semantic quality.
4. Run the regression against v0.4.0 plus the proposed control.
5. Only after regression success decide whether to promote the mechanism into a stable Skill revision.

---

## 13. Core conclusion

The most important finding from this naming run is not a new construction technique.

It is this:

> **Adaptive Naming can overfit positive Owner feedback exactly as a model overfits training data: it can reproduce the visible form of a successful example instead of learning the underlying reason it succeeded.**

The next method improvement should therefore focus on **generalization control**, not on adding more generators.

A stronger system should be able to say:

> “I learned that the Owner values semantic density, mature identity and restrained cleverness — not that I should keep generating classical-root words that resemble Merosophy.”

That is the clearest method-level lesson from #411 so far.
