# Cave Diving 2.0

An AI-guided course in open-circuit cave-diving theory, from understanding the overhead environment to explaining a complete team plan.

## Start the course

Give this repository URL to an AI assistant with repository access. The assistant should read [AGENTS.md](AGENTS.md), [START.md](START.md) and [course.json](course.json), then begin the first scene. You can answer briefly, calculate, ask for an explanation, or say “continue”.

The repository is private: the assistant needs an authenticated connection with permission to read it. A URL alone does not grant access. If access fails, provide the repository files in the conversation. No course content should be invented to hide an access failure.

## Course route

Sixteen short modules build toward one integrated fictional dive case. Gas planning occupies seven modules: inventory, fractions, three matching situations, consumption and emergency demand. Navigation uses schematic routes and consistent English technical terms. Each module contains teaching, exploration, feedback and a later application.

Read [COURSE.md](COURSE.md) for the ordered route, [glossary/TERMS.md](glossary/TERMS.md) for terminology, and [pedagogy/FRAMEWORK.md](pedagogy/FRAMEWORK.md) for the teaching approach.

## Status and boundaries

Course content: **draft**. It supports theory preparation and revision; practical skills require qualified instructor supervision and assessment. Completing this course does not issue a qualification or authorize a dive. All places, divers and numerical cases are fictional unless explicitly stated otherwise.

Subject matter changes are reviewed in GitHub pull requests. Content status is `draft` or `verified`; changing material returns it to `draft`. Review history remains in GitHub.

## Development

Run `python tests/check_course.py`. See [quality/VALIDATION.md](quality/VALIDATION.md) for what automated checks do and what still needs human assessment. The complete teaching path is stored here and has no runtime dependency on another repository or installed skill.
