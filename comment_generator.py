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
        topicId = o["_id"]
        collections.append(topicId)
    res = []
    for x in collections:
        res.append({"topicId": str(x), "message": "test", "userDssId": "1B31D89048FAF0AAE276E2918F60DD27", "dateCreated": 1531302165055.0})
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
