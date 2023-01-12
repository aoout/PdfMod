import fire
import fitz


def toc2file(toc: list, file_path: str) -> None:
    with open(file_path, "w") as f:
        for item in toc:
            item[0] = str(item[0])
            item[-1] = str(item[-1])
            f.write(" ".join(item) + "\n")


def file2toc(file_path: str) -> list:
    toc = []
    with open(file_path) as f:
        for line in f:
            items = line.split(" ")
            lvl = int(items[0])
            if items[-1][-1] == "\n":
                items[-1] = items[-1][:-1]
            pn = int(items[-1])
            cn = " ".join(items[1:-1])
            toc.append([lvl, cn, pn])
    return toc


class Toc:
    def read(self, pdf_path: str) -> None:
        doc = fitz.open(pdf_path)
        toc = doc.get_toc()
        toc2file(toc, pdf_path.replace(".pdf", ".toc"))

    def write(self, pdf_path: str, bias: int = 0) -> None:
        doc = fitz.open(pdf_path)
        toc = file2toc(pdf_path.replace(".pdf", ".toc"))
        for item in toc:
            item[-1] += bias
        doc.set_toc(toc)
        doc.saveIncr()


class PyPdf:
    def __init__(self) -> None:
        self.toc = Toc()

    def delete(self, pdf_path: str, start_pn: int, end_pn: int) -> None:
        doc = fitz.open(pdf_path)
        doc.delete_pages(list(range(start_pn-1, end_pn)))
        doc.saveIncr()

    def join(self, *pdfs_path: str) -> None:
        doc = fitz.open(pdfs_path[0])
        for i in pdfs_path[1:]:
            item = fitz.open(i)
            doc.insert_pdf(item)
        doc.saveIncr()


def main():

    fire.Fire(PyPdf)
