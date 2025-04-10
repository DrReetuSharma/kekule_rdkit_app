# 🧪 MolSketch Analyzer - Kekule + RDKit App

MolSketch Analyzer is an intuitive web-based cheminformatics tool that empowers users to **draw molecules in 2D** and instantly **analyze their molecular properties** using RDKit. The application leverages **Kekule.js** for sketching and **RDKit** for cheminformatics computations, providing a seamless experience for researchers, students, and data scientists working in drug discovery and molecular design.

---

## 🎯 Key Features

1. ✏️ **2D Molecular Sketching**  
   - Interactive sketch pad powered by Kekule.js  
   - Supports atoms, bonds, rings, and advanced molecular structures

2. 🧠 **Property Prediction via RDKit**  
   - Instant calculation of key physicochemical properties:
     - Molecular weight
     - LogP
     - Number of hydrogen bond donors/acceptors
     - Topological polar surface area (TPSA)
     - Number of rotatable bonds

3. 📋 **SMILES Conversion & Analysis**  
   - Converts sketched molecules to SMILES  
   - Real-time analysis from a browser with no installations

4. 📦 **Lightweight & Containerized**  
   - Ready for deployment as a Flask-based app  
   - Dockerized for easy integration into workflows

---

## 🚀 Impact

MolSketch Analyzer can:

- Accelerate **lead optimization** and **drug design** in early-stage discovery
- Serve as an **educational tool** for teaching molecular properties and cheminformatics
- Assist in **high-throughput screening** when paired with automated input systems
- Be embedded into **larger knowledge graph or AI-driven platforms** for molecular analytics

---

## ⚠️ Limitations

- Currently supports **basic property analysis only** (e.g., no QSAR, docking, or 3D visualization)
- Kekule.js drawing is 2D only – **no 3D conformer generation**
- Not optimized for batch analysis (one molecule at a time)
- Requires RDKit Python backend – hosting must support scientific Python stack

---

## 🛠️ Tech Stack

- **Frontend:** HTML5 + Kekule.js
- **Backend:** Python, Flask, RDKit
- **Containerization:** Docker
- **Deployment Ready:**AZURE**

---

## 📷 Screenshot

*(You may insert a UI screenshot here once available)*

---

## 🧪 Example Use

1. Draw a molecule like benzene
2. Click "Analyze"
3. Receive output:

#### Contact: sharmar@aspire10x.com or support@aspire10x.com