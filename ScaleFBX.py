#!/usr/bin/env python

"""scaleFBX.py: A script to scale the native size of the model defined by an ascii FBX file"""

import argparse
import re
import io
import os
from decimal import Decimal

__Author__		= "Daniel Kranich"
__License__		= "MIT"

parser = argparse.ArgumentParser(description="Scale an ascii FBX model")
parser.add_argument("fbxPath", type=str, help="Path to your ascii fbx file")
parser.add_argument("output", type=str, help="Where to save scaled fbx")
parser.add_argument("-s", "--scale", type=float, default=1.0, help="The ammount to scale the fbx model")

args = parser.parse_args()

isvertex = False

vstart = re.compile('Vertices: \*\d* {')
vend = re.compile('}\s*$')
nums = re.compile('[\de,.-]*')
wht = re.compile('\s*a:\s*')
twht = re.compile('\s*P:\s*"Lcl Translation", "Lcl Translation", "", "A",')
trans = re.compile('[\d-][\d,.-]*')
sci = re.compile('e[\d-]*$')

st = ""

try:
	os.remove(args.output)
except OSError:
	pass

with open(args.fbxPath, 'r') as fbx:
	with open(args.output, 'w') as output:
		for line in fbx:
			vertices = []
			if isvertex:
				if vend.search(line):
					isvertex = False
					output.write(line)
				else:
					tabs = wht.findall(line)
					vals = nums.findall(line.strip())
					for val in vals:
						if val:
							vertices += val.split(',')
					if tabs:
						st += str(tabs[0])
					for i, vertex in enumerate(vertices):
						if vertex:
							tail = ""
							if sci.search(vertex):
								tail = sci.findall(vertex)
								vertex = vertex.replace(tail[0], "")
							vertex = float(vertex)
							vertex *= args.scale
							vertex = ('%.12f' % vertex).rstrip('0').rstrip('.')
							if i:
								st += ','
							st += str(vertex)
							if tail:
								st += str(tail[0])
					output.write(st + '\n')
					st = ""
			else:
				output.write(line)
			if vstart.search(line):
				isvertex = True	
			if twht.search(line):
				tabs = twht.findall(line)
				vals = trans.findall(line)
				for val in vals:
					if val:
						vertices += val.split(',')
				if tabs:
					st += str(tabs[0])
				for i, vertex in enumerate(vertices):
					if vertex:
						tail = ""
						if sci.search(vertex):
							tail = sci.findall(vertex)
							vertex = vertex.replace(tail[0], "")
						vertex = float(vertex)
						vertex *= args.scale
						vertex = ('%.8f' % vertex).rstrip('0').rstrip('.')
						if i:
							st += ','
						st += str(vertex)
						if tail:
							st += str(tail[0])
				output.write(st + '\n')
				st = ""
