.PHONY: clean build view figures

PAPER_NAME=paper_template
UNAME = $(shell uname)

ifeq ($(UNAME), Linux)
OPEN=xdg-open
endif
ifeq ($(UNAME), Darwin)
OPEN=open
endif

build: $(PAPER_NAME).pdf

clean:
	rm $(PAPER_NAME).pdf

view: build
	$(OPEN) $(PAPER_NAME).pdf

build-figures: $(wildcard figures/*.pdf) $(wildcard figures/*.tex)
	make -C figures

$(PAPER_NAME).pdf: build-figures $(PAPER_NAME).tex
	latexmk -recorder -pdf -bibtex -pdflatex="pdflatex -synctex=1 --shell-escape %O %S" $(PAPER_NAME)
