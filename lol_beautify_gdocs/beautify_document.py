import re
from lol_beautify_gdocs.gdocs_utils import get_document_id, get_service
from static_data import ddragon
from lol_beautify_gdocs.hardcoded_variables import other_pictures_dict

dd = ddragon.ddragon()


def beautify_document(document_descriptor: str):
    """
    Parameter
    ----------
    document : str
        url or id of the document; must have write access by the authenticated user
    """
    service = get_service()

    document_id = get_document_id(document_descriptor)

    document = service.documents().get(documentId=document_id).execute()
    content = document.get('body').get('content')

    images_requests = []
    tags_removal_requests = []
    # Regex catching numbers into <...>
    tag_regex = re.compile('[0-9]+<.*?>')

    for section in content:
        if 'paragraph' not in section:
            continue
        for element in section['paragraph']['elements']:
            try:
                element_content = element.get('textRun').get('content')
            # This is super dirty but working for the current use case
            except AttributeError:
                continue

            for match in tag_regex.finditer(element_content):
                match_content = match[0]
                match_position = element.get('startIndex') + match.span()[0]

                images_requests.append(create_image_request(match_content, match_position))

                tags_removal_requests.append(create_tag_removal_request(match_content))

    # We sort the image requests in descending position to make sure the insertions are in the right positions.
    images_requests.sort(key=lambda x: x.get('insertInlineImage').get('location').get('index'), reverse=True)

    # Execute the request.
    body = {'requests': images_requests + tags_removal_requests}
    response = service.documents().batchUpdate(documentId=document_id, body=body).execute()


def create_image_request(match_content, match_position):
    # This splits on < and removes the last character which should be >
    # For example, for '20<Braum>', object_name will be 'Braum' and size will be 20
    # The replace statement is here to make sure the typographical apostrophe ’ is properly handled
    object_name = match_content.split('<')[1][:-1].replace('’', "'")
    size = int(match_content.split('<')[0])

    if object_name in dd.championByName.keys():
        uri = dd.getChampion(object_name).image
    elif object_name in other_pictures_dict:
        uri = other_pictures_dict[object_name]
    elif object_name in dd.itemByName.keys():
        uri = dd.getItem(object_name).image

    return {
        'insertInlineImage': {
            'location': {
                'index': match_position
            },
            'uri': uri,
            'objectSize': {
                'height': {
                    'magnitude': size,
                    'unit': 'PT'
                },
                'width': {
                    'magnitude': size,
                    'unit': 'PT'
                }
            }
        }
    }


def create_tag_removal_request(match_content):
    return {
        'replaceAllText': {
            'containsText': {
                'text': match_content,
                'matchCase': 'true'
            },
            'replaceText': None,
        }}
