import urllib
import requests
from bs4 import BeautifulSoup
import markdownify
import re
import os
import requests
from bs4 import BeautifulSoup
import markdownify
import re
import os

def sort_dict_keys_by_length(dictionary):
    # Sort the dictionary keys based on their length in descending order
    sorted_keys = sorted(dictionary.keys(), key=len, reverse=True)
    
    # Create a new dictionary with sorted keys
    sorted_dict = {key: dictionary[key] for key in sorted_keys}
    
    return sorted_dict

def convert_to_custom_camel_case(word_list):
    def custom_camel_case(word):
        # Handle known abbreviations
        for abbr, replacement in sorted_abbreviations.items():
            word = word.replace(abbr, replacement,  1)

        print(word)
        return word
    
    return [custom_camel_case(word) for word in word_list]

def convert_to_camel_case(word):    
    parts = word.split('_GL')
    # Convert 'GL' to 'gl' and capitalize the rest
    parts[0] = 'gl'
    parts[1] = [part.capitalize() for part in parts[1:]]
    # Join the parts together
    return ''.join(parts)

def fetch_html(url):
    headers = {
        "Host": "qb64phoenix.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://qb64phoenix.com/qb64wiki/index.php?search=%24CHECKING&title=Special%3ASearch&profile=default&fulltext=1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None    

def convert_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Remove MediaWiki-specific tags and content
    for tag in soup(['script', 'style', 'meta', 'link', 'nav', 'header', 'footer']):
        tag.decompose()

    # Convert to markdown
    markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

    # Additional cleaning to remove any remaining MediaWiki-specific markup
    markdown_content = re.sub(r'\[\[Category:[^\]]+\]\]', '', markdown_content)
    markdown_content = re.sub(r'\[\[File:[^\]]+\]\]', '', markdown_content)
    markdown_content = re.sub(r'\[\[.*?\|', '', markdown_content)  # Remove links but keep text
    markdown_content = re.sub(r'\]\]', '', markdown_content)

    return markdown_content

def save_markdown(markdown, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown)

def escape_dollar_signs(filename: str) -> str:
    return filename.replace('$', r'\$')        

def process_keyword(keyword, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Correctly encode the keyword for URL use
    if keyword.startswith('_GL'):
        gl_keyword = convert_to_custom_camel_case([keyword])
        encoded_keyword = urllib.parse.quote_plus(gl_keyword[0])
    else:
        encoded_keyword = urllib.parse.quote_plus(keyword)

    # from wiki
    url = f'https://qb64phoenix.com/qb64wiki/index.php/{encoded_keyword}'
    print(url)
    html_content = fetch_html(url)
    if html_content:
        markdown_content = convert_to_markdown(html_content)
        file_path = os.path.join(output_dir, f"{keyword}.md")
        save_markdown(markdown_content, file_path)
        print(f"Processed and saved: {file_path}")

abbreviations = {
    "GL": "gl",
    "DRAW": "Draw",
    "EDGE": "Edge",
    "COPYTEX": "CopyTex",
    "COLOR3B": "Color3b",
    "COLOR3BV": "Color3bv",
    "COLOR3D": "Color3d",
    "COLOR3DV": "Color3dv",
    "COLOR3F": "Color3f",
    "COLOR3FV": "Color3fv",
    "COLOR3I": "Color3i",
    "COLOR3IV": "Color3iv",
    "COLOR3S": "Color3s",
    "COLOR3SV": "Color3sv",
    "COLOR3UB": "Color3ub",
    "COLOR3UI": "Color3ui",
    "COLOR3UBV": "Color3ubv",
    "COLOR3UIV": "Color3uiv",
    "COLOR3US": "Color3us",
    "COLOR3USV": "Color3usv",
    "COLOR4B": "Color4b",
    "COLOR4BV": "Color4bv",
    "COLOR4D": "Color4d",
    "COLOR4DV": "Color4dv",
    "COLOR4F": "Color4f",
    "COLOR4FV": "Color4fv",
    "COLOR4I": "Color4i",
    "COLOR4IV": "Color4iv",
    "COLOR4S": "Color4s",
    "COLOR4SV": "Color4sv",
    "COLOR4UB": "Color4ub",
    "COLOR4UBV": "Color4ubv",
    "COLOR4UI": "Color4ui",
    "COLOR4UIV": "Color4uiv",
    "COLOR4US": "Color4us",
    "COLOR4USV": "Color4usv",
    "COPYPIXELS": "CopyPixels",
    "COPYTEXIMAGE": "CopyTexImage",
    "COPYTEXSUBIMAGE": "CopyTexSubImage",
    "DELETE": "Delete",
    "FLAGV": "Flagv",
    "END": "End",
    "COORD1D": "Coord1d",
    "COORD1DV": "Coord1dv",
    "COORD1F": "Coord1f",
    "COORD1FV": "Coord1fv",
    "COORD2D": "Coord2d",
    "COORD2DV": "Coord2dv",
    "COORD2F": "Coord2f",
    "COORD2FV": "Coord2fv",
    "FOGF": "Fogf",
    "FOGFV": "Fogfv",
    "FOGI": "Fogi",
    "FOGIV": "Fogiv",
    "BOOLEANV": "Booleanv",
    "DOUBLEV": "Doublev",
    "FLOATV": "Floatv",
    "INTEGERV": "Integerv",
    "LIGHTFV": "Lightfv",
    "LIGHTIV": "Lightiv",
    "MAPDV": "Mapdv",
    "MAPFV": "Mapfv",
    "MAPIV": "Mapiv",
    "MATERIALFV": "Materialfv",
    "MATERIALIV": "Materialiv",
    "MATERIALMAPDV": "MaterialMapdv",
    "MATERIALMAPFV": "MaterialMapfv",
    "POINTERV": "Pointerv",
    "ENVFV": "Envfv",
    "ENVIV": "Enviv",
    "GENDV": "Gendv",
    "GENIV": "Geniv",
    "LEVEL": "Level",
    "PARAMETERF": "Parameterf",
    "PARAMETERFV": "Parameterfv",
    "PARAMETERI": "Parameteri",
    "PARAMETERIV": "Parameteriv",
    "INDEXD": "Indexd",
    "INDEXDV": "Indexdv",
    "INDEXF": "Indexf",
    "INDEXFV": "Indexfv",
    "INDEXI": "Indexi",
    "INDEXIVC": "Indexiv",
    "INDEXS": "Indexs",
    "INDEXSV": "Indexsv",
    "INDEXUB": "Indexub",
    "INDEXUBV": "Indexubv",
    "NAMES": "Names",
    "ENABLED": "Enabled",
    "ISTEXTURE": "IsTexture",
    "MODEDLF": "Modelf",
    "MODELFV": "Modelfv",
    "MODELIV": "Modeliv",
    "LIGHTF": "Lightf",
    "LIGHTFV": "Lightfv",
    "LIGHTI": "Lighti",
    "LIGHTIV": "Lightiv",
    "BASE": "Base",
    "WIDTH": "Width",
    "NEW": "New",
    "IDENTITY": "Identity",
    "MATRIXD": "Matrixd",
    "MATRIXF": "Matrixf",
    "MATRIXMODE": "MatrixMode",
    "PASSTHROUGH": "Passthrough",
    "PRIORITIZE": "Prioritize",
    "READBUFFER": "ReadBuffer",
    "READPIXELS": "ReadPixels",
    "SCALEF": "Scalef",
    "SCALEFV": "Scalefv",
    "SCALEI": "Scalei",
    "SCALEIV": "Scaleiv",
    "VERTEX2D": "Vertex2d",
    "VERTEX2DV": "Vertex2dv",
    "VERTEX2F": "Vertex2f",
    "VERTEX2FV": "Vertex2fv",
    "VERTEX2I": "Vertex2i",
    "VERTEX2IV": "Vertex2iv",
    "VERTEX2S": "Vertex2s",
    "VERTEX2SV": "Vertex2sv",
    "VERTEX3D": "Vertex3d",
    "VERTEX3DV": "Vertex3dv",
    "VERTEX3F": "Vertex3f",
    "VERTEX3FV": "Vertex3fv",
    "VERTEX3I": "Vertex3i",
    "VERTEX3IV": "Vertex3iv",
    "VERTEX3S": "Vertex3s",
    "VERTEX3SV": "Vertex3sv",
    "D": "d",
    "DV": "dv",
    "F": "f",
    "FV": "fv",
    "I": "i",
    "S": "s",
    "SV": "sv",
    "IV": "iv",
    "UB": "ub",
    "UBV": "ubv",
    "UBVI": "ubvi",
    "RASTERPOS": "RasterPos",
    "RASTERPOS2D": "RasterPos2d",
    "RASTERPOS2DV": "RasterPos2dv",
    "RASTERPOS2F": "RasterPos2f",
    "RASTERPOS2FV": "RasterPos2fv",
    "RASTERPOS2I": "RasterPos2i",
    "RASTERPOS2IV": "RasterPos2iv",
    "RASTERPOS2S": "RasterPos2s",
    "RASTERPOS2SV": "RasterPos2sv",
    "RASTERPOS3D": "RasterPos3d",
    "RASTERPOS3DV": "RasterPos3dv",
    "RASTERPOS3F": "RasterPos3f",
    "RASTERPOS3FV": "RasterPos3fv",
    "RASTERPOS3I": "RasterPos3i",
    "RASTERPOS3IV": "RasterPos3iv",
    "RASTERPOS3S": "RasterPos3s",
    "RASTERPOS3SV": "RasterPos3sv",
    "RASTERPOS4D": "RasterPos4d",
    "RASTERPOS4DV": "RasterPos4dv",
    "RASTERPOS4F": "RasterPos4f",
    "RASTERPOS4FV": "RasterPos4fv",
    "RASTERPOS4I": "RasterPos4i",
    "RASTERPOS4IV": "RasterPos4iv",
    "RASTERPOS4S": "RasterPos4s",
    "RASTERPOS4SV": "RasterPos4sv",
    "RASTERPOS3": "RasterPos3",
    "RASTERPOS4": "RasterPos4",
    "RASTERPOS3V": "RasterPos3v",
    "RASTERPOS4V": "RasterPos4v",
    "RASTERPOS3X": "RasterPos3x",
    "RASTERPOS4X": "RasterPos4x",
    "RASTERPOS3XV": "RasterPos3xv",
    "RASTERPOS4XV": "RasterPos4xv",   
    "RESIDENT": "Resident",
    "ELEMENT": "Element",
    "BEGIN": "Begin",
    "SCISSOR": "Scissor",
    "ACCUM": "Accum",
    "ALPHA": "Alpha",        
    "FUNC": "Func",
    "ARE": "Are",
    "TEXTURES": "Textures",
    "ARRAY": "Array",
    "BIND": "Bind",
    "TEXTURE": "Texture",
    "BITMAP": "Bitmap",
    "BLEND": "Blend",
    "CALL": "Call",
    "LIST": "List",
    "CALLLISTS": "CallLists",
    "CLEAR": "Clear",
    "COLOR": "Color",
    "DEPTH": "Depth",
    "INDEX": "Index",
    "STENCIL": "Stencil",
    "CLIP": "Clip",
    "PANE": "Pane",
    "PLANE": "Plane",
    "MATRIX": "Matrix",
    "MATRIXMODE": "MatrixMode",
    "MATRIXSTACKDEPTH": "MatrixStackDepth",
    "MATERIAL": "Material",
    "POINT": "Point",
    "POINTS": "Points",
    "POINTER": "Pointer",
    "MASK": "Mask",
    "PIXEL": "Pixel",
    "PIXELS": "Pixels",
    "TEX": "Tex",
    "IMAGE": "Image",
    "SUBIMAGE": "SubImage",
    "CULL": "Cull",
    "FACE": "Face",
    "RANGE": "Range",
    "DISABLE": "Disable",
    "CLIENT": "Client",
    "STATE": "State",
    "ARRAYS": "Arrays",
    "BUFFER": "Buffer",
    "ELEMENTS": "Elements",
    "FLAG": "Flag",
    "ENABLE": "Enable",
    "COORD": "Coord",
    "EVAL": "Eval",
    "MESH": "Mesh",
    "FEEDBACK": "Feedback",
    "FINISH": "Finish",
    "FLUSH": "Flush",
    "FOG": "Fog",
    "FRONT": "Front",
    "FRUSTUM": "Frustum",
    "GEN": "Gen",
    "LISTS": "Lists",
    "TEXTURE": "Texture",
    "BOOLEAN": "Boolean",
    "DOUBLE": "Double",
    "GET": "Get",
    "ERROR": "Error",
    "FLOAT": "Float",
    "INTEGER": "Integer",
    "LIGHT": "Light",
    "MAP": "Map",
    "POLYGON": "Polygon",
    "POLYGONMODE": "PolygonMode",
    "STRING": "String",
    "STIPPLE": "Stipple",
    "TEXCOORD": "TexCoord",
    "TEXENV": "TexEnv",
    "TEXPARAM": "TexParameter",
    "TEXIMAGE": "TexImage",
    "TEXSUBIMAGE": "TexSubImage",
    "TEXGEN": "TexGen",
    "TEXMAT": "TexMat",
    "TEXPARAMETER": "TexParameter",
    "TEXGEN": "TexGen",
    "HINT": "Hint",
    "INDEX": "Index",
    "INIT": "Init",
    "INTERLEAVED": "Interleaved",
    "IS": "Is",
    "MODEL": "Model",
    "NORMAL": "Normal",
    "LOAD": "Load",
    "NAME": "Name",
    "LOGIC": "Logic",
    "OP": "Op",
    "MAP": "Map",
    "GRID": "Grid",
    "MULT": "Mult",
    "NEW": "New",
    "NORMAL": "Normal",
    "PASS": "Pass",
    "ORTHO": "Ortho",
    "ZOOM": "Zoom",
    "TRANSFER": "Transfer",
    "STORE": "Store",
    "SIZE": "Size",
    "ATTRIB": "Attrib",
    "POP": "Pop",
    "PUSH": "Push",
    "RASTER": "Raster",
    "RASTERPO": "RasterPo",
    "RECT": "Rect",
    "ROTATE": "Rotate",
    "RENDER": "Render",
    "MODE": "Mode",
    "SCALE": "Scale",
    "SELECT": "Select",
    "SHADE": "Shade",
    "VERTEX": "Vertex",
    "VIEWPORT": "Viewport"
}

output_directory = 'markdown_files'
sorted_abbreviations = sort_dict_keys_by_length(abbreviations)

# Read keywords from file
current_directory = os.path.dirname(os.path.abspath(__file__))
keywords_file_path = os.path.join(current_directory, 'keywords.txt')
with open('keywords.txt', 'r') as file:
    keywords = [line.strip() for line in file.readlines()]

# Process each keyword
for keyword in keywords:
    process_keyword(keyword, output_directory)

