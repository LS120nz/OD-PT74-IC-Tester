Author:
David-k Otter

Project:
OD-PT74 Pico 74xx Logic IC Tester

Documentation Standard:
Version 1.0

# Documentation Style Guide

## Purpose

This document defines the documentation standards used throughout the OD-PT74 repository.

Following a consistent style improves readability, simplifies maintenance, and provides a professional experience for users and contributors.

---

# General Principles

Documentation should be:

- Clear
- Accurate
- Concise
- Consistent
- Friendly
- Technically correct

Assume the reader has basic electronics knowledge but may be unfamiliar with the project.

---

# Document Structure

Where appropriate, documents should follow this structure:

1. Introduction
2. Before You Begin
3. Main Content
4. Notes or Warnings
5. Next Steps

Not every document requires every section, but the overall structure should remain consistent.

---

# Heading Levels

Use Markdown headings consistently.

```text
# Document Title

## Major Section

### Subsection

#### Minor Subsection
```

Only one H1 heading should appear in each document.

---

# File Naming

Use lowercase filenames with hyphens.

Examples:

build-guide.md

usage-guide.md

supported-ics.md

hardware-design-guide.md

Do not use spaces or mixed capitalisation.

---

# Image Naming

Images should use descriptive filenames.

Examples:

figure-01-system-architecture.svg

01-power-supply.jpg

08-post-screen.jpg

Avoid generic names such as:

image1.png

diagram-new.svg

test.jpg

---

# Figure Captions

Use the following format:

Figure 1. Hardware architecture.

Figure 2. Power system.

Do not abbreviate "Figure".

---

# Callouts

Use GitHub Markdown callouts consistently.

NOTE

General information.

TIP

Helpful advice.

IMPORTANT

Information that should not be overlooked.

WARNING

Potential risk or damage.

---

# Terminology

Always use the following project terminology:

Power-On Self Test (POST)

Device Under Test (DUT)

Raspberry Pi Pico

OD-PT74 Pico 74xx Logic IC Tester

Quick Test

Full Test

Soak Test

Avoid introducing alternative names for the same feature.

---

Always use the following names consistently:

Product:
OD-PT74

Full Product Name:
OD-PT74 Pico 74xx Logic IC Tester

Company:
Otter Designs

Hardware:
Rev-C

Firmware:
v1.0.0

---

# Language

Use British English throughout.

Examples:

colour

centre

organisation

initialise

behaviour

maintainable

---

# Writing Style

Prefer:

Short paragraphs

Active voice

Simple language

Consistent terminology

Avoid:

Long paragraphs

Unnecessary repetition

Marketing language

Humour in technical documentation

---

# Lists

Use bullet lists for related items.

Use numbered lists only when order matters.

---

# Tables

Use tables for:

Specifications

Supported ICs

Comparison data

Pin assignments

Avoid using tables for long explanations.

---

# Diagrams

Engineering diagrams should be created as SVG files.

Source files should be stored in:

graphics/source/

Exported PNG files used by the documentation should be stored in:

graphics/exports/

Always edit the SVG source file and regenerate the PNG export. Do not edit exported PNG files directly.

---

# Photos

Use:

Consistent lighting

Neutral background

Square alignment

High resolution

Minimal editing

---

# Versioning

Documentation should match the current project release.

Current release

Hardware: Rev-C
Firmware: v1.0.0

---

# Cross References

Where appropriate, documents should link to related guides.

For example:

Build Guide

Usage Guide

Troubleshooting Guide

Supported ICs

Project Overview

---

# Repository Philosophy

The OD-PT74 repository documents the OD-PT74 Pico 74xx Logic IC Tester. Future Otter Designs projects, such as the OD-ADU, maintain their own documentation and repositories.

Documentation should describe the current hardware and firmware.

Future projects should maintain their own documentation repositories.

Good documentation should enable a first-time builder to assemble, verify and use the OD-PT74 Pico 74xx Logic IC Tester with confidence, while providing sufficient technical detail for future maintenance and community contributions.

## Related Documentation

| Document | Description |
|----------|-------------|
| [🏠 Project Home](../../README.md) | Return to the main project page |
| [📖 Documentation Index](../README.md) | Documentation overview |
