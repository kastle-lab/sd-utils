import rdflib

from rdflib import Graph, Namespace, RDF, RDFS

import graphviz
import networkx

import os

d = "example"
filename = "abolition.ttl"
filename = os.path.join(d, filename)

pattern = Graph()
kastle = Namespace("https://kastle.cs.wright.edu/enslaved-modl")
pattern.bind("kastle", kastle)

dot = graphviz.Digraph()

entities = set()

with open(filename) as pattern_file:
	pattern.parse(pattern_file)

	for pred in pattern.subjects(RDF.type, RDF.Property):
		# Get Domain
		for domain in pattern.objects(pred, RDFS.domain):
			domain_name = domain.split("#")[-1]
			if domain not in entities:
				entities.add(domain)
				dot.node(domain_name, domain)
		# Get Range
		for range in pattern.objects(pred, RDFS.range):
			range_name = range.split("#")[-1]
			if range not in entities:
				entities.add(range)
				dot.node(range_name, range)

		dot.edge(domain_name, range_name)
dot.render(directory='example')
