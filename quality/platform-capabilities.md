# Platform capability snapshot

status: draft
review_date: 2026-11-05

The project-start documentation review covered official ChatGPT capabilities guidance and official Claude Artifacts guidance. Descriptions below are scoped to documentation review; deployment availability is not promised. No external references are embedded in the course.

| Environment | Evidence | Pedagogical use | Limits / fallback |
|---|---|---|---|
| ChatGPT web/mobile | documented: conversation, image/file understanding and tool-dependent analysis | Stepwise scenes and optional tables/diagrams | Plan/settings vary; exact client rendering and repository access not tested. Text and tables are sufficient. |
| Claude web/Desktop | documented: artifacts for standalone/interactive outputs subject to capability settings | Optional one-variable gas model | Exact account/settings/runtime and course interaction not tested. Use worked text states. |
| Claude mobile | documented: artifact interaction has client-specific scope | Optional view of a supported visual | No mobile course test performed. Use text. |
| Current Work session | available: connected GitHub tools, code execution, visualization-related tools | Course construction and independent arithmetic checks | Availability here does not establish availability for future learners. No learner widget was executed. |
| API/Claude Code/other deployments | unknown for this course's actual deployment | Plain text intent only | No assumed repository access, Mermaid, widgets or memory. |

Documentation retrieval succeeded on the review date; publication/update labels were relative (“8 days ago” and “this week”) and were not converted into exact dates. The snapshot makes no guarantee about every feature, account or plan. No rich teaching UI or fresh-conversation course run has been tested.

At runtime inspect only tools actually exposed, use the simplest supported representation and start promptly. If a renderer or widget fails, show its text equivalent. Recheck platform assumptions at a new project, a material feature change or a failure. No background monitoring is configured.
