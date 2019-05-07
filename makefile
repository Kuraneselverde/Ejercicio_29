all: datos.dat IMG19.png

IMG19.png: datos.dat G29FF.py
	python3 G29FF.py
    
datos.dat: a.out
	./a.out
    
a.out: 29FF.cpp
	g++ 29FF.cpp

clean:
	rm -rf *.x *.dat *.png
