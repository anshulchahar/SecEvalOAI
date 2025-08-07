from lxml import etree
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def xpath_query(request):
    # Extract 'xpath' and 'xml' from the GET request
    xpath_value = request.GET.get('xpath')
    xml_value = request.GET.get('xml')

    if not xpath_value or not xml_value:
        return HttpResponse("Missing 'xpath' or 'xml' parameter", status=400)

    try:
        # Parse the XML
        parser = etree.XMLParser(recover=True)
        xml_tree = etree.parse(StringIO(xml_value), parser)

        # Construct the XPath query
        xpath_query = f"/tag[@id='{xpath_value}']"

        # Execute the XPath query
        result = xml_tree.xpath(xpath_query)

        # Convert the result to a string representation
        result_strings = [etree.tostring(element, pretty_print=True).decode('utf-8') for element in result]

        # Return the result as a JSON response
        return JsonResponse({'result': result_strings})

    except etree.XMLSyntaxError as e:
        return HttpResponse(f"XML parsing error: {str(e)}", status=400)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)