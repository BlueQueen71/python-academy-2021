import os
import sys
import csv
import json
import traceback
from typing import List


def najdi_soubor_json(adresar: str) -> List[str]:
    return [jmeno for jmeno in os.listdir(adresar)
             if os.path.splitext(jmeno)[1] == ".json" and "_" in jmeno]


def uprav_udaj(zamestnanci: List[dict], upravena_jm: list = []) -> List[dict]:
    if not upravena_jm:
        upravena_jm = list()

    for zamestnanec in zamestnanci:
        upravena_jm.append({
            "jmeno": zamestnanec['first_name'],
            "prijmeni": zamestnanec['last_name'],
            "email": zamestnanec['email']
        })
    return upravena_jm


def precti_json(jmeno: str) -> List[dict]:
    try:
        soub_json = open(
            os.path.join("samples", jmeno), "r", encoding="utf-8"
        )
    except FileNotFoundError:
        exc = traceback.format_exc()
        return exc
    else:
        zamestnanci = json.load(soub_json)
        soub_json.close()
        return zamestnanci


def zapis_csv(data: List[dict], soubor: str, i: int):
    try:
        with open(soubor, "a", encoding="utf-8") as csv_out:
            jmena_sloupcu = data[0].keys()
            zapis = csv.DictWriter(csv_out, fieldnames=jmena_sloupcu)

            if not i:
                zapis.writeheader()
                zapis.writerows(data)
            else:
                zapis.writerows(data)

    except KeyError:
        print(sys.exc_info())


if __name__ == "__main__":
    csv_soubor = sys.argv[1]
    upr_zamestnanci = list()

    for index, json_s in enumerate(najdi_soubor_json("samples")):
        zamestnanci= precti_json(json_s)
        upr_udaje = uprav_udaj(zamestnanci)
        zapis_csv(upr_udaje, csv_soubor, index)

