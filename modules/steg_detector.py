from stegano import lsb
from PIL import Image
from PIL.ExifTags import TAGS

def extract_hidden_message(image_path):

    try:
        secret = lsb.reveal(image_path)

        if secret:
            return secret
        else:
            return "No hidden message detected."

    except:
        return "Unable to analyze image."


def extract_metadata(image_path):

    metadata = {}

    try:

        image = Image.open(image_path)

        exifdata = image.getexif()

        for tag_id in exifdata:

            tag = TAGS.get(tag_id, tag_id)

            data = exifdata.get(tag_id)

            metadata[tag] = data

        return metadata

    except:
        return {}