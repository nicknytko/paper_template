pdf_sources = \
	sine.pdf

all: $(pdf_sources)

clean:
	rm $(pdf_sources)

sine.pdf: common.py sine.py
	python3 sine.py --savefig
