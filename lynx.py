import argparse
from modules import instagram, phone_lookup, ip_geolocation

parser = argparse.ArgumentParser(description="Lynx OSINT Tool")

parser.add_argument("--instagram", help="Cari info akun Instagram")
parser.add_argument("--phone", help="Lacak info nomor HP")
parser.add_argument("--ip", help="Geolokasi berdasarkan alamat IP")

args = parser.parse_args()

if args.instagram:
    result = instagram.lookup_instagram(args.instagram)
    print(result)

if args.phone:
    result = phone_lookup.lookup_phone(args.phone)
    print(result)

if args.ip:
    result = ip_geolocation.geolocate_ip(args.ip)
    print(result)
