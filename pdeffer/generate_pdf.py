import logging
from .utils import setup_logging
from weasyprint import HTML
from os import listdir
from os.path import isfile, join

logger = logging.getLogger(__name__)


def generate_pdf(source_dir: str, dest_dir: str) -> None:
    if dest_dir is None:
        dest_dir = source_dir
    files = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
    print(files)

    # TODO grab files that start with numbers
    # TODO sort files that start by number numerically
    logger.info(f"The following files will be combined to create PDF: {files}")

    f = f"{source_dir}/{files[0]}"
    HTML(f).write_pdf(f"{dest_dir}/result.pdf")


if __name__ == "__main__":
    setup_logging(level=logging.INFO)
