LATEXFLAGS?=-interaction=nonstopmode -file-line-error
PDFLATEX=pdflatex $(LATEXFLAGS)
BIBTEX=bibtex

JOB=UserGuide
TEXS=$(wildcard *.tex) $(wildcard *.sty) $(wildcard *.cls)
PICS=$(wildcard *.png) $(filter-out $(JOB).pdf,$(wildcard *.pdf))
BIBS=$(wildcard *.bib) $(wildcard *.bst)

.DEFAULT: all
.PHONY: all clean

all: $(JOB).pdf

# Bootstrap aux file, then keep running pdflatex until it reaches a fixpoint

$(JOB).aux: | $(TEXS) $(PICS)
	$(PDFLATEX) $(JOB)

$(JOB).bbl: $(JOB).aux $(BIBS)
	$(BIBTEX) $(JOB)

$(JOB).pdf: $(TEXS) $(PICS) $(JOB).aux $(JOB).bbl
	@cp -p $(JOB).aux $(JOB).aux.bak
	$(PDFLATEX) $(JOB)
	@if cmp -s $(JOB).aux $(JOB).aux.bak; \
	then touch -r $(JOB).aux.bak $(JOB).aux; \
	else NEWS="$$NEWS -W $(JOB).aux"; fi; rm $(JOB).aux.bak; \
	if [ -n "$$NEWS" ]; then $(MAKE) $$NEWS $@; fi

# Compile latex in your background
daemon:
	latexmk --pdf -pvc ${JOB}.tex

clean:
	rm -f $(JOB).aux $(JOB).log $(JOB).blg $(JOB).bbl $(JOB).out $(JOB).pdf

