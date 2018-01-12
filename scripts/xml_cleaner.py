'''
Script will take a list of xml files (downloaded from USPTO bulk data storage site)
and clean unwanted <!DOCTYPE...> and extra <?xml...?> lines from the file.
'''
import re

file_names = ['test1.xml','ipgb20171226.xml']

def patent_xml_cleaner(file_list):
    doctype_pattern = re.compile('^<!DOCTYPE.*>$')
    xmltag_pattern = re.compile('^<\?xml.*>$')

    for xml_file in file_names:
        raw_file_path = '../raw_data/' + xml_file
        clean_file_path = '../clean_data/clean_' + xml_file
        with open(raw_file_path, 'r') as f1:
            with open(clean_file_path, 'w') as f2:
                f2.write('<?xml version="1.0"?>' + '\n')
                f2.write('<us-patent-grants>' + '\n')
                for line in f1:
                    if not bool(doctype_pattern.match(line)) and not bool(xmltag_pattern.match(line)):
                        f2.write(line)
                f2.write('\n' + '</us-patent-grants>')


patent_xml_cleaner(file_names)
