default: html

SRC=2020-09-14_IWAI
CHROMIUM=chromium
CHROMIUM=/Applications/Chromium.app/Contents/MacOS/Chromium

install:
	pip3 install git+https://github.com/laurentperrinet/slides.py

edit:
	atom $(SRC).py

page:
	python3 $(SRC).py
	#
	cat /tmp/talk.bib |pbcopy
	#atom ~/pool/blog/perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib
	# academic ...

get_figures:
	mkdir -p figures
	# from the paper
	rsync -a ../WhereIsMyMNIST/paper/*.jpg figures

html:
	python3 $(SRC).py index.html

show: html
#	open -a firefox $(SRC).html
	open /Applications/Safari.app/Contents/MacOS/Safari  index.html

github: html
	git pull
	git add figures
	git commit --dry-run -am 'Test' | grep -q -v 'nothing to commit' && git commit -am' updating slides'
	git push
	#firefox  --new-tab https://SpikeAI.github.io/$(SRC)

print: html
	#open -a /Applications/Chromium.app https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true
	#open "https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true"
	$(CHROMIUM) --headless --disable-gpu --pageWidth=1600 --pageHeight=1000 --print-to-pdf=$(SRC).pdf "https://laurentperrinet.github.io/$(SRC)/?print-pdf"
