TEX=lualatex

all:	test1.pdf \
	test2.pdf \
	test3.pdf \
	test4.pdf \
	test5.pdf \
	test6.pdf \
	test7.pdf \
	test8.pdf \
	test9.pdf \
	test10.pdf \
	test11.pdf \
	test12.pdf \
	test13.pdf \
	test14.pdf \
	test15.pdf

.PHONY: clean
clean:
	rm *.pdf
	rm *.log
	rm *.aux

%.pdf:	%.tex
	$(TEX) $<

