# Webex Contact Center Flow Templates

Official Repository for Sample Webex Contact Center Flow Templates that are usable on Flow Designer

# Contributing to Webex Contact Center Flow Templates

Welcome to the `webex-contact-center-flows` repository! 🚀  
This repo contains a curated collection of ready-to-use Flow Templates for Webex Contact Center. 

We welcome external contributions to grow this library.

---

## 📁 Contribution Scope

Our primary contribution area is **adding new Flow Templates**.  
Each new template must follow the existing structure and documentation format.

---

## 🧩 Contribution Steps

### 1. **Fork the Repository**

Start by forking this repo / creating a new branch if you're an admin. Work on your template feature or fix in a branch in your forked copy.  
**Direct pushes to `main` are not allowed.**

### 2. **Create Your Template Folder**

- Follow the naming convention: use **snake-case** and **include the word `template`**.  
  - For example: `my-new-flow-template`, or `subflow-sample-template`
- Inside your folder, add:
  - `YourTemplate_Template.json` – with activity-level descriptions.
  - `template-body-filled.json` – filled template body file.
  - `README.md` – using the required format (see below).
  - Optional:
    - `assets/` folder – if you have images, Postman collections, or supporting documents.

### 3. **Document with `README.md`**

Use the canonical structure from [`simple-inbound-template/README.md`](./simple-inbound-template/README.md) as reference.

Your README **must include** the following sections:

```markdown
# <Marketing Title>

## Name
<Marketing Title Again>

## Labels
<Use relevant labels similar to existing flows>

## Description
<Brief overview of what this template does>

## Details

**Key Features:**
- Feature 1
- Feature 2

### Pre-requisites
- List any setup needed (e.g., enable APIs, integrations

```

- After you're done, push it to your branch / confirm the repo.
- Reach out to a member in the Flow Team to push the template assets into production / across DCs.

> **Important:** We are assuming that the template creator has fully tested their templates, and will post the assets as is.