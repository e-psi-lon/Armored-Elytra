
# Imports
from python_datapack.constants import *
from python_datapack.utils.print import *
from python_datapack.utils.io import *
from .utils.create_craft import create_custom_craft
from .utils.advancements import generate_advancements
from .utils.settings import register_settings
from .utils.abitities.functions import create_functions
from .utils.models import generate_models

# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def main(config: dict) -> None:
	build_datapack = config["build_datapack"]
	namespace: str = config["namespace"]
	version = config["version"]
	datapack_name: str = config["datapack_name"]
	create_custom_craft(config)
	generate_advancements(config)
	register_settings(config)
	create_functions(config)
	generate_models(config)
	write_to_file(f"{build_datapack}/data/{namespace}/function/_unload.mcfunction", f"""
#scores
scoreboard objectives remove {namespace}.settings

tellraw @s [{'{"text": "['+datapack_name+']:","color": "green"}'},{'{"text": "The datapack has succesfully been uninstall","color": "white"}'}]
datapack disable "file/{datapack_name.replace(" ", "")}_datapack.zip"
datapack disable "file/{datapack_name.replace(" ", "")}_datapack"
""")
	

