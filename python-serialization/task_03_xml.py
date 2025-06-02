#!/usr/bin/env python3
"""Module to serialize and deserialize a dictionary using XML format."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    Args:
        dictionary (dict): Data to serialize.
        filename (str): Output XML file.
    """
    root = ET.Element("data")
    for k, v in dictionary.items():
        elem_dict = ET.SubElement(root, k)
        elem_dict.text = str(v)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and return it as a Python dictionary.
    Args:
        filename (str): XML file to read.
    Returns:
        dict: Reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}
    for elem in root:
        new_dict[elem.tag] = elem.text

    return new_dict
