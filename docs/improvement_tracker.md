# Project Alpha - Improvement Tracker

**Project:** Project Alpha

**Purpose**

This document contains approved ideas and future enhancements for Project Alpha.

## Rules

- Improvements listed here are **not** part of the current sprint.
- They must **not** be implemented unless explicitly approved.
- The active sprint always takes priority.
- Completed improvements should be moved to the Decision Log or Changelog.
- Improvement IDs are permanent and must never be renumbered.

---

# Status Legend

| Status | Meaning |
|---------|---------|
| Backlog | Approved idea, not yet scheduled |
| Planned | Scheduled for a future sprint |
| In Progress | Currently being implemented |
| Completed | Finished and merged |
| Rejected | Decided not to implement |

---

# Improvements

| ID | Title | Description | Priority | Status | Target Version | Notes |
|----|-------|-------------|----------|--------|----------------|-------|
| IMP-001 | Proper Python Package Structure | Convert the project into a proper Python package (`alpha_quant`). | Low | Backlog | After v1.0 | Avoid import refactoring during early development. |
| IMP-002 | Research External Protocols First | Mandatory research sprint before integrating external APIs, brokers, or data providers. | High | Completed | Process Rule | Adopted during Dukascopy integration. |
| IMP-003 | Automatic Dukascopy Instrument Metadata Generator | Generate `dukascopy.json` automatically from Dukascopy metadata. | Medium | Backlog | After v1.0 | Eliminates manual metadata maintenance. |
| IMP-004 | Local Download Cache | Cache downloaded BI5 files to avoid repeated network requests. | Medium | Backlog | v1.1 | Similar to the reference implementation. |
| IMP-005 | Resume Interrupted Downloads | Resume partially downloaded files. | Medium | Backlog | v1.1 | Useful for multi-year downloads. |
| IMP-006 | Parallel Historical Downloads | Download multiple dates/instruments concurrently. | Low | Backlog | v1.2 | Performance enhancement. |
| IMP-007 | Automatic Data Validation | Validate downloaded data (duplicates, gaps, timestamps, corruption). | High | Backlog | v1.0 | Prevent invalid datasets. |
| IMP-008 | Progress Indicators | Display progress bars, ETA, and throughput during downloads. | Low | Backlog | v1.1 | User experience improvement. |
| IMP-009 | Retry with Exponential Backoff | Retry failed downloads using exponential backoff. | Medium | Backlog | v1.1 | Better network resilience. |
| IMP-010 | Instrument Metadata Versioning | Track metadata version history. | Low | Backlog | v1.2 | Easier maintenance. |
| IMP-011 | Configuration Profiles | Support Development, Testing and Production profiles. | Medium | Backlog | v1.1 | Environment separation. |
| IMP-012 | Incremental Data Synchronization | Download only missing historical data. | High | Backlog | v1.2 | Faster updates. |
| IMP-013 | Data Integrity Checksums | Verify downloaded and processed files using checksums. | Low | Backlog | v1.2 | Detect corruption. |
| IMP-014 | Multi-Broker Data Adapter | Broker-independent interface supporting Dukascopy, MT5, Deriv and others. | High | Backlog | After v1.0 | Pluggable architecture. |
| IMP-015 | Project Roadmap | Maintain a versioned ROADMAP.md. | Medium | Backlog | v0.2 | Planning and milestones. |

---

# Notes

This tracker is only for future enhancements.

Do **not** use it for:

- Bugs
- Current sprint tasks
- Temporary notes
- Research findings

Those belong in their respective documents.