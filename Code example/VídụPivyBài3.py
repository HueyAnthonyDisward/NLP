from pyvi import ViTokenizer

vd1 = "Hổ mang bò lên núi"
vd1_processed = ViTokenizer.tokenize(vd1)
print(vd1_processed)