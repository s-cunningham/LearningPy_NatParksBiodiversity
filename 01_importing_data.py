## Learning Python with National Parks Biodiversity

# Load libraries
import pandas as pd

# Read in parks
parks = pd.read_csv('data/parks.csv')

# Read in species
species = pd.read_csv('data/species.csv')
print(species)

## Count number of species by park and order
