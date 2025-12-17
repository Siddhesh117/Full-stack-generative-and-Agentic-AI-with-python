masala_spices = ("cardamom","cloves","cinnamon")

(spice1,spice2,spice3) = masala_spices

print(f"Main masala spices: {spice1} {spice2} {spice3}") 
# Main masala spices: cardamom cloves cinnamon

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")
# Ratio is G: 2 and C: 1

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")
# Ratio is G: 1 and C: 2

# membership

print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")
# Is ginger in masala spices ? False

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")
# Is cinnamon in masala spices ? True