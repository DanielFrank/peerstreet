from flask import Flask, jsonify
import re
from zip_dma.model.map.cbsa_msa_id_map import CbsaMsaIdMap
from zip_dma.model.map.msa_map import MsaMap
from zip_dma.model.map.zip_cbsa_map import ZipCbsaMap

#TODO make year(s) obtained configurable

app = Flask(__name__)
cbsa_msa_id_map = CbsaMsaIdMap.get_map()
msa_map = MsaMap.get_map()
zip_cbsa_map = ZipCbsaMap.get_map()
ZIP_REGEX = "^\d{5}$"

@app.route("/zipToDMA/<zip_code>")
def zip_to_dma(zip_code):
    result = empty_result()
    if not check(zip_code):
        return error_message("Zip code must be 5 digits")
    result["Zip"] = zip_code
    cbsa = zip_cbsa_map.get(zip_code)
    if cbsa == "99999":
        return return_result(result)
    result["CBSA"] = cbsa
    msa_id = cbsa_msa_id_map.get(cbsa)
    if msa_id is None:
        return return_result(result)
    msa = msa_map.get(msa_id)
    if msa is None:
        return return_result(result)
    result["MSA"] = msa.msa_name
    result["Pop2014"] = msa.get_population("2014")
    result["Pop2015"] = msa.get_population("2015")
    return return_result(result)

def check(zip_code):
    match = re.search(ZIP_REGEX, zip_code)
    return match is not None

def return_result(result):
    return jsonify(result)

def error_message(msg):
    return jsonify({"error": msg})


def empty_result():
    return {
        "Zip": "",
        "CBSA": "99999",
        "MSA": "N/A",
        "Pop2014": "N/A",
        "Pop2015": "N/A"
        
    }

