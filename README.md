# ⚡ CampusAI EnergyWise
### *AI-Powered Campus Energy Optimization & Sustainability System*

[![1M1B Internship](https://img.shields.io/badge/1M1B-AI%20for%20Sustainability-green.svg)](https://1m1b.org)
[![Collaboration](https://img.shields.io/badge/Collaboration-IBM%20SkillsBuild%20%7C%20AICTE-blue.svg)](https://skillsbuild.org)
[![SDG 7](https://img.shields.io/badge/SDG-7%20Affordable%20%26%20Clean%20Energy-orange.svg)](https://sdgs.un.org/goals/goal7)
[![SDG 11](https://img.shields.io/badge/SDG-11%20Sustainable%20Cities-yellowgreen.svg)](https://sdgs.un.org/goals/goal11)

---

## 📌 Project Overview

**CampusAI EnergyWise** is an intelligent decision-support platform designed to convert raw building energy readings into plain-language explanations, actionable energy-reduction recommendations, and automated risk alerts. 

By combining numerical anomaly detection with Generative AI (IBM Granite Models via RAG logic) and automated agentic workflows (n8n), the system enables facility managers and sustainability teams to identify energy-use patterns without taking away human operational authority.

---

## 🎯 Sustainable Development Goals (SDGs) Alignment

* 🟧 **Primary — SDG 7: Affordable and Clean Energy**
  * Focuses on Target 7.3: Doubling the rate of improvement in energy efficiency by detecting idle HVAC, laboratory, and lighting energy loads.
* 🟩 **Secondary — SDG 11: Sustainable Cities and Communities**
  * Focuses on Target 11.6: Reducing the per capita environmental impact of educational infrastructure.
* 🟦 **Supporting — SDG 13: Climate Action**
  * Translates measured energy conservation into estimated carbon emission reductions using documented grid factors.

---

## 🛠 System Architecture & Workflow


```

[ CSV / Meter Input ] ──> [ Data Validation ] ──> [ Anomaly Logic ]
│
▼
[ Responsible AI Prompt ] <── [ Feature Normalization ] ──┘
│
▼
[ IBM Granite / AI Model ] ──> [ Actionable Alert ] ──> [ Human Review & Approval ]

```

### ⚡ Key Components

1. **📊 Telemetry Ingestion (`sample_campus_energy_data.csv`)**
   * Pre-structured dataset containing building identifiers, timestamps, occupancy percentages, ambient temperatures, and power consumption (kWh).
2. **🐍 Prediction Prototype (`campusai_energywise_prototype.py`)**
   * Python script that normalizes energy readings, evaluates baseline deviations, and constructs context-aware LLM prompts.
3. **🔄 Automated Workflow (`n8n_campusai_energywise_workflow.json`)**
   * An n8n agentic graph that triggers on incoming webhooks, validates parameters, passes engineered prompts to AI endpoints, and formats report alerts.
4. **📄 Documentation & Presentation**
   * `CampusAI_EnergyWise_1M1B_Submission.pptx` & `CampusAI_EnergyWise_Project_Report.pdf` providing detailed system diagrams and design thinking frameworks.

---

## 🚀 Step-by-Step Demo Guide

To demonstrate the full **CampusAI EnergyWise** pipeline:

1. 📽 **Present the Slide Deck (`.pptx` / `.pdf`)**
   * Introduce the problem statement, SDG mapping, and human-in-the-loop decision framework.
2. 📋 **Examine the Input Dataset (`sample_campus_energy_data.csv`)**
   * Show how energy consumption varies across academic, hostel, and laboratory blocks relative to occupancy and outdoor temperature.
3. 💻 **Execute the Python Anomaly Detector (`campusai_energywise_prototype.py`)**
   * Run the script locally to simulate real-time baseline comparison and prompt generation.
4. ⚙ **Demonstrate the n8n Workflow Graph (`n8n_campusai_energywise_workflow.json`)**
   * Import the JSON into n8n to showcase the pipeline logic: `Webhook Ingestion ➔ Data Normalization ➔ AI Prompt Construction ➔ Model Processing ➔ Recommendation Output`.
5. 🛡 **Highlight Responsible AI & Human Oversight**
   * Emphasize that all AI recommendations act purely as a decision-support layer requiring validation by human facility staff before any building adjustment is made.

---

## 🛡 Responsible AI & Safety Framework

* 🤝 **Human Operational Authority:** AI alerts serve exclusively as a decision-support system. No critical electrical, laboratory, or safety infrastructure is controlled automatically.
* ⚖ **Fairness & Localized Baselines:** Energy anomalies are evaluated against individual building operational footprints rather than applying uniform, biased thresholds across different facility types.
* 🔒 **Privacy Protection:** The platform processes aggregated building-level utility metrics; no individual student or personnel tracking is conducted.
* 🔍 **Transparency:** Recommendations explicitly cite input variables, baseline thresholds, and confidence limits behind every generated warning.

---

## ⚠️ Important Compliance & Usage Notes

* 🧪 **Demonstration Data Notice:** The dataset provided (`sample_campus_energy_data.csv`) is synthetic baseline demonstration data designed to evaluate workflow logic. It does **not** represent live or official institutional meter readings.
* 📉 **No Claimed Savings:** Quantitative outcomes from prototype runs demonstrate system capability only; no actual energy or financial savings are claimed without real-world meter integration.
* 🔑 **API Key Security:** The included n8n JSON graph uses placeholders for API credentials. Ensure all endpoint URLs and keys are kept in environment variables rather than committed directly to public repositories.

---

## 📂 File Directory


```

📁 CampusAI-EnergyWise/
├── 📄 README.md                                  # Project Documentation
├── 📊 sample_campus_energy_data.csv              # Synthetic Baseline Dataset
├── 🐍 campusai_energywise_prototype.py           # Anomaly Detection & Prompt Script
├── ⚙️ n8n_campusai_energywise_workflow.json     # Agentic Automation Workflow
├── 📊 CampusAI_EnergyWise_1M1B_Submission.pptx   # Final Presentation Deck
└── 📑 CampusAI_EnergyWise_Project_Report.pdf     # Full Internship Report

```

---

## 👤 Author & Acknowledgments

* **Developer:** Shwetanjali Gautam
* **Institution:** Birla Institute of Technology, Mesra
* **Program:** 1M1B AI for Sustainability Virtual Internship
* **In Collaboration With:** IBM SkillsBuild & AICTE

```

---

