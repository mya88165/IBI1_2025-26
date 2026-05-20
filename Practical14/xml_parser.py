from xml.dom import minidom
import xml.sax
from datetime import datetime

# DOM METHOD

def dom_method(filename):
    start_time = datetime.now()

    # Read the XML file using DOM
    doc = minidom.parse(filename)

    # Get every <term> element
    terms = doc.getElementsByTagName("term")

    # Store best result for each namespace
    results = {
        "molecular_function": ["", "", 0],
        "biological_process": ["", "", 0],
        "cellular_component": ["", "", 0]
    }

    # Go through every GO term
    for term in terms:
        id_tags = term.getElementsByTagName("id")
        name_tags = term.getElementsByTagName("name")
        namespace_tags = term.getElementsByTagName("namespace")
        is_a_tags = term.getElementsByTagName("is_a")

        # Only continue if the important tags exist
        if len(id_tags) > 0 and len(name_tags) > 0 and len(namespace_tags) > 0:
            go_id = id_tags[0].firstChild.nodeValue
            name = name_tags[0].firstChild.nodeValue
            namespace = namespace_tags[0].firstChild.nodeValue

            # Count how many <is_a> elements this term has
            is_a_count = len(is_a_tags)

            # If this term has the highest number so far, save it
            if namespace in results:
                if is_a_count > results[namespace][2]:
                    results[namespace] = [go_id, name, is_a_count]

    end_time = datetime.now()
    time_taken = end_time - start_time

    return results, time_taken

# SAX METHOD

class GOHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_tag = ""

        self.go_id = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0

        self.results = {
            "molecular_function": ["", "", 0],
            "biological_process": ["", "", 0],
            "cellular_component": ["", "", 0]
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag

        # Reset values when a new term starts
        if tag == "term":
            self.go_id = ""
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0

        # Count each <is_a> tag
        if tag == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        # Add text content to the correct variable
        if self.current_tag == "id":
            self.go_id += content

        elif self.current_tag == "name":
            self.name += content

        elif self.current_tag == "namespace":
            self.namespace += content

    def endElement(self, tag):
        # When the term ends, check if it is the biggest so far
        if tag == "term":
            if self.namespace in self.results:
                if self.is_a_count > self.results[self.namespace][2]:
                    self.results[self.namespace] = [
                        self.go_id,
                        self.name,
                        self.is_a_count
                    ]

        self.current_tag = ""


def sax_method(filename):
    start_time = datetime.now()

    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(filename)

    end_time = datetime.now()
    time_taken = end_time - start_time

    return handler.results, time_taken

filename = "go_obo.xml"

dom_results, dom_time = dom_method(filename)
sax_results, sax_time = sax_method(filename)


print("DOM RESULTS")

for namespace, result in dom_results.items():
    print("Namespace:", namespace)
    print("GO ID:", result[0])
    print("Name:", result[1])
    print("Number of is_a elements:", result[2])
    print()

print("DOM time taken:", dom_time)
print()


print("SAX RESULTS")

for namespace, result in sax_results.items():
    print("Namespace:", namespace)
    print("GO ID:", result[0])
    print("Name:", result[1])
    print("Number of is_a elements:", result[2])
    print()

print("SAX time taken:", sax_time)
print()


# Fastest method:
# After running the code, compare DOM time and SAX time.
