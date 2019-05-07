all: datos.dat imagenes.png

%.png: %.dat imagenes.png
	python3 G29F.py
    
%.dat: a.out
	./a.out
    
a.out: 29F.cpp
	g++ 29F.cpp

clean:
	rm -rf *.x *.dat *.png
