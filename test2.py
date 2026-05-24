import os
from dataclasses import dataclass
import asyncio

folder = os.path.dirname(os.path.abspath(__file__))

@dataclass
class PDFFile:
    name: str
    size_mb: float

class PDFScanner:
    def __init__(self, folder: str) -> None:
        self.folder = folder

    def get_pdf_files(self) -> list[PDFFile]:
        files = []
        for file in os.listdir(self.folder):
            if os.path.isfile(self.folder + "/" + file):
                if file.endswith(".pdf"):
                    size = os.path.getsize(self.folder + "/" + file)
                    mb = size / (1024 * 1024)
                    files.append(PDFFile(name=file, size_mb=mb))
        return files
    
    def scan(self) -> None:
        total = 0
        files = self.get_pdf_files()
        for file in files:
            print(f"{file.name} {file.size_mb:.2f}MB")
            total += file.size_mb
        print(f"total:{total:.2f}MB")

    def count(self) -> int:
        return len(self.get_pdf_files())

async def scan_folder(folder):
        scanner = PDFScanner(folder)
        return scanner.count()

async def scan_main():
    results = await asyncio.gather(
        scan_folder("/Users/shogotsumagari/Desktop/practice_Mac"),
        scan_folder("/Users/shogotsumagari/Desktop"),
    )
    print(results)

asyncio.run(scan_main())

def main():
    PDFApp = PDFScanner(folder)
    try:
        PDFApp.scan()
        pdfcounter = PDFApp.count()
        print(f"PDFの数：{pdfcounter}")
    except FileNotFoundError:
        print("フォルダが見つかません")
    except Exception as e:
        print(f"予期しないエラー：{e}")

if __name__ == "__main__":
    main()