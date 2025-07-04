import requests
import argparse
from urllib.parse import urljoin

BASE_URL = "http://localhost:3000"  # Ganti dengan URL server Anda

def upload_file(filename):
    try:
        with open(filename, 'rb') as f:
            response = requests.post(
                urljoin(BASE_URL, "/upload"),
                files={'file': f},
                timeout=10
            )
            print(response.text)
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan!")
    except Exception as e:
        print(f"Error: {str(e)}")

def list_files():
    try:
        response = requests.get(urljoin(BASE_URL, "/api/files"), timeout=5)
        if response.status_code == 200:
            files = response.json().get('files', [])
            if files:
                print("=== Daftar File ===")
                for file in files:
                    print(f"- {file} (URL: {BASE_URL}/public/{file})")
            else:
                print("Belum ada file yang diupload.")
        else:
            print(f"Error: Server merespons dengan kode {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='RakitWeb CLI Tool')
    subparsers = parser.add_subparsers(dest='command', required=True)

    upload_parser = subparsers.add_parser('upload', help='Upload file')
    upload_parser.add_argument('filename', help='Nama file')

    subparsers.add_parser('list', help='List semua file')

    args = parser.parse_args()

    if args.command == 'upload':
        upload_file(args.filename)
    elif args.command == 'list':
        list_files()

if __name__ == "__main__":
    main()
