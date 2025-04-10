from flask import Flask, request, jsonify, render_template, Response
import csv
from rdkit import Chem
from rdkit.Chem import Descriptors

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/process_molecule', methods=['POST'])
def process_molecule():
    data = request.json
    mol_data = data.get('mol')

    try:
        mol = Chem.MolFromMolBlock(mol_data)
        if mol is None:
            return jsonify({"error": "Invalid molecule"}), 400
        
        mol_weight = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        tpsa = Descriptors.TPSA(mol)
        h_donors = Descriptors.NumHDonors(mol)
        h_acceptors = Descriptors.NumHAcceptors(mol)
        rotatable_bonds = Descriptors.NumRotatableBonds(mol)
        smiles = Chem.MolToSmiles(mol)

        # Lipinski's Rule of 5 Evaluation
        lipinski_violations = sum([
            mol_weight > 500,
            logp > 5,
            h_donors > 5,
            h_acceptors > 10
        ])
        lipinski_pass = lipinski_violations == 0

        result = {
            "Molecular Weight": mol_weight,
            "LogP": logp,
            "Topological Polar Surface Area (TPSA)": tpsa,
            "Hydrogen Donors": h_donors,
            "Hydrogen Acceptors": h_acceptors,
            "Rotatable Bonds": rotatable_bonds,
            "SMILES": smiles,
            "Lipinski Rule of 5 Passed": lipinski_pass,
            "Lipinski Violations": lipinski_violations
        }

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download_csv', methods=['POST'])
def download_csv():
    data = request.json
    mol_data = data.get('mol')

    try:
        mol = Chem.MolFromMolBlock(mol_data)
        if mol is None:
            return jsonify({"error": "Invalid molecule"}), 400
        
        mol_weight = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        tpsa = Descriptors.TPSA(mol)
        h_donors = Descriptors.NumHDonors(mol)
        h_acceptors = Descriptors.NumHAcceptors(mol)
        rotatable_bonds = Descriptors.NumRotatableBonds(mol)
        smiles = Chem.MolToSmiles(mol)

        # Lipinski's Rule of 5 Evaluation
        lipinski_violations = sum([
            mol_weight > 500,
            logp > 5,
            h_donors > 5,
            h_acceptors > 10
        ])
        lipinski_pass = lipinski_violations == 0

        csv_data = [
            ["Molecular Weight", mol_weight],
            ["LogP", logp],
            ["Topological Polar Surface Area (TPSA)", tpsa],
            ["Hydrogen Donors", h_donors],
            ["Hydrogen Acceptors", h_acceptors],
            ["Rotatable Bonds", rotatable_bonds],
            ["SMILES", smiles],
            ["Lipinski Rule of 5 Passed", lipinski_pass],
            ["Lipinski Violations", lipinski_violations]
        ]

        def generate_csv():
            yield '\n'.join([','.join(map(str, row)) for row in csv_data])

        return Response(generate_csv(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=molecule_properties.csv"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
