#!/usr/local/bin/python
# -*- encoding=utf-8 -*-

from optparse import OptionParser
import json


def parser(file_path):
    with open(file_path, "rb") as f:
        text = f.readlines()
        json_text = json.loads("".join(text))
        print "there are", len(json_text), "total objects"
    return json_text


def transformer(json_text):
    collections = []
    for o in json_text:
        name = o["name"]
        project_id = o["projectId"]
        target_id = o["target"]["id"]
        view_media = int(o["target"]["viewMedia"])
        if (view_media & 0x0800 == 0) and (view_media & 0x2000 == 0):
            collections.append((name, project_id, target_id, view_media))
    print "there are", len(collections), "filtered results, which are all not dossier"
    res = []
    for x in collections:
        res.append({"topicDssId": str(x[1] + ":" + x[2] + ":K3"), "name": str(x[0]), "dateModified": 1531302179204.0})
    return res


def write_result(data, output_file):
    with open(output_file, "wb") as f:
        for d in data:
            f.write(str(d).replace("'", "\"") + "\n")


def main():
    option_parser = OptionParser()
    option_parser.add_option("-i", "--input", dest="input_file", help="input json file")
    option_parser.add_option("-o", "--output", dest="output_file", help="output json for mongodb")
    (options, args) = option_parser.parse_args()
    text = transformer(parser(options.input_file))
    write_result(text, options.output_file)


if __name__ == "__main__":
    main()
