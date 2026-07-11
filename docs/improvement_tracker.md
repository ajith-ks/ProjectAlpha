# Improvement Tracker

## Purpose

This document contains approved ideas and future enhancements for Project Alpha.

### Rules

- Improvements listed here are **not** part of the current sprint.
- They must **not** be implemented unless explicitly approved.
- The active sprint always takes priority.
- Completed improvements should be moved to the Decision Log or Changelog.

---

## Status Legend

| Status | Meaning |
|---------|---------|
| Backlog | Approved idea, not yet scheduled |
| Planned | Scheduled for a future sprint |
| In Progress | Currently being implemented |
| Completed | Finished and merged |
| Rejected | Decided not to implement |

---

## Improvement List

| ID | Title | Description | Priority | Status | Target Version | Notes |
|----|-------|-------------|----------|--------|----------------|-------|
| IMP-001 | Proper Python Package Structure | Convert the project into a proper Python package (e.g., `alpha_quant`). | Low | Backlog | After v1.0 | Avoid import refactoring during early development. |
| IMP-002 | Research External Protocols First | Add a mandatory research phase before integrating any external API, broker, or data provider. | High | Completed | Process Rule | Adopted during Dukascopy integration. |

---

## Notes

This tracker is intended for **future enhancements only**.

It should **not** be used to track:
- Bugs
- Current sprint tasks
- Feature requests already in progress

Those belong in the Sprint Tracker or Issue Tracker.