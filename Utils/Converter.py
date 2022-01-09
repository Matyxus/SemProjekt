import os
from constants import CWD, file_exists


class Converter:
	""" Class that calls osm filter and netconvert to create network for SUMO """

	def __init__(self, file_name: str):
		self.file_name: str = file_name
		self.cwd: str = str(CWD)

	def osm_filter(self) -> bool:
		"""
		Uses osm filter to filter .osm file, removing everything apart from highways,
		expecting file to be in \\maps\\osm\\original, filtered file will be saved
		in \\maps\\osm\\filtered under the same name (_filtered suffix added)

		:return: True if successful, false otherwise
		"""
		print("Filtering osm file with osm filter")
		file_path: str = (self.cwd + "\\maps\\osm\\original\\" + self.file_name + ".osm")
		if not file_exists(file_path):
			print(f"Could not load file: {file_path}, file does not exist!")
			return False
		command: str = (self.cwd + '\\OSMfilter\\osmfilter.exe ')
		command += file_path
		command += (
			' --hash-memory=720 --keep-ways="highway=primary =tertiary '
			'=residential =primary_link =secondary =secondary_link =trunk =trunk_link =motorway =motorway_link" '
			'--keep-nodes= --keep-relations= > '
		)
		filtered_file_path: str = (self.cwd + "\\maps\\osm\\filtered\\" + self.file_name + "_filtered.osm")
		command += filtered_file_path
		# print("Command: " + command)
		print(f"Done filtering osm file, saved in: {filtered_file_path}")
		try:
			os.system(command)
		except Exception as e:
			print(f"Error occurred: {e}")
			return False
		return True

	def net_convert(self) -> bool:
		"""
		Uses netconvert to convert .osm file into .net.xml, expecting .osm file to be in
		\\maps\\osm\\filtered\\file_name, resulting file will be saved in
		\\maps\\sumo\\file_name

		:return: True if successful, false otherwise
		"""
		print("Creating .net file for SUMO with netconvert on filtered file")
		file_path: str = f"{self.cwd}\\maps\\osm\\filtered\\{self.file_name + '_filtered.osm'}"
		if not file_exists(file_path):
			print(f"Could not load file: {file_path}, file does not exist!")
			return False
		command: str = "netconvert --osm "
		command += file_path
		command += (
			" --geometry.remove --ramps.guess --junctions.join"
			" --roundabouts.guess"
			" --remove-edges.isolated --keep-edges.components 1"
		)
		net_file_path = (self.cwd + "\\maps\\sumo\\" + self.file_name + ".net.xml")
		command += (" -o " + net_file_path)
		# print("Command: " + command)
		print(f"Done creating .net file, saved in: {net_file_path}")
		try:
			os.system(command)
		except Exception as e:
			print(f"Error occurred: {e}")
			return False
		return True
