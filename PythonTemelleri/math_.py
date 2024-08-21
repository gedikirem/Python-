import math
import io
import sys

# Eski stdout'u (standart çıktıyı) sakla
old_stdout = sys.stdout

# Yeni bir stringIO akışı oluştur
new_stdout = io.StringIO()
sys.stdout = new_stdout

# help() fonksiyonunu çağır
help(math)

# stdout'u eski haline getir
sys.stdout = old_stdout

# help çıktısını al ve yazdır
help_string = new_stdout.getvalue()
print(help_string)
