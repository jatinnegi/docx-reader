from fastapi import FastAPI
from os import listdir
from os.path import isfile, join
from utils import all_files
import mammoth

app = FastAPI()


@app.get("/")
def index():

    data = []

    for file in all_files:
        path = f"Career Bank/{file}"

        f = open(path, "rb")
        document = mammoth.convert_to_html(f)

        filename = file
        career_name = filename.replace(".docx", "")
        slug = career_name.replace(" ", "-").lower()
        content = document.value.encode("utf8")

        f.close()

        career_name = (
            career_name.lower()
            .replace("career option in ", "")
            .replace("careeer option in ", "")
            .replace("careers option in ", "")
            .replace("carrer option in ", "")
            .replace("career in", "")
            .title()
        )

        data.append({"name": career_name, "slug": slug, "content": content})

    return data


# Get all file names inside the career bank folder
@app.get("/all-files")
def get_all_files():
    files = [f for f in listdir("Career Bank") if isfile(join("Career Bank", f))]

    return {"files": files}
