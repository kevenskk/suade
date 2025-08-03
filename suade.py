from lxml import etree
from pathlib import Path
import sys

schema_path = './schema/FSA029-Schema.xsd'
samples = ['./sample/FSA029-Sample-Full.xml', './sample/FSA029-Sample-Valid.xml']


class schemaResolver(etree.Resolver):

    def __init__(self, path): 
        super().__init__()
        self.path= path

    def resolve(self, url, pubid, context): # resolve include by rebuilding path string to CommonTypes.xsd
        try:
            schemaFile_name = Path(url).name
            resolvedPath = Path(self.path).parent / schemaFile_name

            if not resolvedPath.exists():
                print(f"{schemaFile_name} not found: {resolvedPath}")
                return None

            return self.resolve_filename(str(resolvedPath), context)

        except Exception as e:
            print(f"Error resolving {url}: {e}")
            return None


def validateXML(XML_file):
    parser = etree.XMLParser(no_network=True) 
    parser.resolvers.add(schemaResolver(schema_path))

    schema_doc = etree.parse(schema_path, parser) # parse schema file with custom resolver
    xmlschema = etree.XMLSchema(schema_doc)
    try:
        xml_doc = etree.parse(XML_file)
        xmlschema.assertValid(xml_doc) ## assertValid returns exception if invalid, and is caught by except block
        print(f"{XML_file} is valid, schema validation successful.")
    
    ## error handling
    except etree.DocumentInvalid as e: 
        print(f"{XML_file} is invalid: {e}")
    except etree.XMLSyntaxError as e:  
        print(f"XML syntax error in {XML_file}: {e}")
    except etree.XMLSchemaParseError as e:
        print(f"Schema parse error in {XML_file}: {e}")
    except FileNotFoundError as e: 
        print(f"File not found: {XML_file}: {e}")


if len(sys.argv) < 2:
        print("Usage:\n  python suade.py ./sample/file.xml")
        print("Usage:\n  python suade.py --all")

else:
    if sys.argv[1] == '--all':
        for sample in samples:
            validateXML(sample)
    else:
        validateXML(sys.argv[1])
