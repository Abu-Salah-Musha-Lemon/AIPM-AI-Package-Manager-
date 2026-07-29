# 1. Introduction

Technical debt is the accumulated cost of design decisions, implementation shortcuts, incomplete features, temporary solutions, missing tests, outdated documentation, and other engineering compromises that may increase the future cost of maintaining or extending the AI Package Manager (AIPM).

Technical debt does not necessarily indicate poor development. Some debt is intentional and can be reasonable when a project is evolving rapidly. However, unmanaged technical debt can gradually reduce maintainability, reliability, security, performance, and development velocity.

AIPM is being developed as a modular, secure, scalable, maintainable, and commercially viable AI package management platform. As the project evolves, technical debt must therefore be identified, documented, prioritized, monitored, and resolved systematically.

This document serves as the central technical-debt register for AIPM.

It records known engineering compromises and architectural weaknesses, explains their potential consequences, assigns priorities, and provides a controlled strategy for resolving them without destabilizing the existing system.

The document is intentionally maintained as a living document. It must be updated whenever:

- A new technical-debt item is identified.
- An existing debt item changes in severity.
- A debt item is partially or completely resolved.
- Architecture or package boundaries change.
- A new dependency introduces maintenance concerns.
- Testing reveals previously unknown weaknesses.
- Security analysis identifies additional technical risks.
- Refactoring creates new temporary compromises.

Technical debt must not be treated as an informal list of "things to fix later." Each significant debt item should have a clear description, reason, impact, priority, affected component, and resolution strategy.

The primary objectives of technical-debt management in AIPM are:

- Preserve architectural integrity.
- Prevent temporary solutions from becoming permanent design decisions.
- Reduce unnecessary complexity.
- Improve code maintainability.
- Increase testability.
- Strengthen security.
- Improve performance and reliability.
- Reduce future development cost.
- Protect backward compatibility.
- Keep the project aligned with its long-term architecture.

Technical debt should be evaluated alongside new feature development rather than being postponed indefinitely. High-risk debt, especially debt affecting security, data integrity, architecture, or core package operations, should take precedence over non-critical feature expansion.

The ultimate goal is not to achieve zero technical debt. A realistic software project will always contain some level of technical debt. The goal is to maintain technical debt at a controlled level where it does not compromise the stability, security, maintainability, scalability, or long-term direction of AIPM.

# 2. Purpose

The purpose of this document is to establish a formal and repeatable process for identifying, documenting, prioritizing, monitoring, and resolving technical debt within the AI Package Manager (AIPM).

Technical debt can accumulate naturally as a software project grows. Without an explicit management process, small implementation compromises can gradually become architectural constraints, increase maintenance costs, introduce defects, and make future development more difficult.

This document provides a centralized reference for understanding the current technical-debt state of AIPM and determining which debt items require immediate attention, which can be scheduled for future milestones, and which can reasonably be accepted as intentional design trade-offs.

The technical-debt management process has the following purposes:

## 2.1 Identify Technical Debt

Identify technical compromises throughout the project, including:

- Architectural weaknesses.
- Code duplication.
- Excessive coupling.
- Inconsistent abstractions.
- Incomplete implementations.
- Temporary workarounds.
- Missing automated tests.
- Weak error handling.
- Outdated documentation.
- Performance bottlenecks.
- Security weaknesses.
- Dependency-related risks.
- Inconsistent interfaces.
- Deprecated or obsolete implementations.

Every significant technical-debt item should be documented rather than relying on memory or informal discussion.

---

## 2.2 Assess Technical Impact

Each debt item should be evaluated according to its potential effect on:

- Maintainability.
- Reliability.
- Security.
- Performance.
- Scalability.
- Testability.
- Developer productivity.
- User experience.
- Compatibility.
- Operational stability.

The assessment should distinguish between minor implementation debt and debt that can threaten the core architecture or production readiness of AIPM.

---

## 2.3 Prioritize Debt

Not all technical debt requires immediate resolution.

Debt should therefore be prioritized according to factors such as:

- Severity.
- Business impact.
- Security implications.
- Architectural impact.
- Probability of failure.
- Cost of postponement.
- Estimated resolution effort.
- Dependencies on other work.

Critical technical debt should be addressed before lower-priority improvements whenever it creates a meaningful risk to the project.

---

## 2.4 Prevent Debt Accumulation

The document establishes practices intended to prevent uncontrolled technical-debt growth.

These practices include:

- Code review.
- Automated testing.
- Static analysis.
- Consistent architecture.
- Documentation updates.
- Dependency reviews.
- Regular refactoring.
- Architecture reviews.
- Release validation.

New technical debt should be intentional, documented, and justified whenever possible.

---

## 2.5 Track Resolution

Technical debt should be tracked throughout the development lifecycle.

Each significant debt item should have:

- Unique identifier.
- Description.
- Affected component.
- Root cause.
- Impact.
- Priority.
- Proposed solution.
- Estimated effort.
- Target milestone.
- Current status.
- Resolution date.

Resolved items should remain in the historical record when they provide useful architectural or development context.

---

## 2.6 Protect the Long-Term Architecture

AIPM is intended to evolve into a professional, scalable, secure, maintainable, and commercially viable AI package management platform.

Technical-debt management therefore exists to ensure that short-term implementation decisions do not gradually undermine the long-term architecture.

Special attention should be given to debt affecting:

- Package boundaries.
- Manager responsibilities.
- Storage abstraction.
- Registry architecture.
- Download and verification workflows.
- Installation and repair workflows.
- History management.
- Configuration management.
- CLI architecture.
- Security boundaries.
- Public APIs.

---

## 2.7 Support Development Planning

Technical debt should be incorporated into the project's development roadmap rather than treated as separate work.

Where appropriate, debt-resolution tasks should be assigned to:

- GitHub Issues.
- GitHub Milestones.
- Pull Requests.
- Refactoring tasks.
- Security work.
- Testing work.
- Release preparation.

This allows technical debt to be managed using the same traceability and accountability mechanisms as normal feature development.

---

## 2.8 Establish a Sustainable Debt Level

The objective is not to eliminate all technical debt.

AIPM should maintain a controlled and sustainable level of technical debt that does not materially compromise:

- Software quality.
- Security.
- Reliability.
- Maintainability.
- Scalability.
- Development velocity.
- Production readiness.

Technical debt that provides a reasonable short-term benefit and has limited long-term consequences may be intentionally accepted.

However, accepted debt should remain documented and periodically reviewed.

---

## 2.9 Provide a Single Source of Truth

This document serves as the authoritative technical-debt register for the project.

Technical-debt information should not be scattered across:

- Personal notes.
- Temporary files.
- Commit messages.
- Chat conversations.
- Untracked TODO comments.
- Informal discussions.

When a technical-debt item becomes significant enough to affect project planning or engineering decisions, it should be recorded in `TECH_DEBT.md` and, where appropriate, linked to a corresponding GitHub Issue.

---

## 2.10 Maintain Engineering Discipline

The ultimate purpose of technical-debt management is to maintain engineering discipline as AIPM grows.

AIPM should continuously balance:

```
Feature Development
        +
Bug Fixing
        +
Security
        +
Testing
        +
Refactoring
        +
Technical Debt Reduction
        =
Sustainable Development
```

Technical debt should therefore be considered a normal engineering concern that requires continuous management rather than an exceptional problem addressed only before major releases.

---

## Purpose Summary

The purpose of `TECH_DEBT.md` is to ensure that technical debt within AIPM is:

- Visible.
- Documented.
- Measurable.
- Prioritized.
- Traceable.
- Actively managed.
- Regularly reviewed.
- Resolved according to risk and project priorities.

This approach ensures that AIPM can continue to evolve without allowing accumulated technical compromises to undermine its architecture, security, reliability, maintainability, or long-term commercial viability.

# 3. Debt Classification

Technical debt within AIPM is classified into defined categories so that each debt item can be analyzed according to its root cause, technical impact, risk level, and expected resolution strategy.

Classification prevents unrelated technical problems from being treated in the same way and makes it easier to prioritize debt during milestone and release planning.

A single debt item may belong to more than one category when its effects cross multiple areas of the system.

---

## 3.1 Architecture Debt

Architecture debt occurs when the current system structure does not adequately support the project's long-term requirements.

Examples include:

- Incorrect package boundaries.
- Excessive coupling between managers.
- Circular dependencies.
- Violations of dependency direction.
- Business logic placed in the CLI layer.
- Inappropriate responsibility assignment.
- Duplicate service responsibilities.
- Inconsistent abstraction layers.
- Architecture that prevents future extensibility.

Architecture debt is considered high priority when it affects multiple packages or makes future development significantly more expensive.

---

## 3.2 Code Debt

Code debt refers to implementation-level compromises that reduce readability, maintainability, or correctness.

Examples include:

- Duplicate code.
- Overly complex functions.
- Large classes.
- Poor naming.
- Inconsistent coding conventions.
- Unnecessary conditionals.
- Repeated logic.
- Dead code.
- Temporary workarounds.
- Missing type annotations.
- Weak exception handling.

Code debt should normally be resolved during feature development or targeted refactoring.

---

## 3.3 Testing Debt

Testing debt occurs when the existing test suite does not provide sufficient confidence in the software.

Examples include:

- Missing unit tests.
- Missing integration tests.
- Missing CLI tests.
- Insufficient edge-case coverage.
- Untested failure paths.
- Missing regression tests.
- Low coverage of critical packages.
- Tests that depend on external services.
- Flaky or nondeterministic tests.

Testing debt is especially important for core workflows such as:

```
Download
    ↓
Install
    ↓
Verify
    ↓
Repair
    ↓
Remove
```

Critical workflows should not remain dependent on manual testing.

---

## 3.4 Documentation Debt

Documentation debt occurs when documentation is incomplete, outdated, inconsistent, or disconnected from the implementation.

Examples include:

- Missing package documentation.
- Outdated README information.
- Missing CLI command documentation.
- Incorrect architecture diagrams.
- Missing API documentation.
- Outdated configuration references.
- Missing migration instructions.
- Documentation that describes planned functionality as implemented functionality.

Documentation debt should be resolved whenever the related implementation changes.

---

## 3.5 Performance Debt

Performance debt occurs when implementation decisions create unnecessary resource consumption or reduce application efficiency.

Examples include:

- Inefficient filesystem operations.
- Repeated unnecessary registry reads.
- Excessive memory consumption.
- Unoptimized metadata processing.
- Slow model verification.
- Unnecessary network requests.
- Inefficient history processing.
- Lack of caching where caching is appropriate.

Performance debt should be measured using benchmarks rather than assumptions.

Optimization should not be performed solely for theoretical performance improvements without evidence of an actual bottleneck.

---

## 3.6 Security Debt

Security debt occurs when known or suspected security weaknesses remain unresolved.

Examples include:

- Insufficient download validation.
- Weak path validation.
- Unsafe filesystem operations.
- Inadequate input validation.
- Missing integrity verification.
- Insecure configuration handling.
- Insufficient permission checks.
- Missing security policies.
- Dependency vulnerabilities.

Security debt receives elevated priority because vulnerabilities in a package-management system can compromise both the application and the user's local environment.

---

## 3.7 Dependency Debt

Dependency debt occurs when external libraries, packages, or runtime requirements create maintenance or compatibility problems.

Examples include:

- Outdated dependencies.
- Deprecated libraries.
- Unmaintained packages.
- Excessive dependency count.
- Conflicting dependency versions.
- Unnecessary third-party libraries.
- Missing dependency version constraints.
- Security vulnerabilities in dependencies.

Dependency debt should be reviewed periodically and before major releases.

---

## 3.8 API Debt

API debt occurs when public interfaces become inconsistent, difficult to maintain, or incompatible with the project's long-term design.

Examples include:

- Inconsistent method signatures.
- Poorly designed public APIs.
- Breaking changes without migration paths.
- Duplicate APIs.
- Unclear return types.
- Inconsistent exception behavior.
- Public exposure of internal implementation details.

API debt is particularly important once AIPM begins supporting external integrations, plugins, REST APIs, or third-party consumers.

---

## 3.9 Data and Storage Debt

Data and storage debt occurs when the persistence model or filesystem structure creates reliability, scalability, or migration problems.

Examples include:

- Fragile metadata storage.
- Non-atomic writes.
- Inconsistent storage formats.
- Missing backup mechanisms.
- Lack of migration strategy.
- Inefficient history storage.
- Uncontrolled cache growth.
- Lack of corruption recovery.

Storage debt should receive high priority when it can cause data loss or prevent reliable recovery.

---

## 3.10 Configuration Debt

Configuration debt occurs when configuration behavior becomes difficult to understand, validate, or maintain.

Examples include:

- Hard-coded paths.
- Duplicate configuration sources.
- Missing default values.
- Weak configuration validation.
- Inconsistent environment-variable handling.
- Configuration options without documentation.
- Configuration behavior that differs between platforms.

Configuration should remain predictable and centrally managed.

---

## 3.11 CLI and UX Debt

CLI/UX debt occurs when user-facing behavior becomes inconsistent, confusing, or difficult to use.

Examples include:

- Inconsistent command syntax.
- Poor error messages.
- Missing exit codes.
- Inconsistent output formatting.
- Missing progress information.
- Commands behaving differently without documented reasons.
- Difficult-to-discover functionality.

This category is important because the CLI is currently one of the primary interfaces to AIPM.

---

## 3.12 Operational Debt

Operational debt refers to weaknesses that make AIPM difficult to monitor, diagnose, recover, or operate reliably.

Examples include:

- Insufficient logging.
- Poor error reporting.
- Missing diagnostic information.
- No recovery mechanism.
- Inconsistent exit status.
- Difficult troubleshooting.
- Missing operational documentation.

Operational debt becomes increasingly important as AIPM moves from development toward production and enterprise environments.

---

## 3.13 Build and CI/CD Debt

Build and CI/CD debt occurs when the project's development and release automation is incomplete or unreliable.

Examples include:

- Missing automated CI.
- Inconsistent development environments.
- Manual release processes.
- Missing automated packaging.
- Incomplete test pipelines.
- Missing release validation.
- Unreproducible builds.
- Inconsistent formatting or linting enforcement.

CI/CD debt should be reduced before the project reaches stable production releases.

---

## 3.14 Compatibility Debt

Compatibility debt occurs when AIPM does not consistently support its declared environments or platforms.

Examples include:

- Platform-specific behavior.
- Inconsistent filesystem handling.
- Python-version incompatibilities.
- Windows/Linux/macOS differences.
- Deprecated operating-system APIs.
- Unverified behavior on supported platforms.

Compatibility debt should be tracked against the project's officially supported environment matrix.

---

## 3.15 Process Debt

Process debt occurs when development practices themselves create recurring technical problems.

Examples include:

- Features merged without tests.
- Incomplete code reviews.
- Untracked architectural changes.
- Missing release checklists.
- Technical debt not recorded.
- Documentation omitted from feature work.
- Inconsistent Git workflows.

Process debt is important because it can continuously generate new technical debt.

---

## 3.16 Intentional Debt

Not all technical debt is accidental.

Intentional debt may be accepted when a temporary implementation provides sufficient short-term value and the long-term cost is understood.

Examples include:

- Temporary compatibility layers.
- Prototype implementations.
- Temporary storage mechanisms.
- Deferred optimization.
- Transitional APIs.
- Simplified implementations during early development.

Intentional debt must still be documented when it has meaningful future consequences.

---

## 3.17 Accidental Debt

Accidental debt occurs when technical problems arise without being deliberately introduced.

Examples include:

- Unplanned coupling.
- Duplicate implementations.
- Incorrect abstractions.
- Incomplete error handling.
- Regression-causing shortcuts.
- Missing tests discovered after implementation.

Accidental debt should be reviewed to determine whether the underlying development process needs improvement.

---

# 3.18 Debt Classification by Severity

In addition to technical category, every debt item should receive a severity classification.

| Severity | Definition |
|----------|------------|
| Critical | Can cause security compromise, data loss, severe corruption, or make the system fundamentally unsafe. |
| High | Significantly affects architecture, reliability, security, maintainability, or core functionality. |
| Medium | Creates measurable maintenance or development problems but does not immediately threaten system stability. |
| Low | Minor inconvenience, cleanup opportunity, or localized improvement. |
| Informational | Known limitation or design consideration that currently requires monitoring rather than immediate action. |

---

# 3.19 Debt Classification by Priority

Severity and priority are related but not identical.

Priority determines how soon the debt should be addressed.

| Priority | Meaning |
|----------|---------|
| P0 | Immediate action required. Release-blocking. |
| P1 | Must be addressed in the current milestone or before the next major release. |
| P2 | Should be addressed in a planned upcoming milestone. |
| P3 | Can be addressed when resources are available. |
| P4 | Long-term improvement or optional cleanup. |

For example, a Medium-severity issue affecting an upcoming feature may become P1, while a High-severity issue with an effective temporary mitigation may be scheduled as P2.

---

# 3.20 Debt Classification by Lifecycle

Each debt item should also have a lifecycle status.

| Status | Meaning |
|--------|---------|
| Identified | Debt has been discovered but not yet evaluated. |
| Assessed | Impact and priority have been evaluated. |
| Accepted | Debt has been intentionally accepted temporarily. |
| Planned | Resolution has been assigned to a future milestone. |
| In Progress | Resolution work has started. |
| Blocked | Resolution cannot proceed because of an external dependency. |
| Resolved | The technical debt has been corrected. |
| Verified | The resolution has been tested and confirmed. |
| Closed | The debt item has been fully completed and documented. |
| Reopened | Previously resolved debt has returned or was not completely resolved. |

---

# 3.21 Classification Record

Every significant technical-debt item should contain, at minimum:

```text
ID:
Category:
Severity:
Priority:
Status:
Component:
Description:
Root Cause:
Impact:
Proposed Resolution:
Estimated Effort:
Target Milestone:
Related Issue:
Related Pull Request:
Created:
Updated:
Resolved:
```

This structure provides consistent tracking across the project.

---

# 3.22 Multiple Classification

A technical-debt item may belong to multiple categories.

For example:

```text
ID: TD-001

Category:
    Architecture
    Code
    Testing

Severity:
    High

Priority:
    P1
```

This is appropriate when one underlying problem affects several engineering areas.

However, duplicate records should not be created for the same underlying debt unless separate resolution paths are required.

---

# 3.23 Classification Principles

AIPM follows these principles when classifying technical debt:

1. Classify the root problem, not only its visible symptom.
2. Use multiple categories when necessary.
3. Separate severity from priority.
4. Record intentional debt explicitly.
5. Do not hide security debt under generic code debt.
6. Do not classify missing tests merely as code cleanup.
7. Reassess debt when architecture changes.
8. Link significant debt to GitHub Issues.
9. Link resolution work to the appropriate milestone.
10. Keep resolved debt in the historical record when it provides useful context.

---

# Classification Summary

AIPM technical debt is primarily classified into:

```text
Architecture
Code
Testing
Documentation
Performance
Security
Dependency
API
Data / Storage
Configuration
CLI / UX
Operational
Build / CI/CD
Compatibility
Process
```

Each item is additionally classified by:

```text
Severity
    ↓
Priority
    ↓
Lifecycle Status
```

This classification system provides a consistent foundation for the remaining sections of `TECH_DEBT.md`, particularly the Current Technical Debt Register, Priority Matrix, Refactoring Candidates, and Resolution Plan.

# 4. Current Technical Debt

This section records the currently identified technical debt in the AI Package Manager (AIPM).

The purpose of this section is to provide a current snapshot of known engineering weaknesses that may affect maintainability, correctness, reliability, security, testing, or future development.

This is a living register. New debt must be added when discovered, and resolved debt must be updated rather than silently removed.

Technical debt identified here should not automatically be treated as a project failure. Some items may be acceptable during the current development stage, while others require immediate correction because they can affect correctness or architectural stability.

---

## 4.1 Current Debt Summary

The currently identified debt can be summarized as follows:

| ID | Category | Severity | Priority | Status |
|----|----------|----------|----------|--------|
| TD-001 | Architecture | High | P1 | Identified |
| TD-002 | Code | High | P1 | Identified |
| TD-003 | Testing | High | P1 | Identified |
| TD-004 | Error Handling | High | P1 | Identified |
| TD-005 | History / Audit | High | P1 | Identified |
| TD-006 | Code Quality | Medium | P2 | Identified |
| TD-007 | Documentation | Medium | P2 | Identified |
| TD-008 | Dependency / API Stability | Medium | P2 | Identified |
| TD-009 | Release Process | Medium | P2 | Identified |
| TD-010 | Performance Benchmarking | Low | P3 | Planned |

The list is intentionally conservative. Additional debt should be added only after verification.

---

# 4.2 TD-001 — Architecture and Responsibility Boundaries

Category:

```text
Architecture
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Several core managers currently coordinate multiple responsibilities directly.

For example, the repair workflow coordinates:

```text
Registry
   ↓
Verify
   ↓
Remove
   ↓
Download
   ↓
Verify
   ↓
History
```

This is functional, but as the project grows, managers that directly coordinate many subsystems may become increasingly coupled.

### Impact

Excessive coupling can make:

- Unit testing harder.
- Refactoring more difficult.
- Dependency direction less clear.
- Future API development harder.
- Alternative implementations more difficult.
- Error handling inconsistent.

### Resolution Direction

The architecture should gradually move toward clearly separated layers:

```text
CLI
 ↓
Application / Service Layer
 ↓
Domain Managers
 ↓
Repositories / Infrastructure
 ↓
Filesystem / Network
```

The objective is not to introduce unnecessary abstractions immediately. Abstractions should be introduced when they provide a measurable architectural benefit.

---

# 4.3 TD-002 — Repair Manager Implementation Complexity

Category:

```text
Code / Architecture
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The repair workflow currently performs several operations inside a single manager method:

```text
Registry lookup
Verification
Health assessment
Removal
Download
Final verification
History recording
Error handling
```

This creates a relatively large orchestration method.

### Impact

A large orchestration method increases the possibility of:

- Incorrect control flow.
- Difficult testing.
- Hidden side effects.
- Inconsistent error handling.
- Future regression bugs.

### Resolution Direction

The repair workflow should eventually be decomposed into clearly testable operations while preserving the public manager API.

Potential conceptual structure:

```text
RepairManager
    ↓
RepairService
    ├── RegistryResolver
    ├── InstallationVerifier
    ├── CorruptionHandler
    ├── ModelDownloader
    └── RepairHistoryRecorder
```

This should be implemented only if the existing project size justifies the abstraction.

---

# 4.4 TD-003 — Insufficient Automated Test Coverage

Category:

```text
Testing
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The core lifecycle workflows require stronger automated coverage before the project can be considered production-ready.

Critical workflows include:

```text
Download
Install
Verify
Update
Repair
Remove
History
```

### Required Test Cases

At minimum, tests should cover:

- Successful installation.
- Missing registry model.
- Invalid model metadata.
- Invalid SHA256 checksum.
- Corrupted installation.
- Failed download.
- Interrupted download.
- Failed removal.
- Failed final verification.
- Successful repair.
- Failed repair.
- History success entry.
- History failure entry.

### Impact

Insufficient automated testing increases the probability that future refactoring will introduce regressions.

### Resolution

Establish a test suite around every core manager and its important failure paths before expanding the architecture significantly.

Target:

```text
Unit Coverage:        ≥90%
Integration Coverage: ≥85%
Critical Workflows:   100%
```

---

# 4.5 TD-004 — Error Handling Consistency

Category:

```text
Code / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Core operations currently use a mixture of:

- Returned result objects.
- `ValueError`.
- Generic `Exception`.
- Logger messages.
- String-based error messages.

For example, a download exception may be caught generically and converted into a `RepairResult`.

### Impact

Inconsistent error semantics can make it difficult for:

- CLI layers to determine the correct exit code.
- Tests to assert specific failures.
- API consumers to handle errors consistently.
- Developers to distinguish expected and unexpected failures.

### Resolution Direction

AIPM should establish a consistent error model.

Potential structure:

```text
AIPMError
├── RegistryError
├── DownloadError
├── VerificationError
├── InstallationError
├── RepairError
├── StorageError
└── ConfigurationError
```

Expected operational failures should be represented consistently, while unexpected programming errors should not be silently converted into generic user-facing messages.

---

# 4.6 TD-005 — History and Audit Integrity

Category:

```text
History / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The repair workflow contains history recording logic that requires correction and stronger validation.

History should represent actual operations and their actual outcomes.

A history entry should never be created merely because a progress flag is enabled.

### Required Behavior

History recording should be independent of:

```text
progress=True
```

Instead:

```text
Operation occurs
        ↓
Outcome determined
        ↓
History entry recorded
```

### Impact

Incorrect history data can make troubleshooting, auditing, and future reporting unreliable.

### Resolution Direction

History handling should be centralized and tested for:

- Success.
- Failure.
- Exception.
- Partial operation.
- Duration.
- Start time.
- End time.
- Model name.
- Model version.
- Error message.

---

# 4.7 TD-006 — Time Tracking and State Management

Category:

```text
Code Quality
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Time-related state in the repair implementation requires restructuring.

A start timestamp should belong to an individual operation rather than being stored as class-level state.

Conceptually:

```text
repair()
    ↓
started = datetime.now()
    ↓
perform operation
    ↓
finished = datetime.now()
```

rather than creating operation-specific state outside the method lifecycle.

### Impact

Incorrect timestamp scope can produce inaccurate duration information, especially when multiple operations occur during the lifetime of the same manager object.

### Resolution

Operation timing should be created and finalized within the operation itself.

A timezone-aware datetime strategy should also be considered for the final production implementation.

---

# 4.8 TD-007 — Documentation and Implementation Synchronization

Category:

```text
Documentation
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

AIPM has a substantial planning and architecture documentation layer, but documentation must remain synchronized with the actual implementation.

The following documents require continuous synchronization:

```text
PROJECT_STATUS.md
NEXT_PHASE_ROADMAP.md
ARCHITECTURE.md
TECH_DEBT.md
README.md
CHANGELOG.md
```

### Impact

Documentation that describes planned functionality as implemented functionality can create confusion about actual project status.

### Resolution

Documentation should distinguish clearly between:

```text
Implemented
Partially Implemented
Planned
Experimental
Deprecated
```

The project status document should always reflect the actual repository state.

---

# 4.9 TD-008 — Dependency and API Stability

Category:

```text
Dependency / API
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

As AIPM expands, dependency and public API boundaries require explicit stabilization.

The project should avoid allowing implementation details from internal packages to become accidental public APIs.

### Risks

Potential risks include:

- Breaking imports.
- Uncontrolled dependency growth.
- Version incompatibilities.
- External consumers depending on internal modules.
- Difficult future refactoring.

### Resolution

Define clearly:

```text
Public API
Internal API
Private Implementation
```

and document supported Python versions and dependency policies.

---

# 4.10 TD-009 — Release Process Maturity

Category:

```text
Release / Process
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The project requires a disciplined release process before reaching stable production status.

The following should eventually become mandatory:

```text
Code Complete
      ↓
Tests
      ↓
Static Analysis
      ↓
Security Checks
      ↓
Documentation Review
      ↓
Version Update
      ↓
Release Candidate
      ↓
Regression Testing
      ↓
Git Tag
      ↓
GitHub Release
```

### Impact

Without a controlled release process, version numbers, documentation, Git history, and actual implementation state can become inconsistent.

### Resolution

Implement a formal release checklist and associate releases with:

- GitHub Milestones.
- Git tags.
- Changelog entries.
- Release notes.
- Test results.

---

# 4.11 TD-010 — Performance Benchmarking

Category:

```text
Performance
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Planned
```

### Description

Performance targets have been defined conceptually, but meaningful benchmark baselines should be established before performance optimization is performed.

Important measurements include:

- CLI startup time.
- Registry lookup time.
- Download throughput.
- SHA256 verification time.
- Installation time.
- Repair time.
- Memory usage.
- History operation performance.

### Resolution

Create reproducible benchmark scenarios and store baseline measurements for comparison between releases.

Optimization decisions should be based on measured bottlenecks.

---

# 4.12 Current Debt Priority

The current priority order is:

```text
P0 — Release Blocking
    None currently confirmed.

P1 — Immediate Engineering Attention
    TD-001 Architecture Boundaries
    TD-002 Repair Manager Complexity
    TD-003 Automated Testing
    TD-004 Error Handling
    TD-005 History Integrity

P2 — Planned Near-Term Work
    TD-006 Time Tracking
    TD-007 Documentation Synchronization
    TD-008 Dependency / API Stability
    TD-009 Release Process

P3 — Future Improvement
    TD-010 Performance Benchmarking
```

This ordering should be revised whenever the repository is re-audited.

---

# 4.13 Current Debt Policy

The following rules apply to the current debt register:

1. No new significant technical debt should be introduced without justification.
2. Critical security or data-integrity debt takes precedence over feature development.
3. P1 debt should be considered during current milestone planning.
4. New debt discovered during implementation should be recorded.
5. Resolved debt should not simply disappear from the historical record.
6. Technical debt must not be used as a substitute for known bugs.
7. Every major debt item should have a corresponding GitHub Issue when project tracking is available.
8. Debt status must be updated when work begins.
9. A debt item is not considered resolved until the associated tests pass.
10. Architecture-changing debt requires an architecture review.

---

# 4.14 Current Debt Review

The current technical-debt register should be reviewed:

- Before starting a major milestone.
- Before creating a release candidate.
- Before Version 1.0.
- After major architectural refactoring.
- After security audits.
- After significant dependency upgrades.

The review should determine:

```text
New Debt
    +
Existing Debt
    +
Resolved Debt
    +
Changed Priorities
    =
Updated Technical Debt Register
```

---

# 4.15 Important Limitation

This section represents the currently identified debt based on the verified implementation context available during the preparation of this document.

It must not be interpreted as a claim that every file, package, dependency, test, or workflow in the repository has been exhaustively re-audited unless such an audit has been explicitly completed.

When a complete repository audit is performed, this section must be updated using actual repository evidence rather than assumptions.

---

# 4.16 Summary

The current AIPM technical debt is concentrated primarily around:

```text
Architecture
    ↓
Core Manager Complexity
    ↓
Testing
    ↓
Error Handling
    ↓
History Integrity
    ↓
Documentation Synchronization
    ↓
Release Engineering
```

The immediate priority should be to stabilize the existing core implementation before continuously introducing new architectural layers.

The project should therefore follow this principle:

> Stabilize → Test → Refactor → Document → Extend

This approach reduces the risk of accumulating additional debt while AIPM continues toward a stable and production-ready architecture.

# 5. Architecture Debt

Architecture debt refers to structural decisions, dependency relationships, abstraction boundaries, and system-design compromises that may make AIPM more difficult to maintain, test, extend, secure, or scale.

Architecture debt is generally more expensive to resolve than localized code debt because architectural problems can affect multiple packages and workflows simultaneously.

The objective of this section is not to force premature abstraction. AIPM is still evolving, and the architecture should remain proportionate to the current project size. The objective is to identify structural risks early enough that they do not become permanent constraints.

---

## 5.1 AD-001 — Manager Responsibility Concentration

Category:

```text
Architecture
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Several AIPM manager components act as both orchestration layers and direct integration points for multiple subsystems.

The repair workflow is a clear example:

```text
RepairManager
    │
    ├── Registry
    ├── Verify
    ├── Remove
    ├── Download
    └── History
```

This is acceptable for a small application, but continued expansion of this pattern can turn manager classes into large coordination points containing too much application logic.

### Architectural Risk

If this pattern continues, managers may become:

* Difficult to test in isolation.
* Highly coupled to infrastructure.
* Difficult to replace or extend.
* Difficult to expose through future APIs.
* Difficult to reuse from CLI, GUI, or service interfaces.

### Resolution Direction

Gradually separate:

```text
Interface Layer
        ↓
Application Service
        ↓
Domain Operation
        ↓
Infrastructure
```

The existing public manager interfaces should not be broken unnecessarily.

Refactoring should be incremental rather than introducing a large abstraction hierarchy prematurely.

---

## 5.2 AD-002 — Direct Cross-Package Coupling

Category:

```text
Architecture / Dependency Management
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Core managers directly import and invoke other package managers.

For example, the repair implementation directly depends on:

```text
download_manager
registry_manager
remove_manager
verify_manager
history_manager
```

This creates explicit coupling between several subsystems.

### Architectural Risk

Direct manager-to-manager dependencies can eventually create:

* Dependency chains.
* Circular dependencies.
* Difficult mocking.
* Tight coupling.
* Reduced replaceability.
* Difficult dependency analysis.

### Resolution Direction

The dependency graph should remain directional.

Preferred conceptual flow:

```text
CLI / Interface
       ↓
Application Services
       ↓
Domain Services
       ↓
Repositories / Infrastructure
```

Higher-level workflows may coordinate lower-level services, but lower-level components should not depend on higher-level interfaces.

---

## 5.3 AD-003 — Insufficient Separation Between Domain and Infrastructure

Category:

```text
Architecture
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Operations such as downloading, filesystem manipulation, verification, logging, and history persistence are infrastructure-oriented concerns.

When these concerns are directly embedded into application workflows, the domain logic becomes dependent on concrete infrastructure implementations.

### Example

A repair operation conceptually requires:

```text
Verify Model
Remove Invalid Installation
Download Model
Verify Reinstallation
Record Result
```

The business workflow should not need to know every low-level detail of:

* HTTP/network access.
* Filesystem implementation.
* Hash calculation.
* Storage format.
* Logging backend.

### Resolution Direction

Over time, introduce appropriate interfaces around infrastructure boundaries.

For example:

```text
ModelDownloader
ModelVerifier
ModelRepository
HistoryRepository
StorageProvider
```

Concrete implementations can then remain in the infrastructure layer.

The abstraction should be introduced when there is a real need for substitution or isolation; unnecessary interfaces should be avoided.

---

## 5.4 AD-004 — Registry as a Potential Architectural Bottleneck

Category:

```text
Architecture / Data Management
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The registry is a central source of model information.

A typical workflow begins with:

```text
Model Name
    ↓
Registry Lookup
    ↓
Model Metadata
    ↓
Operation
```

As AIPM grows, more components may begin depending directly on registry behavior.

### Architectural Risk

The registry can become an architectural bottleneck if:

* Every subsystem accesses it directly.
* Its internal representation becomes part of the public API.
* Registry storage and registry business logic become inseparable.
* Future remote registries become difficult to support.

### Resolution Direction

Separate the concepts of:

```text
Registry API
Registry Domain Model
Registry Storage
Registry Provider
```

This allows future implementations such as:

```text
Local Registry
Remote Registry
Cached Registry
Enterprise Registry
```

without requiring changes throughout the application.

---

## 5.5 AD-005 — Storage Abstraction Risk

Category:

```text
Architecture / Storage
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

AIPM currently operates primarily around filesystem-oriented package/model management.

This is appropriate for the current stage, but storage assumptions should not become deeply embedded throughout business logic.

### Architectural Risk

Future requirements may include:

* Multiple storage locations.
* Configurable model directories.
* Cache management.
* Database-backed metadata.
* Remote storage.
* Cloud storage.
* Enterprise storage policies.

If filesystem operations are scattered throughout domain logic, future migration becomes expensive.

### Resolution Direction

Maintain a clear storage boundary:

```text
Application
    ↓
Storage Interface
    ↓
Filesystem / Database / Remote Storage
```

The project should not introduce a database abstraction merely because one may be needed in the future. It should first establish a clean boundary around storage responsibilities.

---

## 5.6 AD-006 — History as a Cross-Cutting Concern

Category:

```text
Architecture / Audit
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

History is relevant to multiple operations:

```text
Install
Update
Remove
Repair
Verify
Download
```

If each manager implements its own history-recording behavior, history semantics may become inconsistent.

### Architectural Risk

Potential consequences include:

* Different status definitions.
* Inconsistent timestamps.
* Missing failure records.
* Different message formats.
* Duplicate persistence logic.
* Inconsistent audit information.

### Resolution Direction

History should be treated as a centralized application concern with a consistent interface.

Conceptually:

```text
Operation
    ↓
Operation Result
    ↓
History Service
    ↓
History Repository
```

Individual managers should provide operation outcomes rather than implementing their own independent history persistence mechanisms.

---

## 5.7 AD-007 — Result Models and Exception Boundaries

Category:

```text
Architecture / Error Handling
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

AIPM currently uses result models such as `RepairResult` while some failures are communicated through exceptions.

This can be a valid design, but the boundary between expected operational failures and unexpected programming errors must be explicit.

### Architectural Risk

Without a defined error architecture:

```text
Exception
    +
Result Object
    +
String Message
```

may evolve into inconsistent error handling across packages.

### Resolution Direction

Establish a consistent policy:

```text
Expected Operational Failure
        ↓
Domain/Application Result or Typed Exception

Unexpected Programming Failure
        ↓
Exception + Logging + Diagnostic Context
```

The same policy should apply consistently across core operations.

---

## 5.8 AD-008 — CLI Coupling Risk

Category:

```text
Architecture / Interface
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The CLI is currently a primary user interface for AIPM.

The CLI should remain an interface layer rather than becoming the location where business logic is implemented.

### Architectural Rule

Preferred:

```text
CLI
 ↓
Application Service
 ↓
Domain Logic
```

Avoid:

```text
CLI
 ↓
Direct Filesystem
 ↓
Direct Download
 ↓
Direct Registry Manipulation
```

### Impact

Strong CLI coupling would make future interfaces difficult to add.

Potential future interfaces include:

```text
CLI
GUI
REST API
Python API
Plugin Interface
```

All should be able to reuse the same application/domain services.

---

## 5.9 AD-009 — Public API Boundary Not Yet Fully Stabilized

Category:

```text
Architecture / API
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

AIPM is still under active architectural development.

Consequently, the distinction between:

```text
Public API
Internal API
Private Implementation
```

must be explicitly stabilized before Version 1.0.

### Risk

If internal implementation details become publicly consumed, future refactoring may create unnecessary breaking changes.

### Resolution Direction

Before stable release:

* Define supported public imports.
* Define supported manager interfaces.
* Define public models.
* Hide implementation details where appropriate.
* Document compatibility guarantees.
* Establish deprecation policy.

---

## 5.10 AD-010 — Dependency Direction Must Remain Controlled

Category:

```text
Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

As additional packages are introduced, uncontrolled imports can gradually create a tangled dependency graph.

The project should maintain a predictable dependency direction.

### Preferred Structure

```text
Presentation / CLI
        ↓
Application
        ↓
Domain
        ↓
Infrastructure
```

Supporting components such as logging, configuration, and shared models should have carefully controlled dependency relationships.

### Rule

A lower-level package should not depend on a higher-level interface merely because doing so is convenient.

---

## 5.11 AD-011 — Repair Workflow Should Remain an Application Workflow

Category:

```text
Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Repair is not a primitive filesystem operation. It is a multi-step application workflow.

Conceptually:

```text
Resolve Model
     ↓
Inspect Installation
     ↓
Determine Repair Necessity
     ↓
Remove Invalid State
     ↓
Acquire Model
     ↓
Verify Integrity
     ↓
Record Result
```

This workflow should remain at an application-service level rather than being pushed into individual low-level packages.

### Architectural Principle

Low-level components should perform individual responsibilities.

The application layer should coordinate them.

---

## 5.12 AD-012 — Premature Abstraction Risk

Category:

```text
Architecture / Process
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Accepted / Monitored
```

### Description

Because AIPM is intended to become scalable and extensible, there is a risk of introducing abstractions before actual requirements justify them.

Examples could include:

* Excessive repository interfaces.
* Multiple layers for simple operations.
* Unnecessary service classes.
* Generic factories without multiple implementations.
* Excessive dependency injection.

### Risk

Over-abstraction can produce:

* More files.
* More indirection.
* Higher cognitive load.
* More difficult debugging.
* Slower development.

### Resolution Principle

Follow:

```text
Simple First
    ↓
Observe Repetition
    ↓
Identify Stable Boundary
    ↓
Abstract When Justified
```

The project should optimize for architectural clarity rather than maximum abstraction.

---

# 5.13 Architecture Debt Priority

Current architecture-debt priorities are:

| ID     | Debt                                 | Priority |
| ------ | ------------------------------------ | -------- |
| AD-001 | Manager Responsibility Concentration | P1       |
| AD-002 | Direct Cross-Package Coupling        | P1       |
| AD-003 | Domain / Infrastructure Separation   | P1       |
| AD-004 | Registry Architectural Bottleneck    | P2       |
| AD-005 | Storage Abstraction Risk             | P2       |
| AD-006 | History as Cross-Cutting Concern     | P1       |
| AD-007 | Result / Exception Boundaries        | P1       |
| AD-008 | CLI Coupling Risk                    | P2       |
| AD-009 | Public API Stabilization             | P2       |
| AD-010 | Dependency Direction                 | P2       |
| AD-011 | Repair Workflow Boundary             | P2       |
| AD-012 | Premature Abstraction Risk           | P2       |

---

# 5.14 Architecture Debt Resolution Order

Architecture debt should not be resolved by creating an entirely new architecture in a single step.

The preferred sequence is:

```text
1. Stabilize Existing Behavior
            ↓
2. Add Automated Tests
            ↓
3. Define Dependency Boundaries
            ↓
4. Standardize Error / Result Semantics
            ↓
5. Reduce Manager Coupling
            ↓
6. Separate Infrastructure Boundaries
            ↓
7. Stabilize Public APIs
            ↓
8. Introduce Additional Abstractions Only Where Required
```

This minimizes the risk of breaking working functionality during architectural refactoring.

---

# 5.15 Architecture Refactoring Rules

Architecture changes must follow these rules:

1. Existing functionality must remain protected by tests.
2. Public APIs should not be changed without a documented reason.
3. Large architectural changes should be divided into small Pull Requests.
4. Every architectural change must update `ARCHITECTURE.md`.
5. Significant architectural debt must be tracked in `TECH_DEBT.md`.
6. Breaking changes require explicit versioning consideration.
7. Refactoring must not be mixed unnecessarily with unrelated feature work.
8. New abstractions must have a documented justification.
9. Dependency direction must be reviewed after major refactoring.
10. Architecture changes must be validated through integration tests.

---

# 5.16 Architecture Debt Exit Criteria

Architecture debt should be considered resolved only when:

* Responsibility boundaries are clearly defined.
* Dependency direction is controlled.
* Core workflows have sufficient automated coverage.
* Error and result semantics are consistent.
* Infrastructure boundaries are clear.
* Public APIs are explicitly defined.
* Documentation reflects the new architecture.
* Integration tests pass.
* No new circular dependencies have been introduced.

---

# 5.17 Architectural Target State

The long-term target architecture is conceptually:

```text
                    AIPM Interfaces
                          │
             ┌────────────┼────────────┐
             │            │            │
            CLI          GUI         REST/API
             │            │            │
             └────────────┼────────────┘
                          ↓
                 Application Services
                          │
             ┌────────────┼────────────┐
             │            │            │
          Registry      Package      History
          Services     Services      Services
             │            │            │
             └────────────┼────────────┘
                          ↓
                    Domain Models
                          │
                          ↓
                 Infrastructure Layer
             ┌────────────┼────────────┐
             │            │            │
          Storage       Network      Verification
             │            │            │
             └────────────┼────────────┘
                          ↓
                  Operating System
```

This is a target architectural direction, not a requirement to immediately create every layer shown above.

The implementation should evolve toward this structure only when the project's actual complexity justifies each boundary.

---

# 5.18 Summary

The most important architectural debt in AIPM is not the absence of additional features. It is the risk of allowing the existing core workflows to become increasingly coupled as new functionality is added.

The immediate architectural strategy should therefore be:

```text
Do Not Expand Indefinitely
            ↓
Stabilize Core
            ↓
Test Core
            ↓
Control Dependencies
            ↓
Clarify Responsibilities
            ↓
Refactor Carefully
            ↓
Then Expand
```

The central architectural principle is:

> AIPM should evolve incrementally without allowing short-term implementation convenience to become long-term architectural coupling.

Architecture debt should be reduced progressively while preserving working behavior, maintaining test coverage, and keeping the project structure understandable to future contributors.

# 6. Code Debt

Code debt refers to implementation-level compromises that make AIPM source code more difficult to read, test, maintain, debug, modify, or extend.

Unlike architecture debt, which concerns the structure and relationships between system components, code debt primarily concerns the quality and maintainability of individual modules, classes, methods, control flow, state management, error handling, naming, typing, and implementation patterns.

Code debt is expected to exist during active development. However, unresolved code debt should not be allowed to accumulate indefinitely because small implementation compromises can eventually become significant maintenance problems.

The objective of this section is to identify current code-level risks and establish a controlled strategy for reducing them without unnecessary rewrites.

---

## 6.1 CD-001 — Repair Method Is Too Large

Category:

```text
Code / Maintainability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The current `RepairManager.repair()` method coordinates a large number of operations within a single method.

The workflow currently includes:

```text
Registry Lookup
        ↓
Verification
        ↓
Health Check
        ↓
Remove
        ↓
Download
        ↓
Final Verification
        ↓
History
        ↓
Return Result
```

This makes the method responsible for both workflow orchestration and several implementation details.

### Impact

A large method increases:

* Cognitive complexity.
* Testing complexity.
* Regression risk.
* Difficulty of debugging.
* Difficulty of future modification.

### Resolution

The method should remain the primary orchestration point, but individual responsibilities should gradually be extracted into appropriately named private or service-level operations when justified.

For example:

```text
_repair_required()
_remove_corrupted_installation()
_download_model()
_verify_repaired_installation()
_record_repair_history()
```

The exact decomposition should be determined after test coverage is established.

---

## 6.2 CD-002 — Excessive Nesting and Formatting Inconsistency

Category:

```text
Code Quality
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The current implementation contains formatting and indentation patterns that make the control flow harder to visually inspect.

In particular, the repair implementation contains sections where comments, indentation, and statements are not consistently aligned.

This is more than a cosmetic issue because inconsistent formatting makes structural errors harder to identify during code review.

### Impact

Potential consequences include:

* Misreading control flow.
* Accidentally placing statements inside the wrong conditional block.
* Difficult code review.
* Reduced readability.
* Increased maintenance cost.

### Resolution

The project should enforce automated formatting and linting.

Recommended checks include:

```text
Formatter
    ↓
Linter
    ↓
Type Checker
    ↓
Tests
```

Formatting should be automatically applied rather than manually maintained.

---

## 6.3 CD-003 — Operation Start Time Has Incorrect Scope

Category:

```text
Code Correctness
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The current repair implementation contains a timestamp assignment outside the `repair()` method:

```text
started = datetime.now()
```

This means the timestamp is associated with object/module initialization rather than reliably representing the beginning of an individual repair operation.

### Impact

This can produce incorrect:

* Start timestamps.
* Operation durations.
* History records.

It becomes especially problematic when the same `RepairManager` instance performs multiple repairs.

### Resolution

The start timestamp must be created when the operation begins:

```text
repair()
    ↓
started = current time
    ↓
perform repair
    ↓
finished = current time
```

Every repair invocation should have its own independent timing state.

---

## 6.4 CD-004 — History Logic Is Coupled to Progress Output

Category:

```text
Code Correctness / Maintainability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The current implementation places history-related behavior within a `progress` conditional.

Conceptually, this creates an incorrect relationship:

```text
progress=True
        ↓
History behavior
```

Progress reporting and audit/history recording are separate concerns.

### Correct Relationship

The intended architecture should be:

```text
Operation
    ↓
Determine Outcome
    ↓
Record History
```

while:

```text
progress=True
    ↓
Display Additional User Feedback
```

should remain independent.

### Impact

If history recording depends on progress output, an operation performed without progress reporting may produce incomplete audit information.

### Resolution

History recording must be independent of the `progress` parameter.

---

## 6.5 CD-005 — Generic Exception Handling

Category:

```text
Code Quality / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The repair workflow currently catches:

```text
Exception
```

around the download operation.

Catching the base `Exception` type can be appropriate at a top-level boundary, but it is too broad for internal business logic when the code does not distinguish expected operational failures from programming errors.

### Impact

Potential consequences include:

* Hiding programming defects.
* Losing useful exception context.
* Making automated testing less precise.
* Making error diagnosis harder.
* Converting unrelated failures into generic repair failures.

### Resolution

Use specific exception types wherever possible.

Conceptually:

```text
DownloadError
NetworkError
ChecksumError
StorageError
```

Unexpected programming errors should normally be allowed to propagate to an appropriate top-level error boundary where they can be logged with diagnostic context.

---

## 6.6 CD-006 — Result Model Semantics Need Stabilization

Category:

```text
Code / API Design
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

`RepairResult` currently exposes several boolean properties:

```text
success
repaired
downloaded
verified
```

These values can represent multiple dimensions of an operation, but their semantic relationships should be explicitly defined.

For example:

```text
success=False
repaired=True
downloaded=False
verified=False
```

is possible and may be valid, but the meaning of `repaired=True` after a failed operation needs to be clearly documented.

### Impact

Ambiguous result semantics can create inconsistent behavior in:

* CLI output.
* Tests.
* History.
* Future API consumers.
* Automation.

### Resolution

Define precise semantics for every result field.

If necessary, evolve toward a richer result model containing:

```text
status
operation
message
error_code
repaired
downloaded
verified
duration
```

Any such change should be made only after the current behavior is protected by tests.

---

## 6.7 CD-007 — Repeated Verification Conditions

Category:

```text
Code Duplication
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The repair workflow checks the same logical health condition more than once:

```text
exists
AND
checksum_valid
AND
metadata_valid
```

Repeated conditions can become a maintenance problem if the definition of a healthy installation changes.

### Resolution

The verification result should ideally expose a clear semantic property or method representing the overall state.

For example:

```text
verify_result.is_healthy
```

rather than repeatedly reconstructing the definition of health in multiple locations.

The exact implementation should remain consistent with the existing verification model.

---

## 6.8 CD-008 — String-Based Status and Error Semantics

Category:

```text
Code Quality / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Human-readable messages are currently used heavily to communicate operation outcomes.

Messages such as:

```text
"Model is already healthy."
"Repair completed successfully."
"SHA256 mismatch."
```

are useful for users but should not become the primary machine-readable representation of state.

### Impact

Using messages as state can lead to:

* Difficult programmatic handling.
* Fragile tests.
* Inconsistent CLI output.
* Localization difficulties in the future.

### Resolution

Use structured status/error information internally.

For example:

```text
Status:
    SUCCESS
    FAILED
    ALREADY_HEALTHY
    CHECKSUM_MISMATCH
    DOWNLOAD_FAILED
```

Human-readable messages should be generated from structured state.

---

## 6.9 CD-009 — Repeated `datetime.now()` Calls

Category:

```text
Code Quality / Reliability
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Identified
```

### Description

The history logic may evaluate the current time multiple times during one operation:

```text
finished = datetime.now()

duration = (
    datetime.now() - started
).total_seconds()
```

These calls can produce slightly different timestamps.

### Impact

This can cause minor inconsistencies between:

* Recorded finish time.
* Calculated duration.

### Resolution

Capture the finish time once:

```text
finished = current_time()
duration = finished - started
```

This also makes testing easier.

---

## 6.10 CD-010 — Timezone-Aware Datetime Requirement

Category:

```text
Code Quality / Portability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The current implementation uses naive datetime values.

Naive timestamps can become problematic when:

* Logs are generated across time zones.
* History is synchronized between machines.
* AIPM becomes distributed.
* Data is exported.
* Timestamps are consumed by external APIs.

### Resolution

The project should establish a single timestamp policy.

For persistent history and machine-readable data, timezone-aware UTC timestamps are recommended.

The policy should be applied consistently throughout AIPM rather than only within the repair package.

---

## 6.11 CD-011 — Logging and User Feedback Are Not Fully Separated

Category:

```text
Code Quality / Interface
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

The repair implementation uses logging for progress information:

```text
Checking registry...
Verifying installation...
Downloading latest model...
Running final verification...
```

Logging and CLI progress output are related but conceptually different concerns.

### Risk

If the same logging behavior becomes the user interface contract, future interfaces such as:

```text
GUI
REST API
Python API
```

may inherit CLI-specific behavior.

### Resolution

Application operations should return structured results.

The CLI should decide how those results are presented.

Logging should remain primarily diagnostic.

---

## 6.12 CD-012 — Potential Dead or Redundant Imports

Category:

```text
Code Quality
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Identified
```

### Description

The repair package imports several models and components.

As implementation changes, imports that are no longer required can remain in the source code.

Unused imports should not be allowed to accumulate.

### Resolution

Static analysis should detect:

* Unused imports.
* Unused variables.
* Unreachable code.
* Undefined names.
* Incorrect type usage.

These should be automatically checked in CI.

---

## 6.13 CD-013 — Missing Explicit Return Type Policy Across the Codebase

Category:

```text
Code Quality / Type Safety
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

AIPM uses Python type annotations, which is positive for maintainability.

However, type-annotation standards should be applied consistently across all public and internal functions.

### Resolution

Establish a project-wide rule:

```text
Every public function
    ↓
Parameter annotations
    +
Return annotation
```

For important internal functions, annotations should also be used where they materially improve readability or static analysis.

---

## 6.14 CD-014 — Public Models Need Stronger Validation Semantics

Category:

```text
Code Quality / Data Validation
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Pydantic models are used for structured results such as:

```text
RepairResult
```

This provides type validation, but field-level semantic constraints may need to be strengthened as the project grows.

For example, relationships between:

```text
success
repaired
downloaded
verified
```

should be explicitly defined where appropriate.

### Resolution

Review all public Pydantic models for:

* Field constraints.
* Default behavior.
* Optional vs required fields.
* Enum usage.
* Validation rules.
* Serialization behavior.

---

## 6.15 CD-015 — Magic Strings in Operational Messages

Category:

```text
Code Quality
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Identified
```

### Description

Operational messages are currently written directly inside methods.

For example:

```text
"Checking registry..."
"Verifying installation..."
"Removing corrupted model..."
"Downloading latest model..."
```

This is acceptable for an early implementation but can become inconsistent as more commands and interfaces are added.

### Resolution

Do not prematurely centralize every message.

Instead, first establish structured operation states and consistent CLI presentation.

Message centralization should be introduced only if multiple interfaces or localization requirements justify it.

---

# 6.16 CD-016 — Incomplete Method-Level Contracts

Category:

```text
Code Quality / Documentation
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Docstrings exist in the repair package, but method-level contracts should eventually document more than the high-level purpose.

Important public methods should specify:

* Parameters.
* Return type.
* Expected exceptions.
* Side effects.
* State changes.
* Failure behavior.

### Resolution

Use a consistent docstring convention throughout AIPM.

For example:

```text
Method
    ↓
Purpose
    ↓
Parameters
    ↓
Returns
    ↓
Raises
    ↓
Side Effects
```

The exact documentation format should be standardized project-wide.

---

# 6.17 CD-017 — Insufficient Guarding of Multi-Step Operations

Category:

```text
Code Correctness
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Repair is a destructive multi-step operation:

```text
Existing Installation
        ↓
Remove
        ↓
Download
        ↓
Verify
```

A failure between removal and successful reinstallation can temporarily leave the model unavailable.

### Risk

Potential outcomes include:

* Model loss after failed download.
* Partial installation.
* Inconsistent filesystem state.
* Recovery difficulty.

### Resolution Direction

The long-term implementation should consider safer transactional behavior where practical.

Potential strategy:

```text
Existing Model
      ↓
Prepare Temporary Location
      ↓
Download
      ↓
Verify SHA256
      ↓
Atomically Replace
      ↓
Record Success
```

This should be implemented only after the existing download, verification, and storage behavior is fully understood and tested.

---

# 6.18 CD-018 — Lack of Explicit Idempotency Guarantees

Category:

```text
Code Quality / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Core operations should define whether repeated execution is safe.

Examples:

```text
verify()
remove()
repair()
download()
install()
```

A command that is executed twice should have predictable behavior.

### Resolution

Document idempotency expectations for every core operation.

For example:

```text
verify()
    Safe to repeat.

remove()
    Should produce a predictable result if already absent.

repair()
    Should produce a consistent result when the model is already healthy.
```

The exact semantics should be enforced through tests.

---

# 6.19 Code Debt Priority Matrix

Current code-debt priorities:

| ID     | Debt                          | Severity | Priority |
| ------ | ----------------------------- | -------- | -------- |
| CD-001 | Large Repair Method           | High     | P1       |
| CD-002 | Formatting / Nesting          | Medium   | P2       |
| CD-003 | Incorrect Time Scope          | High     | P1       |
| CD-004 | History / Progress Coupling   | High     | P1       |
| CD-005 | Generic Exception Handling    | High     | P1       |
| CD-006 | Result Model Semantics        | Medium   | P2       |
| CD-007 | Repeated Health Condition     | Medium   | P2       |
| CD-008 | String-Based Error Semantics  | Medium   | P2       |
| CD-009 | Repeated Datetime Calls       | Low      | P3       |
| CD-010 | Timezone-Aware Datetime       | Medium   | P2       |
| CD-011 | Logging / UI Separation       | Medium   | P2       |
| CD-012 | Unused / Redundant Imports    | Low      | P3       |
| CD-013 | Type Annotation Policy        | Medium   | P2       |
| CD-014 | Pydantic Validation Semantics | Medium   | P2       |
| CD-015 | Operational Magic Strings     | Low      | P3       |
| CD-016 | Method-Level Contracts        | Medium   | P2       |
| CD-017 | Multi-Step Operation Safety   | High     | P1       |
| CD-018 | Idempotency Guarantees        | Medium   | P2       |

---

# 6.20 Code Debt Resolution Strategy

Code debt should be resolved incrementally.

The preferred sequence is:

```text
1. Establish Tests
        ↓
2. Correct Known Bugs
        ↓
3. Fix High-Risk State Problems
        ↓
4. Standardize Error Handling
        ↓
5. Stabilize Result Models
        ↓
6. Reduce Large Methods
        ↓
7. Improve Type Safety
        ↓
8. Apply Formatting / Linting
        ↓
9. Improve Documentation
        ↓
10. Perform General Cleanup
```

This order is intentional.

Cosmetic cleanup should not take precedence over correctness, data integrity, security, or testability.

---

# 6.21 Code Quality Rules

The following rules should gradually become project standards:

1. Public functions must have type annotations.
2. Public classes and methods must have useful docstrings.
3. Functions should have a single clear responsibility.
4. Large methods should be reviewed for decomposition.
5. Generic exceptions should not be used where specific exceptions are available.
6. Human-readable messages should not replace machine-readable status.
7. Persistent timestamps should follow one project-wide policy.
8. Operation state should not be stored unintentionally at module or class scope.
9. Duplicate business logic should be consolidated when repetition becomes meaningful.
10. Formatting and linting should be automated.
11. Refactoring should be protected by tests.
12. Destructive operations should define failure and recovery behavior.
13. Core operations should define idempotency expectations.
14. Code cleanup should not introduce unnecessary abstractions.

---

# 6.22 Definition of Code Debt Resolved

A code-debt item should not be marked `Resolved` merely because the source code has been changed.

It should be considered resolved when:

```text
Implementation Updated
        ↓
Relevant Tests Added / Updated
        ↓
Tests Passing
        ↓
Static Analysis Passing
        ↓
Behavior Verified
        ↓
Documentation Updated
        ↓
Technical Debt Record Updated
```

For high-priority code debt, regression testing is mandatory.

---

# 6.23 Code Debt Review Policy

Code debt should be reviewed:

* During every major refactoring.
* Before merging architectural changes.
* Before release candidates.
* During milestone planning.
* After significant bug fixes.
* When introducing new core managers.
* When adding new dependencies.

Code debt should not become an excuse for continuous rewriting.

The preferred approach is:

```text
Improve Existing Code
        +
Preserve Working Behavior
        +
Add Tests
        +
Refactor Incrementally
```

---

# 6.24 Summary

The current code debt in AIPM is primarily concentrated around:

```text
Method Complexity
        ↓
State Management
        ↓
Error Handling
        ↓
History Semantics
        ↓
Result Model Semantics
        ↓
Type Safety
        ↓
Testing
        ↓
Operational Reliability
```

The most important principle is:

> Correctness and testability must come before cosmetic cleanup.

AIPM should not undergo a complete rewrite merely to eliminate code debt. Existing working behavior should first be protected with automated tests, after which high-risk implementation problems should be corrected incrementally.

The preferred engineering cycle is:

```text
Understand
    ↓
Test
    ↓
Correct
    ↓
Refactor
    ↓
Verify
    ↓
Document
```

This approach allows AIPM to improve its code quality continuously while minimizing unnecessary disruption to the existing implementation.

# 7. Testing Debt

Testing debt refers to the accumulated gap between the level of automated verification currently available in AIPM and the level required to confidently maintain, refactor, release, and operate the project.

Testing debt is one of the highest-risk categories of technical debt because architectural and code changes made without sufficient automated coverage can introduce regressions without being detected.

For AIPM, testing is particularly important because several core operations are state-changing and potentially destructive:

```text
Download
   ↓
Install
   ↓
Verify
   ↓
Update
   ↓
Repair
   ↓
Remove
```

A failure in any of these operations can result in corrupted files, incomplete installations, invalid metadata, incorrect history records, or loss of a usable model.

The objective of this section is to identify testing gaps, define the required test layers, and establish minimum testing requirements for future milestones and releases.

---

## 7.1 TD-TEST-001 — Insufficient Core Workflow Coverage

Category:

```text
Testing
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

The core AIPM lifecycle requires comprehensive automated testing before significant architectural expansion.

The following workflows are considered critical:

```text
Registry
Download
Install
Verify
Update
Repair
Remove
History
```

Each workflow requires both successful-path and failure-path tests.

### Required Coverage

At minimum:

```text
Success
Failure
Invalid Input
Missing Resource
Corrupted State
Dependency Failure
Recovery
```

---

## 7.2 TD-TEST-002 — Repair Workflow Testing Gap

Category:

```text
Testing / Repair
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

The repair workflow should have dedicated tests because it combines multiple operations.

Required scenarios include:

1. Model does not exist in registry.
2. Model is healthy.
3. Model files are missing.
4. Checksum is invalid.
5. Metadata is invalid.
6. Removal succeeds.
7. Removal fails.
8. Download succeeds.
9. Download fails.
10. Final verification succeeds.
11. Final verification fails.
12. History records success.
13. History records failure.
14. Unexpected exception occurs.
15. Repair is executed against an already healthy model.

The objective is to ensure that every branch of the repair state machine is tested.

---

## 7.3 TD-TEST-003 — Missing Failure-Path Coverage

Category:

```text
Testing / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Successful execution is not sufficient for a package manager.

AIPM must be tested heavily against failure conditions because external resources such as network connections and filesystem state cannot always be trusted.

Important failure cases include:

```text
Network unavailable
Download interrupted
Invalid URL
HTTP failure
Checksum mismatch
Missing file
Permission failure
Disk failure
Invalid metadata
Registry entry missing
Corrupted model
Unexpected exception
```

### Resolution

Failure-path tests should be treated as first-class tests rather than optional edge-case tests.

---

## 7.4 TD-TEST-004 — Filesystem Isolation

Category:

```text
Testing / Infrastructure
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM performs filesystem operations.

Tests must therefore avoid modifying the developer's real model directory or personal configuration.

Tests should use isolated temporary environments.

Conceptually:

```text
Test Starts
    ↓
Create Temporary Directory
    ↓
Prepare Test State
    ↓
Execute Operation
    ↓
Verify Result
    ↓
Destroy Temporary Directory
```

The test environment must be automatically cleaned up.

---

## 7.5 TD-TEST-005 — Network Isolation

Category:

```text
Testing / Infrastructure
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Tests should not depend on live internet connectivity unless they are explicitly classified as integration tests.

Unit tests should mock or substitute network operations.

The following should be simulated:

```text
Successful Download
Timeout
Connection Failure
HTTP Error
Incomplete Response
Corrupted Content
Checksum Mismatch
```

This ensures deterministic test execution.

---

## 7.6 TD-TEST-006 — Checksum Verification Coverage

Category:

```text
Testing / Security
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

SHA256 verification is a security-critical part of model management.

At minimum, tests must verify:

```text
Correct SHA256
    → Valid

Incorrect SHA256
    → Invalid

Missing SHA256
    → Defined failure behavior

Corrupted Download
    → Invalid

Modified File
    → Invalid
```

A checksum mismatch must never be interpreted as a successful installation or repair.

---

## 7.7 TD-TEST-007 — Metadata Validation Coverage

Category:

```text
Testing / Data Integrity
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Metadata validation should be tested independently from checksum validation.

Required cases include:

* Valid metadata.
* Missing metadata.
* Invalid metadata.
* Incomplete metadata.
* Unexpected metadata values.
* Version mismatch.
* Model-name mismatch.
* Invalid metadata format.

The test suite should verify that metadata corruption cannot be silently accepted.

---

## 7.8 TD-TEST-008 — Result Model Testing

Category:

```text
Testing / API
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Models such as `RepairResult` should have explicit tests for their validation and semantic behavior.

For example:

```text
success=True
repaired=False
downloaded=False
verified=True
```

may represent a healthy model that required no repair.

Another result might represent:

```text
success=False
repaired=True
downloaded=False
verified=False
```

The project must define whether such combinations are valid and what they mean.

Tests should prevent accidental semantic changes.

---

## 7.9 TD-TEST-009 — History Testing Gap

Category:

```text
Testing / Audit
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

History is an important audit mechanism and requires independent testing.

Tests should verify:

* Successful operations create correct history.
* Failed operations create correct history.
* Start time is correct.
* Finish time is correct.
* Duration is correct.
* Model name is correct.
* Version is correct.
* Operation type is correct.
* Status is correct.
* Error message is correct.
* History is not dependent on progress output.

The same operation should not produce different audit behavior merely because:

```text
progress=True
```

or:

```text
progress=False
```

was selected.

---

## 7.10 TD-TEST-010 — CLI Testing Gap

Category:

```text
Testing / User Interface
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

The CLI should eventually be tested independently from the underlying application logic.

Tests should verify:

```text
Command Parsing
Argument Validation
Option Handling
Output
Exit Code
Error Display
Progress Behavior
```

For example:

```text
aipm repair model-name
```

should be tested for:

* Successful repair.
* Already healthy model.
* Missing model.
* Failed repair.
* Invalid command arguments.

---

## 7.11 TD-TEST-011 — Exit Code Testing

Category:

```text
Testing / CLI
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

AIPM should use predictable exit codes.

The exact exit-code specification should be defined before stable CLI release.

Conceptually:

```text
0  → Success

Non-zero
    → Failure
```

Different classes of failure may eventually receive different codes.

Tests should verify that the CLI returns the correct exit status for each defined condition.

---

## 7.12 TD-TEST-012 — Regression Testing Debt

Category:

```text
Testing / Maintenance
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Every significant bug discovered in AIPM should eventually receive a regression test.

The expected workflow is:

```text
Bug Found
    ↓
Reproduce
    ↓
Write Regression Test
    ↓
Fix Bug
    ↓
Run Test
    ↓
Prevent Recurrence
```

A bug fix without a regression test should be considered incomplete when a deterministic test is practical.

---

## 7.13 TD-TEST-013 — Test Fixtures and Test Data

Category:

```text
Testing / Maintainability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

AIPM requires reusable test fixtures for common states.

Potential fixtures include:

```text
Healthy Model
Missing Model
Corrupted Model
Invalid Metadata
Invalid Checksum
Valid Registry Entry
Missing Registry Entry
Successful Download
Failed Download
```

Fixtures should be deterministic and isolated.

---

## 7.14 TD-TEST-014 — Unit and Integration Test Boundary

Category:

```text
Testing / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

The project should clearly distinguish unit tests from integration tests.

### Unit Tests

Unit tests should verify isolated behavior.

Examples:

```text
RepairResult validation
Checksum calculation
Metadata validation
Registry lookup logic
Result-state logic
```

External filesystem and network dependencies should normally be mocked or isolated.

### Integration Tests

Integration tests should verify actual collaboration:

```text
Registry
   ↓
Download
   ↓
Storage
   ↓
Verification
   ↓
History
```

Both levels are necessary.

---

## 7.15 TD-TEST-015 — Test Determinism

Category:

```text
Testing / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Tests should produce the same result when executed repeatedly under the same conditions.

Potential sources of nondeterminism include:

* Real network connections.
* Current timestamps.
* Random temporary data.
* Shared filesystem state.
* Environment-specific configuration.
* Global state.
* Test execution order.

Tests that intermittently pass and fail must be treated as defects.

---

## 7.16 TD-TEST-016 — Time-Dependent Logic Testing

Category:

```text
Testing / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

History and duration calculations depend on time.

Tests should not depend on actual wall-clock timing where deterministic behavior is required.

A clock abstraction or controlled time source may eventually be appropriate.

Tests should verify:

```text
started
finished
duration
```

without requiring the test to wait for real time to pass.

---

## 7.17 TD-TEST-017 — Concurrency Testing

Category:

```text
Testing / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Status:

```text
Planned
```

Concurrency may become important when AIPM supports:

* Multiple simultaneous downloads.
* Parallel model verification.
* Multiple CLI processes.
* Background operations.
* Shared model storage.

The project should not introduce concurrency prematurely.

However, once concurrent operations are supported, tests must cover:

```text
Concurrent Download
Concurrent Install
Concurrent Repair
Concurrent History Writes
Concurrent Registry Access
```

and race conditions must be explicitly investigated.

---

## 7.18 TD-TEST-018 — Platform Compatibility Testing

Category:

```text
Testing / Compatibility
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

If AIPM supports multiple operating systems, filesystem behavior must be tested across the supported platforms.

Potential target environments:

```text
Windows
Linux
macOS
```

The official support matrix must be defined before release.

Platform-specific testing should include:

* Paths.
* Permissions.
* File operations.
* Environment variables.
* CLI behavior.
* Process behavior.
* Temporary directories.

---

## 7.19 TD-TEST-019 — Static Analysis and Type Checking

Category:

```text
Testing / Code Quality
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Testing should not be limited to runtime tests.

The project should introduce automated static checks for:

```text
Formatting
Linting
Type Checking
Import Validation
Dead Code Detection
```

These checks should eventually run automatically in CI.

---

## 7.20 TD-TEST-020 — Coverage Metrics Need Formalization

Category:

```text
Testing / Process
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

AIPM should establish meaningful coverage targets.

Initial targets may be:

| Area               | Target |
| ------------------ | ------ |
| Core Domain Logic  | ≥90%   |
| Core Managers      | ≥90%   |
| Critical Workflows | 100%   |
| Infrastructure     | ≥80%   |
| CLI                | ≥80%   |
| Overall Project    | ≥85%   |

These are engineering targets rather than guarantees of software quality.

High coverage does not compensate for poor test design.

---

# 7.21 Critical Workflow Test Matrix

The following workflows should eventually achieve complete critical-path coverage:

| Workflow | Success  | Failure  | Recovery | Regression |
| -------- | -------- | -------- | -------- | ---------- |
| Registry | Required | Required | Required | Required   |
| Download | Required | Required | Required | Required   |
| Install  | Required | Required | Required | Required   |
| Verify   | Required | Required | Required | Required   |
| Update   | Required | Required | Required | Required   |
| Repair   | Required | Required | Required | Required   |
| Remove   | Required | Required | Required | Required   |
| History  | Required | Required | Required | Required   |

"Required" means the behavior must have deterministic automated verification before the corresponding workflow is considered production-ready.

---

# 7.22 Testing Debt Priority Matrix

| ID          | Testing Debt                | Severity | Priority | Status     |
| ----------- | --------------------------- | -------- | -------- | ---------- |
| TD-TEST-001 | Core Workflow Coverage      | High     | P1       | Identified |
| TD-TEST-002 | Repair Testing              | High     | P1       | Identified |
| TD-TEST-003 | Failure Paths               | High     | P1       | Identified |
| TD-TEST-004 | Filesystem Isolation        | High     | P1       | Identified |
| TD-TEST-005 | Network Isolation           | High     | P1       | Identified |
| TD-TEST-006 | SHA256 Verification         | Critical | P0       | Identified |
| TD-TEST-007 | Metadata Validation         | High     | P1       | Identified |
| TD-TEST-008 | Result Model Testing        | Medium   | P2       | Identified |
| TD-TEST-009 | History Testing             | High     | P1       | Identified |
| TD-TEST-010 | CLI Testing                 | Medium   | P2       | Identified |
| TD-TEST-011 | Exit Code Testing           | Medium   | P2       | Identified |
| TD-TEST-012 | Regression Testing          | High     | P1       | Identified |
| TD-TEST-013 | Test Fixtures               | Medium   | P2       | Identified |
| TD-TEST-014 | Unit / Integration Boundary | Medium   | P2       | Identified |
| TD-TEST-015 | Test Determinism            | High     | P1       | Identified |
| TD-TEST-016 | Time Logic Testing          | Medium   | P2       | Identified |
| TD-TEST-017 | Concurrency Testing         | Medium   | P3       | Planned    |
| TD-TEST-018 | Platform Testing            | Medium   | P2       | Planned    |
| TD-TEST-019 | Static Analysis             | Medium   | P2       | Planned    |
| TD-TEST-020 | Coverage Formalization      | Medium   | P2       | Planned    |

---

# 7.23 Testing Debt Resolution Strategy

Testing debt should be resolved in the following order:

```text
1. Test Infrastructure
        ↓
2. Isolated Filesystem / Network Tests
        ↓
3. Checksum & Metadata Verification
        ↓
4. Core Manager Unit Tests
        ↓
5. Failure-Path Tests
        ↓
6. Repair / Install / Remove Integration Tests
        ↓
7. History Tests
        ↓
8. CLI Tests
        ↓
9. Regression Tests
        ↓
10. CI / Static Analysis
        ↓
11. Coverage Enforcement
        ↓
12. Platform / Advanced Tests
```

The project should avoid setting a high global coverage requirement before the core test infrastructure is stable.

---

# 7.24 Definition of Testing Debt Resolved

Testing debt should be considered resolved only when:

```text
Test Case Defined
      ↓
Test Implemented
      ↓
Test Deterministic
      ↓
Test Passing
      ↓
Regression Protection Added
      ↓
CI Validation Enabled
      ↓
Documentation Updated
```

For critical security and data-integrity behavior, the test must also demonstrate failure behavior rather than only successful behavior.

---

# 7.25 Testing Rules for Future Development

Every new AIPM feature should follow:

```text
Feature
  ↓
Test Design
  ↓
Implementation
  ↓
Unit Tests
  ↓
Integration Tests
  ↓
Regression Tests
  ↓
Documentation
```

For bug fixes:

```text
Bug
  ↓
Reproduction Test
  ↓
Fix
  ↓
Regression Verification
```

For architectural refactoring:

```text
Existing Tests
  ↓
Refactor
  ↓
Existing Tests Pass
  ↓
New Boundary Tests
  ↓
Integration Verification
```

---

# 7.26 Testing Exit Criteria Before Stable Release

AIPM should not be considered production-ready until:

* Core workflows have automated tests.
* Critical failure paths are covered.
* SHA256 verification is tested.
* Metadata validation is tested.
* Repair behavior is tested.
* Filesystem operations are isolated.
* Network operations are deterministic in unit tests.
* History behavior is tested.
* Regression tests exist for important fixed bugs.
* CLI exit codes are defined and tested.
* Static analysis runs successfully.
* Type checking is enforced at an appropriate level.
* CI executes the test suite automatically.
* Test results are reproducible.
* Coverage targets are measurable.

---

# 7.27 Summary

Testing is currently one of the most important areas of technical debt in AIPM.

The project should not continue adding substantial features indefinitely while core workflows remain insufficiently tested.

The preferred development sequence is:

```text
Build Core
    ↓
Test Core
    ↓
Stabilize Core
    ↓
Refactor Core
    ↓
Test Again
    ↓
Expand Features
```

The central principle is:

> Every important behavior that AIPM must preserve should eventually have an automated test that proves it.

Testing debt should therefore be reduced before major architectural expansion and before declaring the project production-ready.

# 8. Security Debt

Security debt refers to security weaknesses, missing controls, unsafe defaults, insufficient validation, inadequate integrity protection, and other implementation gaps that could expose AIPM to unauthorized access, malicious files, supply-chain attacks, data corruption, privilege abuse, or unsafe system behavior.

For AIPM, security is particularly important because the application manages AI model files, downloads external resources, interacts with the filesystem, validates checksums, and may eventually operate with elevated privileges or enterprise environments.

Security debt therefore has a higher priority than ordinary maintainability debt.

The objective of this section is to identify security risks that must be addressed before AIPM is considered production-ready.

---

## 8.1 SD-001 — Untrusted Model Download Risk

Category:

```text
Security / Supply Chain
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

### Description

AIPM downloads model artifacts from external URLs.

Any externally downloaded artifact must be treated as untrusted until its integrity and authenticity have been established.

The basic workflow is:

```text
External URL
    ↓
Download
    ↓
Local File
    ↓
SHA256 Verification
    ↓
Accept / Reject
```

### Risk

A compromised or modified download could result in:

* Malicious model files.
* Corrupted model files.
* Supply-chain compromise.
* Man-in-the-middle modification where transport protection is insufficient.
* Distribution of an artifact different from the intended release.

### Resolution

Every downloadable artifact must have a clearly defined integrity-verification policy.

At minimum:

```text
Download
   ↓
Verify Expected SHA256
   ↓
Mismatch → Delete / Reject
   ↓
Match → Continue
```

Checksum verification must never be optional for trusted production artifacts.

---

## 8.2 SD-002 — SHA256 Verification Must Be Mandatory

Category:

```text
Security / Integrity
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

### Description

AIPM already has checksum-related verification behavior, but the security policy must explicitly establish when SHA256 validation is mandatory.

### Required Rule

A model should not be considered successfully installed or repaired when:

```text
expected_sha256 != calculated_sha256
```

The result must be:

```text
Verification Failed
    ↓
Artifact Rejected
    ↓
Unsafe Artifact Not Activated
```

### Additional Requirement

A checksum mismatch should produce structured diagnostic information without exposing unnecessary sensitive filesystem information.

---

## 8.3 SD-003 — Checksum Metadata Trust Problem

Category:

```text
Security / Supply Chain
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

### Description

A SHA256 checksum only proves that a file matches the expected checksum.

It does not prove that the checksum itself came from a trusted source.

For example:

```text
Malicious File
       +
Maliciously Updated Checksum
       ↓
Matching SHA256
       ↓
False Sense of Integrity
```

### Risk

If both:

```text
Model URL
SHA256
```

are obtained from an untrusted or compromised registry, checksum validation alone is insufficient against supply-chain compromise.

### Resolution Direction

A future trusted release mechanism should consider:

```text
Trusted Registry
       ↓
Signed Metadata
       ↓
Trusted Artifact
       ↓
Checksum Verification
```

Digital signatures should be considered for a mature release architecture.

---

## 8.4 SD-004 — HTTPS Enforcement

Category:

```text
Security / Transport
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Model downloads should use secure transport.

Production model URLs should normally use:

```text
https://
```

rather than:

```text
http://
```

### Risk

Unencrypted HTTP can expose downloads to interception or modification.

### Resolution

The registry should reject insecure URLs for production artifacts unless an explicit and documented exception exists.

The security policy should distinguish:

```text
Production
    → HTTPS required

Development / Test
    → Local or controlled resources permitted
```

---

## 8.5 SD-005 — URL Validation

Category:

```text
Security / Input Validation
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

URLs are external input and should not be treated as inherently trustworthy.

Validation should cover:

* Supported schemes.
* Malformed URLs.
* Unsupported protocols.
* Empty URLs.
* Invalid hosts.
* Unexpected URL forms.

### Resolution

The download layer should validate the URL before initiating a network request.

At minimum:

```text
Validate URL
    ↓
Validate Scheme
    ↓
Validate Host
    ↓
Perform Download
```

---

## 8.6 SD-006 — Path Traversal Risk

Category:

```text id="u5h0cd"
Security / Filesystem
```

Severity:

```text
Critical
```

Priority:

```text id="q8a7v4"
P0
```

Status:

```text
Identified
```

### Description

Model names, filenames, metadata values, and registry-controlled paths must never be allowed to escape the intended model directory.

Potential dangerous patterns include:

```text
../
..\ 
absolute paths
unexpected path separators
```

### Risk

An attacker-controlled model name or filename could potentially cause operations to access files outside the intended storage directory.

### Required Rule

Every generated path must be resolved and checked against its intended base directory.

Conceptually:

```text
Base Directory
      +
User / Registry Input
      ↓
Resolved Path
      ↓
Verify Inside Base
      ↓
Allow / Reject
```

This is a P0 security requirement for filesystem operations.

---

## 8.7 SD-007 — Unsafe Archive Extraction

Category:

```text
Security / Filesystem
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Future Risk
```

### Description

If AIPM eventually supports ZIP, TAR, or other compressed model packages, archive extraction introduces a significant path traversal risk.

A malicious archive could contain entries such as:

```text
../../target-file
```

or absolute filesystem paths.

### Resolution

Before extracting any archive:

```text
Archive Entry
    ↓
Normalize Path
    ↓
Resolve Destination
    ↓
Check Destination
    ↓
Extract Only If Safe
```

No archive extraction feature should be considered production-ready without dedicated security tests.

---

## 8.8 SD-008 — Symlink Attack Risk

Category:

```text
Security / Filesystem
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Future Risk
```

### Description

Filesystem operations may become unsafe if symbolic links are followed without consideration.

For example:

```text
Expected:
models/example/model.bin

Malicious:
models/example/model.bin
       ↓
symlink → sensitive/system/file
```

### Risk

Operations such as:

```text
remove()
write()
replace()
verify()
```

could potentially affect unintended targets.

### Resolution

Filesystem security policy must explicitly define how symbolic links are handled.

Where appropriate:

```text
Reject unexpected symlinks
```

or operate using secure filesystem primitives that prevent traversal outside the managed storage area.

---

## 8.9 SD-009 — File Permission Handling

Category:

```text
Security / Operating System
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

AIPM must not assume that all model files can safely be created with unrestricted permissions.

### Risk

Incorrect permissions could allow:

* Unauthorized modification.
* Unauthorized deletion.
* Exposure of model data.
* Cross-user interference.

### Resolution

The project should define appropriate permissions for:

```text
Model Directory
Model Files
Metadata
History
Configuration
Logs
Cache
```

Permissions should follow least privilege.

---

## 8.10 SD-010 — Privilege Escalation Risk

Category:

```text
Security / Operating System
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

### Description

AIPM should not require administrator/root privileges for ordinary operations unless technically necessary.

Running a package manager with elevated privileges increases the impact of any vulnerability.

### Security Principle

Prefer:

```text
Normal User
    ↓
User-Owned Model Directory
```

rather than:

```text
Administrator / Root
    ↓
System-Wide Directory
```

unless system-wide model management is explicitly required.

---

## 8.11 SD-011 — Command Execution Risk

Category:

```text
Security / Code Execution
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

### Description

AIPM should avoid constructing shell commands using untrusted model names, URLs, filenames, or metadata.

Dangerous conceptual pattern:

```text
shell command + user input
```

can lead to command injection.

### Resolution

Prefer native Python APIs wherever possible.

If an external executable must be invoked:

```text
Use argument lists
Avoid shell=True
Validate arguments
Avoid string interpolation
```

Any future subprocess usage must undergo explicit security review.

---

## 8.12 SD-012 — Model Name Validation

Category:

```text
Security / Input Validation
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Model names are used throughout AIPM and may influence:

* Registry lookup.
* Filesystem paths.
* CLI commands.
* History.
* Logs.
* Download locations.

Therefore model names must have a clearly defined format.

### Resolution

Define a canonical model-name policy.

For example:

```text
Allowed:
letters
numbers
hyphen
underscore

Rejected:
path separators
control characters
unexpected shell metacharacters
```

The exact naming specification should be finalized before the stable API.

---

## 8.13 SD-013 — Metadata Validation and Injection

Category:

```text
Security / Data Validation
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Model metadata should be treated as untrusted data.

Metadata must not be able to directly control:

* Filesystem paths.
* Shell commands.
* Network destinations.
* Dynamic imports.
* Arbitrary Python execution.

### Required Principle

```text
Metadata
    ↓
Parse
    ↓
Validate Schema
    ↓
Validate Semantics
    ↓
Use Safely
```

---

## 8.14 SD-014 — Unsafe Deserialization Risk

Category:

```text
Security / Code Execution
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Future Risk
```

### Description

AI model ecosystems frequently contain serialized objects and model formats.

Some serialization mechanisms can execute arbitrary code when loaded from untrusted sources.

Therefore AIPM must never blindly deserialize an untrusted model artifact.

### Security Rule

Model format support must be evaluated individually.

The project should prefer formats designed for safe data-only loading where practical.

Any format capable of arbitrary code execution must require explicit security analysis before being supported.

---

## 8.15 SD-015 — Dependency Vulnerability Management

Category:

```text
Security / Dependencies
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

### Description

AIPM depends on external Python packages.

A vulnerable dependency can become an indirect security vulnerability in AIPM.

### Required Controls

The project should maintain:

```text
Dependency Locking
        ↓
Version Review
        ↓
Automated Vulnerability Scanning
        ↓
Security Updates
```

Dependency updates should be tested before release.

---

## 8.16 SD-016 — Dependency Pinning Policy

Category:

```text
Security / Reproducibility
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

### Description

Uncontrolled dependency upgrades can unexpectedly introduce:

* Vulnerabilities.
* Breaking changes.
* Behavioral changes.
* Supply-chain risks.

### Resolution

Production releases should use a reproducible dependency strategy.

The project should distinguish:

```text
Development Dependency
Runtime Dependency
Optional Dependency
Test Dependency
```

and establish appropriate version constraints for each.

---

## 8.17 SD-017 — Secret and Credential Management

Category:

```text
Security / Secrets
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Planned
```

### Description

AIPM may eventually support:

* Private model registries.
* Authentication.
* API tokens.
* Enterprise repositories.
* Cloud storage.

Credentials must never be embedded directly in source code.

### Forbidden

```text
API_KEY = "..."
TOKEN = "..."
PASSWORD = "..."
```

inside committed source code.

### Preferred Strategy

Use appropriate credential mechanisms such as:

```text
Environment Variables
OS Credential Store
Secure Configuration
CI/CD Secret Store
```

depending on deployment context.

---

## 8.18 SD-018 — Sensitive Information in Logs

Category:

```text
Security / Logging
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Logs should not accidentally expose sensitive information.

Potential sensitive data includes:

* Access tokens.
* Credentials.
* Private URLs containing authentication information.
* User-specific filesystem paths.
* Internal infrastructure details.
* Sensitive metadata.

### Resolution

Logging should follow a safe-data policy.

For example:

```text
Log:
Download failed for model "example"

Avoid:
Authorization: Bearer <secret>
```

Sensitive values should be redacted before logging.

---

## 8.19 SD-019 — Error Message Information Disclosure

Category:

```text
Security / Error Handling
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

### Description

Returning raw exception messages directly to users can reveal internal implementation details.

Examples include:

```text
Internal filesystem paths
Network configuration
Authentication details
Dependency internals
Stack traces
```

### Resolution

Separate:

```text
Internal Diagnostic Information
```

from:

```text
User-Facing Error Message
```

Detailed diagnostics should be available through controlled debug logging rather than always being displayed to end users.

---

## 8.20 SD-020 — Temporary File Security

Category:

```text
Security / Filesystem
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

### Description

Download and repair workflows may require temporary files.

Temporary files must be created securely.

### Requirements

Temporary resources should:

* Use secure temporary-file APIs.
* Avoid predictable filenames.
* Avoid unsafe shared directories where possible.
* Be cleaned after failure.
* Not be unintentionally executable.
* Have appropriate permissions.

---

## 8.21 SD-021 — Atomic Replacement of Model Files

Category:

```text
Security / Integrity
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

### Description

Replacing an existing model directly during download or repair can create partial-state problems.

Unsafe pattern:

```text
Existing Model
    ↓
Delete
    ↓
Download Directly Into Final Location
```

If the process fails, the final location may contain an incomplete artifact.

### Preferred Pattern

```text
Download Temporary Artifact
        ↓
Verify SHA256
        ↓
Verify Metadata
        ↓
Atomic Replacement
```

This reduces the window in which an invalid or incomplete model can become active.

---

## 8.22 SD-022 — Disk Exhaustion / Resource Exhaustion

Category:

```text
Security / Availability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

Large AI models can consume significant disk space.

A malicious or incorrect download could consume excessive storage.

### Risk

Potential consequences include:

* Disk exhaustion.
* Application failure.
* System instability.
* Denial of service.

### Resolution

Future download functionality should consider:

```text
Expected File Size
Available Disk Space
Maximum Download Size
Temporary Storage Requirements
```

The project should fail safely when sufficient storage is unavailable.

---

## 8.23 SD-023 — Resource Limits

Category:

```text
Security / Availability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

### Description

Network and filesystem operations should eventually have reasonable limits.

Potential controls include:

```text
Connection Timeout
Read Timeout
Maximum Artifact Size
Maximum Metadata Size
Maximum Archive Expansion
Retry Limit
```

These limits reduce the risk of resource exhaustion.

---

## 8.24 SD-024 — Retry and Backoff Safety

Category:

```text
Security / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

### Description

Future download retry mechanisms must not retry indefinitely.

An uncontrolled retry loop can produce:

* Network abuse.
* Resource exhaustion.
* Excessive logs.
* Slow recovery.
* Unnecessary server load.

### Resolution

Retries should have:

```text
Maximum Attempts
Backoff Strategy
Retryable Error Classification
Final Failure State
```

---

## 8.25 SD-025 — Security Testing Debt

Category:

```text
Security / Testing
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

Security controls must themselves be tested.

Required security tests should eventually cover:

```text
Invalid Model Name
Path Traversal
Invalid URL
HTTP URL
Checksum Mismatch
Corrupted Artifact
Malicious Metadata
Unsafe Archive Path
Symlink
Permission Failure
Oversized Artifact
Malformed Registry Entry
Credential Leakage
```

Security features without security tests should not be considered complete.

---

# 8.26 Security Debt Priority Matrix

| ID     | Security Debt                 | Severity | Priority | Status      |
| ------ | ----------------------------- | -------- | -------- | ----------- |
| SD-001 | Untrusted Model Download      | Critical | P0       | Identified  |
| SD-002 | Mandatory SHA256 Verification | Critical | P0       | Identified  |
| SD-003 | Checksum Metadata Trust       | Critical | P0       | Identified  |
| SD-004 | HTTPS Enforcement             | High     | P1       | Identified  |
| SD-005 | URL Validation                | High     | P1       | Identified  |
| SD-006 | Path Traversal                | Critical | P0       | Identified  |
| SD-007 | Unsafe Archive Extraction     | Critical | P0       | Future Risk |
| SD-008 | Symlink Attacks               | High     | P1       | Future Risk |
| SD-009 | File Permissions              | High     | P1       | Identified  |
| SD-010 | Privilege Escalation          | Critical | P0       | Identified  |
| SD-011 | Command Execution             | Critical | P0       | Identified  |
| SD-012 | Model Name Validation         | High     | P1       | Identified  |
| SD-013 | Metadata Injection            | High     | P1       | Identified  |
| SD-014 | Unsafe Deserialization        | Critical | P0       | Future Risk |
| SD-015 | Dependency Vulnerabilities    | High     | P1       | Planned     |
| SD-016 | Dependency Pinning            | Medium   | P2       | Planned     |
| SD-017 | Secret Management             | Critical | P0       | Planned     |
| SD-018 | Sensitive Logging             | High     | P1       | Identified  |
| SD-019 | Error Disclosure              | Medium   | P2       | Identified  |
| SD-020 | Temporary File Security       | High     | P1       | Planned     |
| SD-021 | Atomic Replacement            | High     | P1       | Planned     |
| SD-022 | Disk Exhaustion               | High     | P1       | Identified  |
| SD-023 | Resource Limits               | Medium   | P2       | Planned     |
| SD-024 | Retry Safety                  | Medium   | P2       | Planned     |
| SD-025 | Security Testing              | Critical | P0       | Identified  |

---

# 8.27 Security Hardening Order

Security debt should be resolved according to risk rather than convenience.

Recommended order:

```text
1. Path Traversal Protection
        ↓
2. Mandatory SHA256 Verification
        ↓
3. Secure Download / HTTPS Policy
        ↓
4. Input Validation
        ↓
5. Safe Filesystem Operations
        ↓
6. Command / Subprocess Security
        ↓
7. Safe Temporary Files
        ↓
8. Atomic Model Replacement
        ↓
9. Dependency Security
        ↓
10. Logging / Error Sanitization
        ↓
11. Resource Limits
        ↓
12. Advanced Supply-Chain Security
```

---

# 8.28 Security Development Rules

Every future security-sensitive feature should follow:

```text
Threat
   ↓
Security Requirement
   ↓
Implementation
   ↓
Negative Test
   ↓
Positive Test
   ↓
Regression Test
   ↓
Documentation
```

The following rules should become project standards:

1. Never trust external model artifacts by default.
2. Never bypass checksum verification for production artifacts.
3. Never execute untrusted model content as code.
4. Never construct shell commands from untrusted strings.
5. Never allow user-controlled paths to escape managed directories.
6. Never store secrets in source code.
7. Never log credentials or sensitive authentication data.
8. Avoid unnecessary administrator/root privileges.
9. Use secure temporary-file mechanisms.
10. Define resource limits for large downloads and archives.
11. Test security controls explicitly.
12. Treat security regressions as release-blocking defects when they affect critical controls.

---

# 8.29 Security Definition of Done

A security-sensitive feature is complete only when:

```text
Threat Identified
      ↓
Security Control Implemented
      ↓
Positive Test
      ↓
Negative / Attack Test
      ↓
Regression Test
      ↓
Static Analysis
      ↓
Documentation
      ↓
Security Review
```

For P0 security issues, the implementation should not be considered production-ready until corresponding automated tests exist.

---

# 8.30 Security Release Gate

Before AIPM reaches a stable production release, the following must be verified:

* Model downloads use secure transport.
* Production artifacts have integrity verification.
* SHA256 mismatches are rejected.
* Model names are validated.
* Filesystem paths are protected against traversal.
* Unsafe archive extraction is prevented if archives are supported.
* Symlink behavior is defined.
* Temporary files are securely handled.
* External commands are safely invoked, if any exist.
* Unsafe deserialization is prohibited or explicitly controlled.
* Dependencies are scanned for known vulnerabilities.
* Secrets are not stored in source control.
* Logs do not expose sensitive information.
* Error messages do not unnecessarily disclose internals.
* Large downloads cannot trivially exhaust storage.
* Security regression tests are included in CI.

---

# 8.31 Security Debt Exit Criteria

A security-debt item may be marked `Resolved` only when:

```text
Security Risk Understood
        ↓
Mitigation Implemented
        ↓
Automated Test Added
        ↓
Negative Case Verified
        ↓
Regression Protection Added
        ↓
Documentation Updated
        ↓
CI Validation Enabled
```

For critical security issues, code review should explicitly verify that the mitigation cannot be trivially bypassed.

---

# 8.32 Summary

Security debt is currently one of the highest-priority categories of technical debt for AIPM.

This is primarily because AIPM operates at the intersection of:

```text
External Network
      +
Untrusted Files
      +
Filesystem
      +
AI Model Artifacts
      +
Potential Code Execution
```

The most important security principle is:

> AIPM must treat every externally obtained model, metadata value, URL, path, and serialized artifact as untrusted until it has passed the appropriate validation and integrity checks.

The security strategy should therefore be:

```text
Validate
   ↓
Download Safely
   ↓
Verify Integrity
   ↓
Verify Metadata
   ↓
Store Safely
   ↓
Activate Safely
   ↓
Record Audit Information
```

Security should not be postponed until the final release. P0 and P1 security debt should be addressed before significant expansion of AIPM's feature surface.

The project should prioritize security controls that protect the system boundary first, particularly:

```text
Path Safety
Checksum Integrity
Input Validation
Download Security
Filesystem Safety
Code Execution Prevention
Dependency Security
```

Only after these controls are sufficiently hardened should AIPM proceed toward advanced features such as remote registries, plugins, private repositories, automatic updates, or arbitrary model-format support.

# 9. Performance Debt

Performance debt refers to architectural, implementation, and operational decisions that may cause AIPM to become unnecessarily slow, resource-intensive, difficult to scale, or inefficient as the project grows.

Performance debt does not mean that every current implementation must be aggressively optimized.

AIPM is still being stabilized. Premature optimization would create additional complexity and could increase maintenance cost.

The correct strategy is:

```text
Correctness
    ↓
Reliability
    ↓
Measurability
    ↓
Performance Optimization
    ↓
Scalability
```

Performance work should therefore be driven by measurements, profiling, workload characteristics, and defined performance requirements.

---

## 9.1 PD-001 — No Formal Performance Baseline

Category:

```text
Performance / Observability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

AIPM currently needs a formal performance baseline for its major workflows.

Without baseline measurements, it is difficult to determine whether a future change:

```text
Improves Performance
```

or:

```text
Introduces Regression
```

### Required Baseline

The project should eventually measure:

```text
Registry Lookup Time
Download Initialization Time
Download Throughput
Checksum Verification Time
Metadata Verification Time
Repair Duration
Remove Duration
History Write Time
CLI Startup Time
Memory Usage
Disk Usage
```

These measurements should be recorded under controlled conditions.

---

## 9.2 PD-002 — No Defined Performance Budget

Category:

```text
Performance / Engineering Standards
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

AIPM should eventually define performance budgets for critical operations.

Example:

| Operation               |                              Initial Target |
| ----------------------- | ------------------------------------------: |
| CLI startup             |                                  < 1 second |
| Registry lookup         |                                    < 100 ms |
| Local verification      |                  Dependent on artifact size |
| History lookup          |                                    < 100 ms |
| Remove operation        | < 1 second excluding filesystem constraints |
| Download initialization |       < 2 seconds excluding network latency |

These are preliminary engineering targets rather than final guarantees.

Download throughput should not be assigned a universal target because it depends heavily on network conditions, server capacity, disk performance, and artifact size.

---

## 9.3 PD-003 — Large File Checksum Cost

Category:

```text
Performance / Integrity
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

SHA256 verification requires reading the artifact.

For large AI models:

```text
Large File
    ↓
Read Entire Artifact Through Stream
    ↓
Calculate SHA256
```

This can consume substantial disk I/O and CPU time.

### Risk

Repeated verification of very large artifacts may become expensive.

### Resolution Direction

Checksum verification should use streaming reads rather than loading the entire artifact into memory.

Conceptually:

```text
File
 ↓
Chunk
 ↓
Hash
 ↓
Next Chunk
 ↓
Final SHA256
```

This maintains low memory usage while supporting large artifacts.

---

## 9.4 PD-004 — Memory Usage During Model Operations

Category:

```text
Performance / Memory
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM must avoid loading large model artifacts entirely into memory merely to perform file operations.

Operations such as:

```text
Download
Checksum
Copy
Verify
```

should preferably use streaming or chunked processing.

Unsafe conceptual approach:

```text
Entire Model
    ↓
RAM
    ↓
Process
```

Preferred approach:

```text
Model
 ↓
Small Chunk
 ↓
Process
 ↓
Next Chunk
 ↓
Repeat
```

This becomes increasingly important as model sizes grow.

---

## 9.5 PD-005 — Download Buffer Management

Category:

```text
Performance / Network
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Download operations should use an appropriate streaming buffer size.

A buffer that is too small can cause unnecessary overhead.

A buffer that is excessively large can increase memory usage without meaningful throughput improvement.

The final implementation should therefore benchmark reasonable buffer sizes rather than choosing an arbitrary extreme.

---

## 9.6 PD-006 — Duplicate File I/O

Category:

```text
Performance / Filesystem
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

A workflow may potentially read the same artifact multiple times.

For example:

```text
Download
    ↓
Checksum
    ↓
Metadata Verification
    ↓
Final Verification
```

Repeated disk reads may become expensive for very large models.

This should not be optimized prematurely because integrity and correctness are more important.

However, profiling should determine whether redundant reads become a measurable bottleneck.

---

## 9.7 PD-007 — Repair Workflow I/O Cost

Category:

```text
Performance / Repair
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

The repair workflow may involve:

```text
Verify Existing Artifact
        ↓
Remove Artifact
        ↓
Download Artifact
        ↓
Verify Download
```

For large models, this naturally requires substantial I/O.

The project should avoid unnecessary additional verification passes while preserving the integrity guarantees required by the security architecture.

Optimization must never remove mandatory integrity checks merely to improve speed.

---

## 9.8 PD-008 — Registry Lookup Scalability

Category:

```text
Performance / Registry
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Registry lookup is expected to remain fast as the number of registered models grows.

The project should avoid repeatedly scanning large collections when direct indexing is possible.

Preferred conceptual model:

```text
Model Name
    ↓
Indexed Lookup
    ↓
Registry Entry
```

rather than:

```text
Model Name
    ↓
Scan Every Entry
    ↓
Find Match
```

The actual optimization should depend on the registry implementation currently used.

---

## 9.9 PD-009 — History Storage Scalability

Category:

```text
Performance / History
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

History will grow over time.

A system that works efficiently with:

```text
100 history entries
```

may behave differently with:

```text
100,000+
```

entries.

The project should eventually define:

```text
Retention Policy
Storage Format
Indexing Strategy
Pagination
Archiving
Cleanup
```

before history becomes a scalability bottleneck.

---

## 9.10 PD-010 — History Query Performance

Category:

```text
Performance / History
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Future history functionality may include queries such as:

```text
Recent Operations
Model History
Failed Operations
Repair History
Download History
```

These queries should not require loading the complete history dataset into memory.

A scalable architecture should eventually support filtered and bounded retrieval.

---

## 9.11 PD-011 — CLI Startup Overhead

Category:

```text
Performance / CLI
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Identified
```

CLI applications are expected to start quickly.

AIPM should avoid performing expensive initialization before determining which command is being executed.

Potential sources of unnecessary startup cost include:

```text
Heavy Imports
Registry Loading
Network Requests
Environment Scanning
Large Configuration Parsing
```

The CLI should initialize only the components required by the requested command where practical.

---

## 9.12 PD-012 — Eager Import Cost

Category:

```text
Performance / Python Runtime
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Planned
```

As AIPM grows, importing every manager and dependency at application startup may increase startup latency.

Potential future strategy:

```text
CLI Start
    ↓
Parse Command
    ↓
Load Required Module
    ↓
Execute
```

rather than:

```text
CLI Start
    ↓
Load Entire Application
    ↓
Parse Command
    ↓
Execute
```

Lazy imports should only be introduced when profiling demonstrates a meaningful startup problem.

---

## 9.13 PD-013 — Network Timeout Strategy

Category:

```text
Performance / Network / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Network operations must not wait indefinitely.

A download request should have clearly defined timeout behavior.

At minimum, the architecture should distinguish:

```text
Connection Timeout
Read Timeout
Overall Operation Timeout
```

The exact implementation should depend on the HTTP client used by AIPM.

---

## 9.14 PD-014 — Download Retry Performance

Category:

```text
Performance / Network
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Retries can improve reliability but can also significantly increase total operation time.

An uncontrolled retry system could produce:

```text
Failure
 ↓
Retry
 ↓
Failure
 ↓
Retry
 ↓
Failure
 ↓
...
```

The project should eventually define:

```text
Maximum Attempts
Backoff
Retryable Errors
Non-Retryable Errors
Final Timeout
```

---

## 9.15 PD-015 — No Resumable Download Strategy

Category:

```text
Performance / Network
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Future Enhancement
```

Large AI models can take considerable time to download.

If a multi-gigabyte download fails near completion, restarting from zero is inefficient.

Future support may consider HTTP range requests:

```text
Download
   ↓
Interrupted at 70%
   ↓
Persist Partial File
   ↓
Resume From 70%
   ↓
Complete
```

This should only be introduced after the basic download workflow is stable and properly tested.

---

## 9.16 PD-016 — No Download Progress Efficiency Model

Category:

```text
Performance / UX
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Planned
```

Progress reporting can itself introduce overhead if updates are emitted excessively.

The system should avoid logging or rendering progress for every tiny chunk.

A better model is:

```text
Download Chunk
    ↓
Accumulate Progress
    ↓
Update UI Periodically
```

rather than:

```text
Every Chunk
    ↓
Console Update
```

The exact update interval should be measurable and configurable if necessary.

---

## 9.17 PD-017 — Excessive Logging Overhead

Category:

```text
Performance / Logging
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Identified
```

Excessive logging can increase:

```text
CPU Usage
Disk I/O
Console Rendering Cost
Log File Size
```

Logging should therefore be proportional to the configured log level.

Normal operations should not generate excessive output.

---

## 9.18 PD-018 — Logging Large Payloads

Category:

```text
Performance / Logging / Security
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Large model metadata, HTTP responses, or diagnostic objects should not be dumped into logs unnecessarily.

This can create both:

```text
Performance Cost
```

and:

```text
Security Risk
```

Logs should contain concise structured information rather than large raw payloads.

---

## 9.19 PD-019 — Progress and Logging Coupling

Category:

```text
Performance / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Progress reporting should not be tightly coupled to business logic.

The application should ideally separate:

```text
Business Operation
```

from:

```text
Presentation / Progress Reporting
```

This allows the same operation to run efficiently in:

```text
CLI
Automation
Library API
CI/CD
```

without unnecessary console overhead.

---

## 9.20 PD-020 — Repeated Registry Loading

Category:

```text
Performance / Registry
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

If registry data is repeatedly parsed from disk during a single command or workflow, unnecessary I/O and parsing cost may occur.

Potential future strategy:

```text
Command Start
    ↓
Load Registry Once
    ↓
Use In-Memory Representation
    ↓
Command Complete
```

This should only be implemented if registry loading is shown to be a measurable bottleneck.

---

## 9.21 PD-021 — Cache Strategy Not Defined

Category:

```text
Performance / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

AIPM may eventually benefit from caching:

```text
Registry Data
Metadata
Verification Results
Model Information
Remote Metadata
```

However, caching introduces consistency and invalidation problems.

Therefore caching must not be introduced merely because it appears faster.

Before adding a cache, the project should define:

```text
What Is Cached?
Who Owns the Cache?
When Does It Expire?
How Is It Invalidated?
Can It Become Stale?
What Happens When Cache Is Corrupt?
```

---

## 9.22 PD-022 — Verification Result Caching Risk

Category:

```text
Performance / Integrity
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

Verification results may appear suitable for caching, but integrity verification is security-sensitive.

For example:

```text
Model Verified Yesterday
```

does not necessarily mean:

```text
Model Is Still Identical Today
```

if the file can be modified externally.

Therefore cached verification results must never replace mandatory integrity verification when the security model requires fresh verification.

Performance optimization must not weaken security guarantees.

---

## 9.23 PD-023 — Concurrent Operation Architecture

Category:

```text
Performance / Concurrency
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Status:

```text
Future Enhancement
```

Parallel downloads or verification could improve throughput.

However, concurrency introduces:

```text
Race Conditions
File Conflicts
Registry Conflicts
History Conflicts
CPU Contention
Disk Contention
Network Contention
```

Therefore concurrency should not be introduced until the sequential workflow is stable.

The preferred sequence is:

```text
Reliable Sequential Workflow
        ↓
Benchmark
        ↓
Identify Bottleneck
        ↓
Introduce Concurrency
        ↓
Stress Test
        ↓
Measure Again
```

---

## 9.24 PD-024 — Shared Storage Contention

Category:

```text
Performance / Filesystem
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Status:

```text
Future Enhancement
```

Multiple simultaneous model operations can compete for:

```text
Disk Bandwidth
CPU
Memory
Storage IOPS
```

The project should eventually account for storage contention when parallel operations are supported.

---

## 9.25 PD-025 — Large Registry Scalability

Category:

```text
Performance / Registry
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Status:

```text
Future Enhancement
```

The registry design should remain efficient as the number of models increases.

Potential scale levels:

```text
10 Models
100 Models
1,000 Models
10,000+ Models
```

Performance testing should establish the point at which the current registry representation becomes inefficient.

The solution may eventually involve:

```text
Indexing
Structured Database
Binary Cache
Lazy Loading
```

but none should be introduced without evidence.

---

## 9.26 PD-026 — Storage Layout Scalability

Category:

```text
Performance / Filesystem
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Status:

```text
Future Enhancement
```

A flat model directory may become inefficient or difficult to manage as the number of models increases.

Potential future structure:

```text
models/
    vendor/
        model/
            version/
```

or:

```text
models/
    model/
        version/
```

The final layout should balance:

```text
Lookup Speed
Human Readability
Portability
Version Management
Filesystem Limitations
```

No restructuring should occur until the storage requirements are formally defined.

---

## 9.27 PD-027 — Model Version Coexistence

Category:

```text
Performance / Storage
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Future AIPM versions may support multiple versions of the same model.

For example:

```text
model-a
 ├── v1
 ├── v2
 └── v3
```

This can significantly increase disk usage.

The project should eventually define:

```text
Version Retention
Duplicate Detection
Cleanup Policy
Disk Usage Reporting
```

---

## 9.28 PD-028 — Duplicate Artifact Storage

Category:

```text
Performance / Storage
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Future Enhancement
```

Different model versions or registry entries may potentially contain identical artifacts.

Future storage optimization could detect identical SHA256 values and avoid storing duplicate content.

Conceptually:

```text
Artifact A
SHA256 = X

Artifact B
SHA256 = X

        ↓

Same Content
        ↓
Potential Deduplication
```

This should only be considered after the storage model is stable.

---

## 9.29 PD-029 — Resource Usage Observability

Category:

```text
Performance / Monitoring
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

AIPM should eventually provide measurable resource information.

Useful metrics include:

```text
CPU Time
Memory Usage
Download Speed
Downloaded Bytes
Verification Duration
Disk Space Used
Operation Duration
```

These metrics should support diagnostics without creating excessive runtime overhead.

---

## 9.30 PD-030 — Performance Regression Testing

Category:

```text
Performance / CI
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

Once baseline measurements exist, performance regressions should be detected automatically for important workflows.

Conceptually:

```text
Baseline
    ↓
Code Change
    ↓
Benchmark
    ↓
Compare
    ↓
Regression?
    ├── No → Continue
    └── Yes → Investigate
```

Not every small difference should fail CI.

Thresholds should be meaningful and statistically reasonable.

---

# 9.31 Performance Priority Matrix

| ID     | Performance Debt               | Severity | Priority | Status             |
| ------ | ------------------------------ | -------- | -------- | ------------------ |
| PD-001 | No Performance Baseline        | High     | P1       | Identified         |
| PD-002 | No Performance Budget          | Medium   | P2       | Planned            |
| PD-003 | Large File Checksum Cost       | Medium   | P2       | Identified         |
| PD-004 | Model Operation Memory Usage   | High     | P1       | Identified         |
| PD-005 | Download Buffer Management     | Medium   | P2       | Identified         |
| PD-006 | Duplicate File I/O             | Medium   | P2       | Identified         |
| PD-007 | Repair I/O Cost                | Medium   | P2       | Identified         |
| PD-008 | Registry Lookup Scalability    | Medium   | P2       | Identified         |
| PD-009 | History Storage Scalability    | Medium   | P2       | Planned            |
| PD-010 | History Query Performance      | Medium   | P2       | Planned            |
| PD-011 | CLI Startup Overhead           | Low      | P3       | Identified         |
| PD-012 | Eager Import Cost              | Low      | P3       | Planned            |
| PD-013 | Network Timeout Strategy       | High     | P1       | Identified         |
| PD-014 | Download Retry Performance     | Medium   | P2       | Planned            |
| PD-015 | Resumable Downloads            | Medium   | P2       | Future Enhancement |
| PD-016 | Progress Reporting Efficiency  | Low      | P3       | Planned            |
| PD-017 | Excessive Logging              | Low      | P3       | Identified         |
| PD-018 | Large Log Payloads             | Medium   | P2       | Identified         |
| PD-019 | Progress/Logging Coupling      | Medium   | P2       | Identified         |
| PD-020 | Repeated Registry Loading      | Medium   | P2       | Planned            |
| PD-021 | Undefined Cache Strategy       | Medium   | P2       | Planned            |
| PD-022 | Verification Cache Risk        | High     | P1       | Planned            |
| PD-023 | Concurrent Operations          | Medium   | P3       | Future Enhancement |
| PD-024 | Shared Storage Contention      | Medium   | P3       | Future Enhancement |
| PD-025 | Large Registry Scalability     | Medium   | P3       | Future Enhancement |
| PD-026 | Storage Layout Scalability     | Medium   | P3       | Future Enhancement |
| PD-027 | Model Version Coexistence      | Medium   | P3       | Future Enhancement |
| PD-028 | Duplicate Artifact Storage     | Low      | P3       | Future Enhancement |
| PD-029 | Resource Observability         | Medium   | P2       | Planned            |
| PD-030 | Performance Regression Testing | High     | P1       | Planned            |

---

# 9.32 Performance Optimization Strategy

Performance debt should be addressed using evidence rather than assumptions.

The preferred optimization loop is:

```text
Measure
   ↓
Profile
   ↓
Identify Bottleneck
   ↓
Form Hypothesis
   ↓
Optimize
   ↓
Benchmark
   ↓
Compare
   ↓
Keep / Revert
```

The project should avoid optimization based solely on intuition.

---

# 9.33 Optimization Priority

The initial priority should be:

```text
1. Memory Safety
        ↓
2. Large File I/O
        ↓
3. Network Reliability
        ↓
4. Core Workflow Latency
        ↓
5. Registry / History Scalability
        ↓
6. CLI Startup
        ↓
7. Advanced Caching
        ↓
8. Concurrency
        ↓
9. Deduplication
```

This order deliberately prioritizes predictable behavior and resource safety over micro-optimizations.

---

# 9.34 Performance and Security Boundary

Performance optimizations must not weaken security controls.

The following must remain mandatory where applicable:

```text
Checksum Verification
Metadata Verification
Path Validation
Secure Download
Safe File Replacement
Input Validation
```

For example, replacing:

```text
Fresh SHA256 Verification
```

with:

```text
Cached "Already Verified" Result
```

merely to reduce disk I/O is unacceptable if the file may have changed.

The principle is:

> Performance optimization must never trade away integrity, security, or correctness without an explicit architectural decision.

---

# 9.35 Performance Testing Layers

AIPM should eventually use multiple performance-testing layers.

### Microbenchmark

Used for isolated operations:

```text
Checksum
Parsing
Registry Lookup
Path Resolution
```

### Workflow Benchmark

Used for complete operations:

```text
Download
Verify
Repair
Remove
```

### Stress Test

Used for increased workload:

```text
Large Registry
Large History
Large Model
Repeated Operations
```

### Resource Test

Used for:

```text
Memory
CPU
Disk
Network
```

### Regression Benchmark

Used to compare current performance against a known baseline.

---

# 9.36 Performance Definition of Done

A performance-related implementation should be considered complete only when:

```text
Performance Problem Identified
        ↓
Baseline Measured
        ↓
Bottleneck Confirmed
        ↓
Optimization Implemented
        ↓
Correctness Tests Pass
        ↓
Performance Benchmark Passes
        ↓
No Security Regression
        ↓
Documentation Updated
```

Optimization without measurement should not be considered completed performance work.

---

# 9.37 Performance Release Gate

Before a stable production release, AIPM should have:

* A documented performance baseline.
* Streaming handling for large artifacts.
* Controlled network timeouts.
* No unnecessary full-file memory loading.
* Predictable download behavior.
* Efficient registry lookup.
* Reasonable history performance.
* Controlled logging overhead.
* Resource usage measurements.
* Critical performance regression tests.
* No performance optimization that compromises security or integrity.

Advanced features such as resumable downloads, parallel downloads, caching, and deduplication are not mandatory for the first stable release unless actual requirements demand them.

---

# 9.38 Performance Debt Exit Criteria

A performance-debt item may be marked `Resolved` only when:

```text
Problem Measured
      ↓
Baseline Recorded
      ↓
Bottleneck Confirmed
      ↓
Solution Implemented
      ↓
Correctness Verified
      ↓
Benchmark Repeated
      ↓
Improvement Demonstrated
      ↓
Regression Protection Added
      ↓
Documentation Updated
```

If profiling demonstrates that an optimization would provide negligible benefit while significantly increasing complexity, the debt may instead be explicitly accepted and documented.

---

# 9.39 Summary

Performance debt in AIPM should be managed conservatively.

The project is an AI model management system, so large files, network operations, disk I/O, checksum calculations, and storage growth naturally create performance considerations.

However, the project should not respond to these challenges by immediately introducing:

```text
Complex Caching
Parallelism
Async Everywhere
Database Migration
Deduplication
Distributed Storage
```

without evidence that they are required.

The preferred strategy is:

```text
Build Correctly
      ↓
Measure
      ↓
Profile
      ↓
Find Actual Bottleneck
      ↓
Optimize the Bottleneck
      ↓
Benchmark
      ↓
Protect With Regression Tests
```

The most important performance principle for AIPM is:

> Do not optimize what has not been measured.

For the current development stage, the highest-value performance work is therefore not advanced optimization. It is establishing the foundation required to measure performance reliably, especially for large model files, filesystem operations, downloads, verification, registry access, and history operations.

Only after those measurements exist should AIPM move toward advanced performance features such as resumable downloads, caching, concurrency, deduplication, or large-scale registry optimization.

# 10. Testing Debt

Testing debt refers to missing, incomplete, unreliable, insufficiently automated, or poorly structured tests that make it difficult to prove that AIPM behaves correctly and continues to behave correctly after future changes.

Testing debt is particularly important for AIPM because the application operates across several boundaries:

```text
CLI
 ↓
Application Logic
 ↓
Managers / Services
 ↓
Registry
 ↓
Filesystem
 ↓
Network
 ↓
Model Artifacts
 ↓
Integrity Verification
 ↓
History / State
```

A failure in any one of these layers can affect the complete workflow.

Therefore, testing must not be limited to individual functions. AIPM requires layered testing covering unit, integration, workflow, security, filesystem, network, regression, and performance behavior.

The fundamental testing principle is:

> A feature is not complete merely because the implementation works once. It is complete when its expected behavior and important failure modes are automatically verified.

---

## 10.1 TD-001 — Incomplete Automated Test Coverage

Category:

```text
Testing / Coverage
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

### Description

AIPM requires broader automated coverage across its core workflows.

Testing should cover not only successful execution but also expected failures.

The target structure is:

```text
Implementation
    ↓
Happy-Path Test
    ↓
Failure-Path Test
    ↓
Boundary Test
    ↓
Regression Test
```

Coverage percentage alone should not be treated as the definition of quality.

---

## 10.2 TD-002 — Missing Test Strategy

Category:

```text
Testing / Architecture
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM needs a formal testing strategy defining what should be tested at each level.

The strategy should distinguish:

```text
Unit Tests
Integration Tests
End-to-End Tests
Security Tests
Performance Tests
Regression Tests
CLI Tests
Filesystem Tests
Network Tests
```

Without this separation, tests may become duplicated in some areas while critical boundaries remain untested.

---

## 10.3 TD-003 — Unit Test Debt

Category:

```text
Testing / Unit
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Core application logic should have isolated unit tests.

Potential unit-test targets include:

```text
Registry Logic
Model Validation
Path Resolution
Checksum Calculation
Metadata Validation
Configuration Handling
History Logic
Error Classification
Utility Functions
```

Unit tests should be fast and deterministic.

They should not require an actual internet connection or a real large model file unless the test specifically belongs to a higher testing layer.

---

## 10.4 TD-004 — Integration Test Debt

Category:

```text
Testing / Integration
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

Unit tests cannot prove that independently correct components work correctly together.

AIPM therefore requires integration testing for workflows such as:

```text
Registry
   ↓
Download Manager
   ↓
Filesystem
   ↓
Checksum Verification
   ↓
History
```

Integration tests should verify the actual interaction between components.

---

## 10.5 TD-005 — End-to-End Workflow Test Debt

Category:

```text
Testing / E2E
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

AIPM's major user-facing workflows should eventually have end-to-end tests.

At minimum:

```text
Install
List
Verify
Repair
Remove
History
```

The tests should execute the application through its intended public interface rather than directly calling internal functions.

Conceptually:

```text
User Command
    ↓
CLI
    ↓
Application
    ↓
Filesystem / Registry
    ↓
Expected Result
```

---

## 10.6 TD-006 — CLI Test Debt

Category:

```text
Testing / CLI
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Because AIPM is primarily interacted with through CLI commands, CLI behavior must be explicitly tested.

Tests should cover:

```text
Valid Commands
Invalid Commands
Missing Arguments
Invalid Arguments
Help
Version
Exit Codes
Error Messages
Output Format
```

A CLI test should verify both:

```text
stdout
stderr
```

where appropriate.

---

## 10.7 TD-007 — Exit Code Testing

Category:

```text
Testing / CLI / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM will potentially be used in:

```text
Shell Scripts
CI/CD
Automation
System Administration
```

Therefore exit codes are part of the public API.

Tests should verify that:

```text
Success → exit code 0
Failure → non-zero exit code
```

Different failure classes should be mapped consistently where the CLI contract defines them.

---

## 10.8 TD-008 — Filesystem Test Debt

Category:

```text
Testing / Filesystem
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

AIPM is filesystem-intensive.

Tests must cover:

```text
File Exists
File Missing
Directory Exists
Directory Missing
Permission Denied
Read Failure
Write Failure
Delete Failure
Corrupted File
Partial File
Unexpected File
```

Tests should use isolated temporary directories.

Production filesystem locations should never be modified by automated tests.

---

## 10.9 TD-009 — Path Traversal Security Tests

Category:

```text
Testing / Security
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Required
```

The security debt documented in Section 8 must be backed by explicit tests.

Test cases should include:

```text
../file
../../file
..\file
Absolute Path
Mixed Separators
Encoded Path
Unexpected Filename
```

Expected behavior:

```text
Unsafe Path
    ↓
Rejected
```

This must be treated as a release-blocking security test.

---

## 10.10 TD-010 — Checksum Verification Test Debt

Category:

```text
Testing / Integrity
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

Checksum verification should have dedicated automated tests.

Required cases:

```text
Correct SHA256
Incorrect SHA256
Empty File
Modified File
Corrupted File
Large File
Missing File
```

Expected behavior must be deterministic.

For a mismatch:

```text
Expected Hash ≠ Actual Hash
        ↓
Verification Failed
        ↓
Artifact Not Activated
```

---

## 10.11 TD-011 — Corrupted Artifact Test Debt

Category:

```text
Testing / Integrity
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM should explicitly test what happens when a model artifact is corrupted.

Example:

```text
Valid Model
    ↓
Modify Several Bytes
    ↓
Verify
    ↓
Failure Expected
```

The system should not incorrectly report the artifact as healthy.

---

## 10.12 TD-012 — Partial Download Test Debt

Category:

```text
Testing / Network / Filesystem
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

The application should be tested against interrupted downloads.

Possible scenarios:

```text
Connection Lost
Process Interrupted
Server Disconnect
Disk Full
Timeout
Incomplete File
```

The resulting filesystem state must be predictable and safe.

A partially downloaded artifact must not be mistaken for a valid installed model.

---

## 10.13 TD-013 — Network Test Isolation

Category:

```text
Testing / Network
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Tests should not depend on external production URLs.

Bad pattern:

```text
Automated Test
    ↓
Real Internet
    ↓
External Server
```

This causes:

```text
Flaky Tests
Slow Tests
External Dependency
Rate Limits
Unpredictable Results
```

Preferred model:

```text
Test
 ↓
Mock / Controlled HTTP Server
 ↓
Predictable Response
```

---

## 10.14 TD-014 — HTTP Error Test Debt

Category:

```text
Testing / Network
```

Severity:

```text
High
```

Priority:

```text
P1
```

Network handling should be tested against common HTTP failures.

At minimum:

```text
400
401
403
404
408
429
500
502
503
504
```

The application should classify errors appropriately rather than treating every HTTP failure identically.

---

## 10.15 TD-015 — Timeout Test Debt

Category:

```text
Testing / Network / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Timeout handling must be tested.

The test environment should simulate:

```text
Connection Timeout
Read Timeout
Slow Response
Never-Ending Response
```

Expected behavior must include:

```text
Timeout
    ↓
Controlled Failure
    ↓
No Hung Process
```

---

## 10.16 TD-016 — Retry Behavior Test Debt

Category:

```text
Testing / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

If retry functionality exists or is introduced, it must be tested.

Test scenarios:

```text
Immediate Success
Fail → Success
Fail → Fail → Success
All Attempts Fail
Non-Retryable Error
Timeout → Retry
```

The test must verify that the retry limit is respected.

---

## 10.17 TD-017 — Mocking Strategy Debt

Category:

```text
Testing / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

AIPM needs consistent rules for what should be mocked.

Appropriate candidates may include:

```text
HTTP Client
System Clock
External Registry
External Services
```

However, excessive mocking can produce tests that pass while the real components do not work together.

Therefore:

```text
Unit Tests → More Mocking
Integration Tests → Less Mocking
E2E Tests → Minimal Mocking
```

---

## 10.18 TD-018 — Test Fixture Management

Category:

```text
Testing / Maintainability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Tests involving models and files require controlled fixtures.

The project should define reusable fixtures for:

```text
Valid Model
Invalid Model
Corrupted Model
Small Artifact
Metadata
Registry Entry
History Entry
Checksum
```

Fixtures should be small enough to keep tests fast.

Large real-world AI models should not be committed to the test repository merely to test file-management behavior.

---

## 10.19 TD-019 — Test Data Isolation

Category:

```text
Testing / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Each test should operate on isolated state.

A test should not depend on:

```text
Previous Test
User's Existing Models
Existing History
Global Configuration
Real Home Directory
External Network
```

Preferred:

```text
Test
 ↓
Temporary Environment
 ↓
Execute
 ↓
Assert
 ↓
Cleanup
```

---

## 10.20 TD-020 — Test Cleanup Debt

Category:

```text
Testing / Filesystem
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Tests that create:

```text
Files
Directories
History
Cache
Configuration
Temporary Downloads
```

must clean them after completion.

Cleanup must also occur when a test fails.

This prevents state leakage between tests.

---

## 10.21 TD-021 — Regression Test Debt

Category:

```text
Testing / Maintenance
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

Every significant bug discovered in AIPM should eventually receive a regression test.

Preferred workflow:

```text
Bug Discovered
    ↓
Reproduce
    ↓
Write Failing Test
    ↓
Fix Bug
    ↓
Test Passes
    ↓
Keep Test Permanently
```

This prevents previously fixed defects from silently returning.

---

## 10.22 TD-022 — Contract Test Debt

Category:

```text
Testing / Architecture
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM's public contracts should be tested.

Potential contracts include:

```text
CLI Commands
Exit Codes
Registry Schema
Configuration Schema
History Schema
Model Metadata
Public Python APIs
```

Changes to these contracts should require deliberate compatibility decisions.

---

## 10.23 TD-023 — Error Handling Test Debt

Category:

```text
Testing / Reliability
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

Error paths require as much attention as successful paths.

Tests should verify:

```text
Missing Model
Invalid Model
Invalid Registry
Network Failure
Checksum Failure
Permission Failure
Filesystem Failure
Invalid Configuration
Malformed Metadata
Unexpected Exception
```

A system that only tests success paths is not sufficiently tested.

---

## 10.24 TD-024 — Exception Mapping Test Debt

Category:

```text
Testing / Error Handling
```

Severity:

```text
High
```

Priority:

```text
P1
```

Internal exceptions should be mapped to predictable application-level behavior.

Tests should verify:

```text
Low-Level Exception
        ↓
Application Error
        ↓
User-Facing Message
        ↓
Correct Exit Code
```

This prevents internal implementation details from leaking into the CLI contract.

---

## 10.25 TD-025 — Security Regression Testing

Category:

```text
Testing / Security
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Required
```

Security controls documented in Section 8 must be included in regression testing.

Required security cases include:

```text
Path Traversal
Unsafe URL
HTTP URL
Checksum Mismatch
Malicious Filename
Malformed Metadata
Unsafe Archive Entry
Symlink
Permission Failure
Credential Exposure
Unsafe Deserialization
```

A security fix without a permanent regression test should not be considered fully resolved.

---

## 10.26 TD-026 — Unsafe Deserialization Test Debt

Category:

```text
Testing / Security
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Required Before Model Format Expansion
```

If AIPM supports serialized model formats, tests must verify that unsupported or dangerous serialization mechanisms are rejected or handled according to the defined security policy.

The test suite should explicitly prevent accidental introduction of unsafe loading behavior.

---

## 10.27 TD-027 — Permission Test Debt

Category:

```text
Testing / Filesystem / Security
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

Tests should simulate:

```text
Read Permission Denied
Write Permission Denied
Delete Permission Denied
Directory Permission Denied
Read-Only Filesystem
```

The expected result should be a controlled application failure rather than an uncontrolled traceback.

---

## 10.28 TD-028 — Cross-Platform Test Debt

Category:

```text
Testing / Portability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM should eventually be tested across supported operating systems.

At minimum, if these are official targets:

```text
Windows
Linux
macOS
```

Platform-specific concerns include:

```text
Path Separators
Permissions
Home Directory
Temporary Files
Process Execution
Filesystem Semantics
Line Endings
```

Tests should not assume Linux-style filesystem behavior when Windows is supported.

---

## 10.29 TD-029 — Python Version Compatibility Testing

Category:

```text
Testing / Compatibility
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

If AIPM supports multiple Python versions, CI should test the supported matrix.

Example:

```text
Python 3.x
Python 3.y
Python 3.z
```

The exact versions must be defined by the project's supported-runtime policy.

---

## 10.30 TD-030 — Dependency Compatibility Testing

Category:

```text
Testing / Dependencies
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Dependency upgrades should be tested against AIPM's core workflows.

A dependency update should not be considered safe merely because installation succeeds.

Required validation:

```text
Dependency Update
    ↓
Unit Tests
    ↓
Integration Tests
    ↓
CLI Tests
    ↓
Security Tests
    ↓
Regression Tests
```

---

## 10.31 TD-031 — Performance Test Debt

Category:

```text
Testing / Performance
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

The performance debt documented in Section 9 requires corresponding benchmarks.

Important operations include:

```text
CLI Startup
Registry Lookup
Checksum Verification
Large File Processing
Download
Repair
History Operations
```

Performance tests should establish baselines rather than simply asserting that an operation is "fast."

---

## 10.32 TD-032 — Large Artifact Testing

Category:

```text
Testing / Performance / Filesystem
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM's production workload may involve very large artifacts.

Therefore, the test strategy should eventually include representative artifact sizes.

Example categories:

```text
Tiny
Small
Medium
Large
Very Large
```

The exact sizes should be established according to the actual model ecosystem supported by AIPM.

Tests should verify:

```text
Memory Usage
Checksum Time
Download Behavior
Storage Handling
Repair Behavior
```

---

## 10.33 TD-033 — Concurrency Test Debt

Category:

```text
Testing / Concurrency
```

Severity:

```text
Medium
```

Priority:

```text
P3
```

Status:

```text
Future
```

If AIPM eventually supports parallel operations, concurrency tests will become mandatory.

Potential scenarios:

```text
Two Downloads
Download + Remove
Two Repairs
Concurrent History Writes
Concurrent Registry Access
```

The objective is to identify:

```text
Race Conditions
Deadlocks
File Corruption
State Corruption
Lost Updates
```

Concurrency testing should be introduced only when concurrent functionality exists.

---

## 10.34 TD-034 — Test Flakiness Debt

Category:

```text
Testing / Reliability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Tests must be deterministic wherever possible.

Potential causes of flakiness include:

```text
Real Network
Timing Assumptions
Shared Filesystem
Random Data
System Clock
Concurrency
External Services
```

Flaky tests should not simply be retried indefinitely.

The underlying cause should be identified and fixed.

---

## 10.35 TD-035 — Time-Dependent Test Debt

Category:

```text
Testing / Determinism
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

History and timestamps may make tests dependent on the actual system clock.

Where appropriate, the test architecture should allow controlled time.

Conceptually:

```text
Real Clock
    ↓
Injectable Clock
    ↓
Deterministic Test
```

This is especially useful for:

```text
History
Expiration
Retry
Timeout
Timestamp
Cleanup
```

---

## 10.36 TD-036 — Test Naming and Organization Debt

Category:

```text
Testing / Maintainability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Tests should be organized according to the project's architecture.

A possible structure is:

```text
tests/
├── unit/
├── integration/
├── e2e/
├── security/
├── performance/
└── fixtures/
```

The exact structure should follow the actual project framework and tooling.

Test names should describe behavior rather than implementation details.

Prefer:

```text
test_rejects_checksum_mismatch()
```

over:

```text
test_hash_function_2()
```

---

## 10.37 TD-037 — CI Test Automation Debt

Category:

```text
Testing / CI/CD
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Planned
```

Tests that are not automatically executed are easy to forget.

AIPM should eventually integrate core tests into CI.

Minimum pipeline:

```text
Push / Pull Request
        ↓
Install Dependencies
        ↓
Lint / Static Checks
        ↓
Unit Tests
        ↓
Integration Tests
        ↓
Security Tests
        ↓
CLI / E2E Tests
        ↓
Build Validation
```

Performance benchmarks may run separately if they are too expensive for every pull request.

---

## 10.38 TD-038 — Test Failure Reporting Debt

Category:

```text
Testing / CI
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

CI failures should provide enough information to diagnose the problem.

Reports should identify:

```text
Test Name
Failure Reason
Environment
Python Version
OS
Relevant Logs
Artifact Information
```

However, reports must respect the security requirements from Section 8 and must not expose secrets.

---

## 10.39 TD-039 — Coverage Reporting Debt

Category:

```text
Testing / Quality
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

AIPM should eventually generate test coverage reports.

However, coverage percentage should be treated as an indicator rather than a quality guarantee.

For example:

```text
90% Coverage
```

does not necessarily mean:

```text
90% Correctness
```

Critical security and integrity paths should receive explicit tests even when coverage is already high.

---

## 10.40 TD-040 — Mutation / Test Effectiveness Debt

Category:

```text
Testing / Quality
```

Severity:

```text
Low
```

Priority:

```text
P3
```

Status:

```text
Future
```

As the project matures, mutation testing may be used to determine whether tests actually detect meaningful code changes.

Conceptually:

```text
Code
 ↓
Introduce Small Mutation
 ↓
Run Tests
 ↓
Test Fails?
```

If tests continue to pass after a meaningful mutation, the test suite may not be sufficiently effective.

This is an advanced quality technique and should not block the initial stable release.

---

# 10.41 Testing Priority Matrix

| ID     | Testing Debt                 | Severity | Priority | Status     |
| ------ | ---------------------------- | -------- | -------- | ---------- |
| TD-001 | Automated Coverage           | High     | P1       | Identified |
| TD-002 | Test Strategy                | High     | P1       | Identified |
| TD-003 | Unit Tests                   | High     | P1       | Identified |
| TD-004 | Integration Tests            | Critical | P0       | Identified |
| TD-005 | E2E Workflow Tests           | Critical | P0       | Identified |
| TD-006 | CLI Tests                    | High     | P1       | Identified |
| TD-007 | Exit Code Tests              | High     | P1       | Identified |
| TD-008 | Filesystem Tests             | Critical | P0       | Identified |
| TD-009 | Path Traversal Tests         | Critical | P0       | Required   |
| TD-010 | Checksum Tests               | Critical | P0       | Required   |
| TD-011 | Corrupted Artifact Tests     | High     | P1       | Identified |
| TD-012 | Partial Download Tests       | High     | P1       | Planned    |
| TD-013 | Network Isolation            | High     | P1       | Identified |
| TD-014 | HTTP Error Tests             | High     | P1       | Identified |
| TD-015 | Timeout Tests                | High     | P1       | Identified |
| TD-016 | Retry Tests                  | Medium   | P2       | Planned    |
| TD-017 | Mocking Strategy             | Medium   | P2       | Identified |
| TD-018 | Test Fixtures                | Medium   | P2       | Planned    |
| TD-019 | Test Data Isolation          | High     | P1       | Identified |
| TD-020 | Test Cleanup                 | Medium   | P2       | Identified |
| TD-021 | Regression Tests             | Critical | P0       | Identified |
| TD-022 | Contract Tests               | High     | P1       | Planned    |
| TD-023 | Error Handling Tests         | Critical | P0       | Identified |
| TD-024 | Exception Mapping Tests      | High     | P1       | Identified |
| TD-025 | Security Regression          | Critical | P0       | Required   |
| TD-026 | Unsafe Deserialization Tests | Critical | P0       | Required   |
| TD-027 | Permission Tests             | High     | P1       | Planned    |
| TD-028 | Cross-Platform Tests         | High     | P1       | Planned    |
| TD-029 | Python Compatibility         | Medium   | P2       | Planned    |
| TD-030 | Dependency Compatibility     | Medium   | P2       | Planned    |
| TD-031 | Performance Tests            | High     | P1       | Planned    |
| TD-032 | Large Artifact Tests         | High     | P1       | Planned    |
| TD-033 | Concurrency Tests            | Medium   | P3       | Future     |
| TD-034 | Flaky Test Management        | High     | P1       | Identified |
| TD-035 | Time-Dependent Tests         | Medium   | P2       | Planned    |
| TD-036 | Test Organization            | Medium   | P2       | Identified |
| TD-037 | CI Test Automation           | Critical | P0       | Planned    |
| TD-038 | Failure Reporting            | Medium   | P2       | Planned    |
| TD-039 | Coverage Reporting           | Medium   | P2       | Planned    |
| TD-040 | Mutation Testing             | Low      | P3       | Future     |

---

# 10.42 Recommended Testing Pyramid

AIPM should follow a layered testing strategy.

```text
                 ┌───────────────┐
                 │     E2E       │
                 │    Tests      │
                 └───────┬───────┘
                         │
                 ┌───────▼───────┐
                 │  Integration  │
                 │    Tests      │
                 └───────┬───────┘
                         │
              ┌──────────▼──────────┐
              │     Unit Tests      │
              │                     │
              └─────────────────────┘
```

The majority of tests should be fast unit tests.

Integration tests should verify important component boundaries.

E2E tests should focus on critical user workflows rather than attempting to test every internal detail through the CLI.

---

# 10.43 Required Critical Workflow Tests

Before AIPM reaches a stable release, the following workflows should have automated end-to-end coverage:

```text
1. Install Valid Model
        ↓
2. List Installed Model
        ↓
3. Verify Valid Model
        ↓
4. Detect Corrupted Model
        ↓
5. Repair Corrupted Model
        ↓
6. Remove Model
        ↓
7. Record / Read History
```

The complete lifecycle should be testable:

```text
Install
   ↓
Verify
   ↓
Corrupt
   ↓
Verify → Fail
   ↓
Repair
   ↓
Verify → Pass
   ↓
Remove
   ↓
Verify → Not Installed
```

This lifecycle is one of the most important test scenarios in AIPM.

---

# 10.44 Testing and Security Boundary

Security tests are not optional extensions of the test suite.

The following should be treated as release-blocking where applicable:

```text
Path Traversal
Checksum Bypass
Unsafe File Access
Unsafe Deserialization
Command Injection
Credential Leakage
Unsafe Archive Extraction
```

A security control should have:

```text
Implementation
+
Positive Test
+
Negative Test
+
Regression Test
```

---

# 10.45 Testing and Performance Boundary

Performance tests should not replace correctness tests.

For example:

```text
Faster Checksum
```

is not an improvement if:

```text
Checksum Becomes Incorrect
```

Likewise:

```text
Faster Download
```

is not acceptable if:

```text
Corrupted Artifact Can Be Activated
```

The testing priority remains:

```text
Correctness
    ↓
Security
    ↓
Reliability
    ↓
Performance
```

---

# 10.46 Testing Definition of Done

A feature should not be considered complete until the relevant testing layers have been addressed.

```text
Feature Implemented
       ↓
Unit Test
       ↓
Integration Test
       ↓
Failure Test
       ↓
Security Test
       ↓
Regression Test
       ↓
CI Validation
       ↓
Documentation
```

Not every feature requires every layer.

The applicable testing level must be determined by the feature's risk and architectural boundary.

---

# 10.47 Test Debt Resolution Order

The recommended order for reducing current testing debt is:

```text
1. Establish Test Infrastructure
        ↓
2. Unit Tests for Core Logic
        ↓
3. Filesystem Integration Tests
        ↓
4. Checksum / Integrity Tests
        ↓
5. CLI Tests
        ↓
6. Critical E2E Workflows
        ↓
7. Security Regression Tests
        ↓
8. Network Integration Tests
        ↓
9. Performance Baselines
        ↓
10. Cross-Platform CI
        ↓
11. Advanced Testing
```

Advanced techniques such as mutation testing should come later.

---

# 10.48 Testing Release Gate

AIPM should not be considered stable-production-ready until:

* Core unit tests are automated.
* Critical integration tests exist.
* Install, verify, repair, and remove workflows are tested.
* CLI behavior is tested.
* Exit codes are tested.
* Filesystem failures are tested.
* Checksum mismatch is tested.
* Corrupted artifacts are tested.
* Path traversal is tested.
* Network failures are tested without relying on the public internet.
* Critical security controls have regression tests.
* Tests run automatically in CI.
* Test environments are isolated.
* Tests are sufficiently deterministic.
* Important performance baselines are established.
* No known critical test gap remains around a security-sensitive workflow.

---

# 10.49 Testing Debt Exit Criteria

A testing-debt item may be marked `Resolved` only when:

```text
Requirement Identified
       ↓
Test Case Designed
       ↓
Automated Test Implemented
       ↓
Test Passes
       ↓
Failure Case Verified
       ↓
CI Executes Test
       ↓
Regression Protected
       ↓
Documentation Updated
```

A test that only exists locally but is not executed automatically should not be considered fully resolved for release-critical functionality.

---

# 10.50 Summary

Testing debt is one of the most important technical-debt categories remaining for AIPM because the application operates across filesystem, network, registry, integrity, CLI, and model-management boundaries.

The project should not attempt to solve testing debt by simply maximizing test-count or code-coverage percentage.

The correct approach is risk-based testing:

```text
Critical Security Path
        ↓
Critical Data / Integrity Path
        ↓
Critical User Workflow
        ↓
Component Integration
        ↓
Unit-Level Logic
        ↓
Performance / Compatibility
```

The highest priority should be to establish reliable automated verification for the complete model lifecycle:

```text
Install
   ↓
Verify
   ↓
Corrupt
   ↓
Detect
   ↓
Repair
   ↓
Verify Again
   ↓
Remove
   ↓
Confirm Removal
```

The central testing principle for AIPM is:

> Every critical behavior must have an automated test, and every important failure mode must have an automated negative test.

The immediate objective is therefore not to create hundreds of tests indiscriminately. It is to build a small but trustworthy testing foundation around the critical workflows and then expand coverage systematically as the architecture stabilizes.

# 11. Dependency Debt

Dependency debt refers to technical debt created by third-party libraries, packages, frameworks, runtimes, external tools, and other software components on which AIPM depends.

AIPM does not operate in isolation. Its functionality depends on the Python runtime, third-party packages, networking libraries, filesystem-related components, model-format libraries, CLI tooling, and potentially external services.

Poor dependency management can gradually create:

```text
Security Vulnerabilities
Compatibility Problems
Breaking Changes
Version Conflicts
Abandoned Dependencies
Unnecessary Dependencies
Large Installation Size
Slow Installation
Maintenance Burden
Licensing Risk
Supply-Chain Risk
```

Dependency management must therefore be treated as an architectural concern rather than merely a package-installation concern.

---

## 11.1 TD-041 — Dependency Inventory Debt

Category:

```text
Dependencies / Governance
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM requires a clear and authoritative inventory of all direct and indirect dependencies.

The dependency inventory should distinguish:

```text
Direct Dependencies
Transitive Dependencies
Development Dependencies
Testing Dependencies
Optional Dependencies
Build Dependencies
Runtime Dependencies
```

The project should be able to answer:

> Which dependency is required, why is it required, and where is it used?

A dependency that cannot be justified should be considered a candidate for removal.

---

## 11.2 TD-042 — Direct vs Transitive Dependency Debt

Category:

```text
Dependencies / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

AIPM should clearly distinguish packages explicitly selected by the project from packages installed indirectly.

Conceptually:

```text
AIPM
 ↓
Direct Dependency A
 ↓
Transitive Dependency B
 ↓
Transitive Dependency C
```

AIPM should not unnecessarily depend directly on a package merely because another package happens to install it.

Direct dependencies should represent actual application requirements.

---

## 11.3 TD-043 — Dependency Version Pinning Debt

Category:

```text
Dependencies / Reproducibility
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Uncontrolled dependency versions can produce different environments on different machines.

For example:

```text
Developer Machine
        ↓
Package Version A

Production Machine
        ↓
Package Version B
```

This can result in:

```text
Works Locally
       ↓
Fails in Production
```

AIPM needs an explicit dependency-versioning strategy.

The strategy should balance:

```text
Reproducibility
Security Updates
Bug Fixes
Compatibility
Maintenance
```

Blindly pinning every package forever is not sufficient either. The project must also define how versions are intentionally updated.

---

## 11.4 TD-044 — Lockfile / Reproducible Environment Debt

Category:

```text
Dependencies / Reproducibility
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM should provide a reproducible dependency installation process.

A fresh environment should be able to perform:

```text
Clean Environment
      ↓
Install Project
      ↓
Resolve Dependencies
      ↓
Run Tests
      ↓
Run Application
```

with predictable results.

The repository should have a clearly defined source of truth for dependency resolution.

---

## 11.5 TD-045 — Outdated Dependency Debt

Category:

```text
Dependencies / Maintenance
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Requires Dependency Audit
```

Dependencies should periodically be reviewed for:

```text
New Releases
Security Fixes
Bug Fixes
Deprecations
Breaking Changes
Performance Improvements
Python Compatibility
```

However, upgrading a dependency simply because a newer version exists is not an adequate policy.

Each upgrade should be evaluated against:

```text
Compatibility
Security
Tests
Performance
API Changes
Migration Cost
```

---

## 11.6 TD-046 — Vulnerable Dependency Debt

Category:

```text
Dependencies / Security
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Release Blocking
```

Known vulnerable dependencies must not remain unresolved in a production release without a documented risk decision.

The dependency security workflow should be:

```text
Dependency
     ↓
Vulnerability Detected
     ↓
Assess Severity
     ↓
Check Fixed Version
     ↓
Upgrade / Replace / Mitigate
     ↓
Run Tests
     ↓
Security Validation
```

Security scanning should eventually become part of CI.

---

## 11.7 TD-047 — Dependency Supply-Chain Risk

Category:

```text
Dependencies / Security
```

Severity:

```text
Critical
```

Priority:

```text
P0
```

Status:

```text
Identified
```

Third-party packages create software supply-chain risk.

Potential threats include:

```text
Compromised Package
Malicious Release
Typosquatting
Dependency Hijacking
Maintainer Account Compromise
Malicious Transitive Dependency
```

AIPM should therefore minimize unnecessary dependencies.

The principle should be:

```text
Every Dependency
        ↓
Trust Decision
        ↓
Security Review
        ↓
Usage Justification
```

---

## 11.8 TD-048 — Unnecessary Dependency Debt

Category:

```text
Dependencies / Maintainability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Unused packages increase:

```text
Attack Surface
Installation Size
Dependency Resolution Complexity
Maintenance Cost
Upgrade Risk
```

Therefore, unused dependencies should be removed.

A dependency should remain only when it provides meaningful value to the application.

---

## 11.9 TD-049 — Dependency Duplication Debt

Category:

```text
Dependencies / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Multiple libraries may sometimes provide overlapping functionality.

For example:

```text
Library A → HTTP
Library B → HTTP
Library C → HTTP
```

This can increase complexity without providing proportional value.

Where appropriate, AIPM should standardize on one well-supported library per major responsibility.

---

## 11.10 TD-050 — Heavy Dependency Debt

Category:

```text
Dependencies / Performance
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

A dependency may be functionally useful but disproportionately expensive.

Potential costs include:

```text
Large Package Size
Long Installation Time
High Memory Consumption
Slow Startup
Additional Native Libraries
Platform Compatibility Problems
```

Dependency selection should therefore consider operational cost, not only functionality.

---

## 11.11 TD-051 — Optional Dependency Management Debt

Category:

```text
Dependencies / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Not every feature necessarily needs to be installed for every AIPM user.

Where appropriate, dependencies should be separated into:

```text
Core
Optional
Development
Testing
```

Conceptually:

```text
AIPM Core
   │
   ├── Required Dependencies
   │
   └── Optional Feature
          ↓
      Optional Dependency
```

This can reduce installation size and simplify deployment.

---

## 11.12 TD-052 — Development Dependency Separation Debt

Category:

```text
Dependencies / Build
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Development-only packages should not unnecessarily become runtime requirements.

Examples may include:

```text
Test Framework
Coverage Tools
Linting Tools
Formatting Tools
Documentation Tools
Benchmarking Tools
```

The project should maintain a clean separation between:

```text
Runtime Environment
Development Environment
CI Environment
```

---

## 11.13 TD-053 — Testing Dependency Debt

Category:

```text
Dependencies / Testing
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Testing infrastructure may require additional packages.

These should remain isolated from the production runtime unless there is a genuine runtime requirement.

Testing dependencies should also be periodically reviewed because they themselves become part of the maintenance surface.

---

## 11.14 TD-054 — Dependency Compatibility Matrix Debt

Category:

```text
Dependencies / Compatibility
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM needs a defined compatibility matrix covering at least:

```text
Python Version
Operating System
Core Dependencies
Optional Dependencies
Model Format
```

Conceptually:

```text
AIPM Version
      ↓
Python Version
      ↓
OS
      ↓
Dependency Versions
      ↓
Supported
```

This prevents compatibility claims from being ambiguous.

---

## 11.15 TD-055 — Python Runtime Dependency Debt

Category:

```text
Dependencies / Runtime
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Requires Policy
```

The supported Python runtime must be explicitly defined.

The project should specify:

```text
Minimum Python Version
Recommended Python Version
Maximum Tested Version
Unsupported Versions
```

The application should fail clearly when executed under an unsupported runtime rather than producing confusing downstream errors.

---

## 11.16 TD-056 — Native System Dependency Debt

Category:

```text
Dependencies / Portability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Requires Audit
```

Some Python packages may depend on operating-system-level components.

Potential examples include:

```text
C/C++ Runtime
System Libraries
Compiler Toolchain
GPU Runtime
Driver
External Executable
```

These dependencies must be documented separately from Python packages.

The installation model should make clear:

```text
Python Dependency
        ≠
System Dependency
```

---

## 11.17 TD-057 — External Tool Dependency Debt

Category:

```text
Dependencies / Operations
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Requires Audit
```

If AIPM invokes external programs, those tools become part of the effective dependency graph.

For example:

```text
AIPM
 ↓
External Executable
 ↓
Operating System
```

The application must validate the tool's availability and provide a clear error if it is missing.

A silent assumption that a tool exists on the user's machine creates operational debt.

---

## 11.18 TD-058 — Dependency API Stability Debt

Category:

```text
Dependencies / Maintainability
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

AIPM should avoid tightly coupling its internal architecture to unstable third-party APIs.

Preferred architecture:

```text
AIPM Business Logic
        ↓
Internal Abstraction
        ↓
Third-Party Library
```

rather than:

```text
AIPM Business Logic
        ↓
Third-Party API Everywhere
```

An abstraction layer can make future dependency replacement easier.

---

## 11.19 TD-059 — Dependency Upgrade Test Debt

Category:

```text
Dependencies / Testing
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Required
```

Dependency upgrades must trigger automated validation.

Required sequence:

```text
Dependency Upgrade
       ↓
Install
       ↓
Unit Tests
       ↓
Integration Tests
       ↓
CLI Tests
       ↓
Security Tests
       ↓
Regression Tests
```

A package upgrade should never be treated as an isolated file change.

---

## 11.20 TD-060 — Breaking Change Management Debt

Category:

```text
Dependencies / Maintenance
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Major dependency upgrades may contain breaking API changes.

AIPM needs an explicit procedure:

```text
New Major Version
       ↓
Read Changelog
       ↓
Review Migration Guide
       ↓
Identify Breaking Changes
       ↓
Update Code
       ↓
Run Full Test Suite
       ↓
Document Change
```

---

## 11.21 TD-061 — Dependency Deprecation Debt

Category:

```text
Dependencies / Maintenance
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Dependencies can become deprecated before they become completely unusable.

AIPM should monitor:

```text
Deprecated API
Deprecated Package
Unmaintained Project
Archived Repository
End-of-Life Runtime
```

The project should migrate away from deprecated components before they become release blockers.

---

## 11.22 TD-062 — Abandoned Dependency Debt

Category:

```text
Dependencies / Sustainability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

An apparently stable package can become risky if it is no longer maintained.

Warning indicators include:

```text
No Recent Releases
No Maintainer Activity
Unresolved Issues
Unpatched Vulnerabilities
Archived Repository
Outdated Runtime Support
```

AIPM should not automatically replace every inactive package, but inactive dependencies should be explicitly reviewed.

---

## 11.23 TD-063 — Dependency License Audit Debt

Category:

```text
Dependencies / Legal
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Requires Audit
```

Dependency licensing must be reviewed before commercial distribution.

The project should maintain visibility into:

```text
Package
Version
License
Direct / Transitive
Commercial Compatibility
Notice Requirement
```

This is particularly important because AIPM is intended to become a commercial-ready, sellable software product.

A technically valid dependency may still create distribution or licensing constraints.

---

## 11.24 TD-064 — Dependency Notice / Attribution Debt

Category:

```text
Dependencies / Legal / Documentation
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Where dependency licenses require attribution or notices, the project should provide the required documentation.

Possible deliverables:

```text
Third-Party Notices
License Information
Attribution File
Dependency Manifest
```

The exact requirement depends on the licenses actually used.

---

## 11.25 TD-065 — Dependency Security Monitoring Debt

Category:

```text
Dependencies / Security / CI
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

Dependency security should not depend exclusively on manual review.

The project should eventually automate:

```text
Dependency Scan
       ↓
Vulnerability Detection
       ↓
Severity Assessment
       ↓
Alert
       ↓
Upgrade / Mitigation
       ↓
Test
```

This should become part of the project's CI/CD security process.

---

## 11.26 TD-066 — Transitive Vulnerability Visibility Debt

Category:

```text
Dependencies / Security
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM must account for vulnerabilities in transitive dependencies.

For example:

```text
AIPM
 ↓
Library A
 ↓
Library B
 ↓
Vulnerable Library C
```

Even though AIPM did not explicitly select Library C, the vulnerability can still affect the application.

Therefore, security review must inspect the complete dependency graph.

---

## 11.27 TD-067 — Dependency Conflict Debt

Category:

```text
Dependencies / Compatibility
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Different packages can require incompatible versions of the same dependency.

Example:

```text
Package A → Dependency X >= 1,<2

Package B → Dependency X >= 2,<3
```

This can make the environment impossible to resolve cleanly.

Dependency conflicts should be detected during installation and CI rather than discovered by end users.

---

## 11.28 TD-068 — Dependency Upgrade Cadence Debt

Category:

```text
Dependencies / Maintenance
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Dependency maintenance should follow a predictable cadence.

A reasonable lifecycle is:

```text
Periodic Review
      ↓
Security Updates
      ↓
Patch Updates
      ↓
Minor Updates
      ↓
Major Updates
```

Security updates should receive priority over routine upgrade cycles.

---

## 11.29 TD-069 — Dependency Change Documentation Debt

Category:

```text
Dependencies / Documentation
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Dependency changes should be documented when they affect:

```text
Architecture
Installation
Compatibility
Security
Performance
API Behavior
```

A dependency update should therefore be traceable through:

```text
Commit
 ↓
Changelog
 ↓
Release
```

where appropriate.

---

## 11.30 TD-070 — Dependency Rollback Debt

Category:

```text
Dependencies / Reliability
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Dependency upgrades can introduce regressions.

The project should therefore preserve enough version information to reproduce a previous working environment.

Conceptually:

```text
Current Version
      ↓
Regression Detected
      ↓
Identify Previous Known-Good Version
      ↓
Rollback / Pin
      ↓
Investigate
```

Rollback capability is particularly important for production releases.

---

## 11.31 TD-071 — Dependency Reproducibility Across Environments

Category:

```text
Dependencies / DevOps
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

The following environments should ideally produce equivalent dependency environments:

```text
Developer
CI
Staging
Production
```

The desired relationship is:

```text
Same Project Definition
        ↓
Same Dependency Resolution
        ↓
Same Expected Behavior
```

Differences should be intentional and documented.

---

## 11.32 TD-072 — Dependency Documentation Debt

Category:

```text
Dependencies / Documentation
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Identified
```

Documentation should explain the purpose of important dependencies.

For example:

```text
Dependency
   ↓
Purpose
   ↓
Why It Was Selected
   ↓
Where It Is Used
```

This prevents future maintainers from removing a package without understanding its architectural role.

---

## 11.33 TD-073 — Dependency Replacement Cost Debt

Category:

```text
Dependencies / Architecture
```

Severity:

```text
Medium
```

Priority:

```text
P2
```

Status:

```text
Planned
```

Some dependencies may become difficult to replace because their APIs are spread throughout the codebase.

AIPM should minimize this coupling.

Preferred:

```text
Application
    ↓
Internal Interface
    ↓
Dependency
```

This makes future replacement:

```text
Dependency A
      ↓
Dependency B
```

less disruptive.

---

## 11.34 TD-074 — Dependency Surface Area Debt

Category:

```text
Dependencies / Security
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Identified
```

Every additional dependency expands the software's attack and maintenance surface.

Conceptually:

```text
More Dependencies
       ↓
More Code
       ↓
More APIs
       ↓
More Vulnerability Opportunities
       ↓
More Updates
       ↓
More Compatibility Risk
```

Therefore, dependency minimization should be considered a security strategy.

---

## 11.35 TD-075 — Dependency Trust Policy Debt

Category:

```text
Dependencies / Security
```

Severity:

```text
High
```

Priority:

```text
P1
```

Status:

```text
Planned
```

AIPM should establish a dependency trust policy.

The policy should define how the project evaluates:

```text
Package Reputation
Maintenance Activity
Release History
Security Record
License
Community Adoption
API Stability
Project Ownership
```

The goal is not to guarantee that a package is safe, but to establish a consistent selection process.

---

# 11.36 Dependency Priority Matrix

| ID     | Dependency Debt                     | Severity | Priority | Status           |
| ------ | ----------------------------------- | -------- | -------- | ---------------- |
| TD-041 | Dependency Inventory                | High     | P1       | Identified       |
| TD-042 | Direct vs Transitive Dependencies   | Medium   | P2       | Identified       |
| TD-043 | Version Pinning                     | High     | P1       | Identified       |
| TD-044 | Lockfile / Reproducibility          | High     | P1       | Planned          |
| TD-045 | Outdated Dependencies               | High     | P1       | Requires Audit   |
| TD-046 | Vulnerable Dependencies             | Critical | P0       | Release Blocking |
| TD-047 | Supply-Chain Risk                   | Critical | P0       | Identified       |
| TD-048 | Unnecessary Dependencies            | Medium   | P2       | Identified       |
| TD-049 | Dependency Duplication              | Medium   | P2       | Planned          |
| TD-050 | Heavy Dependencies                  | Medium   | P2       | Planned          |
| TD-051 | Optional Dependencies               | Medium   | P2       | Planned          |
| TD-052 | Development Dependency Separation   | Medium   | P2       | Identified       |
| TD-053 | Testing Dependencies                | Medium   | P2       | Planned          |
| TD-054 | Compatibility Matrix                | High     | P1       | Planned          |
| TD-055 | Python Runtime                      | High     | P1       | Requires Policy  |
| TD-056 | Native System Dependencies          | High     | P1       | Requires Audit   |
| TD-057 | External Tools                      | Medium   | P2       | Requires Audit   |
| TD-058 | API Stability                       | High     | P1       | Identified       |
| TD-059 | Upgrade Testing                     | High     | P1       | Required         |
| TD-060 | Breaking Changes                    | High     | P1       | Identified       |
| TD-061 | Deprecations                        | Medium   | P2       | Planned          |
| TD-062 | Abandoned Dependencies              | Medium   | P2       | Planned          |
| TD-063 | License Audit                       | High     | P1       | Requires Audit   |
| TD-064 | Attribution / Notices               | Medium   | P2       | Planned          |
| TD-065 | Security Monitoring                 | High     | P1       | Planned          |
| TD-066 | Transitive Vulnerability Visibility | High     | P1       | Planned          |
| TD-067 | Dependency Conflicts                | Medium   | P2       | Planned          |
| TD-068 | Upgrade Cadence                     | Medium   | P2       | Planned          |
| TD-069 | Change Documentation                | Medium   | P2       | Planned          |
| TD-070 | Rollback Capability                 | Medium   | P2       | Planned          |
| TD-071 | Environment Reproducibility         | High     | P1       | Planned          |
| TD-072 | Dependency Documentation            | Medium   | P2       | Identified       |
| TD-073 | Replacement Cost                    | Medium   | P2       | Planned          |
| TD-074 | Dependency Surface Area             | High     | P1       | Identified       |
| TD-075 | Trust Policy                        | High     | P1       | Planned          |

---

# 11.37 Dependency Management Lifecycle

AIPM should eventually manage dependencies through a controlled lifecycle:

```text
Identify
   ↓
Justify
   ↓
Evaluate
   ↓
Add
   ↓
Pin / Resolve
   ↓
Test
   ↓
Monitor
   ↓
Update
   ↓
Security Scan
   ↓
Retest
   ↓
Document
   ↓
Remove When Unnecessary
```

Dependency management should therefore be continuous rather than a one-time setup task.

---

# 11.38 Dependency Upgrade Definition of Done

A dependency upgrade should not be considered complete merely because installation succeeds.

The minimum workflow should be:

```text
New Dependency Version
        ↓
Compatibility Review
        ↓
Security Review
        ↓
Code Update
        ↓
Unit Tests
        ↓
Integration Tests
        ↓
CLI Tests
        ↓
Regression Tests
        ↓
Build / Package Test
        ↓
Documentation Update
```

For major upgrades, additional migration analysis may be required.

---

# 11.39 Dependency Removal Definition of Done

Removing a dependency should also be treated as a controlled change.

Required process:

```text
Identify Usage
      ↓
Confirm No Required Runtime Usage
      ↓
Remove Code References
      ↓
Remove Dependency
      ↓
Clean Environment Installation
      ↓
Run Tests
      ↓
Security Scan
      ↓
Verify Packaging
```

The goal is to ensure that the package was not being used indirectly by an overlooked feature.

---

# 11.40 Dependency Release Gate

Before a production or commercial release, AIPM should satisfy the following dependency requirements:

* All direct runtime dependencies are documented.
* Dependency versions are reproducible.
* Known critical vulnerabilities are resolved or explicitly risk-accepted.
* Dependency licenses have been reviewed.
* Transitive dependencies are visible.
* Unsupported Python/runtime combinations are documented.
* Important system-level dependencies are documented.
* Dependency upgrades have passed the relevant test suite.
* Unnecessary dependencies have been removed where practical.
* Dependency-related security checks are integrated into CI.
* Important dependency changes are traceable through version control.
* The project can reproduce a known-good dependency environment.

---

# 11.41 Dependency Debt Resolution Order

The recommended order for resolving dependency debt is:

```text
1. Inventory Dependencies
        ↓
2. Identify Runtime / Dev / Test Separation
        ↓
3. Establish Reproducible Dependency Resolution
        ↓
4. Audit Vulnerabilities
        ↓
5. Audit Licenses
        ↓
6. Identify Unused Dependencies
        ↓
7. Review Python / OS Compatibility
        ↓
8. Review API Coupling
        ↓
9. Establish Upgrade Policy
        ↓
10. Automate Dependency Monitoring
```

Security vulnerabilities and severe compatibility problems should always take precedence over routine cleanup.

---

# 11.42 Dependency Debt Exit Criteria

A dependency-debt item may be marked `Resolved` when:

```text
Dependency Identified
       ↓
Purpose Documented
       ↓
Version Policy Defined
       ↓
Security Status Reviewed
       ↓
Compatibility Verified
       ↓
Tests Pass
       ↓
CI Validation Passes
       ↓
Documentation Updated
```

For dependency removal:

```text
Usage Removed
       ↓
Package Removed
       ↓
Clean Installation Verified
       ↓
Tests Pass
       ↓
Packaging Verified
```

---

# 11.43 Summary

Dependency debt is not simply the problem of having old packages.

It includes the complete set of risks associated with relying on third-party software:

```text
Version
Security
Compatibility
Licensing
Maintenance
Supply Chain
Performance
Reproducibility
API Stability
Operational Availability
```

For AIPM, dependency management is especially important because the project is intended to evolve from an academic/legacy project into a:

```text
Professional
Scalable
Secure
Maintainable
Commercial-Ready
Sellable
```

software product.

The core principle should therefore be:

> Every dependency must have a reason to exist, a defined compatibility boundary, a reproducible version strategy, and an acceptable security and licensing profile.

The immediate focus should be to establish an authoritative dependency inventory and reproducible environment first. Once that foundation exists, vulnerability scanning, license auditing, upgrade automation, and dependency minimization can be implemented systematically.

Dependency debt should ultimately be managed as part of the project's normal engineering lifecycle rather than treated as occasional cleanup.

# 12. Refactoring Candidates

Refactoring is the controlled restructuring of existing source code without intentionally changing its externally observable behavior.

For AIPM, refactoring is necessary because the project is being transitioned from an older/academic implementation toward a professional, scalable, secure, maintainable, and commercial-ready architecture.

The objective is not to rewrite everything unnecessarily.

The objective is:

```text
Existing Working Code
        ↓
Identify Structural Problems
        ↓
Refactor High-Value Areas
        ↓
Preserve Existing Behavior
        ↓
Improve Maintainability
        ↓
Improve Testability
        ↓
Improve Extensibility
```

Refactoring should therefore be evidence-driven and performed incrementally.

---

## 12.1 Refactoring Principles

AIPM refactoring should follow these principles:

1. Do not refactor without identifying a concrete problem.
2. Do not combine large architectural changes with unrelated refactoring.
3. Preserve existing behavior unless the change is explicitly a feature change.
4. Add or improve tests before high-risk refactoring.
5. Prefer small, reviewable commits.
6. Refactor according to dependency and architectural boundaries.
7. Remove duplication rather than merely moving it.
8. Avoid premature abstraction.
9. Avoid introducing design patterns without a demonstrated need.
10. Every significant refactor must leave the code easier to understand than before.

The target is not:

```text
More Abstraction
```

The target is:

```text
Better Structure
```

---

# 12.2 RC-001 — Project Structure Refactoring

Category:

```text
Architecture / Structure
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

The project structure should be reviewed to ensure that responsibilities are clearly separated.

The desired structure should conceptually distinguish:

```text
Application Logic
       ↓
Domain / Business Logic
       ↓
Infrastructure
       ↓
External Dependencies
```

The project should avoid allowing unrelated responsibilities to accumulate inside a single module or file.

---

# 12.3 RC-002 — Large Module Refactoring

Category:

```text
Code Structure
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Large modules should be reviewed for excessive responsibilities.

A module that performs:

```text
Input Handling
Validation
Business Logic
File Operations
Network Operations
Error Handling
Output Formatting
```

is difficult to maintain.

The preferred direction is:

```text
Input
 ↓
Validation
 ↓
Business Logic
 ↓
Infrastructure
 ↓
Output
```

Each layer should have a clear responsibility.

---

# 12.4 RC-003 — God Function Refactoring

Category:

```text
Code Quality
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Functions containing large amounts of unrelated logic should be decomposed.

A problematic function may resemble:

```text
function process():
    validate()
    load_data()
    transform_data()
    calculate()
    save()
    generate_output()
    print_result()
```

The preferred direction is:

```text
process()
   ├── validate_input()
   ├── load_data()
   ├── transform_data()
   ├── calculate_result()
   ├── persist_result()
   └── generate_output()
```

The goal is not to create dozens of tiny functions.

The goal is meaningful separation of responsibilities.

---

# 12.5 RC-004 — Duplicate Logic Refactoring

Category:

```text
Code Quality
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Repeated logic should be identified and evaluated.

Example:

```text
Module A → same validation
Module B → same validation
Module C → same validation
```

If the logic represents the same business rule, it should have a single authoritative implementation.

However, superficially similar code should not automatically be merged.

The rule is:

```text
Same Meaning
    +
Same Responsibility
    =
Potential Shared Implementation
```

---

# 12.6 RC-005 — Conditional Complexity Refactoring

Category:

```text
Code Quality
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Deep conditional structures should be reviewed.

Example:

```text
if A:
    if B:
        if C:
            ...
```

Potential improvements may include:

```text
Guard Clauses
Strategy Pattern
Polymorphism
Dedicated Functions
Configuration Mapping
```

The appropriate solution depends on the actual business logic.

Patterns should not be introduced merely to make code appear sophisticated.

---

# 12.7 RC-006 — Error Handling Refactoring

Category:

```text
Reliability
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Error handling should be consistent throughout the application.

The preferred conceptual flow is:

```text
Error Occurs
     ↓
Identify Error Type
     ↓
Capture Context
     ↓
Log Appropriate Information
     ↓
Return Controlled Error
```

The project should avoid:

```text
Silent Failure
Generic Catch-All
Hidden Exceptions
Unclear Error Messages
Duplicated Error Handling
```

---

# 12.8 RC-007 — Input Validation Refactoring

Category:

```text
Security / Code Quality
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Input validation should be separated from core business logic where appropriate.

Conceptually:

```text
Raw Input
   ↓
Validation
   ↓
Normalized Input
   ↓
Business Logic
```

This makes business logic easier to test and reduces repeated validation code.

---

# 12.9 RC-008 — Configuration Refactoring

Category:

```text
Architecture / Configuration
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Configuration values should not be unnecessarily hard-coded throughout the source code.

Problematic:

```text
Module A → hard-coded value
Module B → same hard-coded value
Module C → different copy
```

Preferred:

```text
Configuration
     ↓
Application
```

Environment-specific values should be separated from application logic.

---

# 12.10 RC-009 — File I/O Refactoring

Category:

```text
Infrastructure
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Direct filesystem operations scattered throughout application logic should be reviewed.

Preferred:

```text
Business Logic
      ↓
File / Storage Abstraction
      ↓
Filesystem
```

This makes future changes easier, such as:

```text
Local Storage
      ↓
Cloud Storage
```

without rewriting business logic.

---

# 12.11 RC-010 — External Service Coupling Refactoring

Category:

```text
Architecture
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Direct coupling to external services should be minimized.

Instead of:

```text
Business Logic
      ↓
External API
```

prefer:

```text
Business Logic
      ↓
Internal Interface
      ↓
Service Adapter
      ↓
External API
```

This improves testability and future replacement capability.

---

# 12.12 RC-011 — Data Transformation Refactoring

Category:

```text
Code Quality
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Repeated data transformation logic should be centralized where the transformation represents a stable domain rule.

The desired pattern is:

```text
Raw Data
   ↓
Normalization
   ↓
Domain Representation
   ↓
Processing
```

This reduces inconsistent transformations across different parts of the system.

---

# 12.13 RC-012 — Naming Refactoring

Category:

```text
Maintainability
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Ambiguous names should be replaced with names that communicate intent.

Bad:

```text
data
temp
obj
result
process()
handle()
run()
```

Better names should describe the actual responsibility.

For example:

```text
load_configuration()
validate_model_input()
generate_prediction_report()
```

Naming refactoring is low-risk but has significant long-term maintainability benefits.

---

# 12.14 RC-013 — Magic Value Refactoring

Category:

```text
Code Quality
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Repeated unexplained constants should be replaced with meaningful named constants or configuration values where appropriate.

Instead of:

```text
if score > 0.75:
```

a domain-specific name may be preferable:

```text
if score > HIGH_CONFIDENCE_THRESHOLD:
```

This should only be done when the value has meaningful semantic significance.

---

# 12.15 RC-014 — Logging Refactoring

Category:

```text
Observability
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Logging should be standardized.

The project should distinguish:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Logs should contain sufficient context to diagnose failures without exposing secrets or sensitive information.

The logging architecture should eventually support:

```text
Application
    ↓
Central Logging Interface
    ↓
Configured Handler
```

---

# 12.16 RC-015 — CLI / Interface Refactoring

Category:

```text
Interface
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

If AIPM exposes command-line functionality, CLI responsibilities should be separated from internal business logic.

Preferred:

```text
CLI
 ↓
Argument Parsing
 ↓
Validation
 ↓
Application Service
 ↓
Domain Logic
```

The CLI should not contain the core processing algorithm itself.

This allows the same functionality to later be exposed through:

```text
CLI
API
GUI
Web Interface
```

without duplicating business logic.

---

# 12.17 RC-016 — API Boundary Refactoring

Category:

```text
Architecture
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

If AIPM is intended to become commercially usable, internal application functionality should be organized around stable service boundaries.

Conceptually:

```text
Interface
    ↓
Application Service
    ↓
Domain Logic
    ↓
Infrastructure
```

This makes future API development substantially easier.

---

# 12.18 RC-017 — Model / Business Logic Separation

Category:

```text
Architecture
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Model-processing code should be separated from generic application infrastructure where practical.

The conceptual separation should be:

```text
Application
    │
    ├── Input Handling
    ├── Model Management
    ├── Inference / Processing
    ├── Result Processing
    └── Output
```

This makes model replacement easier.

For example:

```text
Model A
   ↓
Model Interface
   ↓
Application
```

can later become:

```text
Model B
   ↓
Same Interface
   ↓
Application
```

---

# 12.19 RC-018 — Resource Management Refactoring

Category:

```text
Reliability / Performance
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Resources should be acquired and released deterministically.

Relevant resources may include:

```text
Files
Sockets
Database Connections
Processes
Model Resources
Memory
Temporary Files
```

Preferred conceptual pattern:

```text
Acquire
  ↓
Use
  ↓
Cleanup
```

even when an operation fails.

---

# 12.20 RC-019 — Temporary File Handling Refactoring

Category:

```text
Infrastructure / Security
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Temporary files should have:

```text
Controlled Location
Predictable Lifecycle
Unique Names
Cleanup Strategy
Permission Control
```

Temporary artifacts should not accumulate indefinitely.

The application should avoid leaving sensitive intermediate files on the system after successful execution.

---

# 12.21 RC-020 — Global State Refactoring

Category:

```text
Architecture / Testability
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Global mutable state makes software difficult to reason about and test.

Problem:

```text
Global State
    ↓
Module A modifies it
    ↓
Module B depends on it
    ↓
Module C changes it again
```

Preferred:

```text
Explicit Input
     ↓
Function / Service
     ↓
Explicit Output
```

State should be owned by the component that actually needs it.

---

# 12.22 RC-021 — Dependency Injection Refactoring

Category:

```text
Architecture / Testing
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Where appropriate, dependencies should be injected rather than instantiated deep inside business logic.

Instead of:

```text
Service
  ↓
new ExternalClient()
```

prefer:

```text
Service
  ↑
Injected Client
```

This improves:

```text
Testability
Replaceability
Configuration
Separation of Concerns
```

Dependency injection should only be used where it genuinely improves design.

---

# 12.23 RC-022 — Interface Segregation Refactoring

Category:

```text
Architecture
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Large interfaces should be reviewed for unrelated responsibilities.

Instead of:

```text
LargeInterface
 ├── Method A
 ├── Method B
 ├── Method C
 ├── Method D
 └── Method E
```

the project may benefit from smaller interfaces:

```text
Interface A
Interface B
Interface C
```

Only when the responsibilities are genuinely distinct.

---

# 12.24 RC-023 — Dead Code Refactoring

Category:

```text
Code Quality
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Unused code should be identified and removed after confirming that it is genuinely unreachable or obsolete.

Potential candidates:

```text
Unused Functions
Unused Classes
Unused Imports
Unused Variables
Obsolete Modules
Old Compatibility Code
Commented-Out Code
```

Dead code should not remain simply because it might be useful someday.

Version control already preserves historical implementations.

---

# 12.25 RC-024 — Commented-Out Code Refactoring

Category:

```text
Maintainability
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Large blocks of commented-out implementation should generally be removed after verification.

Instead of:

```text
# old implementation
# ...
# ...
```

use Git history to preserve the previous implementation.

Comments should explain:

```text
Why
```

rather than merely restating:

```text
What
```

---

# 12.26 RC-025 — Dead Configuration Refactoring

Category:

```text
Configuration
```

Priority:

```text
P2
```

Status:

```text
Candidate
```

Unused configuration options should be identified and removed.

Configuration should remain synchronized with actual application behavior.

The target relationship is:

```text
Configuration
       ↕
Application
```

rather than:

```text
Configuration
       ↓
Unknown / Obsolete Settings
```

---

# 12.27 RC-026 — Compatibility Layer Refactoring

Category:

```text
Migration
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Legacy compatibility code should be isolated where possible.

Instead of allowing legacy assumptions throughout the application:

```text
Legacy Logic
 ↓
Every Module
```

prefer:

```text
Legacy Logic
 ↓
Compatibility Layer
 ↓
Modern Application
```

This is particularly important during the migration of AIPM from an older project structure.

---

# 12.28 RC-027 — Legacy API Refactoring

Category:

```text
Migration / Architecture
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Old APIs should be identified and either:

```text
Removed
Replaced
Wrapped
Deprecated
```

depending on their current usage.

A legacy API should not remain simply because removing it feels inconvenient.

Its actual consumers must first be identified.

---

# 12.29 RC-028 — Refactoring Around Test Boundaries

Category:

```text
Testing / Architecture
```

Priority:

```text
P1
```

Status:

```text
Required
```

Refactoring should improve test boundaries.

A component should ideally be testable without requiring the entire system.

Preferred:

```text
Component
   ↓
Focused Test
```

rather than:

```text
One Small Function
   ↓
Entire Application
   ↓
Huge Test Setup
```

This is one of the strongest indicators that an architectural refactor is successful.

---

# 12.30 RC-029 — Refactoring Around Single Responsibility

Category:

```text
Architecture
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

Components should have coherent responsibilities.

A component responsible for:

```text
Authentication
File Management
Model Loading
Business Rules
Reporting
Logging
```

should be reviewed carefully.

The goal is not necessarily one class per method.

The goal is:

```text
One Component
      ↓
One Coherent Reason to Change
```

---

# 12.31 RC-030 — Refactoring Around Separation of Concerns

Category:

```text
Architecture
```

Priority:

```text
P1
```

Status:

```text
Candidate
```

The following concerns should be separated wherever practical:

```text
Input
Validation
Business Logic
Persistence
External Services
Model Processing
Logging
Error Handling
Output
```

This makes changes localized.

For example:

```text
Change Output Format
        ↓
Should Not Require
        ↓
Changing Core Business Logic
```

---

# 12.32 Refactoring Priority Matrix

| ID     | Refactoring Candidate             | Priority | Risk   |
| ------ | --------------------------------- | -------- | ------ |
| RC-001 | Project Structure                 | P1       | High   |
| RC-002 | Large Modules                     | P1       | High   |
| RC-003 | God Functions                     | P1       | Medium |
| RC-004 | Duplicate Logic                   | P1       | Medium |
| RC-005 | Conditional Complexity            | P2       | Medium |
| RC-006 | Error Handling                    | P1       | High   |
| RC-007 | Input Validation                  | P1       | Medium |
| RC-008 | Configuration                     | P1       | Medium |
| RC-009 | File I/O                          | P1       | High   |
| RC-010 | External Service Coupling         | P1       | High   |
| RC-011 | Data Transformation               | P2       | Medium |
| RC-012 | Naming                            | P2       | Low    |
| RC-013 | Magic Values                      | P2       | Low    |
| RC-014 | Logging                           | P1       | Medium |
| RC-015 | CLI / Interface                   | P1       | Medium |
| RC-016 | API Boundaries                    | P1       | High   |
| RC-017 | Model / Business Logic Separation | P1       | High   |
| RC-018 | Resource Management               | P1       | High   |
| RC-019 | Temporary Files                   | P1       | Medium |
| RC-020 | Global State                      | P1       | High   |
| RC-021 | Dependency Injection              | P2       | Medium |
| RC-022 | Interface Segregation             | P2       | Medium |
| RC-023 | Dead Code                         | P1       | Low    |
| RC-024 | Commented-Out Code                | P2       | Low    |
| RC-025 | Dead Configuration                | P2       | Low    |
| RC-026 | Compatibility Layer               | P1       | High   |
| RC-027 | Legacy API                        | P1       | High   |
| RC-028 | Test Boundaries                   | P1       | High   |
| RC-029 | Single Responsibility             | P1       | Medium |
| RC-030 | Separation of Concerns            | P1       | High   |

---

# 12.33 Recommended Refactoring Order

The refactoring work should not be performed randomly.

The recommended order is:

```text
1. Establish Tests
        ↓
2. Identify High-Risk Legacy Components
        ↓
3. Separate Configuration
        ↓
4. Standardize Error Handling
        ↓
5. Separate I/O from Business Logic
        ↓
6. Separate Model Processing
        ↓
7. Reduce Global State
        ↓
8. Remove Dead Code
        ↓
9. Reduce Duplication
        ↓
10. Refactor Large Functions / Modules
        ↓
11. Establish Stable Interfaces
        ↓
12. Introduce Dependency Injection Where Needed
        ↓
13. Improve CLI / API Boundaries
        ↓
14. Final Structural Cleanup
```

This order minimizes the risk of performing large refactors without sufficient validation.

---

# 12.34 Refactoring Rules for AIPM

The following rules should be applied to future refactoring commits:

```text
Rule 1:
One logical refactoring per commit where practical.

Rule 2:
Do not mix unrelated feature development with structural refactoring.

Rule 3:
Tests must remain green after each major refactor.

Rule 4:
Do not introduce abstractions without a concrete need.

Rule 5:
Do not preserve dead code merely for historical reasons.

Rule 6:
Do not optimize code without evidence of a performance problem.

Rule 7:
Do not change public behavior during a pure refactoring.

Rule 8:
Document intentional architectural decisions.

Rule 9:
Prefer simple code over clever code.

Rule 10:
Every refactor should reduce future maintenance cost.
```

---

# 12.35 Refactoring Definition of Done

A refactoring task can be marked complete when:

```text
Problem Identified
      ↓
Scope Defined
      ↓
Tests Added / Verified
      ↓
Refactoring Performed
      ↓
Behavior Preserved
      ↓
Tests Pass
      ↓
Static Checks Pass
      ↓
Documentation Updated Where Necessary
      ↓
Code Review Completed
```

---

# 12.36 Refactoring Anti-Patterns

AIPM should explicitly avoid:

```text
Big-Bang Rewrite
Premature Abstraction
Pattern Overuse
Unnecessary Frameworks
Massive Unreviewable Commits
Refactoring Without Tests
Refactoring Everything at Once
Optimization Without Measurement
Changing Behavior During Refactoring
```

The biggest danger is turning technical-debt reduction into another source of technical debt.

---

# 12.37 Refactoring Success Criteria

Refactoring should produce measurable improvements.

The following indicators should improve over time:

```text
Reduced Code Duplication
Reduced Function Complexity
Reduced Module Complexity
Improved Test Coverage
Improved Test Isolation
Reduced Global State
Reduced Dependency Coupling
Improved Error Handling
Improved Documentation
Improved Maintainability
```

The final objective is:

```text
Legacy / Difficult-to-Maintain Code
              ↓
Controlled Refactoring
              ↓
Clean Internal Boundaries
              ↓
Testable Components
              ↓
Stable Architecture
              ↓
Commercial-Ready Codebase
```

---

# 12.38 Important Constraint

Refactoring is not equivalent to rewriting.

For AIPM, the preferred strategy is:

```text
Audit
  ↓
Protect Existing Behavior
  ↓
Refactor Incrementally
  ↓
Test
  ↓
Measure
  ↓
Continue
```

not:

```text
Delete Everything
      ↓
Rewrite Everything
      ↓
Hope It Works
```

The existing project contains useful working behavior and domain knowledge. The refactoring process must preserve that value while removing structural weaknesses.

---

# 12.39 Section 12 Conclusion

AIPM has a number of potential refactoring areas that should be handled systematically rather than simultaneously.

The highest-value refactoring targets are expected to be:

```text
Project Structure
Large Modules
Large Functions
Duplicated Logic
Error Handling
Configuration
File / External I/O
Model Processing Separation
Global State
Legacy Compatibility
Testing Boundaries
API / Service Boundaries
```

These areas should be addressed only after the project audit identifies the exact files and components involved.

The principle for this project is:

> Refactor only where the architectural or maintenance benefit is greater than the risk and cost of the change.

This keeps technical-debt reduction controlled and prevents the modernization process itself from becoming technical debt.

# 13. Priority Matrix

The purpose of this section is to convert the technical-debt findings documented in the previous sections into a practical prioritization model.

AIPM contains different types of technical debt:

```text
Architecture Debt
Code Debt
Testing Debt
Security Debt
Documentation Debt
Performance Debt
Dependency Debt
Refactoring Candidates
```

These items do not have equal risk or equal urgency.

A security vulnerability affecting downloaded files, for example, must be addressed before a minor naming inconsistency in source code.

Therefore, AIPM requires a unified priority framework.

---

## 13.1 Priority Levels

Technical debt will be classified into four priority levels:

```text
P0 — Critical / Release Blocking
P1 — High / Immediate Engineering Priority
P2 — Medium / Planned Improvement
P3 — Low / Opportunistic Cleanup
```

The priority represents the recommended order of remediation, not merely the technical severity of the problem.

---

## 13.2 P0 — Critical / Release Blocking

P0 items are issues that can create unacceptable security, data-integrity, reliability, or operational risk.

A P0 issue should normally block a production or commercial release.

Typical examples include:

```text
Critical Security Vulnerability
Unsafe Remote File Handling
Missing Mandatory Integrity Verification
Arbitrary Command Execution Risk
Path Traversal Vulnerability
Critical Dependency Vulnerability
Data Corruption Risk
Destructive Operation Without Protection
Authentication / Authorization Bypass
Critical Release Failure
```

P0 remediation principle:

```text
Identify
   ↓
Contain
   ↓
Fix
   ↓
Test
   ↓
Verify
   ↓
Release
```

A P0 item should not be deferred simply because it is inconvenient to fix.

---

## 13.3 P1 — High / Immediate Engineering Priority

P1 items are significant technical problems that can materially affect:

```text
Security
Reliability
Maintainability
Scalability
Testability
Commercial Readiness
```

Examples include:

```text
Major Architecture Problems
Insufficient Test Coverage
Important Dependency Risks
Poor Error Handling
High-Coupling Components
Major Performance Bottlenecks
Unstable APIs
Missing Important Documentation
Legacy Compatibility Problems
```

P1 items should normally be addressed before major feature expansion.

---

## 13.4 P2 — Medium / Planned Improvement

P2 items represent meaningful technical improvements that should be addressed as part of planned engineering work.

Examples:

```text
Code Duplication
Moderate Complexity
Non-critical Documentation Gaps
Minor Dependency Cleanup
Refactoring Opportunities
Moderate Performance Improvements
Improved Developer Experience
```

P2 issues should not normally block a release unless they become associated with a higher-risk issue.

---

## 13.5 P3 — Low / Opportunistic Cleanup

P3 items have limited immediate impact.

Examples:

```text
Minor Naming Improvements
Cosmetic Code Cleanup
Small Documentation Enhancements
Non-critical Formatting Issues
Low-impact Refactoring
```

These may be addressed when the affected area is already being modified.

P3 items should not consume engineering capacity ahead of P0 or P1 problems.

---

# 13.6 Severity Classification

Priority and severity are related but not identical.

Severity describes the potential consequence of the problem.

Priority describes how soon the team should address it.

The severity model is:

```text
Critical
High
Medium
Low
```

A useful relationship is:

```text
Severity
   +
Impact
   +
Likelihood
   +
Exploitability
   +
Remediation Cost
   =
Priority
```

---

# 13.7 Impact Classification

Technical debt impact should be evaluated across five dimensions:

```text
Security
Reliability
Maintainability
Performance
Business / Commercial
```

Each dimension can be rated:

```text
0 = None
1 = Low
2 = Moderate
3 = High
4 = Critical
```

For example:

```text
Security Impact       = 4
Reliability Impact    = 3
Maintainability      = 2
Performance Impact   = 1
Business Impact      = 4
```

This indicates that the issue deserves significant attention even if it is not primarily a performance problem.

---

# 13.8 Risk Score

AIPM can use a simplified risk score:

```text
Risk Score =
Impact × Likelihood
```

where both values range from 1 to 5.

Therefore:

```text
Minimum Risk Score = 1
Maximum Risk Score = 25
```

Suggested interpretation:

```text
1–4     → Low
5–9     → Moderate
10–15   → High
16–25   → Critical
```

This score should support engineering judgment rather than replace it.

A known exploitable security vulnerability may require P0 treatment even if its calculated score is imperfect.

---

# 13.9 Likelihood Classification

Likelihood should be evaluated as:

```text
1 = Rare
2 = Unlikely
3 = Possible
4 = Likely
5 = Almost Certain
```

Factors include:

```text
Frequency of Execution
Ease of Triggering
External Exposure
User Interaction Required
Existing Mitigation
Historical Failure Rate
Dependency Behavior
```

---

# 13.10 Technical Debt Priority Formula

A practical prioritization model for AIPM is:

```text
Priority Score =
Business Impact
+
Security Impact
+
Reliability Impact
+
Maintainability Impact
+
Performance Impact
+
Likelihood
```

However, numerical scoring should not override explicit release-blocking rules.

The following always take precedence:

```text
Critical Security Issue
Critical Data Integrity Issue
Critical Remote Code Execution Risk
Critical Destructive Operation Risk
Critical Release Integrity Issue
```

These should be treated as P0 regardless of numerical score.

---

# 13.11 Priority Matrix

The basic risk matrix is:

| Impact \ Likelihood |   1 Rare | 2 Unlikely | 3 Possible | 4 Likely | 5 Almost Certain |
| ------------------- | -------: | ---------: | ---------: | -------: | ---------------: |
| 5 Critical          |     High |       High |   Critical | Critical |         Critical |
| 4 High              | Moderate |       High |       High | Critical |         Critical |
| 3 Medium            | Moderate |   Moderate |       High |     High |         Critical |
| 2 Low               |      Low |   Moderate |   Moderate |     High |             High |
| 1 Minimal           |      Low |        Low |   Moderate | Moderate |             High |

This matrix should be combined with engineering judgment.

---

# 13.12 Master Technical Debt Priority Groups

The AIPM technical-debt backlog should be grouped into:

```text
P0
↓
Release Blocking

P1
↓
Immediate Engineering Work

P2
↓
Planned Engineering Work

P3
↓
Opportunistic Cleanup
```

The resulting workflow is:

```text
P0
 ↓
P1
 ↓
P2
 ↓
P3
```

---

# 13.13 P0 Master Backlog

The following classes of issues should be considered P0 candidates.

| Area        | Typical Issue                            | Reason                              |
| ----------- | ---------------------------------------- | ----------------------------------- |
| Security    | Arbitrary command execution              | Critical security risk              |
| Security    | Path traversal                           | Unauthorized filesystem access      |
| Security    | Unsafe remote content                    | Supply-chain / malware risk         |
| Integrity   | Missing mandatory SHA256 verification    | Cannot establish artifact integrity |
| Security    | Critical dependency vulnerability        | Potential compromise                |
| Data        | Destructive operation without safeguards | Data loss                           |
| Release     | Critical installation failure            | Product unusable                    |
| Reliability | Unrecoverable core workflow failure      | Core functionality blocked          |

P0 items require explicit verification before release.

---

# 13.14 P1 Master Backlog

P1 represents the largest immediate engineering category.

Typical areas include:

```text
Architecture
Testing
Security Hardening
Dependency Management
Error Handling
Resource Management
Performance Bottlenecks
Legacy Migration
Documentation of Critical Workflows
API Boundaries
```

The expected approach is:

```text
Current Phase
     ↓
Resolve P0
     ↓
Resolve High-Risk P1
     ↓
Continue Feature Development
```

---

# 13.15 P2 Master Backlog

P2 work should be incorporated into planned development cycles.

Typical items:

```text
Code Duplication
Moderate Refactoring
Non-critical Documentation
Developer Experience
Dependency Cleanup
Minor Performance Improvements
Code Organization
Naming Improvements
```

P2 work should be scheduled rather than handled randomly.

---

# 13.16 P3 Master Backlog

P3 items should generally be handled opportunistically.

Examples:

```text
Minor Naming
Small Formatting Improvements
Minor Comment Cleanup
Non-critical Refactoring
Cosmetic Documentation Improvements
```

P3 work should not delay:

```text
Security
Reliability
Testing
Core Architecture
Release Stability
```

---

# 13.17 Category-Based Priority Matrix

| Category      | P0                                       | P1                               | P2                       | P3                    |
| ------------- | ---------------------------------------- | -------------------------------- | ------------------------ | --------------------- |
| Architecture  | Critical failures                        | Major structural problems        | Moderate coupling        | Cosmetic cleanup      |
| Code          | Critical correctness issue               | High complexity / duplication    | Moderate cleanup         | Minor cleanup         |
| Testing       | Missing critical validation              | Major coverage gaps              | Additional tests         | Minor test cleanup    |
| Security      | Exploitable vulnerability                | Major hardening gap              | Security improvement     | Documentation         |
| Documentation | Missing critical operational information | Major workflow gaps              | Moderate gaps            | Cosmetic updates      |
| Performance   | System unusable                          | Major bottleneck                 | Optimization opportunity | Minor optimization    |
| Dependency    | Critical vulnerability                   | Compatibility / maintenance risk | Cleanup                  | Minor update          |
| Refactoring   | Dangerous legacy structure               | High-value refactor              | Planned cleanup          | Opportunistic cleanup |

---

# 13.18 Security Priority Override

Security issues receive special treatment.

The normal priority calculation can be overridden when a security issue has:

```text
Remote Exploitability
Privilege Escalation
Arbitrary Code Execution
Unauthorized File Access
Sensitive Data Exposure
Supply-Chain Risk
Integrity Bypass
```

In such cases:

```text
Security Risk
     ↓
Immediate Assessment
     ↓
Potential P0
```

This prevents security issues from being incorrectly classified as ordinary technical cleanup.

---

# 13.19 Release Gate Priority

Before an AIPM production or commercial release, the following must be satisfied:

```text
P0 = 0 unresolved
```

In addition:

```text
Critical P1 = 0 unresolved
```

unless there is an explicit documented risk acceptance.

The release gate should therefore be:

```text
P0 Critical Debt
       ↓
Must Resolve

Critical P1
       ↓
Must Resolve

Non-critical P1
       ↓
Review

P2
       ↓
Schedule

P3
       ↓
Optional
```

---

# 13.20 Technical Debt Ownership

Every P0 and P1 item should have an owner.

Required information:

```text
Debt ID
Category
Description
Severity
Priority
Owner
Created Date
Target Resolution
Status
Verification Method
```

Example:

```text
ID:
SD-001

Category:
Security

Severity:
Critical

Priority:
P0

Owner:
Security / Core Engineering

Status:
Open

Verification:
Security Regression Test
```

An unassigned high-priority technical-debt item should be considered a process gap.

---

# 13.21 Technical Debt Status

Each debt item should have one of the following statuses:

```text
Identified
Triaged
Planned
In Progress
Blocked
Resolved
Verified
Accepted Risk
Won't Fix
```

The preferred lifecycle is:

```text
Identified
    ↓
Triaged
    ↓
Planned
    ↓
In Progress
    ↓
Resolved
    ↓
Verified
```

---

# 13.22 Risk Acceptance

Not every technical-debt item must necessarily be eliminated.

A risk may be accepted when:

```text
Remediation Cost Is Very High
        +
Risk Is Well Understood
        +
Impact Is Acceptable
        +
Mitigation Exists
        +
Decision Is Documented
```

Risk acceptance must never be used casually for:

```text
Critical Security Vulnerabilities
Known Data Corruption
Known Arbitrary Code Execution
Critical Integrity Failures
```

An accepted risk must contain:

```text
Reason
Impact
Mitigation
Owner
Review Date
Expiration / Reassessment Condition
```

---

# 13.23 Recommended Resolution Order

The overall technical-debt resolution sequence for AIPM should be:

```text
Phase 1
P0 Security / Integrity / Release Blockers
        ↓
Phase 2
Critical P1 Architecture and Testing
        ↓
Phase 3
Critical P1 Dependency and Reliability Issues
        ↓
Phase 4
P1 Maintainability / Refactoring
        ↓
Phase 5
P2 Planned Improvements
        ↓
Phase 6
P3 Opportunistic Cleanup
```

This prevents the project from spending significant time on low-value cleanup while critical risks remain unresolved.

---

# 13.24 Master Priority Summary

| Priority | Meaning  | Release Impact                  | Recommended Action         |
| -------- | -------- | ------------------------------- | -------------------------- |
| P0       | Critical | Blocks release                  | Fix immediately            |
| P1       | High     | Usually blocks major release    | Fix before major expansion |
| P2       | Medium   | Normally does not block release | Schedule                   |
| P3       | Low      | Does not block release          | Opportunistic              |

---

# 13.25 Priority Decision Tree

When a new technical-debt item is discovered, use:

```text
Is there a critical security or integrity risk?
          │
       Yes ─────→ P0
          │
         No
          ↓
Does it significantly affect reliability,
architecture, testing, or commercial readiness?
          │
       Yes ─────→ P1
          │
         No
          ↓
Does it create meaningful maintenance,
performance, or development cost?
          │
       Yes ─────→ P2
          │
         No
          ↓
P3
```

This decision tree should be used consistently across the project.

---

# 13.26 Priority Review Cadence

Priority should not remain permanently fixed.

A technical-debt item should be reassessed when:

```text
Architecture Changes
New Security Information Appears
Dependency Changes
Usage Increases
Production Incident Occurs
New Feature Depends On It
Commercial Distribution Begins
Risk Exposure Changes
```

A P2 item can become P1.

A P1 item can become P0.

A resolved item can be reopened if the underlying problem returns.

---

# 13.27 Technical Debt Dashboard Requirements

A future project dashboard should expose at minimum:

```text
Total Debt Items
P0 Count
P1 Count
P2 Count
P3 Count
Open Items
In Progress
Blocked
Resolved
Verified
Accepted Risk
Debt by Category
Debt by Severity
Debt by Priority
Oldest Open Debt
Critical Security Debt
Release Blocking Debt
```

Example:

```text
Technical Debt
────────────────────────
P0   0
P1   12
P2   24
P3   17
────────────────────────
Total 53
```

The exact values must come from the authoritative debt register rather than being manually maintained in multiple places.

---

# 13.28 Priority Matrix Governance

The priority matrix should be treated as a living project-management artifact.

Whenever a technical-debt item is:

```text
Created
Updated
Reclassified
Resolved
Verified
Accepted
Reopened
```

the master debt register should be updated.

This prevents the documentation from becoming disconnected from the actual project state.

---

# 13.29 Priority Matrix Rules

AIPM should follow these rules:

```text
Rule 1:
P0 issues block release.

Rule 2:
Critical security issues override ordinary priority scoring.

Rule 3:
Every P0/P1 item requires an owner.

Rule 4:
Every resolved item requires verification.

Rule 5:
Risk acceptance must be documented.

Rule 6:
P3 work must not displace P0/P1 work.

Rule 7:
Priority must be reviewed when risk changes.

Rule 8:
Technical debt should be tracked in one authoritative register.

Rule 9:
Priority must be based on impact and likelihood, not developer preference.

Rule 10:
Debt reduction should be measurable over time.
```

---

# 13.30 Section 13 Conclusion

The purpose of the priority matrix is not merely to label technical debt.

Its purpose is to answer the critical engineering question:

> What should be fixed first?

For AIPM, the answer should always begin with:

```text
Security
   ↓
Integrity
   ↓
Reliability
   ↓
Testing
   ↓
Architecture
   ↓
Maintainability
   ↓
Performance
   ↓
Documentation
   ↓
Cosmetic Cleanup
```

The project should therefore avoid a common modernization failure:

```text
Old Project
    ↓
Start Cleaning Everything
    ↓
Many Refactors
    ↓
No Clear Priority
    ↓
No Release
```

Instead:

```text
Audit
 ↓
Classify
 ↓
Prioritize
 ↓
Assign
 ↓
Resolve
 ↓
Verify
 ↓
Release
```

The final target is to reach a state where:

```text
P0 = 0
Critical P1 = 0
Known Security Blockers = 0
Release Blocking Debt = 0
```

before declaring AIPM ready for its next major production or commercial milestone.

# 14. Resolution Plan

The purpose of this section is to define how AIPM's identified technical debt will be systematically resolved.

The resolution plan converts the technical-debt inventory and priority matrix into an actionable engineering process.

The objective is not to eliminate every technical-debt item immediately.

The objective is to:

```text
Identify
   ↓
Prioritize
   ↓
Plan
   ↓
Implement
   ↓
Test
   ↓
Verify
   ↓
Document
   ↓
Close
```

Technical-debt remediation must therefore be treated as an engineering activity with defined scope, ownership, validation, and completion criteria.

---

## 14.1 Resolution Strategy

AIPM technical debt should be resolved using a risk-first approach.

The general order is:

```text
P0 — Critical / Release Blocking
        ↓
P1 — High / Immediate Engineering Priority
        ↓
P2 — Medium / Planned Improvement
        ↓
P3 — Low / Opportunistic Cleanup
```

The project should not spend substantial engineering time on P3 cleanup while unresolved P0 or critical P1 issues remain.

---

## 14.2 Resolution Principles

The following principles govern technical-debt remediation:

```text
1. Fix risk before cosmetics.
2. Prefer incremental remediation over large rewrites.
3. Preserve working behavior during refactoring.
4. Test before and after high-risk changes.
5. Resolve root causes rather than symptoms.
6. Avoid introducing new dependencies unnecessarily.
7. Document architectural decisions.
8. Verify every claimed resolution.
9. Keep remediation commits focused.
10. Update the technical-debt register after every meaningful change.
```

The goal is not merely to reduce the number of debt entries.

The goal is to reduce actual engineering risk.

---

# 14.3 Phase 1 — Stabilization

The first resolution phase focuses on making the existing system safe enough for continued modernization.

Primary objectives:

```text
Application Stability
Security Baseline
Dependency Visibility
Basic Testing
Critical Error Handling
Environment Reproducibility
```

The workflow is:

```text
Existing Project
      ↓
Stability Audit
      ↓
Critical Failure Identification
      ↓
P0 Remediation
      ↓
Basic Regression Tests
      ↓
Stable Baseline
```

No major architectural refactoring should begin before the project has a sufficiently reliable baseline.

---

# 14.4 Phase 2 — Security Resolution

Security debt receives the highest engineering priority after immediate stabilization.

The security-resolution workflow is:

```text
Security Audit
      ↓
Threat Identification
      ↓
Risk Classification
      ↓
P0 / P1 Prioritization
      ↓
Remediation
      ↓
Security Regression Testing
      ↓
Verification
```

Important security areas include:

```text
Input Validation
Path Handling
File Operations
Command Execution
Remote Resources
Authentication
Authorization
Secrets
Dependencies
Integrity Verification
Logging
Error Disclosure
```

Any critical vulnerability discovered during implementation should immediately return to the P0 triage process.

---

# 14.5 Phase 3 — Testing Foundation

Technical debt cannot be safely resolved at scale without reliable tests.

The project should therefore establish a minimum testing foundation before performing high-risk refactoring.

The preferred sequence is:

```text
Existing Behavior
      ↓
Characterization Tests
      ↓
Unit Tests
      ↓
Integration Tests
      ↓
Regression Tests
```

Characterization tests are particularly important for legacy code because they document what the existing implementation actually does before structural changes are introduced.

---

# 14.6 Phase 4 — Architecture Resolution

After stabilization and security hardening, architectural debt should be addressed.

The architecture-resolution process should focus on:

```text
Separation of Concerns
Module Boundaries
Dependency Direction
Service Boundaries
I/O Isolation
Model Processing Separation
Configuration Management
Global State Reduction
Interface Stability
```

The target structure is:

```text
Interface
    ↓
Application Layer
    ↓
Domain / Core Logic
    ↓
Infrastructure
    ↓
External Dependencies
```

The exact implementation should follow the actual project structure discovered during the audit rather than imposing unnecessary abstractions.

---

# 14.7 Phase 5 — Code Debt Resolution

Code debt should be addressed after the major architectural boundaries become clear.

The primary targets are:

```text
Large Functions
Large Modules
Duplicated Logic
Dead Code
Complex Conditionals
Poor Naming
Magic Values
Inconsistent Error Handling
Global State
Tight Coupling
```

The recommended order is:

```text
High-Risk Code
      ↓
High-Complexity Code
      ↓
Duplicated Logic
      ↓
Dead Code
      ↓
Minor Maintainability Issues
```

This prevents cosmetic cleanup from distracting from structurally important problems.

---

# 14.8 Phase 6 — Dependency Resolution

Dependency debt should be resolved through a controlled lifecycle.

```text
Inventory
   ↓
Classify
   ↓
Security Audit
   ↓
License Audit
   ↓
Compatibility Review
   ↓
Remove Unnecessary Dependencies
   ↓
Pin / Resolve Versions
   ↓
Test
   ↓
Document
```

The project should distinguish:

```text
Runtime Dependencies
Development Dependencies
Testing Dependencies
Optional Dependencies
System Dependencies
External Tools
```

This classification becomes especially important before commercial distribution.

---

# 14.9 Phase 7 — Performance Resolution

Performance work should be evidence-driven.

The project should not optimize code merely because it appears inefficient.

The preferred process is:

```text
Measure
   ↓
Identify Bottleneck
   ↓
Determine Root Cause
   ↓
Optimize
   ↓
Benchmark
   ↓
Regression Test
```

Potential targets include:

```text
Startup Time
Memory Usage
CPU Usage
I/O
Network Operations
Model Loading
Repeated Computation
Large Data Processing
```

Performance optimization should never compromise security or correctness without an explicit engineering decision.

---

# 14.10 Phase 8 — Documentation Resolution

Documentation debt should be resolved alongside the corresponding technical work.

For example:

```text
Architecture Change
      ↓
Architecture Documentation Update
```

and:

```text
Dependency Change
      ↓
Dependency Documentation Update
```

The documentation should cover at least:

```text
Installation
Configuration
Architecture
Usage
CLI / API
Testing
Security
Dependencies
Troubleshooting
Deployment
Release Process
```

Documentation should describe the actual system rather than an intended future system.

---

# 14.11 Phase 9 — Refactoring

Refactoring should begin only after sufficient tests and architectural boundaries exist.

The preferred sequence is:

```text
Characterize Existing Behavior
      ↓
Add / Improve Tests
      ↓
Refactor One Component
      ↓
Run Tests
      ↓
Review
      ↓
Commit
```

Large-scale "rewrite everything" approaches should be avoided.

The modernization strategy is:

```text
Legacy Code
    ↓
Controlled Refactoring
    ↓
Verified Improvement
    ↓
Next Component
```

---

# 14.12 Phase 10 — Commercial Readiness

Once the major P0/P1 technical debt has been addressed, the project can move toward commercial-readiness validation.

Commercial-readiness review should include:

```text
Security
Reliability
Installation
Dependency Licensing
Documentation
Configuration
Error Handling
Testing
Upgrade Process
Versioning
Packaging
Deployment
Supportability
```

The goal is to ensure that the project can be distributed and maintained by people other than its original developer.

---

# 14.13 P0 Resolution Workflow

P0 issues require an accelerated workflow:

```text
P0 Detected
    ↓
Immediately Triage
    ↓
Assign Owner
    ↓
Contain Risk
    ↓
Implement Fix
    ↓
Add Regression Test
    ↓
Security / Integrity Verification
    ↓
Code Review
    ↓
Resolve
    ↓
Verify
```

A P0 issue should not simply be marked resolved after a source-code change.

The fix must be validated.

---

# 14.14 P1 Resolution Workflow

P1 remediation should follow:

```text
P1 Identified
    ↓
Scope
    ↓
Assign
    ↓
Create Implementation Plan
    ↓
Add / Verify Tests
    ↓
Implement
    ↓
Run Regression Suite
    ↓
Review
    ↓
Resolve
    ↓
Verify
```

P1 work should normally be incorporated into the active engineering roadmap.

---

# 14.15 P2 Resolution Workflow

P2 issues should be handled through planned development work:

```text
P2 Identified
    ↓
Estimate
    ↓
Group With Related Work
    ↓
Schedule
    ↓
Implement
    ↓
Test
    ↓
Verify
```

Related P2 items may be grouped into a single engineering task when doing so reduces repeated work.

---

# 14.16 P3 Resolution Workflow

P3 issues should normally be resolved opportunistically.

For example:

```text
Developer Modifies Module
        ↓
Nearby P3 Issue Found
        ↓
Small Safe Cleanup
        ↓
Tests
        ↓
Commit
```

P3 issues should not trigger large refactoring projects.

---

# 14.17 Root-Cause Resolution

AIPM should avoid fixing symptoms repeatedly.

Example:

```text
Repeated Runtime Error
        ↓
Patch Error
        ↓
Same Error Returns
        ↓
Another Patch
```

This creates additional technical debt.

Instead:

```text
Repeated Error
        ↓
Root Cause Analysis
        ↓
Architectural / Code Problem
        ↓
Root Cause Fix
        ↓
Regression Test
```

The objective is to reduce recurrence.

---

# 14.18 Debt Clustering

Related technical-debt items should be grouped where possible.

For example:

```text
Configuration Debt
      +
Global State
      +
Testing Difficulty
      ↓
Configuration Architecture Refactor
```

Similarly:

```text
Dependency Debt
      +
Compatibility Debt
      +
Installation Debt
      ↓
Environment Reproducibility Work
```

This reduces duplicated engineering effort.

---

# 14.19 Resolution Dependencies

Some technical-debt items cannot safely be resolved before others.

The dependency relationship may look like:

```text
Testing Foundation
        ↓
Safe Refactoring
        ↓
Architecture Cleanup
        ↓
Performance Optimization
```

Another example:

```text
Dependency Inventory
        ↓
Security Audit
        ↓
Dependency Upgrade
        ↓
Compatibility Testing
```

Therefore, the backlog should consider technical dependencies between debt items.

---

# 14.20 Resolution Order Matrix

| Resolution Area          | Depends On                | Priority |
| ------------------------ | ------------------------- | -------- |
| Critical Security Fixes  | Immediate audit           | P0       |
| Release Blockers         | Stabilization             | P0       |
| Testing Foundation       | Stable execution baseline | P1       |
| Dependency Inventory     | Environment audit         | P1       |
| Architecture Refactoring | Tests + baseline          | P1       |
| Code Refactoring         | Architecture boundaries   | P1       |
| Performance Optimization | Measurement               | P1/P2    |
| Documentation            | Actual implementation     | P1/P2    |
| Dependency Cleanup       | Dependency inventory      | P1/P2    |
| Commercial Hardening     | P0/P1 resolution          | P1       |

---

# 14.21 Resolution Through Git Commits

Technical-debt remediation should be traceable through version control.

A good remediation commit should have:

```text
Focused Scope
Clear Message
Small Logical Change
Tests
No Unrelated Modifications
```

Examples of appropriate commit intent:

```text
fix: resolve unsafe file path handling
test: add regression coverage for invalid input
refactor: isolate filesystem operations
refactor: separate model loading from application logic
chore: remove unused dependency
docs: update installation requirements
```

The exact commit naming convention should follow the project's Git policy.

---

# 14.22 Resolution Verification

Every resolved debt item requires verification.

Verification may include:

```text
Unit Test
Integration Test
Regression Test
Security Test
Static Analysis
Dependency Scan
Benchmark
Manual Verification
Build Verification
Installation Test
```

The verification method must correspond to the nature of the debt.

For example:

```text
Security Debt
     ↓
Security Regression Test

Performance Debt
     ↓
Benchmark

Documentation Debt
     ↓
Documentation Review

Dependency Debt
     ↓
Clean Installation + Tests
```

---

# 14.23 Resolution Definition of Done

A technical-debt item is not complete when the developer finishes coding.

It is complete when:

```text
Problem Understood
      ↓
Root Cause Identified
      ↓
Fix Implemented
      ↓
Relevant Tests Added / Updated
      ↓
Tests Pass
      ↓
No Regression Detected
      ↓
Documentation Updated
      ↓
Code Reviewed
      ↓
Debt Register Updated
      ↓
Resolution Verified
```

Only then should the status become:

```text
Verified
```

---

# 14.24 Debt Status Transition

The expected state transition is:

```text
Identified
    ↓
Triaged
    ↓
Planned
    ↓
In Progress
    ↓
Resolved
    ↓
Verified
```

Alternative states:

```text
Blocked
Accepted Risk
Won't Fix
```

must include an explanation.

A debt item should not disappear from the register merely because the team decided not to fix it.

---

# 14.25 Accepted Risk Resolution

When a debt item is intentionally retained, the project must record:

```text
Debt ID
Reason for Acceptance
Known Impact
Current Mitigation
Owner
Review Date
Trigger for Reassessment
```

Example:

```text
Status:
Accepted Risk

Reason:
Remediation cost currently exceeds expected benefit.

Mitigation:
Restricted usage and additional validation.

Review:
Before next major commercial release.
```

Acceptance should be reviewed periodically.

---

# 14.26 Resolution Metrics

Technical-debt remediation should be measurable.

Useful metrics include:

```text
P0 Open Count
P1 Open Count
P2 Open Count
P3 Open Count
Total Open Debt
Debt Resolved Per Release
Average Debt Age
Security Debt Count
Critical Dependency Count
Test Coverage
Regression Failure Rate
Architecture Debt Remaining
```

A useful high-level trend is:

```text
Open Debt
   ↓
Should decrease over time
```

while:

```text
Test Coverage
   ↓
Should increase over time
```

and:

```text
Critical Security Issues
   ↓
Should reach zero before release
```

---

# 14.27 Technical Debt Budget

Technical debt remediation should receive explicit engineering capacity.

A project that allocates 100% of its engineering capacity to new features will eventually accumulate additional debt.

A balanced development cycle can conceptually contain:

```text
Feature Development
+
Bug Fixing
+
Technical Debt Reduction
+
Testing
+
Documentation
```

The exact allocation should depend on project phase and risk.

During modernization, technical-debt work may temporarily receive a larger share of engineering capacity.

---

# 14.28 Debt Prevention

Resolution alone is insufficient.

AIPM should prevent newly created debt where possible.

The prevention process is:

```text
New Change
    ↓
Architecture Review
    ↓
Security Review
    ↓
Testing
    ↓
Dependency Review
    ↓
Code Review
    ↓
Merge
```

New technical debt should be documented when it is intentionally introduced.

This creates an important distinction:

```text
Unknown Debt
    ≠
Known / Managed Debt
```

Known debt is significantly easier to manage.

---

# 14.29 New Debt Registration Rule

When a developer knowingly introduces a compromise, the project should create a debt record.

Example:

```text
Temporary Implementation
        ↓
Known Limitation
        ↓
Create TD Record
        ↓
Assign Priority
        ↓
Add Future Resolution
```

This prevents temporary solutions from silently becoming permanent architecture.

---

# 14.30 Resolution Roadmap

The overall AIPM technical-debt resolution roadmap should follow:

```text
Stage 1
Project Stabilization
        ↓
Stage 2
P0 Security / Integrity Fixes
        ↓
Stage 3
Testing Foundation
        ↓
Stage 4
Dependency & Environment Stabilization
        ↓
Stage 5
Architecture Remediation
        ↓
Stage 6
Code Refactoring
        ↓
Stage 7
Performance Optimization
        ↓
Stage 8
Documentation Completion
        ↓
Stage 9
Commercial Hardening
        ↓
Stage 10
Final Technical-Debt Review
```

This sequence should be adjusted if the actual project audit identifies a different dependency order.

---

# 14.31 Final Release Resolution Gate

Before a major release is declared technically ready, the following conditions should be satisfied:

```text
P0 Unresolved
        = 0

Critical P1 Unresolved
        = 0

Critical Security Vulnerabilities
        = 0

Known Critical Dependency Vulnerabilities
        = 0

Required Regression Tests
        = Passing

Critical Installation Path
        = Verified

Critical Documentation
        = Complete
```

Remaining P2/P3 debt may be accepted only when it is understood, documented, and does not compromise release quality.

---

# 14.32 Resolution Plan Summary

The AIPM technical-debt resolution model is:

```text
                    TECHNICAL DEBT
                           │
                           ▼
                      TRIAGE / AUDIT
                           │
                           ▼
                    PRIORITY MATRIX
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
         P0               P1               P2/P3
          │                │                │
          ▼                ▼                ▼
      Immediate        Planned High      Scheduled
       Fixes             Priority         Cleanup
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                         TEST
                           ↓
                       REVIEW
                           ↓
                      VERIFICATION
                           ↓
                     DOCUMENTATION
                           ↓
                      DEBT REGISTER
                           ↓
                         CLOSED
```

The core rule is:

> Technical debt is considered resolved only when the underlying problem has been addressed, the relevant behavior has been verified, and the debt register has been updated.

---

# 14.33 Section 14 Conclusion

AIPM's technical-debt remediation must be controlled, prioritized, and verifiable.

The project should not attempt to solve every historical problem simultaneously.

The preferred modernization strategy is:

```text
Stabilize
   ↓
Secure
   ↓
Test
   ↓
Structure
   ↓
Refactor
   ↓
Optimize
   ↓
Document
   ↓
Harden
   ↓
Verify
   ↓
Release
```

The most important principle is:

> Fix the highest-risk problems first, preserve working behavior through tests, and never mark technical debt as resolved without verification.

This resolution plan provides the bridge between the technical-debt inventory and the actual implementation roadmap. The following section, **Section 15 — Debt Tracking Workflow**, will define how these items are recorded, updated, reviewed, and tracked throughout the project's lifecycle.

# 15. Debt Tracking Workflow

The purpose of this section is to define the operational workflow for identifying, recording, prioritizing, assigning, resolving, verifying, and closing technical-debt items in AIPM.

Technical debt should not exist only as informal knowledge in a developer's mind.

Every meaningful technical-debt item should be:

```text
Identified
    ↓
Recorded
    ↓
Triaged
    ↓
Prioritized
    ↓
Assigned
    ↓
Planned
    ↓
Implemented
    ↓
Tested
    ↓
Verified
    ↓
Closed
```

This workflow converts `TECH_DEBT.md` from a static document into a controlled engineering process.

---

## 15.1 Tracking Objectives

The technical-debt tracking system should answer the following questions at any point in the project:

```text
What technical debt exists?

Where does it exist?

Why does it matter?

What is its severity?

What is its priority?

Who owns it?

What depends on it?

What is the planned resolution?

What is its current status?

Has the fix been tested?

Has the resolution been verified?

What technical debt remains before release?
```

If these questions cannot be answered, technical-debt management is incomplete.

---

# 15.2 Single Source of Truth

AIPM should maintain one authoritative technical-debt register.

The recommended conceptual structure is:

```text
TECH_DEBT.md
     ↓
Technical Debt Register
     ↓
Individual Debt Records
     ↓
Status / Priority / Ownership
```

Other project documents may reference debt IDs, but they should not maintain independent conflicting copies of the same debt information.

For example:

```text
TD-001
TD-002
TD-003
TD-004
```

should remain unique identifiers throughout the project's lifecycle.

---

# 15.3 Debt ID Convention

Every technical-debt item should receive a unique identifier.

Recommended format:

```text
TD-001
TD-002
TD-003
...
```

If the project eventually becomes large enough to require category prefixes, the format may evolve into:

```text
ARCH-001
CODE-001
SEC-001
TEST-001
DEP-001
DOC-001
PERF-001
```

However, a single global ID system is preferable for the initial AIPM modernization phase.

---

# 15.4 Debt Record Structure

Every significant debt item should contain at least:

```text
Debt ID
Title
Category
Description
Location
Root Cause
Impact
Severity
Likelihood
Priority
Owner
Dependencies
Proposed Resolution
Status
Created Date
Target Date
Resolution Date
Verification Method
Verification Result
Related Commit / PR
Notes
```

A conceptual record:

```text
TD-014
────────────────────────────
Title:
Unsafe temporary-file handling

Category:
Security / Infrastructure

Severity:
High

Priority:
P1

Status:
Planned

Owner:
Core Engineering

Location:
File handling subsystem

Root Cause:
Temporary files are not centrally managed.

Impact:
Potential security and cleanup issues.

Resolution:
Centralize temporary-file management.

Verification:
Security regression test +
cleanup test
```

---

# 15.5 Debt Categories

The tracking system should use standardized categories.

Recommended categories:

```text
Architecture
Code
Security
Testing
Dependency
Performance
Documentation
Infrastructure
Reliability
Maintainability
Compatibility
Release
```

A debt item may have more than one impact area, but it should have one primary category for reporting.

---

# 15.6 Debt Discovery Sources

Technical debt can be discovered from several sources.

```text
Source Code Audit
Architecture Review
Security Audit
Dependency Scan
Testing
Bug Reports
Performance Profiling
Production Incidents
Code Review
Developer Observation
User Feedback
Deployment Problems
Documentation Review
```

The source of discovery should be recorded when useful.

Example:

```text
Source:
Security Audit — July 2026
```

This provides historical context for why the issue entered the register.

---

# 15.7 New Debt Identification Workflow

Whenever a significant technical-debt issue is discovered:

```text
Problem Found
     ↓
Confirm It Is Real
     ↓
Determine Scope
     ↓
Create Debt ID
     ↓
Record Evidence
     ↓
Initial Severity
     ↓
Initial Priority
     ↓
Add to Register
```

The item should not immediately be marked P0/P1 without sufficient evidence unless it clearly represents an urgent security or integrity problem.

---

# 15.8 Debt Triage

After registration, the debt item should be triaged.

Triage determines:

```text
Is the issue valid?

What component is affected?

What is the actual impact?

How likely is the problem to occur?

Is it security-sensitive?

Does it block a release?

Does another task depend on it?

What is the estimated remediation effort?
```

The result should be a confirmed:

```text
Severity
Likelihood
Priority
```

---

# 15.9 Debt Priority Assignment

Priority should follow the rules defined in Section 13.

```text
P0
Critical / Release Blocking

P1
High / Immediate Engineering Priority

P2
Medium / Planned Improvement

P3
Low / Opportunistic Cleanup
```

The priority should be based on actual project risk rather than personal preference.

---

# 15.10 Debt Ownership

Every P0 and P1 item must have an owner.

The owner is responsible for:

```text
Understanding the Problem
Coordinating Remediation
Updating Status
Communicating Blockers
Ensuring Tests Exist
Requesting Verification
Closing the Item
```

Ownership does not necessarily mean that the owner personally writes all code.

The owner is accountable for the remediation lifecycle.

---

# 15.11 Debt Status Lifecycle

The standard status lifecycle should be:

```text
Identified
    ↓
Triaged
    ↓
Planned
    ↓
In Progress
    ↓
Resolved
    ↓
Verified
    ↓
Closed
```

Alternative states include:

```text
Blocked
Accepted Risk
Won't Fix
Duplicate
Invalid
```

These states require an explanation.

---

# 15.12 Status Definitions

### Identified

The issue has been discovered but has not yet been fully evaluated.

### Triaged

The issue has been reviewed and its impact and priority have been established.

### Planned

The remediation has been accepted into the engineering backlog.

### In Progress

Implementation work has started.

### Blocked

Work cannot continue because of a dependency, missing information, or external constraint.

### Resolved

The proposed implementation has been completed, but verification may still be pending.

### Verified

Testing and review have confirmed that the original debt has been addressed.

### Closed

The debt record is complete and no further action is currently required.

---

# 15.13 Status Transition Rules

Valid transitions should generally follow:

```text
Identified
   ↓
Triaged
   ↓
Planned
   ↓
In Progress
   ↓
Resolved
   ↓
Verified
   ↓
Closed
```

A blocked task may return to:

```text
Planned
```

after its blocker is removed.

A verified issue may be reopened if the underlying problem returns.

---

# 15.14 Blocked Debt

When a debt item becomes blocked, the record must identify:

```text
Blocker
Reason
Affected Work
Expected Resolution
Owner
Next Review Date
```

Example:

```text
Status:
Blocked

Blocker:
Waiting for dependency compatibility assessment.

Impact:
Architecture refactor cannot safely continue.

Next Action:
Complete dependency compatibility test.

Review:
After dependency audit.
```

A blocked item should never remain indefinitely without review.

---

# 15.15 Debt Resolution Workflow

Once a debt item enters `In Progress`:

```text
Review Existing Behavior
       ↓
Identify Root Cause
       ↓
Define Remediation
       ↓
Implement Change
       ↓
Add / Update Tests
       ↓
Run Regression Tests
       ↓
Review Code
       ↓
Mark Resolved
```

The item then moves to:

```text
Verified
```

only after independent or appropriate validation.

---

# 15.16 Verification Workflow

Verification must answer:

> Did the remediation actually solve the original problem without introducing unacceptable regressions?

Verification may involve:

```text
Unit Tests
Integration Tests
Regression Tests
Security Tests
Static Analysis
Dependency Scanning
Performance Benchmarks
Build Validation
Installation Testing
Manual Review
```

The verification method must match the debt category.

---

# 15.17 Security Debt Verification

Security debt requires stronger verification.

The workflow should be:

```text
Security Debt
     ↓
Fix
     ↓
Regression Test
     ↓
Security Review
     ↓
Verify Exploit Path Is Closed
     ↓
Close
```

For high-risk security findings, the project should retain evidence of the verification.

Examples:

```text
Security Test ID
Scan Result
Code Review
Dependency Scan
Reproduction Test
```

---

# 15.18 Performance Debt Verification

Performance-related debt should be measured before and after remediation.

The workflow is:

```text
Baseline Measurement
       ↓
Optimization
       ↓
New Measurement
       ↓
Compare
       ↓
Regression Check
       ↓
Verify
```

Example metrics:

```text
Execution Time
Memory Consumption
CPU Usage
Startup Time
I/O Time
Throughput
Latency
```

Performance debt should not be marked resolved merely because the code "looks faster."

---

# 15.19 Dependency Debt Verification

Dependency remediation should verify:

```text
Dependency Installation
Version Compatibility
Application Startup
Runtime Behavior
Tests
Build
Packaging
License Requirements
Security Status
```

The preferred workflow is:

```text
Dependency Change
      ↓
Clean Environment
      ↓
Install
      ↓
Build
      ↓
Test
      ↓
Run
      ↓
Verify
```

---

# 15.20 Architecture Debt Verification

Architecture debt is harder to verify than a simple bug fix.

Verification should examine:

```text
Dependency Direction
Module Boundaries
Coupling
Testability
Responsibility Separation
Extension Capability
Regression Behavior
```

Architecture changes should be evaluated against the architecture documented in `ARCHITECTURE.md`.

The documentation and implementation should remain consistent.

---

# 15.21 Refactoring Debt Verification

Refactoring must preserve intended behavior.

The preferred workflow is:

```text
Existing Tests
      ↓
Refactor
      ↓
Same Tests
      ↓
Additional Regression Tests
      ↓
Static Analysis
      ↓
Code Review
```

The key condition is:

```text
Behavior Preserved
+
Structure Improved
```

---

# 15.22 Documentation Debt Verification

Documentation debt is resolved only when the documentation accurately reflects the implementation.

Verification should check:

```text
Installation Steps
Configuration
Commands
File Paths
Architecture
Dependencies
Examples
Screenshots Where Necessary
Troubleshooting
Version Information
```

Documentation should be tested by following the instructions in a clean environment whenever practical.

---

# 15.23 Related Work Tracking

A debt item should link to related engineering work where possible.

Possible references:

```text
Issue
Task
Pull Request
Commit
Test
Security Finding
Architecture Decision
Release
```

Example:

```text
Debt:
TD-017

Related Work:
Issue #42
PR #57
Commit abc1234

Verification:
Test SEC-014
```

This creates traceability from problem to resolution.

---

# 15.24 Debt-to-Code Traceability

High-priority debt should be traceable to the affected project components.

Conceptually:

```text
Debt ID
   ↓
Affected Component
   ↓
Affected File / Module
   ↓
Implementation Change
   ↓
Test
   ↓
Verification
```

This is especially important for P0 and P1 issues.

---

# 15.25 Debt-to-Test Traceability

Where applicable, each important debt item should have a corresponding test.

Example:

```text
TD-021
Unsafe Input Handling
       ↓
SEC-TEST-007
Invalid Input Regression
```

This prevents the same debt from silently returning later.

The relationship is:

```text
Technical Debt
      ↓
Regression Test
      ↓
Future Protection
```

---

# 15.26 Debt Aging

The project should track how long debt remains unresolved.

Useful values:

```text
Created Date
Age in Days
Age in Release Cycles
Age in Milestones
```

Example:

```text
TD-031
Priority: P1
Created: 2026-07-01
Age: 28 days
Status: Planned
```

Old unresolved P1 debt should receive additional review.

---

# 15.27 Debt Aging Thresholds

Suggested review thresholds:

```text
P0:
Immediate

P1:
Review every development cycle

P2:
Review every major milestone

P3:
Review periodically
```

An item should be escalated when its age becomes inconsistent with its risk.

For example:

```text
P1
+
Long Unresolved Duration
+
Increasing Product Exposure
=
Reassessment Required
```

---

# 15.28 Debt Reclassification

Technical-debt priority can change.

Example:

```text
P2
 ↓
New Feature Depends On It
 ↓
Risk Increases
 ↓
P1
```

Or:

```text
P1
 ↓
Mitigation Added
 ↓
Risk Reduced
 ↓
P2
```

Every priority change should have a reason.

---

# 15.29 Debt Escalation

A debt item should be escalated when:

```text
Security Risk Increases
Production Failure Occurs
New Dependency Is Introduced
More Users Become Exposed
Business Impact Increases
Release Depends On It
A Workaround Stops Working
```

Escalation may change:

```text
Priority
Owner
Deadline
Scope
Verification Requirements
```

---

# 15.30 Release-Based Tracking

Technical debt should be reviewed before each significant release.

The release review should identify:

```text
Open P0
Open Critical P1
Open P1
New Security Debt
New Dependency Debt
Regression Risk
Accepted Risks
Release-Specific Debt
```

A release should not be declared ready while an unresolved P0 remains.

---

# 15.31 Release Debt Gate

The release gate should follow:

```text
P0 = 0
```

and:

```text
Critical P1 = 0
```

unless an explicit, documented risk-acceptance decision exists.

Remaining P2/P3 items should be reviewed for:

```text
User Impact
Security Impact
Commercial Impact
Operational Impact
Future Maintenance Cost
```

---

# 15.32 Debt Review Meeting

A formal meeting is not required for every minor item.

However, P0/P1 debt should be reviewed regularly.

The review should cover:

```text
New Debt
Resolved Debt
Blocked Debt
Escalated Debt
Aging Debt
Security Debt
Release Blocking Debt
Upcoming Debt
```

The output should be:

```text
Priority Changes
Owner Changes
Target-Date Changes
Resolution Decisions
Risk Acceptance Decisions
```

---

# 15.33 Technical Debt Review Checklist

Before each major milestone:

```text
[ ] Review all P0 items
[ ] Review all P1 items
[ ] Review aging debt
[ ] Review security findings
[ ] Review dependency findings
[ ] Review blocked items
[ ] Review accepted risks
[ ] Verify completed items
[ ] Update owners
[ ] Update target dates
[ ] Update status
[ ] Update technical-debt register
```

---

# 15.34 Debt Metrics

The project should track the following metrics:

```text
Total Open Debt
P0 Count
P1 Count
P2 Count
P3 Count
Resolved Debt
Verified Debt
Average Debt Age
Oldest P1 Debt
Security Debt
Dependency Debt
Architecture Debt
Testing Debt
Debt Created Per Release
Debt Resolved Per Release
```

A useful trend is:

```text
Resolved Debt
     ↑

Critical Debt
     ↓

Debt Age
     ↓

Regression Coverage
     ↑
```

---

# 15.35 Debt Burn-Down

AIPM can use a technical-debt burn-down view.

Conceptually:

```text
Open Technical Debt
│
│\
│ \
│  \
│   \
│    \
│     \____
│
└──────────────────→ Time
```

The objective is not necessarily to reach zero total technical debt.

The objective is to:

```text
Reduce Critical Debt
Reduce High-Priority Debt
Prevent Debt Growth
Reduce Average Debt Age
```

---

# 15.36 Debt Inflow vs Outflow

A healthy modernization process should monitor:

```text
Debt Created
vs
Debt Resolved
```

If:

```text
Debt Created > Debt Resolved
```

for sustained periods, technical debt is growing.

If:

```text
Debt Resolved > Debt Created
```

the technical-debt backlog is shrinking.

However, raw counts should not be the only measure because one critical security issue may be more important than ten minor cleanup items.

---

# 15.37 Technical Debt Dashboard

A future AIPM engineering dashboard should display:

```text
TECHNICAL DEBT
────────────────────────────
P0          0
P1          X
P2          X
P3          X

Open        X
Resolved    X
Verified    X
Blocked     X

Security    X
Architecture X
Code        X
Testing     X
Dependency  X
Performance X

Oldest P1   X days
```

The dashboard should derive these values from the authoritative debt register.

---

# 15.38 Debt Register Example

A simple register may look like:

| ID     | Category      | Priority | Status      | Owner            | Target        |
| ------ | ------------- | -------- | ----------- | ---------------- | ------------- |
| TD-001 | Security      | P0       | Resolved    | Core Engineering | Immediate     |
| TD-002 | Testing       | P1       | In Progress | Core Engineering | Phase 1       |
| TD-003 | Architecture  | P1       | Planned     | Architecture     | Phase 2       |
| TD-004 | Dependency    | P1       | Planned     | DevOps           | Phase 2       |
| TD-005 | Code          | P2       | Identified  | Core Engineering | Phase 3       |
| TD-006 | Documentation | P2       | Planned     | Documentation    | Phase 3       |
| TD-007 | Code          | P3       | Identified  | Core Engineering | Opportunistic |

The values above are illustrative. Actual project status must come from the authoritative audit and tracking register.

---

# 15.39 Debt Record Template

Each new debt record can follow this structure:

```text
## TD-XXX — [Short Title]

Category:
[Architecture / Code / Security / Testing / Dependency / etc.]

Status:
[Identified / Triaged / Planned / In Progress / Blocked / Resolved / Verified / Closed]

Priority:
[P0 / P1 / P2 / P3]

Severity:
[Critical / High / Medium / Low]

Likelihood:
[1–5]

Location:
[Module / File / Component]

Description:
[What is wrong?]

Root Cause:
[Why does the problem exist?]

Impact:
[What happens because of it?]

Dependencies:
[Related technical-debt items or external dependencies]

Owner:
[Responsible person / team]

Proposed Resolution:
[How should it be fixed?]

Verification:
[How will the fix be verified?]

Related Work:
[Issue / PR / Commit / Test]

Created:
[Date]

Target:
[Date / Milestone]

Resolved:
[Date]

Verified:
[Date]

Notes:
[Additional context]
```

---

# 15.40 Closure Requirements

A debt item may be marked `Closed` only when:

```text
[ ] Root cause addressed
[ ] Implementation completed
[ ] Required tests added/updated
[ ] Tests pass
[ ] Regression checks pass
[ ] Relevant review completed
[ ] Documentation updated
[ ] Verification completed
[ ] Related work linked
[ ] Debt register updated
```

For security-sensitive items:

```text
[ ] Security verification completed
```

For performance items:

```text
[ ] Performance measurement completed
```

For dependency items:

```text
[ ] Clean installation/build verified
```

---

# 15.41 Reopening a Closed Debt Item

A closed debt item may be reopened when:

```text
The problem returns
A regression occurs
A new dependency recreates the issue
A new attack vector is discovered
The original fix is insufficient
The underlying architecture changes
```

Reopening should preserve the historical record.

The existing ID should normally be retained rather than creating an unrelated duplicate.

---

# 15.42 Duplicate Debt Handling

If a new issue duplicates an existing debt item:

```text
New Finding
     ↓
Search Existing Register
     ↓
Duplicate Found
     ↓
Link to Existing TD
     ↓
Do Not Create Duplicate Debt
```

The duplicate finding may still be recorded as evidence if useful.

This keeps the backlog clean.

---

# 15.43 Invalid Debt Handling

Sometimes an issue initially reported as technical debt may turn out not to be a real problem.

Such an item should be marked:

```text
Invalid
```

with a reason.

Example:

```text
Status:
Invalid

Reason:
Initial assumption was incorrect after architecture verification.

Evidence:
Architecture review + test results.
```

It should remain in the historical record rather than being silently deleted.

---

# 15.44 Won't Fix

Some issues may intentionally remain unresolved.

The `Won't Fix` status requires:

```text
Reason
Risk Assessment
Mitigation
Owner
Approval / Decision
Review Condition
```

This status should be used sparingly.

It should not be used to hide unresolved high-risk technical debt.

---

# 15.45 Technical Debt and GitHub Issues

If GitHub is used for project management, each significant technical-debt item should map to a GitHub Issue.

Suggested labels:

```text
technical-debt
priority:p0
priority:p1
priority:p2
priority:p3

area:architecture
area:security
area:testing
area:dependency
area:performance
area:documentation
area:code
```

The GitHub Issue should reference the corresponding debt ID.

Example:

```text
TD-018
→ GitHub Issue #81
```

---

# 15.46 Technical Debt and Milestones

Technical debt should be grouped into project milestones.

Example:

```text
Milestone 1
Stabilization

Milestone 2
Security & Testing

Milestone 3
Architecture Modernization

Milestone 4
Refactoring

Milestone 5
Performance & Hardening

Milestone 6
Commercial Release
```

The exact milestone names should remain synchronized with `NEXT_PHASE_ROADMAP.md`.

---

# 15.47 Technical Debt and Releases

Each release should record its technical-debt state.

Example:

```text
Release:
v2.0.0

P0:
0

Critical P1:
0

Remaining P1:
3

P2:
12

P3:
7

Accepted Risks:
2
```

This gives future maintainers historical visibility.

---

# 15.48 Technical Debt and Architecture Decisions

If resolving a debt changes architecture, the decision should be documented.

The relationship should be:

```text
Technical Debt
      ↓
Architecture Decision
      ↓
Implementation
      ↓
Verification
```

Relevant architecture decisions should be reflected in:

```text
ARCHITECTURE.md
```

This prevents the same architectural debate from recurring.

---

# 15.49 Technical Debt and CHANGELOG

Significant debt resolutions that affect users, installation, compatibility, or behavior should be reflected in the project's changelog.

Examples:

```text
Security Fix
Dependency Upgrade
Compatibility Fix
Performance Improvement
Installation Fix
Breaking Architecture Change
```

Internal cleanup that has no user-facing effect does not necessarily need a public changelog entry.

---

# 15.50 Technical Debt and Documentation Synchronization

The following documents should remain synchronized:

```text
TECH_DEBT.md
ARCHITECTURE.md
NEXT_PHASE_ROADMAP.md
PROJECT_STATUS.md
CHANGELOG
README
```

Their responsibilities differ:

```text
PROJECT_STATUS.md
→ Current state

ARCHITECTURE.md
→ System design

TECH_DEBT.md
→ Known engineering debt

NEXT_PHASE_ROADMAP.md
→ Planned future work

CHANGELOG
→ Released changes

README
→ User/developer entry point
```

The same information should not be copied unnecessarily across all files.

---

# 15.51 Workflow Automation

Where practical, technical-debt tracking should eventually be automated.

Potential automation includes:

```text
Dependency Scanning
Static Analysis
Test Coverage
Security Scanning
Code Quality Checks
Build Verification
Linting
Formatting
License Checks
```

Automation should generate evidence that supports the debt-management process.

For example:

```text
Dependency Scan
      ↓
New Vulnerability
      ↓
Create / Update Debt Record
      ↓
Assign Priority
```

Automation should supplement engineering judgment, not replace it.

---

# 15.52 CI/CD Integration

A mature AIPM workflow should integrate technical-debt controls into CI/CD.

Conceptually:

```text
Pull Request
     ↓
Build
     ↓
Unit Tests
     ↓
Integration Tests
     ↓
Static Analysis
     ↓
Security Scan
     ↓
Dependency Scan
     ↓
Quality Gate
     ↓
Merge
```

A P0-level security issue discovered by automated tooling should be capable of blocking the release pipeline.

---

# 15.53 Quality Gates

Recommended quality gates include:

```text
Build Must Pass
Required Tests Must Pass
Critical Security Checks Must Pass
No Critical Dependency Vulnerability
Required Static Checks Must Pass
Required Documentation Must Be Updated
```

The exact gates should be defined according to the project's actual technology stack and release requirements.

---

# 15.54 Monthly / Milestone Debt Review

For long-running development, the technical-debt register should be reviewed periodically.

Review:

```text
New Debt
Resolved Debt
Aging Debt
Priority Changes
Security Findings
Dependency Findings
Architecture Changes
Upcoming Releases
Accepted Risks
```

The review should result in updated:

```text
Priority
Owner
Target Date
Status
Resolution Plan
```

---

# 15.55 Debt Tracking KPIs

The following KPIs are recommended:

| KPI                       | Purpose                                 |
| ------------------------- | --------------------------------------- |
| Open P0 Count             | Measures critical release risk          |
| Open P1 Count             | Measures high-priority engineering risk |
| Average Debt Age          | Measures backlog aging                  |
| Debt Resolution Rate      | Measures remediation effectiveness      |
| Debt Creation Rate        | Measures new debt generation            |
| Debt Burn-Down            | Measures backlog reduction              |
| Security Debt Count       | Measures security exposure              |
| Critical Dependency Count | Measures supply-chain risk              |
| Test Coverage             | Measures regression protection          |
| Verification Rate         | Measures quality of debt closure        |

A particularly important metric is:

```text
Verified Resolutions / Total Resolutions
```

because simply marking items resolved does not prove that the debt was actually removed.

---

# 15.56 Leading vs Lagging Indicators

AIPM should distinguish between leading and lagging indicators.

Leading indicators:

```text
Test Coverage
Code Review Coverage
Dependency Scanning
Static Analysis
Security Scanning
Architecture Review
```

Lagging indicators:

```text
Production Bugs
Security Incidents
Failed Releases
Performance Incidents
Data Loss
Emergency Fixes
```

The goal is to use leading indicators to prevent lagging failures.

---

# 15.57 Debt Tracking Anti-Patterns

The project should avoid:

```text
Deleting Debt Instead of Resolving It
Changing Priority to Hide Risk
Marking Work Resolved Without Tests
Leaving P1 Items Unassigned
Allowing Blocked Items to Remain Forgotten
Creating Duplicate Debt Records
Maintaining Multiple Conflicting Registers
Tracking Only Code Debt
Ignoring Security Debt
Ignoring Dependency Debt
Treating Documentation as Optional
```

These practices create the appearance of debt reduction without actual risk reduction.

---

# 15.58 End-to-End Tracking Example

A complete technical-debt lifecycle can be represented as:

```text
Developer Finds Unsafe File Handling
              ↓
Create TD-042
              ↓
Category: Security
              ↓
Severity: High
              ↓
Likelihood: 4
              ↓
Priority: P1
              ↓
Assign Owner
              ↓
Create GitHub Issue
              ↓
Plan Remediation
              ↓
Implement Secure Handling
              ↓
Add Regression Test
              ↓
Run Security Test
              ↓
Code Review
              ↓
Mark Resolved
              ↓
Security Verification
              ↓
Mark Verified
              ↓
Update TECH_DEBT.md
              ↓
Close Issue
              ↓
Include in Release Notes if Applicable
```

This provides complete traceability.

---

# 15.59 Final Technical Debt Lifecycle

The complete AIPM workflow is:

```text
                    FIND
                     │
                     ▼
                  RECORD
                     │
                     ▼
                   TRIAGE
                     │
                     ▼
                 PRIORITIZE
                     │
                     ▼
                  ASSIGN
                     │
                     ▼
                  PLAN
                     │
                     ▼
                IMPLEMENT
                     │
                     ▼
                   TEST
                     │
                     ▼
                 REVIEW
                     │
                     ▼
                VERIFY
                     │
                     ▼
                 DOCUMENT
                     │
                     ▼
                  CLOSE
                     │
                     ▼
                MONITOR
                     │
                     ▼
             REOPEN IF NEEDED
```

This lifecycle should become the standard technical-debt management process for AIPM.

---

# 15.60 Final Technical Debt Governance Model

The complete governance model is:

```text
                    TECHNICAL DEBT
                           │
                           ▼
                     DEBT REGISTER
                           │
                           ▼
                         TRIAGE
                           │
                           ▼
                    PRIORITY MATRIX
                           │
          ┌────────────────┼────────────────┐
          │                │                │
         P0               P1              P2/P3
          │                │                │
          ▼                ▼                ▼
      Immediate         Planned          Scheduled
       Action            Work             Cleanup
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                      IMPLEMENT
                           │
                           ▼
                         TEST
                           │
                           ▼
                       VERIFY
                           │
                           ▼
                      DOCUMENT
                           │
                           ▼
                         CLOSE
                           │
                           ▼
                      RELEASE
                           │
                           ▼
                    REASSESS DEBT
```

The system is therefore cyclical rather than linear.

---

# 15.61 TECH_DEBT.md Completion Criteria

`TECH_DEBT.md` should be considered operationally complete when:

```text
[ ] Technical-debt categories are defined
[ ] Existing debt has been inventoried
[ ] Architecture debt is documented
[ ] Code debt is documented
[ ] Testing debt is documented
[ ] Security debt is documented
[ ] Documentation debt is documented
[ ] Performance debt is documented
[ ] Dependency debt is documented
[ ] Refactoring candidates are documented
[ ] Priority matrix exists
[ ] Resolution plan exists
[ ] Tracking workflow exists
[ ] Debt IDs are assigned
[ ] Ownership is defined
[ ] Verification requirements are defined
[ ] Release gates are defined
[ ] Risk acceptance process is defined
[ ] Debt metrics are defined
```

---

# 15.62 Section 15 Conclusion

Technical debt management should not be treated as a one-time cleanup activity.

For AIPM, it should become a continuous engineering process:

```text
Audit
  ↓
Track
  ↓
Prioritize
  ↓
Resolve
  ↓
Verify
  ↓
Release
  ↓
Monitor
  ↓
Audit Again
```

The most important operational principle is:

> A technical-debt item is not resolved because someone changed the code. It is resolved only when the underlying risk has been addressed and the result has been verified.

The technical-debt management system should therefore remain connected to:

```text
PROJECT_STATUS.md
ARCHITECTURE.md
NEXT_PHASE_ROADMAP.md
GitHub Issues
GitHub Milestones
CI/CD
Testing
Security Scanning
Release Management
CHANGELOG
```

This completes the planned `TECH_DEBT.md` structure.

The resulting document now provides the complete chain:

```text
What is wrong?
        ↓
Why does it matter?
        ↓
How serious is it?
        ↓
What should be fixed first?
        ↓
How should it be fixed?
        ↓
How will it be tracked?
        ↓
How will we verify the fix?
        ↓
When can it be considered closed?
```

This makes `TECH_DEBT.md` an actionable engineering governance document rather than merely a list of problems.


# 16. Technical Debt Register Template & Maintenance Rules

This section defines the standardized technical-debt register that should be used to record and maintain all known technical-debt items in AIPM.

The purpose of the register is to provide a structured, searchable, auditable, and continuously maintainable record of engineering debt.

The register should function as the operational data source behind the policies and workflows defined in the previous sections.

---

## 16.1 Purpose of the Register

The technical-debt register exists to answer five fundamental questions:

```text
What is the debt?
Where does it exist?
Why does it matter?
What will be done about it?
What is its current state?
```

The register must therefore contain enough information for another developer to understand the issue without requiring undocumented historical knowledge.

---

## 16.2 Standard Debt Record

Every significant technical-debt item should use the following structure:

```text
TD-ID
Title
Category
Subcategory
Status
Severity
Likelihood
Priority
Affected Component
Affected File(s)
Description
Root Cause
Impact
Current Workaround
Proposed Resolution
Dependencies
Owner
Created Date
Target Date
Resolution Date
Verification Method
Verification Result
Related Issue
Related Pull Request
Related Commit
Related Test
Release
Notes
```

This structure should remain consistent throughout the project.

---

# 16.3 Debt ID

Every debt item must have a unique identifier.

Recommended format:

```text
TD-001
TD-002
TD-003
TD-004
```

The identifier must never be reused.

If `TD-014` is closed, the next unrelated issue should not reuse `TD-014`.

Historical identifiers should remain stable because other documents may reference them.

---

# 16.4 Title

The title should describe the actual engineering problem rather than the desired solution.

Good:

```text
Unsafe temporary-file handling
```

Better than:

```text
Implement secure temporary-file service
```

The first describes the debt.

The second describes a possible solution.

The distinction is important because the solution may change during implementation.

---

# 16.5 Category

The primary category should identify the engineering domain affected.

Allowed categories should include:

```text
Architecture
Code
Security
Testing
Dependency
Performance
Documentation
Infrastructure
Reliability
Compatibility
Release
Maintainability
```

Each item should normally have one primary category.

Additional affected areas may be listed separately.

---

# 16.6 Subcategory

A more detailed subcategory may be used where necessary.

Examples:

```text
Architecture
→ Coupling
→ Responsibility Separation
→ Global State

Security
→ Input Validation
→ File Handling
→ Authentication
→ Authorization

Code
→ Duplication
→ Complexity
→ Dead Code
→ Naming

Testing
→ Missing Coverage
→ Weak Regression Protection
→ Integration Gap

Dependency
→ Outdated Package
→ Vulnerability
→ License Risk
→ Compatibility
```

Subcategories should remain stable enough to support reporting.

---

# 16.7 Status

The register should use controlled status values.

```text
Identified
Triaged
Planned
In Progress
Blocked
Resolved
Verified
Closed
Accepted Risk
Won't Fix
Duplicate
Invalid
```

Free-form status values should be avoided.

For example:

```text
"Almost done"
"Waiting"
"Need fix"
"Later"
```

should not be used as formal status values.

---

# 16.8 Severity

Severity describes the potential impact of the problem.

Recommended values:

```text
Critical
High
Medium
Low
```

Severity is different from priority.

For example:

```text
Severity:
High

Priority:
P2
```

may be appropriate if the issue has serious consequences but is unlikely to affect the current release.

---

# 16.9 Likelihood

Likelihood represents the probability of the problem occurring.

Recommended scale:

```text
1 — Rare
2 — Unlikely
3 — Possible
4 — Likely
5 — Very Likely
```

Likelihood should be based on evidence where possible.

---

# 16.10 Priority

Priority determines when the project should address the debt.

```text
P0 — Critical
P1 — High
P2 — Medium
P3 — Low
```

Priority should consider:

```text
Impact
Likelihood
Security
Release Risk
Business Impact
Technical Dependencies
Remediation Cost
```

Priority is therefore a decision, not merely a copy of severity.

---

# 16.11 Affected Component

The register should identify the affected subsystem.

Examples:

```text
Authentication
Database
File Management
Configuration
Core Processing
API
CLI
UI
Reporting
Deployment
Testing
Documentation
```

The component name should correspond to the architecture documented in `ARCHITECTURE.md`.

---

# 16.12 Affected File(s)

Where practical, the debt record should identify the exact files or directories involved.

Example:

```text
Affected Files:

app/Services/ExampleService.php
app/Http/Controllers/ExampleController.php
tests/Feature/ExampleTest.php
```

For architecture-level debt, the record may identify directories or modules rather than individual files.

---

# 16.13 Description

The description should clearly explain what is wrong.

It should answer:

```text
What is currently happening?

What should ideally happen?

Why is the current implementation considered debt?
```

The description should remain factual.

Avoid emotional or subjective wording such as:

```text
"This code is terrible."

"This implementation is very bad."
```

Use engineering language instead:

```text
"The module performs filesystem operations directly inside the application layer, creating tight coupling between business logic and infrastructure concerns."
```

---

# 16.14 Root Cause

The root cause explains why the debt exists.

Possible causes include:

```text
Legacy Design
Time Constraint
Feature Deadline
Incomplete Refactoring
Missing Requirement
Dependency Limitation
Insufficient Testing
Architecture Evolution
Temporary Workaround
Developer Knowledge Gap
External Constraint
```

Root cause analysis is important because fixing only the visible symptom may leave the debt unresolved.

---

# 16.15 Impact

The impact field should describe consequences.

Possible impact areas:

```text
Security
Reliability
Maintainability
Performance
Scalability
Testability
Developer Productivity
Deployment
User Experience
Commercial Readiness
```

Example:

```text
Impact:

The current implementation increases coupling,
makes automated testing difficult, and increases
the probability of regression during future changes.
```

---

# 16.16 Current Workaround

If a workaround exists, it should be recorded.

Example:

```text
Current Workaround:

Developers manually validate the input before
calling the affected operation.
```

The workaround should not be treated as a permanent resolution.

---

# 16.17 Proposed Resolution

This field describes the intended direction.

Example:

```text
Proposed Resolution:

Move filesystem operations into a dedicated
infrastructure service and expose a narrow
application-level interface.
```

The proposed resolution may be revised after implementation begins.

---

# 16.18 Dependencies

Some debt items depend on other work.

Example:

```text
Dependencies:

TD-003 — Testing Foundation
TD-007 — Configuration Refactor
```

Dependencies should be tracked in both directions where useful.

For example:

```text
TD-014
depends on TD-003
```

and:

```text
TD-003
blocks TD-014
```

---

# 16.19 Owner

Every P0/P1 item must have an owner.

The owner may be:

```text
Individual Developer
Core Engineering
Security
DevOps
QA
Architecture
Documentation
```

The owner is responsible for ensuring that the debt lifecycle continues moving.

---

# 16.20 Dates

The register should maintain:

```text
Created Date
Target Date
Resolution Date
Verification Date
```

Example:

```text
Created:
2026-07-29

Target:
2026-08-10

Resolved:
2026-08-07

Verified:
2026-08-08
```

Dates make debt aging measurable.

---

# 16.21 Verification Method

The register should specify how resolution will be verified.

Examples:

```text
Unit Test
Feature Test
Integration Test
Security Regression Test
Static Analysis
Dependency Scan
Performance Benchmark
Manual Verification
Clean Installation
Build Verification
Architecture Review
```

---

# 16.22 Verification Result

The verification result should contain evidence rather than a simple statement.

Weak:

```text
Verified: Yes
```

Better:

```text
Verified:

Regression test SEC-TEST-014 passes.
Clean installation completed successfully.
No related security finding remains.
```

This creates an audit trail.

---

# 16.23 Related Work

Where applicable, link the debt to:

```text
GitHub Issue
Pull Request
Commit
Test
Architecture Decision
Release
Security Finding
```

Example:

```text
Issue:
#84

Pull Request:
#91

Commit:
a8d92c1

Test:
SEC-TEST-014
```

---

# 16.24 Release Association

Every resolved debt item should identify the release or milestone in which it was resolved.

Example:

```text
Resolved In:
v2.1.0
```

This allows future maintainers to answer:

> In which release was this problem fixed?

---

# 16.25 Standard Debt Record Template

The following template should be used for new entries.

```text
## TD-XXX — [Title]

Category:
[Primary Category]

Subcategory:
[Subcategory]

Status:
[Status]

Severity:
[Critical / High / Medium / Low]

Likelihood:
[1–5]

Priority:
[P0 / P1 / P2 / P3]

Affected Component:
[Component]

Affected File(s):
[Files / Directories]

Description:
[Description]

Root Cause:
[Root Cause]

Impact:
[Impact]

Current Workaround:
[Workaround or N/A]

Proposed Resolution:
[Resolution]

Dependencies:
[Related TD IDs or N/A]

Owner:
[Owner]

Created:
[Date]

Target:
[Date]

Resolved:
[Date or N/A]

Verified:
[Date or N/A]

Verification Method:
[Method]

Verification Result:
[Evidence]

Related Issue:
[Issue ID / N/A]

Related Pull Request:
[PR / N/A]

Related Commit:
[Commit / N/A]

Related Test:
[Test / N/A]

Release:
[Release / N/A]

Notes:
[Additional information]
```

---

# 16.26 Example — Security Debt

```text
## TD-001 — Unsafe File Path Handling

Category:
Security

Subcategory:
File Handling

Status:
Triaged

Severity:
Critical

Likelihood:
4

Priority:
P0

Affected Component:
File Management

Affected File(s):
[Actual affected files]

Description:
User-controlled path information is not sufficiently
restricted before filesystem operations.

Root Cause:
The original implementation assumes that incoming
path information is trusted.

Impact:
Potential unauthorized filesystem access.

Current Workaround:
Restricted execution environment.

Proposed Resolution:
Centralize path validation and enforce an explicit
allowed-directory policy.

Dependencies:
Testing Foundation

Owner:
Core Engineering

Created:
[Date]

Target:
Immediate

Resolved:
N/A

Verified:
N/A

Verification Method:
Security regression tests and manual security review.

Verification Result:
Pending

Related Issue:
[Issue]

Related Pull Request:
N/A

Related Commit:
N/A

Related Test:
SEC-TEST-001

Release:
N/A
```

The example demonstrates the expected structure. Actual AIPM debt records must be based on verified findings from the project audit.

---

# 16.27 Example — Architecture Debt

```text
## TD-002 — Excessive Coupling Between Application and Infrastructure

Category:
Architecture

Subcategory:
Coupling

Status:
Planned

Severity:
High

Likelihood:
4

Priority:
P1

Affected Component:
Application Core

Description:
Application logic directly performs infrastructure-level
operations.

Root Cause:
The current architecture evolved incrementally without
a clear infrastructure boundary.

Impact:
Reduced testability and increased maintenance cost.

Proposed Resolution:
Introduce a dedicated abstraction between application
logic and infrastructure services.

Dependencies:
TD-003 — Testing Foundation

Owner:
Architecture / Core Engineering

Verification Method:
Architecture review, dependency analysis,
and regression tests.
```

---

# 16.28 Example — Testing Debt

```text
## TD-003 — Insufficient Regression Coverage

Category:
Testing

Subcategory:
Regression Protection

Status:
In Progress

Severity:
High

Likelihood:
5

Priority:
P1

Affected Component:
Core Processing

Description:
Critical behavior is not sufficiently protected by
automated regression tests.

Impact:
Refactoring may introduce undetected behavioral changes.

Proposed Resolution:
Introduce characterization tests followed by
targeted unit and integration coverage.

Verification:
Required test suite passes in CI.
```

---

# 16.29 Example — Dependency Debt

```text
## TD-004 — Dependency Version Stabilization

Category:
Dependency

Subcategory:
Version Management

Status:
Planned

Severity:
Medium

Likelihood:
3

Priority:
P2

Affected Component:
Dependency Layer

Description:
Dependency versions require a systematic compatibility
and security review.

Impact:
Potential installation, compatibility, and security risks.

Proposed Resolution:
Inventory dependencies, review versions, evaluate
security advisories, and establish reproducible
installation requirements.

Verification:
Clean environment installation + automated tests.
```

---

# 16.30 Example — Documentation Debt

```text
## TD-005 — Incomplete Installation Documentation

Category:
Documentation

Subcategory:
Installation

Status:
Planned

Severity:
Medium

Likelihood:
4

Priority:
P2

Affected Component:
Developer Documentation

Description:
The current installation instructions do not fully
describe the environment and configuration required
to reproduce the project.

Impact:
New developers may be unable to reliably reproduce
the development environment.

Proposed Resolution:
Create verified installation documentation based on
a clean environment.

Verification:
A new developer should be able to follow the documented
process successfully.
```

---

# 16.31 Register Maintenance Rules

The technical-debt register must follow these rules:

```text
1. Every P0/P1 item must have an owner.

2. Every P0/P1 item must have a clear verification method.

3. Every resolved item must have evidence.

4. Closed items must not be silently deleted.

5. Duplicate items should be linked rather than recreated.

6. Priority changes must have a reason.

7. Blocked items must identify the blocker.

8. Accepted risks must identify mitigation.

9. Debt records should reference related work where possible.

10. The register must be reviewed before major releases.
```

---

# 16.32 Register Update Rules

The register should be updated whenever any of the following occurs:

```text
New Debt Identified
Priority Changes
Owner Changes
Implementation Starts
Work Becomes Blocked
Implementation Completes
Verification Completes
Debt Is Reopened
Debt Is Accepted
Debt Is Reclassified
Release Is Completed
```

The register should not be updated only at the end of a development cycle.

---

# 16.33 Stale Record Detection

A debt record should be considered stale when:

```text
No Status Update for a Long Period
No Owner
Target Date Passed
P1 Remains Planned for Multiple Releases
Blocked Without Review
Verification Missing
Architecture Changed Since Record Creation
```

Stale records must be reviewed.

---

# 16.34 Target-Date Policy

Target dates should be realistic.

Do not assign arbitrary dates merely to make the register appear organized.

For P0:

```text
Immediate / Release Blocking
```

For P1:

```text
Current or Next Engineering Milestone
```

For P2:

```text
Planned Future Milestone
```

For P3:

```text
Opportunistic / Backlog
```

If a target date changes, the reason should be documented.

---

# 16.35 Evidence Requirements

A technical-debt record should contain evidence proportional to its risk.

For P0:

```text
Reproduction Evidence
Impact Evidence
Security / Integrity Evidence
Resolution Evidence
Verification Evidence
```

For P1:

```text
Problem Evidence
Impact Evidence
Resolution Evidence
Verification Evidence
```

For P2/P3:

```text
Sufficient Technical Description
Resolution Context
```

This prevents unsupported claims from becoming permanent project documentation.

---

# 16.36 Historical Integrity

Technical-debt history should be preserved.

For example:

```text
TD-010
Created → P2
       ↓
Risk Increased
       ↓
P1
       ↓
Resolved
       ↓
Verified
       ↓
Closed
```

This historical transition should not be overwritten with only the final status.

Git history, GitHub Issues, pull requests, or a change log can provide the detailed historical record.

---

# 16.37 Register and Git History

The register should not attempt to replace Git.

Their responsibilities are different:

```text
TECH_DEBT.md
→ Why the debt exists
→ Risk
→ Priority
→ Resolution status

Git
→ What code changed
→ When it changed
→ Who changed it
→ Exact implementation history
```

The two systems should be linked.

---

# 16.38 Register and GitHub

If GitHub is used, the preferred model is:

```text
TECH_DEBT.md
      ↓
TD-023
      ↓
GitHub Issue #103
      ↓
Pull Request #117
      ↓
Commit
      ↓
Tests
      ↓
Release
```

This creates end-to-end traceability.

---

# 16.39 Register and PROJECT_STATUS.md

`PROJECT_STATUS.md` should summarize the debt situation rather than duplicating the entire register.

Example:

```text
Technical Debt Summary

P0:
0

P1:
4

P2:
11

P3:
8

Critical Security Debt:
0

Blocked:
2

Oldest P1:
41 days
```

The detailed information remains in `TECH_DEBT.md`.

---

# 16.40 Register and NEXT_PHASE_ROADMAP.md

The roadmap should reference debt items when technical debt affects planned work.

Example:

```text
Phase 2 — Architecture Modernization

Related Debt:
TD-003
TD-007
TD-014
```

This ensures that technical debt becomes part of actual project planning rather than remaining a separate document.

---

# 16.41 Register and ARCHITECTURE.md

Architecture-related debt should reference relevant architectural areas.

Example:

```text
Architecture Area:
Application / Infrastructure Boundary

Related Debt:
TD-002
TD-008
```

After resolution, `ARCHITECTURE.md` should be updated if the architecture changed.

---

# 16.42 Release Review Register

Before a release, the register should generate a release-oriented summary:

```text
Release:
vX.Y.Z

P0:
0

Critical P1:
0

Remaining P1:
X

P2:
X

P3:
X

Accepted Risks:
X

Security Findings:
X

Dependency Findings:
X

Blocked Items:
X
```

This summary should become part of the release decision process.

---

# 16.43 Definition of a Healthy Register

A healthy technical-debt register should have:

```text
Clear IDs
Clear Ownership
Controlled Statuses
Meaningful Priorities
Evidence
Verification
Recent Updates
Traceability
Release Association
Minimal Duplication
```

A register with hundreds of undocumented entries is less useful than a smaller register containing well-understood and actionable items.

---

# 16.44 Definition of an Unhealthy Register

Warning signs include:

```text
Many Items Without Owners
Many P1 Items Without Target Dates
Repeated Duplicate Entries
Large Number of "Unknown" Statuses
No Verification Evidence
Old Blocked Items
No Security Classification
No Release Association
No Relationship With GitHub
No Relationship With Testing
No Updates for Long Periods
```

These indicate that technical-debt management itself has become a process problem.

---

# 16.45 Technical Debt Register Quality Gate

Before accepting a new P0/P1 debt record, verify:

```text
[ ] Unique ID assigned
[ ] Title is clear
[ ] Category assigned
[ ] Severity assigned
[ ] Likelihood assessed
[ ] Priority assigned
[ ] Affected component identified
[ ] Problem described
[ ] Root cause identified
[ ] Impact described
[ ] Owner assigned
[ ] Proposed resolution defined
[ ] Verification method defined
[ ] Dependencies identified
```

---

# 16.46 Resolution Quality Gate

Before marking an item `Closed`:

```text
[ ] Root cause addressed
[ ] Implementation completed
[ ] Tests added or updated
[ ] Tests pass
[ ] Regression verified
[ ] Security verified where applicable
[ ] Performance verified where applicable
[ ] Documentation updated where applicable
[ ] Related work linked
[ ] Resolution evidence recorded
[ ] Release association recorded
[ ] Status changed to Closed
```

---

# 16.47 Periodic Register Cleanup

The register should periodically be cleaned for:

```text
Duplicates
Invalid Items
Obsolete Items
Incorrect Priorities
Stale Owners
Expired Target Dates
Missing Verification
Broken References
Outdated Architecture References
```

Cleanup must preserve historical information.

The goal is to improve accuracy, not erase inconvenient history.

---

# 16.48 Recommended Register Lifecycle

The complete operational lifecycle is:

```text
                NEW FINDING
                     │
                     ▼
              CREATE TD-ID
                     │
                     ▼
                 TRIAGE
                     │
                     ▼
              CLASSIFICATION
                     │
                     ▼
              PRIORITIZATION
                     │
                     ▼
                 ASSIGN
                     │
                     ▼
                  PLAN
                     │
                     ▼
               IMPLEMENT
                     │
                     ▼
                  TEST
                     │
                     ▼
                VERIFY
                     │
                     ▼
                 RECORD
                  EVIDENCE
                     │
                     ▼
                  CLOSE
                     │
                     ▼
              RELEASE REVIEW
                     │
                     ▼
             PERIODIC REASSESSMENT
```

---

# 16.49 Final Register Governance

The AIPM technical-debt register should be governed by the following rules:

```text
One debt → One unique ID

One P0/P1 → One accountable owner

One resolution → Verification evidence

One architecture change → Architecture documentation review

One release → Technical-debt review

One accepted risk → Documented justification

One reopened issue → Historical continuity
```

These rules keep the technical-debt process predictable and auditable.

---

# 16.50 Section 16 Conclusion

The technical-debt register is the operational foundation of AIPM's technical-debt management process.

The complete relationship is:

```text
TECH_DEBT.md
      │
      ├── Debt Inventory
      │
      ├── Classification
      │
      ├── Priority
      │
      ├── Resolution Strategy
      │
      ├── Tracking Workflow
      │
      └── Debt Register
              │
              ├── GitHub Issues
              ├── Git Commits
              ├── Tests
              ├── Architecture Decisions
              ├── Releases
              └── Verification Evidence
```

The register must remain a living engineering artifact.

It should evolve as the AIPM codebase evolves.

The final principle is:

> If a technical problem is important enough to affect AIPM's security, reliability, maintainability, scalability, or commercial readiness, it is important enough to be explicitly tracked.

With this section, `TECH_DEBT.md` now contains the complete technical-debt management model:

```text
Identification
      ↓
Classification
      ↓
Assessment
      ↓
Prioritization
      ↓
Resolution
      ↓
Verification
      ↓
Tracking
      ↓
Governance
      ↓
Continuous Review
```

This completes the operational design of the technical-debt management system.

# 17. Technical Debt Audit, Governance & Compliance

This section defines the audit, governance, compliance, and accountability framework for managing technical debt in AIPM.

The objective is to ensure that technical debt is not merely documented but continuously monitored, evaluated, controlled, and incorporated into engineering and release decisions.

Technical debt management should therefore operate as a governance process rather than a one-time documentation exercise.

---

## 17.1 Purpose

The primary objectives of technical-debt governance are:

```text id="4x8m1k"
Detect undocumented debt
        ↓
Validate existing debt
        ↓
Assess current risk
        ↓
Verify remediation progress
        ↓
Prevent uncontrolled debt growth
        ↓
Ensure release readiness
```

The governance process must ensure that:

* Critical technical debt cannot remain hidden.
* High-priority debt has accountable ownership.
* Debt status remains accurate.
* Resolved debt is actually verified.
* Accepted risks are explicitly documented.
* Architecture and implementation remain aligned.
* Technical debt is considered during release decisions.

---

# 17.2 Governance Principles

AIPM technical-debt governance should follow these principles:

```text id="j8v0tq"
Visibility
Accountability
Traceability
Evidence
Risk-Based Prioritization
Continuous Review
Release Awareness
Security First
Architecture Consistency
Historical Integrity
```

Technical debt should be managed according to engineering risk rather than convenience.

---

# 17.3 Governance Hierarchy

The governance model should be:

```text id="n9g4xe"
Project Governance
       │
       ▼
Engineering Governance
       │
       ▼
Technical Debt Governance
       │
       ├── Architecture
       ├── Security
       ├── Code Quality
       ├── Testing
       ├── Dependencies
       ├── Performance
       └── Documentation
```

Technical debt is therefore part of the larger engineering quality system.

---

# 17.4 Technical Debt Governance Roles

Depending on project size, the following responsibilities should exist:

```text id="3p7r2e"
Project Owner
Technical Lead
Architecture Owner
Security Owner
Core Developer
QA / Testing
DevOps / Infrastructure
Documentation Owner
```

A single person may hold multiple responsibilities in a small team.

The responsibilities must still be explicitly understood.

---

# 17.5 Project Owner Responsibilities

The Project Owner is responsible for ensuring that technical debt does not undermine project objectives.

Responsibilities include:

```text id="j5f9h4"
Approve major risk decisions
Review critical debt
Approve accepted risks
Ensure resources for P0/P1 remediation
Review release readiness
```

The Project Owner does not necessarily perform the technical remediation.

---

# 17.6 Technical Lead Responsibilities

The Technical Lead should oversee engineering-level debt.

Responsibilities:

```text id="w4b8t3"
Review P0/P1 items
Coordinate remediation
Review architecture implications
Monitor debt growth
Ensure technical decisions are documented
Escalate unresolved risks
```

---

# 17.7 Architecture Owner Responsibilities

Architecture-related debt should be reviewed by the architecture owner or technical lead.

Responsibilities include:

```text id="x2p9a1"
Review architectural coupling
Review module boundaries
Review dependency direction
Approve major refactoring
Maintain architecture consistency
Update ARCHITECTURE.md
```

Architecture debt should not be resolved solely through local code changes if the underlying design remains incorrect.

---

# 17.8 Security Responsibilities

Security-related debt requires dedicated attention.

Security review should consider:

```text id="6k2n7v"
Authentication
Authorization
Input Validation
Output Encoding
Secrets
File Handling
Database Security
Session Security
Dependency Vulnerabilities
Configuration
Logging
Data Protection
```

Critical security debt should receive priority independent of ordinary feature scheduling.

---

# 17.9 QA / Testing Responsibilities

Testing responsibilities include:

```text id="m5w1qa"
Validate regression protection
Review test coverage
Verify remediation
Confirm release gates
Identify missing test cases
Maintain reproducible test evidence
```

Testing debt should be treated as risk because insufficient regression protection increases the cost of every future change.

---

# 17.10 DevOps / Infrastructure Responsibilities

Where applicable, infrastructure governance should monitor:

```text id="q8x3fc"
Build Reproducibility
Deployment
Environment Configuration
Dependency Installation
CI/CD
Backups
Monitoring
Logging
Secrets Management
Production Configuration
```

Infrastructure debt can remain invisible during local development and become critical during deployment.

---

# 17.11 Documentation Responsibilities

Documentation governance should ensure that:

```text id="z4n8vk"
README
ARCHITECTURE.md
PROJECT_STATUS.md
TECH_DEBT.md
NEXT_PHASE_ROADMAP.md
CHANGELOG
```

remain reasonably synchronized.

Documentation must reflect the actual system rather than the intended system.

---

# 17.12 Audit Frequency

Technical debt should be audited at multiple levels.

Recommended schedule:

```text id="4x3q7a"
Continuous
→ Automated checks

Per Pull Request
→ Localized technical review

Per Milestone
→ Technical-debt review

Before Major Release
→ Full release debt audit

Periodic
→ Full technical-debt reassessment
```

The exact frequency may be adjusted according to project size and development velocity.

---

# 17.13 Continuous Audit

Continuous checks should detect issues such as:

```text id="m1w6pt"
Build Failures
Test Failures
Security Vulnerabilities
Dependency Vulnerabilities
Static Analysis Findings
Linting Problems
Code Quality Regression
```

Automated findings should feed the technical-debt process when they represent persistent engineering problems rather than transient failures.

---

# 17.14 Pull Request Audit

Each significant Pull Request should be evaluated for technical debt.

Questions:

```text id="p0s8wq"
Does this change introduce new debt?

Does it resolve existing debt?

Does it increase coupling?

Does it reduce testability?

Does it introduce a security concern?

Does it create duplicate logic?

Does it require documentation updates?

Does it alter architecture?
```

The purpose is not to reject every imperfect implementation.

The purpose is to prevent uncontrolled accumulation.

---

# 17.15 Milestone Audit

At the end of each major milestone:

```text id="2n4j8e"
Review New Debt
Review Resolved Debt
Review Open P0
Review Open P1
Review Aging Debt
Review Security Debt
Review Dependency Debt
Review Architecture Debt
Review Blocked Debt
Review Accepted Risks
```

The result should update:

```text id="g7r5v1"
PROJECT_STATUS.md
TECH_DEBT.md
NEXT_PHASE_ROADMAP.md
```

where appropriate.

---

# 17.16 Pre-Release Technical Debt Audit

Before a major release, the following audit should be performed:

```text id="s3f9qc"
[ ] P0 review
[ ] P1 review
[ ] Security review
[ ] Dependency review
[ ] Test review
[ ] Architecture review
[ ] Performance review
[ ] Documentation review
[ ] Build verification
[ ] Deployment verification
[ ] Accepted-risk review
```

The release should not proceed automatically simply because the application builds successfully.

---

# 17.17 P0 Release Gate

The default release rule should be:

```text id="5k3m7d"
Open P0 = 0
```

Any exception must be explicitly approved and documented.

For security-related P0 debt, release should normally be blocked until remediation and verification are complete.

---

# 17.18 P1 Release Gate

P1 debt requires a risk-based decision.

The preferred rule is:

```text id="f8v2kd"
Critical P1 = 0
```

Remaining non-critical P1 items require:

```text id="w2x6hs"
Documented Impact
Mitigation
Owner
Target Resolution
Release Approval
```

---

# 17.19 P2/P3 Release Handling

P2 and P3 items normally do not block releases.

However, they should still be evaluated for:

```text id="r4v7np"
Cumulative Impact
Age
Future Maintenance Cost
Dependency Risk
Commercial Impact
```

A large accumulation of P2/P3 debt may eventually become P1-level risk.

---

# 17.20 Risk Acceptance

Sometimes debt cannot immediately be resolved.

The project may explicitly accept the risk.

An accepted-risk record should include:

```text id="q1t6ze"
Debt ID
Risk Description
Reason for Acceptance
Business / Technical Impact
Mitigation
Owner
Acceptance Date
Review Date
Approval
```

Example:

```text id="b8w2rm"
Debt:
TD-021

Status:
Accepted Risk

Reason:
Remediation requires architectural changes scheduled
for the next major modernization phase.

Mitigation:
Additional validation and restricted access.

Owner:
Technical Lead

Review:
Before v3.0 release.
```

Acceptance is not equivalent to resolution.

---

# 17.21 Risk Acceptance Expiration

Accepted risks should not remain permanently accepted without review.

Every accepted risk should have a review condition.

Examples:

```text id="m9q4xz"
Next Major Release
Architecture Refactor
Security Review
User Growth
Dependency Upgrade
Production Incident
```

When the condition occurs, the risk must be reassessed.

---

# 17.22 Technical Debt Audit Evidence

An audit should produce evidence.

Possible evidence includes:

```text id="a6f3jp"
Debt Register Snapshot
GitHub Issue Status
Test Results
Security Scan
Dependency Scan
Build Logs
Performance Measurements
Architecture Review
Code Review
Release Checklist
```

Evidence should be stored or referenced in a way that remains accessible to the engineering team.

---

# 17.23 Audit Findings

Audit findings should be categorized.

```text id="c7d1qm"
Critical
High
Medium
Low
Observation
```

A finding should contain:

```text id="y8m3pa"
Finding
Evidence
Risk
Recommendation
Owner
Priority
Target Date
```

---

# 17.24 Audit Finding Example

```text id="n2q8sv"
Finding:
Multiple critical application paths lack sufficient
automated regression coverage.

Evidence:
Existing test suite does not cover the affected workflows.

Risk:
Future refactoring may introduce undetected regressions.

Priority:
P1

Recommendation:
Add characterization and integration tests before
major architectural refactoring.

Owner:
Core Engineering

Target:
Phase 1 — Stabilization
```

---

# 17.25 Compliance Matrix

AIPM should maintain a simple compliance view:

| Control              | Required    | Evidence            | Status    |
| -------------------- | ----------- | ------------------- | --------- |
| P0 Debt Tracking     | Yes         | Debt Register       | Pass/Fail |
| P1 Ownership         | Yes         | Debt Register       | Pass/Fail |
| Security Review      | Yes         | Security Evidence   | Pass/Fail |
| Regression Testing   | Yes         | Test Results        | Pass/Fail |
| Dependency Review    | Yes         | Dependency Scan     | Pass/Fail |
| Architecture Review  | Conditional | Architecture Review | Pass/Fail |
| Documentation Update | Conditional | Documentation       | Pass/Fail |
| Release Debt Review  | Yes         | Release Checklist   | Pass/Fail |

This should be adapted as the actual project matures.

---

# 17.26 Governance Metrics

Governance effectiveness should be measured through metrics such as:

```text id="s6m9bx"
P0 Resolution Rate
P1 Resolution Rate
Average Debt Age
Unassigned Debt
Overdue Debt
Blocked Debt
Accepted Risk Count
Debt Reopened Rate
Verification Rate
Audit Finding Closure Rate
Security Debt Closure Rate
```

The purpose is not to optimize numbers artificially.

The purpose is to determine whether engineering risk is actually being controlled.

---

# 17.27 Debt Governance KPIs

Recommended KPIs:

```text id="g0w4yx"
P0 Resolution Rate
=
Resolved P0 / Total P0

P1 Resolution Rate
=
Resolved P1 / Total P1

Verification Rate
=
Verified Resolutions / Total Resolutions

Overdue Debt Rate
=
Overdue Open Debt / Total Open Debt

Unassigned Debt Rate
=
Unassigned Debt / Total Open Debt
```

A healthy system should generally trend toward:

```text id="f6m3zr"
P0 → 0
Critical P1 → 0
Unassigned P1 → 0
Unverified Resolution → 0
Overdue Critical Debt → 0
```

---

# 17.28 Debt Governance Dashboard

A future engineering dashboard should provide:

```text id="x9b4kp"
TECHNICAL DEBT GOVERNANCE
────────────────────────────

P0 Open                  0
Critical P1 Open         X
Total P1                 X
Total Open Debt          X

Overdue Debt              X
Blocked Debt              X
Unassigned Debt           X
Accepted Risks            X

Verification Rate         X%
P1 Resolution Rate        X%
Average Debt Age          X days

Security Debt             X
Architecture Debt         X
Testing Debt              X
Dependency Debt           X
```

This should be generated from authoritative project data rather than manually maintained numbers whenever practical.

---

# 17.29 Governance Escalation

Technical debt should be escalated when:

```text id="z4m7cs"
P0 Remains Open
Critical Security Risk Exists
P1 Remains Unassigned
Target Date Is Repeatedly Missed
Risk Increases
Production Incident Occurs
Debt Blocks Major Architecture Work
Debt Threatens Release
```

Escalation may result in:

```text id="k5n1ye"
Priority Increase
Resource Reallocation
Release Blocking
Architecture Review
Security Review
Emergency Remediation
```

---

# 17.30 Architecture Governance Integration

Technical-debt governance must be connected to architecture governance.

When a debt item proposes:

```text id="r2d8fk"
New Service
New Module
Database Change
API Change
Dependency Boundary
Infrastructure Change
Major Refactor
```

the architecture should be reviewed before implementation.

This prevents technical-debt remediation from creating a second architectural problem.

---

# 17.31 Security Governance Integration

Security debt should be connected to the project's security process.

The relationship should be:

```text id="v3p7la"
Security Finding
      ↓
Technical Debt
      ↓
Risk Assessment
      ↓
Remediation
      ↓
Security Verification
      ↓
Closure
```

Security findings must not disappear merely because a code change has been merged.

---

# 17.32 Testing Governance Integration

Technical-debt governance should ensure that remediation creates appropriate regression protection.

The preferred relationship is:

```text id="c8y5qm"
Debt
 ↓
Fix
 ↓
Test
 ↓
CI
 ↓
Future Regression Protection
```

A recurring debt item should trigger investigation into why existing testing failed to detect it earlier.

---

# 17.33 Dependency Governance Integration

Dependency-related technical debt should be reviewed against:

```text id="t7p3kw"
Current Version
Supported Version
Security Advisories
Compatibility
License
Transitive Dependencies
Build Reproducibility
Runtime Compatibility
```

Dependency upgrades should be tested rather than performed solely by version replacement.

---

# 17.34 Change Management

Major debt remediation should follow controlled change management.

At minimum:

```text id="a5q9zr"
Problem Identified
      ↓
Impact Assessed
      ↓
Change Planned
      ↓
Implementation
      ↓
Testing
      ↓
Review
      ↓
Verification
      ↓
Release
```

For high-risk architecture changes, additional review may be required.

---

# 17.35 Audit Independence

For critical findings, verification should be performed by someone other than the person who implemented the remediation when practical.

For example:

```text id="p4m8cs"
Developer
→ Implements Fix

QA / Security / Technical Lead
→ Verifies Fix
```

This reduces confirmation bias.

For small teams where independent verification is impractical, automated tests and documented evidence should provide additional safeguards.

---

# 17.36 Audit Sampling

Not every low-risk item requires the same level of audit.

A risk-based sampling approach may be used.

```text id="n6q1vt"
P0
→ Full Review

P1
→ Detailed Review

P2
→ Standard Review

P3
→ Periodic Sampling
```

This allows governance effort to remain proportional to risk.

---

# 17.37 Audit Trail

Important decisions should remain traceable.

The audit trail may include:

```text id="x8v4qp"
Original Finding
Priority Changes
Ownership Changes
Implementation
Tests
Review
Verification
Risk Acceptance
Release
Closure
```

GitHub, Git, CI/CD, and project documentation can collectively provide this trail.

---

# 17.38 Governance Anti-Patterns

The following practices should be avoided:

```text id="d7k2mc"
Declaring Debt Resolved Without Evidence
Closing Issues to Improve Metrics
Ignoring P0 Because a Release Is Urgent
Keeping P1 Items Without Owners
Accepting Risk Without Documentation
Changing Priority Without Explanation
Deleting Historical Debt
Ignoring Security Debt
Ignoring Dependency Debt
Treating Tests as Optional
Maintaining an Outdated Register
```

These practices undermine the entire governance process.

---

# 17.39 Governance Review Questions

During a technical-debt governance review, ask:

```text id="w9r3na"
What is our most dangerous open debt?

Which debt is blocking architecture modernization?

Which debt is increasing fastest?

Which debt is oldest?

Which debt has no owner?

Which debt is overdue?

Which accepted risk is becoming unacceptable?

Which resolved items lack verification?

What debt was introduced during the last milestone?

Are releases becoming more difficult because of accumulated debt?
```

These questions should drive decisions rather than merely reviewing counts.

---

# 17.40 Governance Decision Framework

For each significant debt item:

```text id="f4x8kp"
             TECHNICAL DEBT
                    │
                    ▼
               RISK ASSESSMENT
                    │
        ┌───────────┼───────────┐
        │           │           │
      Low         Medium       High
        │           │           │
        ▼           ▼           ▼
    Backlog      Planned     Immediate
        │         Work        Action
        │           │           │
        └───────────┼───────────┘
                    ▼
                Verification
                    │
                    ▼
                  Closure
```

---

# 17.41 Technical Debt Governance Checklist

Before each major release:

```text id="p7c3mv"
[ ] TECH_DEBT.md reviewed
[ ] All P0 items reviewed
[ ] Critical P1 items reviewed
[ ] Security debt reviewed
[ ] Dependency debt reviewed
[ ] Architecture debt reviewed
[ ] Testing debt reviewed
[ ] Overdue debt reviewed
[ ] Blocked debt reviewed
[ ] Accepted risks reviewed
[ ] Owners confirmed
[ ] Target dates confirmed
[ ] Verification evidence reviewed
[ ] Release gate confirmed
```

---

# 17.42 Compliance Status

AIPM may use the following status model:

```text id="u5j8qw"
COMPLIANT
Partially Compliant
Non-Compliant
Not Applicable
Pending Verification
```

`Compliant` should mean that sufficient evidence exists.

It should not mean merely that someone verbally confirmed the requirement.

---

# 17.43 Non-Compliance Handling

When a governance requirement is not satisfied:

```text id="b3r7nk"
Non-Compliance
      ↓
Record Finding
      ↓
Assess Risk
      ↓
Assign Owner
      ↓
Define Corrective Action
      ↓
Set Target Date
      ↓
Implement
      ↓
Verify
      ↓
Close Finding
```

Critical non-compliance should be escalated immediately.

---

# 17.44 Corrective Action

Corrective actions may include:

```text id="r8x2mf"
Code Change
Architecture Refactor
Test Addition
Dependency Upgrade
Security Hardening
Documentation Update
CI/CD Improvement
Monitoring Improvement
Process Change
```

Corrective action should address the underlying cause whenever practical.

---

# 17.45 Preventive Action

A mature governance system should not only fix existing debt.

It should prevent recurrence.

Examples:

```text id="c5v9qk"
New Coding Standard
New Automated Test
New CI Quality Gate
Architecture Rule
Dependency Policy
Security Check
Documentation Template
Code Review Checklist
```

The preferred outcome is:

```text id="w2n7ms"
Problem
 ↓
Fix
 ↓
Root Cause
 ↓
Preventive Control
```

---

# 17.46 Governance Maturity Levels

AIPM technical-debt governance can evolve through the following maturity levels.

### Level 0 — Unmanaged

```text
Debt exists but is largely undocumented.
```

### Level 1 — Documented

```text
Debt is recorded in TECH_DEBT.md.
```

### Level 2 — Tracked

```text
Debt has IDs, owners, priorities, and statuses.
```

### Level 3 — Measured

```text
Debt metrics and aging are monitored.
```

### Level 4 — Integrated

```text
Debt is integrated with GitHub, testing,
architecture, security, and releases.
```

### Level 5 — Preventive

```text
Automation and engineering controls prevent
significant new debt from accumulating.
```

The target for a commercial-ready AIPM should be at least Level 4, with selected Level 5 controls.

---

# 17.47 Governance Maturity Assessment

AIPM should periodically evaluate:

```text id="y1p8zc"
Documentation
Tracking
Ownership
Prioritization
Verification
Automation
Security
Architecture
Testing
Release Integration
```

The objective is continuous improvement rather than achieving a perfect score.

---

# 17.48 Technical Debt Governance and Commercial Readiness

For a commercial-ready product, technical-debt governance becomes particularly important.

Commercial deployment increases the importance of:

```text id="z4k6qp"
Security
Reliability
Maintainability
Upgradeability
Supportability
Documentation
Deployment Reproducibility
Dependency Management
Testing
Incident Response
```

Therefore, technical debt that might be acceptable in an academic prototype may be unacceptable in a commercial product.

---

# 17.49 Commercial Release Debt Gate

Before a commercial release, AIPM should target:

```text id="x9f4mv"
P0 Critical Debt:
0

Unverified Critical Findings:
0

Critical Security Vulnerabilities:
0

Unowned P1 Debt:
0

Critical Build Failures:
0

Critical Regression Failures:
0
```

Remaining lower-priority debt must be explicitly documented.

---

# 17.50 Governance Reporting

A technical-debt report should be produced for major milestones and releases.

Minimum report:

```text id="v3k8qs"
Current Debt
New Debt
Resolved Debt
P0
P1
P2
P3
Security Debt
Architecture Debt
Testing Debt
Dependency Debt
Overdue Debt
Blocked Debt
Accepted Risks
Verification Rate
Recommended Actions
```

This report should be summarized in `PROJECT_STATUS.md` where relevant.

---

# 17.51 Governance Report Example

```text id="m8q2dz"
Technical Debt Governance Report
Release: vX.Y.Z

Open P0:
0

Open Critical P1:
0

Open P1:
3

Open P2:
11

Open P3:
8

New Debt Since Previous Release:
4

Resolved:
7

Verified:
7

Blocked:
1

Accepted Risks:
2

Oldest P1:
41 days

Release Recommendation:
Proceed with documented P1/P2 risks.
```

The numbers above are examples only.

Actual values must come from the current project state.

---

# 17.52 Governance Record Retention

Technical-debt records should remain available throughout the project's lifecycle.

Closed debt should generally not be deleted because it provides:

```text id="q6n3wf"
Historical Context
Architecture Evolution
Recurring Problem Detection
Engineering Lessons
Release History
Risk History
```

Historical records are especially useful when the same class of problem appears again.

---

# 17.53 Recurring Debt Analysis

If the same category repeatedly appears, investigate the process rather than treating every instance independently.

Example:

```text id="r7c1mx"
Repeated Input Validation Debt
        ↓
Individual Fixes
        ↓
Same Problem Reappears
        ↓
Root Process Problem
        ↓
Introduce Central Validation Policy
        ↓
Automated Enforcement
```

Recurring debt is often evidence of missing engineering controls.

---

# 17.54 Root-Cause Governance

The governance process should distinguish:

```text id="m3v8qa"
Symptom
   ↓
Local Fix

versus

Root Cause
   ↓
Systemic Fix
```

For repeated debt, the second approach is preferred.

---

# 17.55 Technical Debt Prevention Controls

Potential preventive controls include:

```text id="n8f5cr"
Coding Standards
Architecture Guidelines
Pull Request Templates
Automated Testing
Static Analysis
Security Scanning
Dependency Scanning
CI Quality Gates
Documentation Templates
Release Checklists
```

Controls should be introduced selectively according to actual project risk.

---

# 17.56 Final Governance Model

The complete governance system should operate as:

```text id="s7q4mp"
                PROJECT
                   │
                   ▼
              ENGINEERING
                   │
                   ▼
            TECHNICAL DEBT
                   │
          ┌────────┼────────┐
          │        │        │
      Security  Quality  Architecture
          │        │        │
          └────────┼────────┘
                   ▼
               REGISTER
                   │
                   ▼
                AUDIT
                   │
                   ▼
              PRIORITIZE
                   │
                   ▼
              REMEDIATE
                   │
                   ▼
               VERIFY
                   │
                   ▼
               RELEASE
                   │
                   ▼
              REASSESS
                   │
                   └──────────→ CONTINUOUS CYCLE
```

---

# 17.57 Section 17 Completion Criteria

This section is considered implemented when:

```text id="h4n9xs"
[ ] Governance responsibilities defined
[ ] Audit frequency defined
[ ] Release gates defined
[ ] Risk acceptance defined
[ ] Audit evidence defined
[ ] Compliance model defined
[ ] Escalation process defined
[ ] Governance metrics defined
[ ] Commercial release criteria defined
[ ] Preventive controls defined
[ ] Maturity model defined
[ ] Reporting process defined
```

---

# 17.58 Section 17 Conclusion

Technical debt becomes dangerous when it is invisible, unowned, unmeasured, or repeatedly ignored.

AIPM should therefore treat technical debt as an engineering governance concern:

```text
Identify
   ↓
Document
   ↓
Assess
   ↓
Prioritize
   ↓
Assign
   ↓
Remediate
   ↓
Verify
   ↓
Audit
   ↓
Release
   ↓
Reassess
```

The central governance principle is:

> Technical debt must be visible to decision-makers before it becomes a release, security, reliability, or commercial-readiness problem.

The relationship between the major project documents should therefore remain:

```text
PROJECT_STATUS.md
        │
        ├── Current State
        │
        ▼
ARCHITECTURE.md
        │
        ├── System Structure
        │
        ▼
TECH_DEBT.md
        │
        ├── Engineering Risks
        │
        ▼
NEXT_PHASE_ROADMAP.md
        │
        ├── Planned Remediation
        │
        ▼
Implementation
        │
        ▼
Testing / Verification
        │
        ▼
Release
```

This completes the governance layer of `TECH_DEBT.md`.

The next section should move from governance theory toward the final operational control layer: **Technical Debt Acceptance Criteria, Definition of Done, and Release Readiness Rules**.
# 18. Technical Debt Acceptance Criteria, Definition of Done & Release Readiness Rules

This section defines the formal acceptance criteria for technical-debt remediation in AIPM.

The purpose is to establish objective rules for determining when a technical-debt item can move from:

```text
Identified
   ↓
Planned
   ↓
In Progress
   ↓
Resolved
   ↓
Verified
   ↓
Closed
```

A technical-debt item must not be considered complete merely because code has been changed.

Completion requires evidence that the underlying problem has been addressed and that the change does not introduce unacceptable regression, security, architecture, reliability, or maintainability risk.

---

## 18.1 Purpose

The acceptance framework exists to prevent premature closure of technical debt.

The central principle is:

> Code changed is not the same as debt resolved.

A debt item is resolved only when:

```text
Problem Understood
        ↓
Root Cause Addressed
        ↓
Implementation Completed
        ↓
Tests Updated
        ↓
Verification Passed
        ↓
Documentation Updated
        ↓
Evidence Recorded
        ↓
Release Impact Assessed
        ↓
Debt Closed
```

---

## 18.2 Acceptance Criteria

Every technical-debt remediation should satisfy applicable acceptance criteria.

The criteria are divided into:

```text
A. Functional Acceptance
B. Code Quality Acceptance
C. Architecture Acceptance
D. Security Acceptance
E. Testing Acceptance
F. Performance Acceptance
G. Documentation Acceptance
H. Deployment Acceptance
I. Traceability Acceptance
```

Not every category applies to every debt item, but applicability should be explicitly considered.

---

# 18.3 General Acceptance Criteria

A technical-debt item may be marked `Resolved` only when:

```text
[ ] Original problem has been addressed
[ ] Root cause has been considered
[ ] Required implementation is complete
[ ] Relevant tests have been created or updated
[ ] Existing regression tests pass
[ ] Relevant review is complete
[ ] No known critical regression exists
[ ] Documentation has been updated where necessary
[ ] Related issue / task is linked
[ ] Verification method has been executed
```

It may be marked `Closed` only after verification evidence has been recorded.

---

# 18.4 Functional Acceptance

Functional acceptance verifies that remediation preserves or improves expected behavior.

Required checks:

```text
[ ] Existing supported behavior still works
[ ] Intended behavior is implemented
[ ] Edge cases have been considered
[ ] Invalid input behaves appropriately
[ ] Error conditions are handled appropriately
[ ] No unintended behavior change is observed
```

For behavior-preserving refactoring, the expected functional output should remain unchanged unless the debt item explicitly requires a behavior change.

---

# 18.5 Behavior-Preserving Refactoring

For refactoring debt, the default rule is:

```text
Before Refactor
      ↓
Known Behavior
      ↓
Characterization / Regression Tests
      ↓
Refactor
      ↓
Same Expected Behavior
```

A refactoring should not silently change business behavior.

If behavior intentionally changes, the task should be treated as both:

```text
Technical Debt Remediation
+
Functional Change
```

and should receive the corresponding review.

---

# 18.6 Code Quality Acceptance

The remediation should improve or at least not materially worsen code quality.

Review should consider:

```text
Readability
Maintainability
Complexity
Duplication
Naming
Responsibility Separation
Error Handling
Dependency Direction
Testability
Dead Code
Configuration Handling
```

The remediation should not simply move the same problem into another file or layer.

---

# 18.7 Complexity Acceptance

Where debt involves excessive complexity, the remediation should demonstrate meaningful improvement.

Possible evidence:

```text
Reduced Function Complexity
Reduced Nesting
Reduced Branching
Reduced Duplication
Reduced Responsibility Count
Improved Module Boundaries
Improved Testability
```

A refactor should be evaluated by structure and maintainability, not merely by lines of code removed.

---

# 18.8 Architecture Acceptance

Architecture debt requires architectural verification.

The implementation should be checked against:

```text
ARCHITECTURE.md
Module Boundaries
Dependency Direction
Application / Infrastructure Separation
Domain Responsibilities
Service Responsibilities
Controller Responsibilities
Data Access Boundaries
External Integration Boundaries
```

A local code fix should not be accepted if it creates a new architectural violation.

---

# 18.9 Architecture Change Acceptance

If remediation changes the architecture:

```text
[ ] Architecture impact identified
[ ] Relevant architecture decision documented
[ ] ARCHITECTURE.md reviewed
[ ] Dependency direction verified
[ ] Module ownership verified
[ ] Integration points verified
[ ] Tests updated
```

The architecture documentation should reflect the actual post-change architecture.

---

# 18.10 Security Acceptance

Security-related debt requires stronger acceptance criteria.

Applicable checks include:

```text
[ ] Input validation
[ ] Authorization
[ ] Authentication
[ ] Session handling
[ ] File handling
[ ] Path validation
[ ] SQL safety
[ ] Output encoding
[ ] Sensitive data exposure
[ ] Secret handling
[ ] Error information disclosure
[ ] Logging behavior
[ ] Dependency vulnerabilities
```

For P0 security debt, successful remediation and verification are required before normal release.

---

# 18.11 Security Verification

A security debt should not be closed solely because a vulnerable code path was modified.

Verification should demonstrate that:

```text
Original Attack / Failure Condition
              ↓
          No Longer Works
              ↓
Expected Secure Behavior
              ↓
       Regression Protected
```

Evidence may include:

```text
Security Test
Static Analysis
Dependency Scan
Manual Review
Reproduction Test
Integration Test
```

---

# 18.12 Testing Acceptance

Testing is a core part of technical-debt remediation.

The minimum testing strategy should be selected according to risk.

```text
Low Risk
→ Targeted Test

Medium Risk
→ Unit / Feature Test

High Risk
→ Unit + Integration / Feature Tests

Critical Risk
→ Full Relevant Regression + Security / Deployment Verification
```

---

# 18.13 Regression Acceptance

Before closing debt, the relevant regression suite must pass.

The test result should be recorded as evidence.

Example:

```text
Test Suite:
PHPUnit

Result:
Passed

Tests:
128

Assertions:
412

Failures:
0

Errors:
0
```

The exact numbers must reflect actual project execution.

---

# 18.14 Test Coverage Acceptance

The objective is not to maximize coverage percentage blindly.

The objective is to ensure that the risk introduced by the affected code is adequately protected.

Priority should be given to:

```text
Critical Business Logic
Security Boundaries
Data Integrity
Authentication
Authorization
File Operations
Database Operations
Core Services
High-Complexity Functions
Previously Failed Paths
```

---

# 18.15 Characterization Test Requirement

When refactoring poorly understood legacy behavior, characterization tests should be considered before major changes.

The process is:

```text
Existing Implementation
        ↓
Observe Current Behavior
        ↓
Write Characterization Tests
        ↓
Refactor
        ↓
Run Tests
        ↓
Compare Behavior
```

This is particularly important for legacy modules where requirements are incomplete.

---

# 18.16 Error Handling Acceptance

Where debt involves error handling, acceptance requires:

```text
[ ] Expected errors are handled
[ ] Unexpected errors fail safely
[ ] Sensitive details are not exposed
[ ] Errors are logged where appropriate
[ ] User-facing messages are appropriate
[ ] Exceptions are not silently swallowed
[ ] Error handling remains consistent across related paths
```

The remediation should not replace visible failures with silent failures merely to make tests pass.

---

# 18.17 Data Integrity Acceptance

For database-related debt, acceptance must verify:

```text
Data Consistency
Transaction Behavior
Validation
Constraint Handling
Concurrency Considerations
Rollback Behavior
Migration Safety
Relationship Integrity
```

For changes affecting persistent data, rollback and migration behavior should be explicitly reviewed.

---

# 18.18 Database Change Acceptance

A database-related remediation should satisfy:

```text
[ ] Migration is valid
[ ] Migration works on clean database
[ ] Migration works on representative existing database
[ ] Data loss risk assessed
[ ] Rollback behavior considered
[ ] Constraints verified
[ ] Relevant queries tested
[ ] Application compatibility verified
```

A database migration should never be considered safe merely because it succeeds on one developer machine.

---

# 18.19 Dependency Debt Acceptance

For dependency-related debt:

```text
[ ] Target version identified
[ ] Compatibility reviewed
[ ] Security advisories reviewed
[ ] Transitive dependencies reviewed
[ ] Application tests pass
[ ] Build succeeds
[ ] Installation succeeds in a clean environment
[ ] License implications considered where applicable
```

Dependency upgrades should be verified against the actual AIPM environment.

---

# 18.20 Performance Acceptance

Performance debt requires measurable evidence where performance is part of the problem.

Possible evidence:

```text
Execution Time
Memory Usage
Database Query Count
Response Time
Throughput
CPU Utilization
I/O Operations
```

The remediation should compare:

```text
Before
vs.
After
```

where reliable baseline measurements exist.

---

# 18.21 Performance Regression Rule

A remediation intended to improve maintainability should not introduce a severe performance regression without explicit acceptance.

For example:

```text
Maintainability Improved
+
Performance Significantly Degraded
=
Not Automatically Accepted
```

The trade-off must be evaluated according to actual project requirements.

---

# 18.22 Documentation Acceptance

Documentation must be updated when remediation changes:

```text
Architecture
Installation
Configuration
API
CLI
Database
Deployment
Security Procedures
Developer Workflow
User-Facing Behavior
```

Documentation should describe actual behavior.

---

# 18.23 Documentation Consistency

After a significant change, review:

```text
README
ARCHITECTURE.md
PROJECT_STATUS.md
TECH_DEBT.md
NEXT_PHASE_ROADMAP.md
CHANGELOG
```

Not every file requires modification for every change.

The rule is:

> Update documentation wherever the documented reality has changed.

---

# 18.24 Deployment Acceptance

For deployment-related debt:

```text
[ ] Build succeeds
[ ] Dependencies install successfully
[ ] Environment configuration is documented
[ ] Required environment variables are known
[ ] Database migration works
[ ] Static assets build correctly
[ ] Application starts successfully
[ ] Relevant smoke tests pass
```

A fix that works only in local development should not be considered fully resolved deployment debt.

---

# 18.25 Clean Environment Acceptance

Where reproducibility is relevant, the remediation should be tested in a clean environment.

The objective is:

```text
Clean Environment
      ↓
Install Dependencies
      ↓
Configure Application
      ↓
Run Migrations
      ↓
Build
      ↓
Run Tests
      ↓
Application Starts
```

This helps identify hidden local-machine dependencies.

---

# 18.26 Traceability Acceptance

Every significant debt remediation should be traceable.

Preferred relationship:

```text
TD-ID
  ↓
Issue
  ↓
Pull Request
  ↓
Commit
  ↓
Test
  ↓
Verification
  ↓
Release
```

The exact tooling may vary, but the relationship should remain understandable.

---

# 18.27 Definition of Done

A technical-debt task is considered `Done` only when all applicable requirements have been satisfied.

```text
DEFINITION OF DONE

[ ] Debt item identified correctly
[ ] Scope understood
[ ] Root cause analyzed
[ ] Implementation completed
[ ] Code reviewed
[ ] Tests created / updated
[ ] Regression suite passed
[ ] Security checked where applicable
[ ] Architecture checked where applicable
[ ] Performance checked where applicable
[ ] Documentation updated where applicable
[ ] Verification completed
[ ] Evidence recorded
[ ] Related issue / PR linked
[ ] Release impact assessed
```

---

# 18.28 Definition of Done vs Definition of Resolved

These terms should not be treated as identical.

```text
Resolved
→ Implementation has addressed the problem.

Done
→ All applicable engineering and verification requirements
  have been completed.

Closed
→ The remediation has been verified and formally recorded.
```

Therefore:

```text
Resolved ≠ Done ≠ Closed
```

This distinction prevents premature closure.

---

# 18.29 Definition of Closed

A debt item may be marked `Closed` only when:

```text
[ ] Resolution completed
[ ] Verification passed
[ ] Evidence recorded
[ ] Required documentation updated
[ ] No unresolved blocker remains
[ ] Related work is traceable
[ ] Release association recorded
```

---

# 18.30 Reopening Criteria

A closed debt item must be reopened if:

```text
Original Problem Returns
Fix Was Incomplete
Regression Is Discovered
Security Risk Remains
Architecture Violation Remains
Verification Was Insufficient
New Evidence Invalidates Closure
```

Reopening should preserve the original TD-ID whenever possible.

---

# 18.31 Reopened Debt

Example lifecycle:

```text
TD-014
   ↓
Resolved
   ↓
Verified
   ↓
Closed
   ↓
Regression Discovered
   ↓
Reopened
   ↓
Reassessed
   ↓
Remediated
   ↓
Reverified
   ↓
Closed
```

This history should remain visible.

---

# 18.32 Release Readiness Model

Technical-debt release readiness should be evaluated through multiple gates:

```text
Gate 1 — Critical Risk
Gate 2 — Security
Gate 3 — Testing
Gate 4 — Architecture
Gate 5 — Dependencies
Gate 6 — Performance
Gate 7 — Documentation
Gate 8 — Deployment
Gate 9 — Risk Acceptance
```

A release should be evaluated against all applicable gates.

---

# 18.33 Gate 1 — Critical Risk

Required:

```text
Open P0:
0
```

Exceptions require explicit approval.

A critical technical debt item should normally block release.

---

# 18.34 Gate 2 — Security

Before release:

```text
[ ] Critical security findings reviewed
[ ] P0 security debt resolved
[ ] Relevant security tests pass
[ ] Dependency security review completed
[ ] Sensitive configuration reviewed
```

---

# 18.35 Gate 3 — Testing

Before release:

```text
[ ] Relevant automated tests pass
[ ] Regression suite passes
[ ] Critical workflows verified
[ ] Known test debt documented
[ ] No unexplained critical test failure exists
```

---

# 18.36 Gate 4 — Architecture

Required when architecture has changed:

```text
[ ] Architecture impact reviewed
[ ] Dependency direction checked
[ ] Module boundaries checked
[ ] ARCHITECTURE.md updated where necessary
[ ] Technical-debt register updated
```

---

# 18.37 Gate 5 — Dependencies

Before release:

```text
[ ] Dependency versions reviewed
[ ] Critical vulnerabilities addressed
[ ] Installation verified
[ ] Compatibility verified
[ ] Lockfile / dependency state reproducible
```

---

# 18.38 Gate 6 — Performance

Applicable when the release affects performance-sensitive areas.

Check:

```text
[ ] Known performance debt reviewed
[ ] Critical regression tested
[ ] Relevant benchmark compared
[ ] Database performance considered
[ ] Resource consumption considered
```

---

# 18.39 Gate 7 — Documentation

Before release:

```text
[ ] README accurate
[ ] Architecture documentation accurate
[ ] Installation instructions accurate
[ ] Configuration documented
[ ] Relevant technical debt updated
[ ] Release notes prepared
```

---

# 18.40 Gate 8 — Deployment

Before release:

```text
[ ] Build verified
[ ] Clean installation verified
[ ] Migration verified
[ ] Environment requirements documented
[ ] Deployment process verified
[ ] Smoke test passed
```

---

# 18.41 Gate 9 — Risk Acceptance

Any remaining significant debt must be explicitly classified.

Possible decisions:

```text
Release
Release With Mitigation
Release With Accepted Risk
Delay Release
Block Release
```

The decision must be supported by evidence.

---

# 18.42 Release Readiness Decision Matrix

| Condition                             | Default Decision |
| ------------------------------------- | ---------------- |
| P0 open                               | Block            |
| Critical security vulnerability open  | Block            |
| Critical regression failure           | Block            |
| Unverified critical remediation       | Block            |
| Critical migration risk               | Block            |
| High-risk P1 with no mitigation       | Block            |
| High-risk P1 with verified mitigation | Review           |
| Medium P2 debt                        | Usually Release  |
| Low P3 debt                           | Release          |
| Documented accepted risk              | Review           |

This is a default governance model, not a substitute for project-specific risk assessment.

---

# 18.43 Release Status

The release may use:

```text
READY
READY WITH ACCEPTED RISKS
CONDITIONALLY READY
NOT READY
BLOCKED
```

A release should not be marked `READY` when a mandatory gate remains unresolved.

---

# 18.44 Release Readiness Record

Recommended template:

```text
Release:
vX.Y.Z

Critical P0:
0

Critical Security Findings:
0

Critical Regression Failures:
0

Open P1:
X

Open P2:
X

Open P3:
X

Accepted Risks:
X

Blocked Items:
X

Verification Status:
PASS / FAIL

Architecture Review:
PASS / N/A

Dependency Review:
PASS / N/A

Deployment Verification:
PASS / FAIL

Release Decision:
READY / CONDITIONAL / BLOCKED

Approved By:
[Name / Role]

Date:
[Date]
```

Actual values must come from release evidence.

---

# 18.45 Technical Debt Exit Criteria

A technical-debt phase should not be considered complete simply because planned code changes were implemented.

The phase should exit only when:

```text
[ ] Planned P0 debt resolved
[ ] Critical P1 debt resolved or formally accepted
[ ] Required regression protection added
[ ] Architecture changes documented
[ ] Security verification complete
[ ] Dependencies stabilized
[ ] Documentation synchronized
[ ] Remaining debt re-prioritized
[ ] Next-phase debt identified
```

---

# 18.46 Refactoring Exit Criteria

For a major refactoring phase:

```text
[ ] Existing behavior verified
[ ] Refactor completed
[ ] Duplicate logic reduced
[ ] Responsibilities clarified
[ ] Dependencies reviewed
[ ] Tests pass
[ ] No new critical debt introduced
[ ] Architecture documentation updated
[ ] Performance impact assessed
```

---

# 18.47 Stabilization Phase Exit Criteria

For a stabilization phase:

```text
[ ] Critical defects addressed
[ ] Error handling standardized
[ ] Data integrity verified
[ ] Core workflows tested
[ ] Security risks reviewed
[ ] Logging reviewed
[ ] Deployment verified
[ ] Remaining debt documented
```

---

# 18.48 Commercial Readiness Exit Criteria

Before commercial deployment, the project should target:

```text
[ ] No open P0 debt
[ ] No unresolved critical security vulnerability
[ ] No critical regression failure
[ ] Core workflows covered by tests
[ ] Dependency state reproducible
[ ] Deployment process reproducible
[ ] Architecture documented
[ ] Configuration documented
[ ] Known risks documented
[ ] Support-impacting debt documented
[ ] Release rollback strategy considered
```

Commercial readiness is a risk threshold, not a claim that the codebase contains zero technical debt.

---

# 18.49 No-Zero-Debt Principle

AIPM should not pursue the unrealistic objective of eliminating all technical debt.

The correct objective is:

```text
Uncontrolled Debt
       ↓
Visible Debt
       ↓
Prioritized Debt
       ↓
Managed Debt
       ↓
Acceptable Engineering Risk
```

Some low-priority debt may remain permanently if its remediation cost exceeds its practical value.

The important condition is that the debt is understood and intentionally managed.

---

# 18.50 Debt Acceptance vs Debt Avoidance

The project should distinguish between:

```text
Accepted Debt
```

and:

```text
Ignored Debt
```

Accepted debt has:

```text
Known Risk
Owner
Reason
Mitigation
Review Condition
```

Ignored debt has none of these.

Therefore:

```text
Accepted Debt = Managed Risk

Ignored Debt = Uncontrolled Risk
```

---

# 18.51 Quality Gate Summary

The complete technical-debt quality gate is:

```text
             DEBT REMEDIATION
                    │
                    ▼
             ROOT CAUSE FIXED?
                /        \
              NO          YES
              │             │
            Reject          ▼
                       TESTS PASS?
                       /        \
                     NO          YES
                     │             │
                   Reject          ▼
                             SECURITY CHECK
                                  │
                                  ▼
                            ARCHITECTURE CHECK
                                  │
                                  ▼
                            DOCUMENTATION CHECK
                                  │
                                  ▼
                              VERIFICATION
                                  │
                                  ▼
                             EVIDENCE RECORDED
                                  │
                                  ▼
                                CLOSED
```

---

# 18.52 Release Gate Summary

```text
             RELEASE CANDIDATE
                    │
                    ▼
               P0 = 0?
              /       \
            NO         YES
            │            │
          BLOCK          ▼
                    SECURITY PASS?
                    /          \
                  NO            YES
                  │               │
                BLOCK             ▼
                             REGRESSION PASS?
                             /            \
                           NO              YES
                           │                 │
                         BLOCK               ▼
                                      ARCHITECTURE OK?
                                      /           \
                                    NO             YES
                                    │                │
                                  REVIEW              ▼
                                             DEPLOYMENT OK?
                                             /          \
                                           NO            YES
                                           │               │
                                         BLOCK             ▼
                                                     RISK REVIEW
                                                          │
                                                          ▼
                                                       RELEASE
```

---

# 18.53 Acceptance Evidence Standard

Evidence should be proportional to the risk.

### P0

```text
Required:
Implementation Evidence
Test Evidence
Security Evidence where applicable
Independent Review where practical
Release Evidence
```

### P1

```text
Required:
Implementation Evidence
Test Evidence
Review Evidence
Verification Evidence
```

### P2

```text
Required:
Implementation Evidence
Relevant Test / Review Evidence
```

### P3

```text
Required:
Appropriate Engineering Verification
```

---

# 18.54 Evidence Quality

Evidence should be:

```text
Relevant
Specific
Reproducible
Traceable
Current
Understandable
```

Weak evidence:

```text
"Looks good."
"Tested."
"Fixed."
"Working now."
```

Strong evidence:

```text
"Regression test suite completed successfully;
affected workflow passes expected validation and
the original failure condition is no longer reproducible."
```

---

# 18.55 Technical Debt Closure Checklist

Before closing any significant debt:

```text
[ ] TD-ID confirmed
[ ] Original problem confirmed
[ ] Root cause reviewed
[ ] Scope completed
[ ] Code reviewed
[ ] Tests updated
[ ] Tests passed
[ ] Security reviewed where applicable
[ ] Architecture reviewed where applicable
[ ] Performance reviewed where applicable
[ ] Documentation reviewed
[ ] Verification performed
[ ] Evidence recorded
[ ] Related work linked
[ ] Release identified
[ ] Status changed to Closed
```

---

# 18.56 Release Readiness Checklist

Before major release:

```text
[ ] TECH_DEBT.md reviewed
[ ] P0 = 0
[ ] Critical security risk = 0
[ ] Critical regression failures = 0
[ ] P1 reviewed
[ ] P2/P3 reviewed
[ ] Accepted risks documented
[ ] Test evidence reviewed
[ ] Architecture reviewed
[ ] Dependency state reviewed
[ ] Deployment verified
[ ] Documentation synchronized
[ ] Release decision recorded
```

---

# 18.57 Relationship With Other Project Documents

The acceptance and release rules should remain synchronized with:

```text
PROJECT_STATUS.md
        │
        ├── Current Project Condition
        │
        ▼
ARCHITECTURE.md
        │
        ├── Actual System Structure
        │
        ▼
TECH_DEBT.md
        │
        ├── Risks
        ├── Acceptance Criteria
        └── Release Gates
        │
        ▼
NEXT_PHASE_ROADMAP.md
        │
        ├── Planned Remediation
        │
        ▼
Implementation
        │
        ▼
Testing
        │
        ▼
Verification
        │
        ▼
Release
```

No document should claim a condition that contradicts verified project evidence.

---

# 18.58 Auditability Requirement

Every significant technical-debt decision should be explainable after the fact.

An engineer reviewing the project later should be able to determine:

```text
Why was this debt created?
Why was it prioritized?
Who owned it?
What changed?
How was it tested?
Why was it considered resolved?
When was it released?
Was the risk actually eliminated?
```

If these questions cannot be answered, the debt-management process is incomplete.

---

# 18.59 Section 18 Completion Criteria

Section 18 is considered operationally complete when the project has:

```text
[ ] Technical Debt Acceptance Criteria
[ ] Definition of Done
[ ] Definition of Resolved
[ ] Definition of Closed
[ ] Reopening Criteria
[ ] Security Acceptance Rules
[ ] Testing Acceptance Rules
[ ] Architecture Acceptance Rules
[ ] Performance Acceptance Rules
[ ] Documentation Acceptance Rules
[ ] Deployment Acceptance Rules
[ ] Release Readiness Gates
[ ] Risk Acceptance Rules
[ ] Release Decision Model
[ ] Closure Checklist
```

---

# 18.60 Section 18 Conclusion

Technical debt must never be considered resolved merely because a developer changed the affected code.

AIPM should use the following standard:

```text
Understand
   ↓
Fix
   ↓
Test
   ↓
Review
   ↓
Verify
   ↓
Document
   ↓
Record Evidence
   ↓
Release Assessment
   ↓
Close
```

The most important distinction is:

> A technical-debt item is not closed when the code is changed; it is closed when the engineering risk has been addressed and the resolution has been verified.

The release principle is equally important:

> A release is ready when its remaining technical debt is known, assessed, mitigated where necessary, and explicitly accepted—not when the project happens to have zero technical debt.

The complete AIPM technical-debt management lifecycle is now:

```text
SECTION 1–3
Foundation
        ↓
SECTION 4–6
Debt Identification & Classification
        ↓
SECTION 7–10
Risk / Quality / Maintainability Analysis
        ↓
SECTION 11–12
Dependency & Refactoring Debt
        ↓
SECTION 13
Priority Matrix
        ↓
SECTION 14–15
Remediation & Tracking
        ↓
SECTION 16
Debt Register
        ↓
SECTION 17
Audit, Governance & Compliance
        ↓
SECTION 18
Acceptance, Definition of Done & Release Readiness
```

This establishes the complete control loop:

```text
IDENTIFY
   ↓
CLASSIFY
   ↓
ASSESS
   ↓
PRIORITIZE
   ↓
PLAN
   ↓
REMEDIATE
   ↓
TEST
   ↓
VERIFY
   ↓
AUDIT
   ↓
ACCEPT
   ↓
RELEASE
   ↓
REASSESS
```

This section therefore forms the final quality and release-control layer of `TECH_DEBT.md`.
