# Operations Engine - Documentation Standards

## 1. Trigger
Executed by the **SOP Manager** when writing or updating any operational document in the repository.

## 2. Standard SOP Markdown Template
Every SOP in the repository must use the following standard markdown layout:
- **Title**: Use a single `#` header with the name of the Engine and file name.
- **Section 1: Trigger**: Define the exact event, cadence, or decision that initiates this SOP.
- **Section 2: Steps**: Numbered, logical steps outlining who does what.
- **Section 3: Quality Check / Metrics**: Explain how to verify that the steps were executed correctly.

## 3. Formatting Principles
- **No Placeholders**: Do not leave dummy text, template variables (unless clearly marked with bracket brackets), or incomplete checklists.
- **Clickable File Links**: All file references within documentation must be formatted as clickable markdown links (e.g. `[discovery-sop.md](file:///path/to/discovery-sop.md)`).
- **Clear Tone**: Write instructions in a crisp, direct, imperative tone. Avoid corporate jargon.
