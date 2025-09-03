# Flowscribe Project Checklist (Build & Professional)

## Core Project Structure
- [x] `README.md` (badges, install, usage, contributing)
- [x] `LICENSE` (MIT)
- [x] Source code in `flowscribe/`
- [x] Tests in `tests/`
- [x] `.autodev/ra.yaml`, `.autodev/flows.yaml` (config/catalog)
- [x] `.autodev/copilot_init.md` (Copilot init)
- [x] `CHECKLIST.md` (this file)

## Core Functionality
- [x] Basic event/flow/session classes
- [x] Console, JSONL, and SQLite sinks
- [x] Artifact writers (`summary.md`, `ask.md`, `trace.jsonl`)
- [x] Config loading and environment overrides
- [x] Flow catalog integration
- [x] Redaction and payload limits
- [x] CLI and Python API entry point
- [x] Example usage and test flows

## Documentation & Community
- [x] Documentation polish and badges
- [ ] `CHANGELOG.md` (release notes/version history)
- [ ] `CONTRIBUTING.md` (contribution guidelines)
- [ ] `CODE_OF_CONDUCT.md` (community standards)
- [ ] Contact/support info in README or separate file

- [x] CI configuration (e.g., GitHub Actions for tests/linting)
- [x] Badges for CI status, coverage, etc. (if CI is set up)
- [ ] Issue and PR templates (for GitHub community health)
+- [x] Issue and PR templates (for GitHub community health)
- [x] `pyproject.toml` for packaging and dependencies
- [x] `.gitignore` (ignore `.pyc`, `.env`, `.autodev/trace.jsonl`, etc.)
- [x] More tests (covering edge cases, sinks, privacy, etc.)
- [x] CI configuration (e.g., GitHub Actions for tests/linting)
- [ ] Badges for CI status, coverage, etc. (if CI is set up)
- [ ] Issue and PR templates (for GitHub community health)
- [ ] Documentation site or docs folder (for larger projects)

## VS Code & Copilot
- [x] VS Code/Copilot integration tips
