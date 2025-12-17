chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !") 
# Order for Priya : Ginger chai please !

chai_description = "Aromatic and Bold" 
print(f"length: {chai_description.__len__()}") # 17
print(f"First word: {chai_description[0:8]}") # First word: Aromatic
print(f"First word: {chai_description[0:8:1]}") # First word: Aromatic
print(f"First word: {chai_description[0:8:2]}") # First word: Aoai  (Second Char skip)
print(f"First word: {chai_description[:8]}") # First word: Aromatic
print(f"Last word: {chai_description[12:]}") # Last word:  Bold
print(f"Last word: {chai_description[::-1]}") # Last word: dloB dna citamorA (reverse)

#[start:end:step|skip]

label_text = "Chai Speci@l"
encoded_label = label_text.encode("utf-8")

print(f"Encoded Label: {encoded_label}")
print(f"Non Encoded Label: {label_text}")
decoded_label =  encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")