import phonenumbers
from phonenumbers import geocoder, carrier

def lookup_phone(number):
    try:
        parsed = phonenumbers.parse(number, None)
        location = geocoder.description_for_number(parsed, 'en')
        provider = carrier.name_for_number(parsed, 'en')
        return {
            "Number": number,
            "Location": location,
            "Carrier": provider,
            "Valid": phonenumbers.is_valid_number(parsed)
        }
    except Exception as e:
        return {"error": str(e)}
