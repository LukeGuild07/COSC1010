#
# Name Luke Guild
# Date 9/14/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Named Constants
HOTDOG_PACK=10
HOTDOG_BUNS=8
# User input
people= int(input('How many people are going to be at the cookout?: '))
hotdogs_per_person= int(input('How many hotdogs does each person get?'))
# Calculate total hotdogs/buns required
total_hotdogs= people*hotdogs_per_person
# Calculate number of hotdog packages required
hotdog_packages= total_hotdogs/HOTDOG_PACK
# Calculate number of bun packages required
hotdog_bun_packs= total_hotdogs/HOTDOG_BUNS
# Some math stuff
import math
total_hotdog_packages=(math.ceil(hotdog_packages))
total_bun_packages=(math.ceil(hotdog_bun_packs))
# Calculate number of hotdogs/buns leftover
hotdog_decimal= total_hotdog_packages-hotdog_packages
leftover_hotdogs= hotdog_decimal*HOTDOG_PACK
bun_decimal= total_bun_packages-hotdog_bun_packs
leftover_buns= bun_decimal*HOTDOG_BUNS
# Display everything
print('You need at least',total_hotdog_packages,'hotdog packages')
print('You need at least',total_bun_packages,'bun packages')
print('You will have',leftover_hotdogs,'hotdogs left over')
print('You will have',leftover_buns,'buns left over')
